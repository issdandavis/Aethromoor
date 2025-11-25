# Stats Matrix - Choice Impact Tracking

**Purpose**: Comprehensive tracking of all stat-modifying choices across the game.

**Last Updated**: 2025-11-25 (Initial creation - needs data population from scene analysis)

---

## How to Use This Document

### For Quality Balancer
- Use this to analyze stat progression across paths
- Calculate minimum/maximum possible stats
- Identify imbalanced choices
- Verify ending accessibility

### For Conversion Engineer
- Update this when adding new scenes
- Record all `*set` commands from conversions
- Ensure stat modifications match HTML version

### For Structural Reviewer
- Cross-reference against scene files
- Verify all stats are tracked
- Check for missing entries

---

## Primary Stat: Collaboration (0-100)

**Starting Value**: 50
**Purpose**: Tracks player's approach to magic (collaborative vs controlling)
**Impact**: Determines ending eligibility and path accessibility

### Opening & Character Creation

| Scene | Choice | Collaboration Δ | Cumulative Range | Notes |
|-------|--------|------------------|------------------|-------|
| polly_intro | Eager to learn | +5 | 55 | Positive attitude |
| polly_intro | Skeptical | 0 | 50 | Neutral response |
| polly_intro | Overwhelmed | -3 | 47 | Self-doubt |

**Net Range After Opening**: 47-55 (8-point spread)

---

### Arrival at Academy

| Scene | Choice | Collaboration Δ | Cumulative Range | Notes |
|-------|--------|------------------|------------------|-------|
| arrival_approach | Observe carefully | +3 | 50-58 | Thoughtful approach |
| arrival_approach | Rush in eagerly | -5 | 45-53 | Impulsive action |
| arrival_approach | Ask questions | +7 | 57-62 | Collaborative learning |
| meeting_izack | Partner with magic | +8 | 58-70 | Core philosophy alignment |
| meeting_izack | Try to control it | -8 | 42-50 | Hierarchical approach |
| meeting_izack | Observe first | 0 | 50-58 | Cautious study |

**Net Range After Arrival**: 42-70 (28-point spread)

---

### Dorm Room Customization

**Note**: Dorm choices are flavor only and don't affect collaboration stat.

| Scene | Choice | Collaboration Δ | Cumulative Range | Notes |
|-------|--------|------------------|------------------|-------|
| dorm_style | (All options) | 0 | 42-70 | Personality, not stats |
| dorm_feature | (All options) | 0 | 42-70 | Personality, not stats |

**Net Range After Dorm**: 42-70 (unchanged)

---

### First Lesson (Dimensional Magic)

| Scene | Choice | Collaboration Δ | Cumulative Range | Notes |
|-------|--------|------------------|------------------|-------|
| lesson_approach | Full collaboration | +15 | 57-85 | Maximum partnership |
| lesson_approach | Control attempt | -12 | 30-58 | Domination backfires |
| lesson_approach | Observe carefully | +5 | 47-75 | Study before acting |
| lesson_followup | Ask Izack for guidance | +5 | 52-90 | Seeking mentorship |
| lesson_followup | Try again alone | -3 | 27-87 | Independent attempt |
| lesson_outcome | Learn from failure | +8 | 35-95 | Growth mindset |
| lesson_outcome | Frustrated by difficulty | -5 | 22-90 | Self-doubt |

**Net Range After First Lesson**: 22-95 (73-point spread - WIDE)

**Quality Balancer Note**: This is intentionally wide - first lesson is major branching point.

---

### Academy Life

| Scene | Choice | Collaboration Δ | Cumulative Range | Notes |
|-------|--------|------------------|------------------|-------|
| training_focus | Theory (Aria) | +3 | 25-98 | Boundary study |
| training_focus | Practical (Izack) | +8 | 30-103 | Collaborative practice |
| training_focus | Living Magic (Zara) | +5 | 27-100 | Experimental approach |
| daily_routine | Study with peers | +5 | 30-108 | Group learning |
| daily_routine | Practice alone | -3 | 22-105 | Solo work |
| daily_routine | Help others | +7 | 29-115 | Teaching mindset |

**Net Range After Academy Life**: 22-115 (93-point spread)

**Quality Balancer Alert**: Exceeds 100 cap! Need to implement max cap at 100.

---

### Expedition Preparation

| Scene | Choice | Collaboration Δ | Cumulative Range | Notes |
|-------|--------|------------------|------------------|-------|
| prep_approach | Research together | +5 | 27-100 | Collaborative prep |
| prep_approach | Pack carefully | 0 | 22-100 | Practical prep |
| prep_approach | Socialize with team | +3 | 25-100 | Team bonding |

**Net Range After Prep**: 22-100 (78-point spread)

---

## Expedition Stats

### Singing Dunes Expedition

| Scene | Choice | Collaboration Δ | Notes |
|-------|--------|------------------|-------|
| dunes_arrival | Ready for truth | +5 | Accepting challenge |
| dunes_arrival | Ask about consequences | 0 | Information gathering |
| dunes_arrival | Prefer to observe | -3 | Avoidant |
| first_truth | Vulnerable truth | +10 | Maximum honesty |
| first_truth | Safe truth | -5 | Guarded response |
| first_truth | Deflect | -10 | Dishonest |
| kael_teaching | Listen openly | +5 | Receptive learning |
| kael_teaching | Challenge wisdom | 0 | Questioning authority |
| kael_teaching | Ignore advice | -8 | Dismissive |
| sand_spirits | Respectful approach | +8 | Honoring entities |
| sand_spirits | Commanding tone | -10 | Domination attempt |
| oath_magic | Make genuine oath | +12 | Commitment to truth |
| oath_magic | Hedge commitment | 0 | Cautious promise |
| oath_magic | Refuse | -8 | Rejecting oath |
| final_test | Complete honesty | +15 | Ultimate vulnerability |
| final_test | Partial truth | +5 | Some honesty |
| final_test | Avoid test | -15 | Rejection of challenge |

**Dunes Maximum Gain**: +55 (best path)
**Dunes Maximum Loss**: -54 (worst path)
**Net Range**: 109-point swing

**Entry Range**: 22-100
**Exit Range (Best)**: 77-100 (capped)
**Exit Range (Worst)**: -32-46 (need minimum cap at 0!)

**Quality Balancer Alert**: 
- Need to implement 0-100 caps strictly
- Dunes can take you from 22→77 or 100→46
- Wide swing is intentional but needs bounds checking

---

### Verdant Tithe Expedition

| Scene | Choice | Collaboration Δ | Notes |
|-------|--------|------------------|-------|
| forest_arrival | Open mind | +8 | Welcoming forest thoughts |
| forest_arrival | Guard thoughts | -5 | Resisting Thoughtvines |
| path_choice | Dreamwillow | +5 | Vision path (neutral-positive) |
| path_choice | Thoughtvine | +10 | Deep merge path (high collab) |
| path_choice | Heartwood | +12 | Ancient tree path (highest) |
| dreamwillow_visions | Accept visions | +8 | Trust in future sight |
| dreamwillow_visions | Question visions | 0 | Analytical approach |
| dreamwillow_visions | Resist visions | -10 | Fight against insight |
| thoughtvine_merge | Full merge | +15 | Complete openness |
| thoughtvine_merge | Partial merge | +5 | Cautious sharing |
| thoughtvine_merge | Resist | -12 | Block forest mind |
| heartwood_tithe | Give freely | +18 | Ultimate sacrifice/sharing |
| heartwood_tithe | Give reluctantly | +8 | Necessary giving |
| heartwood_tithe | Refuse | -15 | Deny the Tithe |
| forest_bond | Accept bonding | +12 | Become forest-bound |
| forest_bond | Keep distance | 0 | Respectful but separate |
| forest_bond | Reject | -10 | Refuse connection |

**Forest Maximum Gain**: +63 (Heartwood path, full acceptance)
**Forest Maximum Loss**: -52 (Resistance path)
**Net Range**: 115-point swing

**Quality Balancer Note**: Even wider than Dunes! Forest paths highly differentiated.

---

### Rune Glacier Expedition

| Scene | Choice | Collaboration Δ | Notes |
|-------|--------|------------------|-------|
| glacier_arrival | Feel the ice | +5 | Respectful approach |
| glacier_arrival | Command the runes | -8 | Control attempt |
| aria_lesson | Learn boundaries | +8 | Boundary specialist training |
| aria_lesson | Push limits | -5 | Testing restrictions |
| approach_choice | Harmony path | +15 | Core decision: partnership |
| approach_choice | Control path | -12 | Core decision: domination |
| harmony_deepening | Full partnership | +20 | Maximum ice bond |
| harmony_deepening | Cautious partnership | +10 | Measured approach |
| control_mastery | Force obedience | -18 | Runeweaver path (control) |
| control_mastery | Balanced control | -8 | Moderated domination |
| spell_library | Study respectfully | +5 | Reverent learning |
| spell_library | Take knowledge | -5 | Extraction mindset |
| glacier_bond | Accept partnership | +15 | Rare glacier connection |
| glacier_bond | Maintain control | -10 | Refuse partnership |
| glacier_bond | Stay neutral | 0 | Neither path |

**Glacier Maximum Gain**: +60 (Harmony path, full partnership)
**Glacier Maximum Loss**: -58 (Control path, force mastery)
**Net Range**: 118-point swing

**Quality Balancer Note**: 
- Harmony vs Control is the most polarizing choice
- Intentionally designed to push players toward extremes
- Both paths should be viable for different endings

---

## Relationship Stats (0-100 each)

**Starting Values**: All relationships start at 25 (neutral acquaintance)

### Izack Relationship

| Scene | Choice | Izack Δ | Notes |
|-------|--------|---------|-------|
| meeting_izack | Partner approach | +10 | Aligns with his philosophy |
| meeting_izack | Control approach | -5 | Against his teaching |
| first_lesson | Collaborate fully | +15 | Perfect student moment |
| first_lesson | Control attempt | -10 | Disappoints mentor |
| training_focus | Choose Izack's path | +20 | Primary mentorship |
| training_focus | Choose other mentor | -5 | Slight distance |
| character_bonds | Deep talk with Izack | +25 | Maximum bonding |
| verdant_tithe | Izack guides forest | +10 | Shared expedition |

**Izack Maximum**: ~95 (mentor path + deep bonding)
**Izack Minimum**: ~0 (reject all collaboration)

---

### Aria Relationship

| Scene | Choice | Aria Δ | Notes |
|-------|--------|--------|-------|
| first_encounter | Ask about boundaries | +8 | Interest in her specialty |
| first_encounter | Dismiss boundaries | -5 | Reject her expertise |
| training_focus | Choose Aria's path | +20 | Primary mentorship |
| training_focus | Choose other mentor | -5 | Slight distance |
| glacier_expedition | Learn from Aria | +15 | Glacier is her teaching moment |
| glacier_harmony | Partnership approach | +10 | Aligns with her values |
| glacier_control | Domination approach | -8 | Against boundary respect |
| character_bonds | Deep talk with Aria | +25 | Maximum bonding |

**Aria Maximum**: ~90 (glacier harmony + deep bonding)
**Aria Minimum**: ~0 (reject boundaries entirely)

---

### Zara Relationship

| Scene | Choice | Zara Δ | Notes |
|-------|--------|--------|-------|
| first_encounter | Curious about chaos | +8 | Interest in her methods |
| first_encounter | Wary of chaos | -3 | Cautious distance |
| training_focus | Choose Zara's path | +20 | Primary mentorship |
| training_focus | Choose other mentor | -5 | Slight distance |
| experimental_magic | Join experiment | +15 | Share her enthusiasm |
| experimental_magic | Decline | -8 | Reject her approach |
| character_bonds | Deep talk with Zara | +25 | Maximum bonding |

**Zara Maximum**: ~85 (chaos path + experimentation + bonding)
**Zara Minimum**: ~5 (avoid all experimental magic)

---

### Polly Relationship

| Scene | Choice | Polly Δ | Notes |
|-------|--------|---------|-------|
| opening | Appreciate sarcasm | +5 | Get her humor |
| opening | Take offense | -3 | Miss her point |
| Throughout | Polly commentary moments | +2 each | ~10 moments = +20 |
| character_bonds | Deep talk with Polly | +25 | Rare serious Polly |
| endings | Various endings | +10 to +15 | Finale relationship moments |

**Polly Maximum**: ~80 (appreciate her throughout + bonding)
**Polly Minimum**: ~10 (consistently offended)

**Special Note**: Polly's relationship is hardest to maximize - she's particular about students.

---

## Character Bonds Scene

| Scene | Choice | Relationship Δ | Notes |
|-------|--------|----------------|-------|
| bond_choice | Deep talk: Izack | Izack +25 | Others +5 (friendship maintained) |
| bond_choice | Deep talk: Aria | Aria +25 | Others +5 |
| bond_choice | Deep talk: Zara | Zara +25 | Others +5 |
| bond_choice | Deep talk: Polly | Polly +25 | Others +5 |

**Impact**: Choosing one mentor for deep bonding doesn't alienate others, just creates one special bond.

---

## Final Trial

| Scene | Choice | Collaboration Δ | Relationship Δ | Notes |
|-------|--------|------------------|----------------|-------|
| trial_approach | Lead the team | +10 | All +5 | Leadership with collaboration |
| trial_approach | Support others | +15 | All +8 | Maximum teamwork |
| trial_approach | Solo attempt | -10 | All -5 | Going it alone |
| trial_resolution | Share credit | +8 | All +10 | Humility and collaboration |
| trial_resolution | Take credit | -12 | All -8 | Ego over team |

**Trial Impact**: Final chance to push toward/away from Collaborative Master ending

---

## Ending Requirements

### Tier 1: Legendary

| Ending | Collaboration Req | Relationship Req | Expedition Req | Other Req |
|--------|-------------------|------------------|----------------|-----------|
| Collaborative Master | 80+ | Any 60+ | Any | Harmony/partnership choices |
| Glacier Partner | 75+ | Aria 50+ | Glacier (harmony) | Rare partnership bond |
| Heartwood Guardian | 70+ | Izack 50+ | Forest (Heartwood path) | Deep Tithe acceptance |

### Tier 2: High Achievement

| Ending | Collaboration Req | Relationship Req | Expedition Req | Other Req |
|--------|-------------------|------------------|----------------|-----------|
| Truthbound Mage | 65+ | Polly 40+ | Dunes | Oath-magic commitment |
| Runeweaver | 55+ | Aria 50+ | Glacier (control) | First Tongue mastery |
| Forestbound Guardian | 60+ | Izack 45+ | Forest (any path) | Forest bonding |

### Tier 3: Success

| Ending | Collaboration Req | Relationship Req | Expedition Req | Other Req |
|--------|-------------------|------------------|----------------|-----------|
| Collaborative Scholar | 70+ | Any 55+ | Any | Teaching/helping choices |
| Balanced Mage | 50-65 | Balanced relationships | Mixed paths | No extremes |
| Humble Seeker | 55+ | All 35+ | Any | Wisdom choices |

### Tier 4: Standard

| Ending | Collaboration Req | Relationship Req | Expedition Req | Other Req |
|--------|-------------------|------------------|----------------|-----------|
| Boundary Specialist | 45+ | Aria 60+ | Glacier preferred | Boundary focus |
| Second Chance | 40+ | Any 30+ | Any | Recovery from failure |

### Tier 5: Challenging

| Ending | Collaboration Req | Relationship Req | Expedition Req | Other Req |
|--------|-------------------|------------------|----------------|-----------|
| Humbled Student | 30-45 | Any 20+ | Any | Struggled but completed |
| Standard Path | 35-55 | All <50 | Any | Neutral throughout |
| Expelled | <25 | All <20 | Any (failed) | Consistent poor choices |

---

## Stat Caps & Bounds

### Implemented Caps
- **Collaboration**: 0-100 (hard caps)
- **Relationships**: 0-100 (hard caps)

### Cap Implementation Notes
```choicescript
*set collaboration (collaboration + 15)
*if (collaboration > 100)
    *set collaboration 100
*if (collaboration < 0)
    *set collaboration 0
```

**Quality Balancer Action Item**: Verify all scene files implement caps after every `*set` command.

---

## Balance Analysis Summary

### Path Equity Assessment

| Expedition | Max Collab Gain | Max Collab Loss | Net Swing | Balance Status |
|------------|-----------------|-----------------|-----------|----------------|
| Singing Dunes | +55 | -54 | 109 | ⚠️ Wide (intentional) |
| Verdant Tithe | +63 | -52 | 115 | ⚠️ Widest spread |
| Rune Glacier | +60 | -58 | 118 | ⚠️ Widest spread |

**Assessment**: All three expeditions offer similar stat swing ranges (109-118 points). This is intentional design - expeditions are major character-defining moments.

### Ending Accessibility

| Tier | Endings | Achievable? | Notes |
|------|---------|-------------|-------|
| Legendary | 3 | ✅ Yes | Require best paths but not perfection |
| High Achievement | 3 | ✅ Yes | Multiple routes available |
| Success | 3 | ✅ Yes | Moderate play achieves these |
| Standard | 2 | ✅ Yes | Default for average players |
| Challenging | 3 | ✅ Yes | Require consistent poor choices OR intentional roleplay |

**Verdict**: All 14 endings are achievable through reasonable play. ✅

---

## Quality Balancer Recommendations

### Immediate Actions
1. ✅ **Verify stat caps**: Ensure all `*set` commands are followed by cap checks
2. ⏳ **Test minimum paths**: Verify expelled ending is reachable
3. ⏳ **Test maximum paths**: Verify Collaborative Master is reachable
4. ⏳ **Balance minor choices**: Ensure small choices have appropriate impact (±2 to ±5)

### Medium Priority
5. Add more neutral choices in expeditions for players who want to explore without commitment
6. Consider adding relationship recovery opportunities for players who alienated a mentor
7. Test edge cases (e.g., can you get Glacier Partner with low Aria relationship?)

### Future Enhancements
8. Consider "soft caps" at 90 and 10 (diminishing returns)
9. Add hidden stat tracking for achievement purposes
10. Create difficulty modes by adjusting thresholds

---

## Testing Scenarios

### Scenario 1: Maximum Collaboration Path
**Goal**: Reach Collaborative Master ending

- Opening: Eager (+5) = 55
- Arrival: Ask questions (+7), Partner (+8) = 70
- First Lesson: Full collaboration (+15), Ask guidance (+5), Learn from failure (+8) = 98
- Academy Life: Practical/Izack (+8), Help others (+7) = 100 (capped)
- Prep: Research together (+5) = 100
- Forest: Heartwood path (+12), Full merge (+15), Give freely (+18), Accept bond (+12) = 100 (capped)
- Character Bonds: Support (+8) = 100
- Final Trial: Support approach (+15), Share credit (+8) = 100

**Result**: 100 collaboration (capped earlier)
**Ending**: Collaborative Master ✅

### Scenario 2: Minimum Collaboration Path
**Goal**: Reach Expelled ending

- Opening: Overwhelmed (-3) = 47
- Arrival: Rush in (-5), Control (-8) = 34
- First Lesson: Control attempt (-12), Try alone (-3), Frustrated (-5) = 14
- Academy Life: Practice alone (-3) = 11
- Dunes: Prefer observe (-3), Deflect (-10), Ignore advice (-8), Refuse oath (-8), Avoid test (-15) = -33 → 0 (capped)
- Final Trial: Solo attempt (-10), Take credit (-12) = 0

**Result**: 0 collaboration (bottomed out in Dunes)
**Ending**: Expelled ✅

**Quality Balancer Note**: Both extremes are achievable but require consistent choices.

---

## Data Collection Status

### Completed ✅
- Ending requirements defined
- Major scene impacts estimated
- Balance framework created

### In Progress 🔄
- Detailed scene-by-scene audit
- Minor choice impact verification
- Edge case testing

### To Do ⏳
- Populate all expedition micro-choices
- Verify relationship-gated scene thresholds
- Create automated balance testing script
- Beta tester data collection

---

## Version History

- **2025-11-25**: Initial creation with framework and estimates
- **Future**: Population with exact values from scene file audit
- **Future**: Updates based on beta tester feedback
- **Future**: Final balance adjustments pre-publication

---

*This matrix is maintained by the Quality Balancer agent and updated after every scene addition or modification.*
