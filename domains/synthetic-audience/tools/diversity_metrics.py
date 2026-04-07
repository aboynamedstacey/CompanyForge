#!/usr/bin/env python3
"""
Diversity metrics for synthetic audience response verification.

Deterministic tool -- not an agent. Validates that synthetic persona panels
produce genuinely diverse responses rather than surface-level variations of
the same underlying output.

Usage:
    python tools/diversity_metrics.py responses.json [comparative|variance]

Input: JSON list of objects with required fields:
    - persona_id: unique identifier
    - segment: segment label
    - response_text: the persona's response

Optional structured fields:
    - sentiment.valence: float (-1.0 to 1.0)
    - sentiment.activation: float (-1.0 to 1.0)
    - funnel_position: one of dismiss|passive_awareness|active_research|consideration|purchase_intent
    - concerns: list of {concern: str, decision_impact: float}
    - sycophancy_canary: bool

Provenance fields (checked for completeness):
    - persona_version, stimulus_version, prompt_template_version, context_version

Output: JSON report with pass/fail per metric, overall_pass, failed_checks.
Exit code: 0 if overall pass, 1 if any check fails.
"""

import json
import math
import re
import sys
from collections import Counter, defaultdict

# ---------------------------------------------------------------------------
# Tokenization
# ---------------------------------------------------------------------------

_WORD_RE = re.compile(r"[a-zA-Z']+")


def tokenize(text):
    """Lowercase word tokenization. Strips punctuation except apostrophes."""
    return [w.lower() for w in _WORD_RE.findall(text)]


def ngrams(tokens, n):
    """Generate n-grams from a token list."""
    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]


# ---------------------------------------------------------------------------
# TF-IDF and cosine similarity (stdlib fallback)
# ---------------------------------------------------------------------------

def _try_sklearn_tfidf(docs):
    """Attempt sklearn TF-IDF. Returns (matrix, True) or (None, False)."""
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity

        vec = TfidfVectorizer(stop_words="english", min_df=1)
        mat = vec.fit_transform(docs)
        sim = cosine_similarity(mat)
        return sim, True
    except ImportError:
        return None, False


def _manual_tfidf_cosine(docs):
    """Pure-stdlib TF-IDF cosine similarity matrix."""
    n_docs = len(docs)
    tokenized = [tokenize(d) for d in docs]

    # Document frequency
    df = Counter()
    for tokens in tokenized:
        df.update(set(tokens))

    vocab = sorted(df.keys())
    vocab_idx = {w: i for i, w in enumerate(vocab)}
    v_len = len(vocab)

    if v_len == 0:
        return [[1.0] * n_docs for _ in range(n_docs)]

    # TF-IDF vectors
    vectors = []
    for tokens in tokenized:
        tf = Counter(tokens)
        vec = [0.0] * v_len
        for word, count in tf.items():
            if word in vocab_idx:
                idf = math.log((n_docs + 1) / (df[word] + 1)) + 1
                vec[vocab_idx[word]] = count * idf
        vectors.append(vec)

    # Cosine similarity matrix
    def dot(a, b):
        return sum(x * y for x, y in zip(a, b))

    def norm(a):
        return math.sqrt(dot(a, a))

    norms = [norm(v) for v in vectors]
    sim = [[0.0] * n_docs for _ in range(n_docs)]
    for i in range(n_docs):
        for j in range(n_docs):
            if norms[i] == 0 or norms[j] == 0:
                sim[i][j] = 0.0
            else:
                sim[i][j] = dot(vectors[i], vectors[j]) / (norms[i] * norms[j])
    return sim


def cosine_similarity_matrix(docs):
    """Compute pairwise cosine similarity. Prefers sklearn, falls back to stdlib."""
    sim, ok = _try_sklearn_tfidf(docs)
    if ok:
        return [[float(sim[i][j]) for j in range(len(docs))] for i in range(len(docs))]
    return _manual_tfidf_cosine(docs)


# ---------------------------------------------------------------------------
# Sentiment classification (keyword-based v1)
# ---------------------------------------------------------------------------

_POSITIVE_WORDS = {
    "love", "great", "amazing", "excellent", "good", "awesome", "fantastic",
    "wonderful", "perfect", "happy", "enjoy", "like", "best", "beautiful",
    "brilliant", "outstanding", "impressive", "superb", "delighted", "pleased",
    "excited", "positive", "recommend", "favorite", "glad", "nice", "cool",
    "fun", "helpful", "useful", "convenient", "easy", "comfortable", "trust",
    "reliable", "quality", "worth", "value", "fresh", "innovative",
}

_NEGATIVE_WORDS = {
    "hate", "terrible", "awful", "bad", "horrible", "worst", "ugly", "boring",
    "annoying", "disappointing", "poor", "waste", "useless", "expensive",
    "overpriced", "cheap", "broken", "frustrating", "confused", "confusing",
    "difficult", "complicated", "unreliable", "distrust", "skeptical", "doubt",
    "concern", "worry", "dislike", "avoid", "never", "refuse", "ridiculous",
    "pointless", "mediocre", "meh", "whatever", "don't", "wouldn't", "can't",
}


def classify_sentiment(text):
    """Keyword-based sentiment: positive, negative, or neutral."""
    words = set(tokenize(text))
    pos = len(words & _POSITIVE_WORDS)
    neg = len(words & _NEGATIVE_WORDS)
    if pos > neg:
        return "positive"
    if neg > pos:
        return "negative"
    return "neutral"


# ---------------------------------------------------------------------------
# Statistics helpers
# ---------------------------------------------------------------------------

def mean(values):
    if not values:
        return 0.0
    return sum(values) / len(values)


def stdev(values):
    if len(values) < 2:
        return 0.0
    m = mean(values)
    return math.sqrt(sum((x - m) ** 2 for x in values) / (len(values) - 1))


def coefficient_of_variation(values):
    m = mean(values)
    if m == 0:
        return 0.0
    return (stdev(values) / abs(m)) * 100


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

VALID_FUNNEL_STAGES = {
    "dismiss", "passive_awareness", "active_research", "consideration", "purchase_intent"
}


def check_cross_segment_similarity(responses_by_segment):
    """
    Check 1: TF-IDF cosine similarity between segment-aggregated responses.
    Threshold: < 0.85.
    """
    segments = sorted(responses_by_segment.keys())
    if len(segments) < 2:
        return {
            "check": "cross_segment_similarity",
            "passed": True,
            "note": "Single segment -- cross-segment check not applicable.",
            "details": {},
        }

    # Aggregate all response text per segment
    docs = [" ".join(responses_by_segment[s]) for s in segments]
    sim = cosine_similarity_matrix(docs)

    pairs = {}
    max_sim = 0.0
    for i in range(len(segments)):
        for j in range(i + 1, len(segments)):
            key = f"{segments[i]} vs {segments[j]}"
            pairs[key] = round(sim[i][j], 4)
            max_sim = max(max_sim, sim[i][j])

    passed = max_sim < 0.85
    return {
        "check": "cross_segment_similarity",
        "passed": passed,
        "threshold": "< 0.85",
        "max_similarity": round(max_sim, 4),
        "pairs": pairs,
        "note": (
            "PASS: segments are lexically distinct."
            if passed
            else f"FAIL: max cosine similarity {max_sim:.4f} >= 0.85. Segments may have collapsed."
        ),
    }


def check_sentiment_distribution(responses):
    """
    Check 2: Keyword-based sentiment classification per segment.
    Flag if >80% positive across all segments.
    """
    by_segment = defaultdict(list)
    for r in responses:
        by_segment[r["segment"]].append(classify_sentiment(r["response_text"]))

    segment_reports = {}
    all_positive_pcts = []
    for seg, sentiments in sorted(by_segment.items()):
        total = len(sentiments)
        counts = Counter(sentiments)
        pct_pos = (counts.get("positive", 0) / total) * 100 if total else 0
        all_positive_pcts.append(pct_pos)
        segment_reports[seg] = {
            "positive": counts.get("positive", 0),
            "negative": counts.get("negative", 0),
            "neutral": counts.get("neutral", 0),
            "pct_positive": round(pct_pos, 1),
        }

    overall_pos = mean(all_positive_pcts)
    passed = overall_pos <= 80
    return {
        "check": "sentiment_distribution",
        "passed": passed,
        "threshold": "<= 80% positive",
        "overall_pct_positive": round(overall_pos, 1),
        "segments": segment_reports,
        "note": (
            "PASS: sentiment distribution includes sufficient negative/neutral."
            if passed
            else f"FAIL: {overall_pos:.1f}% positive across segments. Possible sycophancy."
        ),
    }


def check_response_variance(responses):
    """
    Check 3: Word count coefficient of variation across segments.
    Must be >10%.
    """
    by_segment = defaultdict(list)
    for r in responses:
        wc = len(tokenize(r["response_text"]))
        by_segment[r["segment"]].append(wc)

    segment_means = [mean(wcs) for wcs in by_segment.values()]
    cv = coefficient_of_variation(segment_means)

    passed = cv > 10
    return {
        "check": "response_variance",
        "passed": passed,
        "threshold": "> 10% CV",
        "cv_pct": round(cv, 2),
        "segment_mean_word_counts": {
            seg: round(mean(wcs), 1) for seg, wcs in sorted(by_segment.items())
        },
        "note": (
            f"PASS: response length CV is {cv:.1f}%."
            if passed
            else f"FAIL: response length CV is {cv:.1f}% (<= 10%). Responses too uniform in length."
        ),
    }


def check_phrasing_overlap(responses_by_segment):
    """
    Check 4: Bigram/trigram overlap between segments.
    Weight: 40% bigram, 60% trigram. Threshold: <80% combined.
    """
    segments = sorted(responses_by_segment.keys())
    if len(segments) < 2:
        return {
            "check": "phrasing_overlap",
            "passed": True,
            "note": "Single segment -- phrasing overlap check not applicable.",
            "details": {},
        }

    def segment_ngram_sets(n):
        result = {}
        for seg in segments:
            all_tokens = []
            for text in responses_by_segment[seg]:
                all_tokens.extend(tokenize(text))
            result[seg] = set(ngrams(all_tokens, n))
        return result

    bigram_sets = segment_ngram_sets(2)
    trigram_sets = segment_ngram_sets(3)

    def pairwise_overlap(sets_dict):
        overlaps = []
        segs = list(sets_dict.keys())
        for i in range(len(segs)):
            for j in range(i + 1, len(segs)):
                a, b = sets_dict[segs[i]], sets_dict[segs[j]]
                union = a | b
                if len(union) == 0:
                    overlaps.append(0.0)
                else:
                    overlaps.append(len(a & b) / len(union))
        return mean(overlaps) if overlaps else 0.0

    bigram_overlap = pairwise_overlap(bigram_sets)
    trigram_overlap = pairwise_overlap(trigram_sets)
    combined = 0.4 * bigram_overlap + 0.6 * trigram_overlap
    combined_pct = combined * 100

    passed = combined_pct < 80
    return {
        "check": "phrasing_overlap",
        "passed": passed,
        "threshold": "< 80% combined",
        "bigram_overlap_pct": round(bigram_overlap * 100, 2),
        "trigram_overlap_pct": round(trigram_overlap * 100, 2),
        "combined_pct": round(combined_pct, 2),
        "note": (
            f"PASS: combined phrasing overlap is {combined_pct:.1f}%."
            if passed
            else f"FAIL: combined phrasing overlap is {combined_pct:.1f}% (>= 80%). Segments share too much phrasing."
        ),
    }


def check_intra_segment_consensus(responses_by_segment):
    """
    Check 5: Mean pairwise cosine similarity WITHIN each segment.
    Flag if > 0.85 or sentiment consensus > 90%.
    """
    results = {}
    any_failed = False

    for seg, texts in sorted(responses_by_segment.items()):
        if len(texts) < 2:
            results[seg] = {
                "cosine_mean": None,
                "sentiment_consensus_pct": None,
                "passed": True,
                "note": "Single response in segment -- consensus check not applicable.",
            }
            continue

        sim = cosine_similarity_matrix(texts)
        pairs = []
        for i in range(len(texts)):
            for j in range(i + 1, len(texts)):
                pairs.append(sim[i][j])
        mean_sim = mean(pairs) if pairs else 0.0

        sentiments = [classify_sentiment(t) for t in texts]
        most_common_count = Counter(sentiments).most_common(1)[0][1]
        consensus_pct = (most_common_count / len(sentiments)) * 100

        seg_passed = mean_sim <= 0.85 and consensus_pct <= 90
        if not seg_passed:
            any_failed = True

        results[seg] = {
            "cosine_mean": round(mean_sim, 4),
            "sentiment_consensus_pct": round(consensus_pct, 1),
            "passed": seg_passed,
            "note": (
                "OK"
                if seg_passed
                else f"Premature consensus: cosine={mean_sim:.4f}, sentiment_consensus={consensus_pct:.1f}%"
            ),
        }

    return {
        "check": "intra_segment_consensus",
        "passed": not any_failed,
        "threshold": "cosine <= 0.85 AND sentiment consensus <= 90%",
        "segments": results,
        "note": (
            "PASS: no premature intra-segment consensus detected."
            if not any_failed
            else "FAIL: one or more segments show premature consensus."
        ),
    }


def check_panel_size(responses, analysis_type):
    """
    Check 6: Panel size sufficiency.
    Comparative: 5 minimum per segment. Variance: 10 minimum per segment.
    """
    min_required = 5 if analysis_type == "comparative" else 10
    by_segment = defaultdict(int)
    for r in responses:
        by_segment[r["segment"]] += 1

    insufficient = {
        seg: count
        for seg, count in by_segment.items()
        if count < min_required
    }

    passed = len(insufficient) == 0
    return {
        "check": "panel_size",
        "passed": passed,
        "analysis_type": analysis_type,
        "min_per_segment": min_required,
        "segment_counts": dict(sorted(by_segment.items())),
        "insufficient_segments": insufficient,
        "note": (
            f"PASS: all segments meet {min_required}-persona minimum for {analysis_type} analysis."
            if passed
            else f"FAIL: {len(insufficient)} segment(s) below {min_required}-persona minimum."
        ),
    }


def check_provenance(responses):
    """
    Check 7: Provenance completeness.
    Required fields: persona_version, stimulus_version, prompt_template_version, context_version.
    """
    required = {"persona_version", "stimulus_version", "prompt_template_version", "context_version"}
    missing_by_persona = {}

    for r in responses:
        missing = required - set(r.keys())
        if missing:
            missing_by_persona[r["persona_id"]] = sorted(missing)

    passed = len(missing_by_persona) == 0
    return {
        "check": "provenance_completeness",
        "passed": passed,
        "required_fields": sorted(required),
        "missing_by_persona": missing_by_persona,
        "note": (
            "PASS: all responses include complete provenance."
            if passed
            else f"FAIL: {len(missing_by_persona)} response(s) missing provenance fields."
        ),
    }


def check_sentiment_matrix(responses):
    """
    Check 8: 2x2 sentiment matrix distribution.
    Validate valence and activation present and distributed.
    Flag if stdev(valence) < 0.5 or all activation values identical.
    """
    valences = []
    activations = []

    for r in responses:
        sentiment = r.get("sentiment", {})
        if isinstance(sentiment, dict):
            v = sentiment.get("valence")
            a = sentiment.get("activation")
            if v is not None:
                valences.append(float(v))
            if a is not None:
                activations.append(float(a))

    if not valences or not activations:
        return {
            "check": "sentiment_matrix_distribution",
            "passed": True,
            "note": "No structured sentiment data (valence/activation) present. Skipped.",
            "details": {},
        }

    valence_std = stdev(valences)
    activation_unique = len(set(round(a, 4) for a in activations))
    activation_all_same = activation_unique <= 1

    passed = valence_std >= 0.5 and not activation_all_same
    return {
        "check": "sentiment_matrix_distribution",
        "passed": passed,
        "valence_stdev": round(valence_std, 4),
        "activation_unique_values": activation_unique,
        "valence_range": [round(min(valences), 4), round(max(valences), 4)],
        "activation_range": [round(min(activations), 4), round(max(activations), 4)],
        "note": (
            "PASS: sentiment matrix shows adequate distribution."
            if passed
            else (
                f"FAIL: "
                + (f"valence stdev {valence_std:.4f} < 0.5" if valence_std < 0.5 else "")
                + (" AND " if valence_std < 0.5 and activation_all_same else "")
                + ("all activation values identical" if activation_all_same else "")
                + ". Personas clustered in sentiment space."
            )
        ),
    }


def check_funnel_distribution(responses):
    """
    Check 9: 5-stage funnel distribution.
    Flag if all at same stage or no personas at dismiss/passive_awareness.
    """
    positions = []
    for r in responses:
        fp = r.get("funnel_position")
        if fp:
            positions.append(fp)

    if not positions:
        return {
            "check": "funnel_distribution",
            "passed": True,
            "note": "No funnel_position data present. Skipped.",
            "details": {},
        }

    counts = Counter(positions)
    unique_stages = set(positions)
    all_same = len(unique_stages) <= 1
    missing_low = not (unique_stages & {"dismiss", "passive_awareness"})

    passed = not all_same and not missing_low
    return {
        "check": "funnel_distribution",
        "passed": passed,
        "stage_counts": dict(sorted(counts.items())),
        "unique_stages": len(unique_stages),
        "has_low_funnel": not missing_low,
        "note": (
            "PASS: funnel positions distributed across stages."
            if passed
            else (
                "FAIL: "
                + ("all personas at same funnel stage" if all_same else "")
                + (" AND " if all_same and missing_low else "")
                + ("no personas at dismiss or passive_awareness stages" if missing_low else "")
                + ". Panel lacks realistic funnel diversity."
            )
        ),
    }


def check_concern_weighting_variance(responses):
    """
    Check 10: Concern weighting variance.
    For shared concerns across personas, check that decision_impact rankings differ.
    Flag if mean stdev of impact scores < 0.15 across personas sharing the same concern.
    """
    concern_impacts = defaultdict(list)

    for r in responses:
        concerns = r.get("concerns", [])
        if isinstance(concerns, list):
            for c in concerns:
                if isinstance(c, dict) and "concern" in c and "decision_impact" in c:
                    concern_impacts[c["concern"]].append(float(c["decision_impact"]))

    # Only evaluate concerns that appear across multiple personas
    shared = {k: v for k, v in concern_impacts.items() if len(v) >= 2}

    if not shared:
        return {
            "check": "concern_weighting_variance",
            "passed": True,
            "note": "No shared concerns across personas or no concern data present. Skipped.",
            "details": {},
        }

    stdevs = {}
    for concern, impacts in sorted(shared.items()):
        stdevs[concern] = round(stdev(impacts), 4)

    mean_std = mean(list(stdevs.values()))
    passed = mean_std >= 0.15

    return {
        "check": "concern_weighting_variance",
        "passed": passed,
        "threshold": "mean stdev >= 0.15",
        "mean_stdev": round(mean_std, 4),
        "per_concern_stdev": stdevs,
        "note": (
            f"PASS: personas weight shared concerns differently (mean stdev {mean_std:.4f})."
            if passed
            else (
                f"FAIL: mean stdev of shared concern weights is {mean_std:.4f} (< 0.15). "
                f"Personas are ranking concerns too similarly."
            )
        ),
    }


def check_sycophancy_canary(responses):
    """
    Check 11: Sycophancy canary check.
    If a persona is tagged sycophancy_canary=true, check if its sentiment valence
    is positive (> 0). If so, flag the entire panel.
    """
    canaries = [r for r in responses if r.get("sycophancy_canary") is True]

    if not canaries:
        return {
            "check": "sycophancy_canary",
            "passed": True,
            "note": "No sycophancy canary personas in panel. Skipped.",
            "details": {},
        }

    flagged = []
    for c in canaries:
        # Check structured valence first, fall back to keyword classification
        sentiment = c.get("sentiment", {})
        if isinstance(sentiment, dict) and sentiment.get("valence") is not None:
            is_positive = float(sentiment["valence"]) > 0
            evidence = f"valence={sentiment['valence']}"
        else:
            kw_sentiment = classify_sentiment(c["response_text"])
            is_positive = kw_sentiment == "positive"
            evidence = f"keyword_sentiment={kw_sentiment}"

        if is_positive:
            flagged.append({
                "persona_id": c["persona_id"],
                "segment": c["segment"],
                "evidence": evidence,
            })

    passed = len(flagged) == 0
    return {
        "check": "sycophancy_canary",
        "passed": passed,
        "canary_count": len(canaries),
        "flagged_canaries": flagged,
        "note": (
            f"PASS: {len(canaries)} canary persona(s) responded as expected (not positive)."
            if passed
            else (
                f"FAIL: {len(flagged)} of {len(canaries)} canary persona(s) responded positively. "
                f"Panel may be compromised by sycophancy."
            )
        ),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_all_checks(responses, analysis_type):
    """Run all checks and return the full report."""
    # Group responses by segment
    by_segment = defaultdict(list)
    for r in responses:
        by_segment[r["segment"]].append(r["response_text"])

    checks = [
        check_cross_segment_similarity(by_segment),
        check_sentiment_distribution(responses),
        check_response_variance(responses),
        check_phrasing_overlap(by_segment),
        check_intra_segment_consensus(by_segment),
        check_panel_size(responses, analysis_type),
        check_provenance(responses),
        check_sentiment_matrix(responses),
        check_funnel_distribution(responses),
        check_concern_weighting_variance(responses),
        check_sycophancy_canary(responses),
    ]

    failed = [c["check"] for c in checks if not c["passed"]]
    overall = len(failed) == 0

    return {
        "overall_pass": overall,
        "analysis_type": analysis_type,
        "total_responses": len(responses),
        "segments": sorted(by_segment.keys()),
        "checks": checks,
        "failed_checks": failed,
    }


def validate_input(data):
    """Validate input format and required fields."""
    if not isinstance(data, list):
        return False, "Input must be a JSON array of response objects."
    if len(data) == 0:
        return False, "Input array is empty."

    required = {"persona_id", "segment", "response_text"}
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            return False, f"Item {i} is not an object."
        missing = required - set(item.keys())
        if missing:
            return False, f"Item {i} (persona_id={item.get('persona_id', '?')}) missing required fields: {sorted(missing)}"

    return True, None


def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/diversity_metrics.py responses.json [comparative|variance]", file=sys.stderr)
        sys.exit(2)

    input_path = sys.argv[1]
    analysis_type = sys.argv[2] if len(sys.argv) > 2 else "comparative"

    if analysis_type not in ("comparative", "variance"):
        print(f"Unknown analysis type: {analysis_type}. Use 'comparative' or 'variance'.", file=sys.stderr)
        sys.exit(2)

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {input_path}", file=sys.stderr)
        sys.exit(2)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}", file=sys.stderr)
        sys.exit(2)

    valid, error = validate_input(data)
    if not valid:
        print(f"Validation error: {error}", file=sys.stderr)
        sys.exit(2)

    report = run_all_checks(data, analysis_type)
    print(json.dumps(report, indent=2))

    sys.exit(0 if report["overall_pass"] else 1)


if __name__ == "__main__":
    main()
