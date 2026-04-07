# Domain Context Engine — Competitive BBQ

Quick reference for what context to gather and where to find it. The Scout
uses this before the Builder starts work.

---

## What to Gather

Every workflow needs some subset of this. Scale depth to the tier — a trivial
question doesn't need a weather forecast.

### Competition Rules (if applicable)
- Which sanctioning body governs (KCBS, MBN, SCA, other)
- Turn-in categories and windows
- Garnish, container, and sauce rules
- Equipment and fuel restrictions

### Weather and Altitude (if cook is scheduled)
- Ambient temperature — affects cook time (cold/windy = longer cooks, more fuel)
- Altitude — lower boiling point increases evaporation, can extend the stall. Mainly relevant in mountain states (Colorado, etc.) where elevation is significant. `[GENERATED DEFAULT — refine through use]`
- Wind and rain — affects fire management and fuel consumption
- For competition: forecast for the full event (setup day through awards)

### Equipment and Protein
- Cooker type (offset, kamado, pellet, WSM, drum, cabinet) — each cooks differently
- Fuel type (stick, lump, briquette, pellet) — affects flavor and management
- Protein cut, grade, weight if known
- Prior cook data from claude-mem for this protein/equipment combo

---

## Source Priority

Search in this order, stop when you have a clear answer.

**Level 1 — Official Competition Rules (always check if competition)**
Sanctioning body rulebook, category-specific rules, equipment rules, food safety requirements.

**Level 2 — Practitioner Knowledge (when rules don't cover it)**
Established techniques (3-2-1, Texas crutch, rest protocols), protein-specific knowledge (stall temps, target internals, probe tender), equipment behavior (offset fire management, kamado airflow, WSM water pan). `[GENERATED DEFAULT — refine through use]`

Standard temps are practitioner knowledge — don't research brisket done at 200-205F probe tender unless conditions are unusual.

**Level 3 — Environmental Data (when conditions matter)**
Weather services, altitude data, historical weather patterns. `[GENERATED DEFAULT — refine through use]`

**Level 4 — Community Knowledge (context, not authority)**
Competition forums, prior cook data from claude-mem, regional judging tendencies (real — southern circuits run sweeter, Texas circuits favor savory/smoke-forward).

---

## Where to Look — Source Mapping

### KCBS (Kansas City Barbeque Society)
| Source Type | Where to Find |
|---|---|
| Official rules | kcbs.us — Rules & Regulations document |
| Category rules | KCBS rules — Chicken, Ribs, Pork, Brisket sections |
| Scoring criteria | KCBS rules — Appearance, Taste, Tenderness (2-9 scale, 6 judges) |
| Turn-in format | KCBS rules — Styrofoam container, garnish rules |
| Equipment rules | KCBS rules — fire/fuel restrictions |

### MBN (Memphis Barbecue Network)
| Source Type | Where to Find |
|---|---|
| Official rules | mbnbbq.com — competition rules |
| Categories | Whole Hog, Shoulder, Ribs (varies by event) |
| On-site judging | MBN uses on-site judging — presentation to judges at your booth |

### SCA (Steak Cookoff Association)
| Source Type | Where to Find |
|---|---|
| Official rules | steakcookoffs.com |
| Format | Single protein (steak), ancillary categories vary |

### Other Competition Bodies (FBA, local sanctioning, invitational events) `[GENERATED DEFAULT — refine through use]`
| Source Type | Where to Find |
|---|---|
| Official rules | Web search for the specific body's current rulebook |
| Category rules | Event-specific documentation or competition packet |
| Scoring criteria | Varies — some follow KCBS format, others use unique scales |
| Turn-in format | Event-specific — confirm container and garnish rules |

**Note:** Regional and local bodies often modify KCBS or MBN rules. Never assume KCBS rules apply — always verify for the specific event.

### Environmental Data
| Source Type | Where to Find |
|---|---|
| Weather forecast | weather.gov, openweathermap |
| Altitude | USGS elevation data, Google Earth |
| Historical weather | weatherspark.com for regional patterns |

---

## Flags for the Human

Escalate if:
- Competition rules are ambiguous or contradictory
- Severe weather forecast (extreme cold, rain, high wind) that may require strategy change
- Altitude above 5000ft where cooking physics change significantly `[GENERATED DEFAULT — refine through use]`
- Equipment limitations that prevent the planned technique
- Food safety concern that conflicts with technique preference
- Turn-in schedule requires overlapping cook windows with insufficient equipment
