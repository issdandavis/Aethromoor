# 📊 Stats Matrix
## Tracking Stat Modifications Across All Choices

**Last Updated:** November 24, 2025  
**Purpose:** Track every choice that affects stats for balance checking

---

## 🎯 Stat Overview

### Primary Stats:
- **collaboration** - Core mechanic (range: 0-120+)
- **izack_relationship** - Relationship with Izack Thorne
- **aria_relationship** - Relationship with Aria Ravencrest
- **zara_relationship** - Relationship with Zara
- **polly_relationship** - Relationship with Polly (hidden bonus)

### Secondary Stats (Expedition-specific):
- **truth_level** - Singing Dunes honesty tracking
- **forest_bond** - Verdant Tithe connection level
- **glacier_approach** - Rune Glacier control vs harmony

---

## 📋 Complete Stat Change Log

### 🌟 Opening & Arrival Scenes

#### arrival.txt

| Choice | Location/Label | Stat Change | Cumulative | Notes |
|--------|----------------|-------------|------------|-------|
| Polite greeting | arrival_polite | collaboration +5 | 55 | Friendly first impression |
| Curious questions | arrival_curious | collaboration +3 | 53 | Engaged approach |
| Confident stance | arrival_confident | collaboration +0 | 50 | Neutral baseline |
| Meet Izack (polite) | meet_izack | izack_relationship +3 | - | Initial positive |
| Meet Aria (polite) | meet_aria | aria_relationship +3 | - | Initial positive |
| Meet Zara (polite) | meet_zara | zara_relationship +3 | - | Initial positive |

**Starting Baseline:** collaboration = 50

---

### 📚 First Lesson Scenes

#### first_lesson.txt

| Choice | Location/Label | Stat Change | Cumulative | Notes |
|--------|----------------|-------------|------------|-------|
| Share power equally | lesson_share | collaboration +10 | 60-65 | KEY collaborative moment |
| Control power yourself | lesson_control | collaboration -5 | 45-48 | Hierarchical approach |
| Let partner lead | lesson_defer | collaboration +5 | 55-58 | Trust-building |
| Ask Izack for guidance | breakthrough_izack | izack_relationship +5 | - | Mentor bond |
| Work through crisis alone | crisis_alone | collaboration -3 | varies | Independence penalty |
| Seek help in crisis | crisis_help | collaboration +5 | varies | Asking for help rewarded |
| Thank Aria for lesson | lesson_end_aria | aria_relationship +3 | - | Polite closure |

**Key Thresholds:**
- Breakthrough path: collaboration ≥ 60
- Crisis path: collaboration < 60

---

## 🏜️ Singing Dunes Expedition

#### singing_dunes.txt

| Choice | Location/Label | Stat Change | Cumulative | Notes |
|--------|----------------|-------------|------------|-------|
| "I'm ready, nothing to hide" | dunes_arrival | collaboration +5 | varies | Confident honesty |
| "What if sand turns red?" | dunes_arrival | collaboration +0 | varies | Cautious question |
| "Can we observe first?" | dunes_arrival | collaboration -3 | varies | Avoidance |
| **First Truth Trial** | | | | |
| Speak vulnerable truth | dunes_first_truth | truth_level +10 | 10 | KEY honesty moment |
| | | collaboration +5 | varies | Rewarded vulnerability |
| Share something safe | dunes_first_truth | truth_level +5 | 5 | Mild honesty |
| | | collaboration +0 | varies | Neutral |
| Deflect with humor | dunes_first_truth | truth_level +0 | 0 | Avoidance |
| | | collaboration -5 | varies | Desert disapproves |
| **Kael Interaction** | | | | |
| Ask about his history | kael_talk | izack_relationship +2 | - | Learns about Izack |
| Share your own story | kael_talk | collaboration +3 | varies | Opens up |
| **Oath Magic Lesson** | | | | |
| Embrace oath-binding | oath_lesson | collaboration +5 | varies | Understanding promises |
| Question the ethics | oath_lesson | collaboration +0 | varies | Critical thinking (ok) |
| Refuse to participate | oath_lesson | collaboration -5 | varies | Closed-minded |
| **Final Truth Test** | | | | |
| Complete honesty | final_truth | truth_level +15 | 25-30 | MAJOR moment |
| | | collaboration +10 | varies | Desert's blessing |
| Partial truth | final_truth | truth_level +5 | 10-15 | Acceptable |
| | | collaboration +3 | varies | Mixed response |
| Deception attempt | final_truth | truth_level +0 | 0-5 | Desert rejects |
| | | collaboration -10 | varies | Severe penalty |

**Ending Thresholds (Singing Dunes):**
- Truthbound Mage: truth_level ≥ 25 AND collaboration ≥ 70
- Standard completion: truth_level ≥ 10
- Rejection: truth_level < 5

---

## 🌳 Verdant Tithe Expedition

#### verdant_tithe.txt

| Choice | Location/Label | Stat Change | Cumulative | Notes |
|--------|----------------|-------------|------------|-------|
| **Path Selection** | | | | |
| Choose Dreamwillow path | tithe_path | forest_bond +0 | 0 | Vision-focused |
| Choose Thoughtvine path | tithe_path | forest_bond +0 | 0 | Consciousness path |
| Choose Heartwood path | tithe_path | forest_bond +0 | 0 | Deep bond path |
| **Dreamwillow Scenes** | | | | |
| Accept vision openly | dreamwillow_grove | forest_bond +5 | 5 | Openness to future |
| | | collaboration +5 | varies | Trusting visions |
| Question vision validity | dreamwillow_grove | forest_bond +0 | 0 | Skepticism (neutral) |
| Reject vision entirely | dreamwillow_grove | forest_bond -5 | -5 | Closed off |
| **Thoughtvine Scenes** | | | | |
| Merge consciousness deeply | thoughtvine_merge | forest_bond +10 | 10 | DEEP connection |
| | | collaboration +7 | varies | Ultimate sharing |
| Merge cautiously | thoughtvine_merge | forest_bond +5 | 5 | Careful bonding |
| Resist merge | thoughtvine_merge | forest_bond +0 | 0 | Protection (neutral) |
| **Heartwood Scenes** | | | | |
| Offer genuine tithe | heartwood_tithe | forest_bond +15 | 15 | RARE deep bond |
| | | collaboration +10 | varies | Forest accepts fully |
| | | izack_relationship +5 | - | Izack impressed |
| Offer calculated tithe | heartwood_tithe | forest_bond +7 | 7 | Transactional |
| Refuse the tithe | heartwood_tithe | forest_bond -10 | -10 | Forest rejects |
| | | collaboration -10 | varies | Severe penalty |

**Ending Thresholds (Verdant Tithe):**
- Heartwood Guardian: forest_bond ≥ 15 (Heartwood path only)
- Forestbound Guardian: forest_bond ≥ 7
- Standard completion: forest_bond ≥ 0
- Rejection: forest_bond < -5

---

## ❄️ Rune Glacier Expedition

#### rune_glacier.txt

| Choice | Location/Label | Stat Change | Cumulative | Notes |
|--------|----------------|-------------|------------|-------|
| **Approach Choice** | | | | |
| Control the ice | glacier_approach | glacier_approach = "control" | - | Dominance path |
| | | collaboration -5 | varies | Hierarchical |
| Partner with ice | glacier_approach | glacier_approach = "harmony" | - | Partnership path |
| | | collaboration +5 | varies | Collaborative |
| **Control Path Outcomes** | | | | |
| Success through force | control_success | aria_relationship +5 | - | Aria approves skill |
| | | collaboration +3 | varies | Competent control |
| Backlash from ice | control_backlash | collaboration -10 | varies | Ice resists |
| | | aria_relationship +0 | - | Neutral (learning) |
| **Harmony Path Outcomes** | | | | |
| Deep ice partnership | harmony_success | collaboration +10 | varies | Ice accepts |
| | | aria_relationship +7 | - | Aria deeply impressed |
| Ice cautiously accepts | harmony_partial | collaboration +5 | varies | Working bond |
| **Mystery Path** (hidden) | | | | |
| Discover true partnership | glacier_mystery | collaboration +15 | varies | RARE achievement |
| | | aria_relationship +10 | - | Ultimate approval |
| **Spell Library** | | | | |
| Study collaboratively | spell_library | collaboration +5 | varies | Sharing knowledge |
| Hoard knowledge | spell_library | collaboration -5 | varies | Selfish learning |

**Ending Thresholds (Rune Glacier):**
- Glacier Partner: glacier_approach = "harmony" AND collaboration ≥ 75 (mystery path)
- Runeweaver: glacier_approach = "control" AND aria_relationship ≥ 70
- Boundary Specialist: aria_relationship ≥ 60
- Standard completion: collaboration ≥ 40

---

## 🏆 Ending Requirements

### Complete Requirements Table

| Ending Name | Collaboration | Special Stats | Other Requirements | Priority |
|-------------|---------------|---------------|-------------------|----------|
| **Collaborative Master** | ≥ 80 | Any expedition | Highest tier | Legendary |
| **Truthbound Mage** | ≥ 70 | truth_level ≥ 25 | Singing Dunes | High |
| **Forestbound Guardian** | ≥ 60 | forest_bond ≥ 7 | Verdant Tithe | High |
| **Heartwood Guardian** | ≥ 65 | forest_bond ≥ 15 | Verdant Tithe Heartwood | Legendary |
| **Runeweaver** | ≥ 60 | aria_relationship ≥ 70 | Rune Glacier control | High |
| **Glacier Partner** | ≥ 75 | glacier harmony + mystery | Rune Glacier rare | Legendary |
| **Balanced Mage** | 60-75 | No special | Moderate all paths | Medium |
| **Boundary Specialist** | ≥ 50 | aria_relationship ≥ 60 | Aria focus | Medium |
| **Collaborative Scholar** | ≥ 75 | - | No expedition focus | High |
| **Humble Seeker** | 40-60 | - | Wisdom choices | Medium |
| **Second Chance** | 35-50 | - | Recovery from low | Medium |
| **Humbled Student** | 20-40 | - | Struggled but completed | Low |
| **Expelled** | < 20 | - | Major failures | Failure |
| **Standard Path** | 50-60 | - | Default middle | Standard |

---

## ⚖️ Balance Analysis

### Collaboration Progression Paths

#### Optimal High Path:
```
Start:                    50
Polite arrival:          +5  = 55
Share power (lesson):   +10  = 65
Help in crisis:          +5  = 70
Vulnerable truth (dunes): +5  = 75
Final truth:            +10  = 85
Deep merge (forest):     +7  = 92
Harmony (glacier):      +10  = 102
Partnership bonus:      +15  = 117
```
**Max Achievable: ~115-120**

#### Typical Good Path:
```
Start:                    50
Curious arrival:         +3  = 53
Share power:            +10  = 63
Standard choices:        +8  = 71
Expedition bonuses:     +15  = 86
```
**Typical High: ~80-90**

#### Struggling Path:
```
Start:                    50
Confident arrival:       +0  = 50
Control power:           -5  = 45
Crisis alone:            -3  = 42
Safe choices:            +5  = 47
Some recovery:          +10  = 57
```
**Low Path: ~35-60**

#### Failure Path:
```
Start:                    50
Negative choices:       -15  = 35
Expedition failures:    -20  = 15
EXPELLED
```
**Failure: < 20**

---

## 🎯 Balance Recommendations

### Current Issues to Address:

✅ **Well Balanced:**
- Starting value (50) allows room in both directions
- Ending thresholds spread across range
- Multiple paths to each tier

⚠️ **Needs Attention:**
- Verify expedition stat gains are comparable (~15-25 each)
- Check that failure path is achievable but requires effort
- Ensure recovery path exists from low points

### Stat Progression Guidelines:

**Major Choices:** ±10 collaboration  
**Standard Choices:** ±5 collaboration  
**Minor Choices:** ±3 collaboration  
**Flavor Choices:** ±0 collaboration

**Relationships:**
- Major bonding: +10
- Positive interaction: +5
- Neutral: +0 to +3
- Negative: -5 or less

---

## 🔍 Testing Checklist

### Paths to Verify:

- [ ] **Highest possible collaboration** achievable
- [ ] **Lowest possible collaboration** leads to expulsion
- [ ] **Recovery path** from low to moderate exists
- [ ] **Each ending reachable** with reasonable choices
- [ ] **Legendary endings require** optimal play
- [ ] **Failure ending requires** consistent poor choices
- [ ] **Standard ending** is easiest to achieve

### Balance Tests:

- [ ] No impossible thresholds
- [ ] No trivially easy legendary endings
- [ ] Choices feel impactful
- [ ] Stats match narrative tone
- [ ] Expedition difficulties comparable
- [ ] Multiple routes to each tier

---

## 📝 Notes for Balancing

### Common Patterns:
- **Vulnerability rewarded** with collaboration bonuses
- **Controlling behavior** penalized with collaboration loss
- **Asking for help** rewarded over going alone
- **Relationships** affect scene access but not endings directly

### Design Philosophy:
- Collaboration is primary stat determining success tier
- Special stats (truth_level, forest_bond, etc.) unlock specific endings
- Relationships provide flavor and alternative paths
- Legendary endings require both high collaboration AND special conditions

---

## 🔄 Update Log

- **2025-11-24:** Created initial stats matrix
- **2025-11-24:** Documented all current stat changes
- **2025-11-24:** Projected expedition stat progressions
- **2025-11-24:** Calculated balance paths

---

**Update this file when:**
- Adding new scenes with stat changes
- Adjusting existing stat values
- Discovering balance issues in testing
- Adding new endings or changing requirements
- After playtest feedback on difficulty

---

*"The spiral continues. Balance brings fairness."*
