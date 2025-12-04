# STATS_MATRIX.md
**Comprehensive Stat Tracking for All Choices**

## Purpose
This matrix tracks every choice that affects character stats (Collaboration, relationships, etc.) across all scenes. Use this to balance difficulty, identify stat progression paths, and ensure fair distribution of stat-boosting opportunities.

---

## Stat Definitions

### Primary Stats (Range: 0-100, Start: 50)
- **Collaboration** - Primary metric for collaborative magic mastery
- **Power** - Individual magical strength (opposed to Collaboration)
- **Knowledge** - Academic understanding and lore
- **Empathy** - Emotional intelligence and connection to others

### Relationship Stats (Range: 0-100, Start: 50)
- **izack_relationship** - Relationship with Izack Thorne (headmaster)
- **aria_relationship** - Relationship with Aria Ravencrest (boundary magic professor)
- **zara_relationship** - Relationship with Zara (eccentric professor)
- **polly_relationship** - Relationship with Polly (sarcastic raven familiar)

### Boolean Flags
- **izack_romance** - Pursuing romantic relationship with Izack
- **aria_romance** - Pursuing romantic relationship with Aria
- **zara_romance** - Pursuing romantic relationship with Zara

---

## Collaboration Stat Changes by Scene

### startup.txt
- **Initial Value**: 50 (baseline)

### arrival.txt
| Line | Choice/Action | Delta | Running Total | Context |
|------|---------------|-------|---------------|---------|
| 32 | Choose collaborative boat arrival | +15 | 65 | "I came here to learn, not to show off" |
| 79 | Listen to Polly's advice on boat | +5 | 70 | Accepting guidance |
| 105 | Dismissive response to Polly | -5 | 45 | Rejecting collaboration |
| 127 | Arrogant carriage arrival | -5 | 45 | "I'll manage fine on my own" |
| 137 | Humble carriage arrival | +15 | 65 | Open to learning |
| 150 | Respectful teleportation arrival | +5 | 55 | Acknowledging power with humility |

**Scene Total Range**: -10 to +20 possible change

### familiar_selection.txt
| Line | Choice/Action | Delta | Context |
|------|---------------|-------|---------|
| 65 | Choose Eagle with collaborative mindset | +3 | "Together we'll soar" |
| 100 | Choose Cat with curiosity | +3 | Open to learning |
| 106 | Choose Owl wisely | +2 | Thoughtful approach |
| 122 | Choose Fox adaptably | +2 | Flexible collaboration |
| (Choosing Polly directly) | +0 | No immediate bonus, but unlocks unique paths |

**Scene Total Range**: 0 to +3 possible change

### dorm_room.txt
| Line | Choice/Action | Delta | Context |
|------|---------------|-------|---------|
| 100 | Share space cooperatively | +2 | Working with roommate |

**Scene Total Range**: 0 to +2 possible change

### first_lesson.txt
| Line | Choice/Action | Delta | Context |
|------|---------------|-------|---------|
| Multiple choices | Varies | +5 to +15 | Based on collaborative approach vs individual power |

**Scene Total Range**: -5 to +15 possible change
**Notes**: Most impactful early scene for establishing play style

### academy_life.txt
| Line | Choice/Action | Delta | Context |
|------|---------------|-------|---------|
| 41 | Study with others | +2 | Group learning |
| 66 | Help struggling student | +4 | Teaching collaboration |
| 86 | Collaborative research | +3 | Working together |
| 108 | Successful group project | +4 | Team achievement |
| 120 | Share knowledge freely | +2 | Open collaboration |

**Scene Total Range**: 0 to +15 possible change

### expedition_prep.txt
| Line | Choice/Action | Delta | Context |
|------|---------------|-------|---------|
| 32 | Listen to guide's advice | +2 | Respecting expertise |
| 86 | Prepare collaboratively | +1 | Team preparation |

**Scene Total Range**: 0 to +3 possible change

### character_bonds.txt
| Line | Choice/Action | Delta | Context |
|------|---------------|-------|---------|
| 32 | Meaningful conversation | +2 | Building connection |
| 153 | Deep bonding moment | +2 | Trust building |

**Scene Total Range**: 0 to +4 possible change

### final_trial.txt
| Line | Choice/Action | Delta | Context |
|------|---------------|-------|---------|
| 88 | Collaborative approach to challenge | +5 | Working with others |
| 92 | Share power with partner | +5 | True collaboration |
| 96 | Listen to advice | +5 | Accepting guidance |
| 167 | Harmonize with dimensional forces | +5 | Understanding partnership |
| 179 | Breakthrough collaboration | +15 | Perfect harmony achieved |
| 204 | Request help appropriately | +10 | Acknowledging limits |
| 264 | Reject help arrogantly | -10 | Refusing collaboration |
| 290 | Ultimate collaborative act | +15 | Mastery demonstrated |
| 386 | Final trial success | +20 | Major achievement |
| 414 | Perfect dimensional harmony | +15 | Legendary collaboration |

**Scene Total Range**: -10 to +95 possible change
**Notes**: Most impactful late-game scene, can dramatically shift outcomes

---

## Collaboration Progression Paths

### Optimal Collaboration Path (Maximum ~140 total)
1. Start: 50
2. Arrival (boat, humble): +20 → 70
3. Familiar selection (thoughtful): +3 → 73
4. Dorm room (cooperative): +2 → 75
5. First lesson (fully collaborative): +15 → 90
6. Academy life (all collaborative choices): +15 → 105
7. Character bonds (deep connections): +4 → 109
8. Expedition prep (team approach): +3 → 112
9. Final trial (perfect collaboration): +30 → 142 (capped at 100)

**Result**: Guaranteed Collaborative Master ending

### Minimum Collaboration Path (Lowest ~15 total)
1. Start: 50
2. Arrival (arrogant): -10 → 40
3. Skip collaborative choices
4. First lesson (individualistic): -5 → 35
5. Academy life (solitary): 0 → 35
6. Final trial (reject help): -10 → 25

**Result**: Leads to Expelled or Humbled Student ending

### Balanced Path (~60-75 total)
1. Start: 50
2. Mix of choices: +10 to +25
3. Result: Standard Path or Balanced Mage ending

---

## Relationship Stat Changes by Scene

### Izack Relationship
| Scene | Choices Available | Max Change | Notes |
|-------|------------------|------------|-------|
| arrival.txt | Initial impression | ±10 | First meeting sets tone |
| first_lesson.txt | Performance in lesson | ±5 | Demonstrates potential |
| character_bonds.txt | Deep conversation | +10 | Optional bonding scene |
| final_trial.txt | Seeking guidance | +15 | Asking for Izack's help |

**Relationship Path to Romance**: Requires 70+ relationship + specific dialogue choices

### Aria Relationship
| Scene | Choices Available | Max Change | Notes |
|-------|------------------|------------|-------|
| academy_life.txt | Boundary magic interest | +5 | Showing aptitude |
| character_bonds.txt | Learning from Aria | +10 | Study sessions |
| rune_glacier.txt | Aria as expedition mentor | +20 | Working together closely |

**Relationship Path to Romance**: Requires 75+ relationship + glacier expedition

### Zara Relationship
| Scene | Choices Available | Max Change | Notes |
|-------|------------------|------------|-------|
| academy_life.txt | Eccentric experiments | +5 | Appreciating unconventional methods |
| character_bonds.txt | Understanding Zara | +10 | Seeing past eccentricity |
| golem_workshop.txt | Creating golem together | +15 | Collaborative creation |

**Relationship Path to Romance**: Requires 70+ relationship + golem workshop

### Polly Relationship
| Scene | Choices Available | Max Change | Notes |
|-------|------------------|------------|-------|
| arrival.txt | Listening to advice | +5 | Respecting wisdom |
| familiar_selection.txt | Choosing Polly | +20 | Special bond |
| All scenes | Polly banter responses | ±2 per scene | Ongoing relationship |

**Special**: Polly relationship affects ending narration tone

---

## Artifact Earning Requirements

### Truth-Sworn Sand (Singing Dunes)
- **Requirement**: Complete Singing Dunes expedition + pass honesty tests
- **Stat Impact**: Unlocks Truthbound Mage ending if Collaboration > 60

### Heartwood Guardian (Verdant Tithe)
- **Requirement**: Bond with Heartwood Tree + high Empathy (>60)
- **Stat Impact**: Unlocks Heartwood Guardian ending

### Glacier Partnership (Rune Glacier)
- **Requirement**: Harmonize with glacier + Collaboration > 70
- **Stat Impact**: Unlocks Glacier Partner ending

### Forest Bond - General (Verdant Tithe)
- **Requirement**: Complete forest with Dreamwillow or Thoughtvine path
- **Stat Impact**: Unlocks Forestbound Guardian ending

---

## Ending Thresholds

| Ending | Collaboration Required | Artifact Required | Other Stats |
|--------|----------------------|-------------------|-------------|
| Collaborative Master | > 85 | Any partnership artifact | High relationship with mentor |
| Truthbound Mage | > 60 | Truth-Sworn Sand | Honesty axis > 60 |
| Heartwood Guardian | > 50 | Heartwood Guardian artifact | Empathy > 60 |
| Glacier Partner | > 70 | Glacier Partnership | - |
| Runeweaver | > 60 | Any glacier artifact | Knowledge > 55 |
| Forestbound Guardian | > 50 | Any forest artifact | Empathy > 50 |
| Balanced Mage | 45-65 | None or balanced artifacts | All stats 40-60 |
| Boundary Specialist | > 50 | None | Aria relationship > 70, Knowledge > 60 |
| Collaborative Scholar | 55-75 | None | Knowledge > 65 |
| Humble Seeker | 40-55 | None | Positive attitude choices |
| Second Chance | 30-45 | None | Failures < 3 |
| Humbled Student | 25-40 | None | Learned from mistakes |
| Expelled | < 25 | None | Failures > 3 OR warnings ignored > 2 |
| Standard Path | 45-60 | None | No special achievements |

---

## Stat Balancing Notes

### Current Balance Assessment
- ✅ **Well Balanced**: Multiple paths to each ending type
- ✅ **Fair Distribution**: Stat boosts available in all play styles
- ⚠️ **Potential Issue**: Final trial can swing stats dramatically (+95 or -10)
  - **Solution**: This is intentional - final trial is the culmination
- ✅ **Accessible**: Even low-collaboration paths have good endings available

### Recommendations for Balance
1. **Keep final_trial impact** - It's the climax and should matter
2. **Minor adjustments**: Consider +1 or +2 boosts in early game for struggling players
3. **Testing needed**: Verify all 14 endings are reachable via natural play

### Difficulty Curve
- **Early Game** (arrival - first_lesson): Easy to gain +20 to +35 Collaboration
- **Mid Game** (academy_life - expedition): Steady +10 to +20 available
- **Late Game** (final_trial): High stakes, ±50 potential swing
- **Total Range**: Realistic playthrough ranges from 30 to 95 Collaboration

---

## Usage Guidelines for AI Collaborators

### Lore Curator
- Ensure stat changes make narrative sense
- Flag any stat boost that contradicts character moment

### Conversion Engineer
- Copy stat changes exactly from HTML version when converting
- Note any deviations in this file

### Structural Reviewer
- Verify stat totals match between HTML and ChoiceScript
- Check threshold accessibility (all endings reachable)

### Quality Balancer
- Use this matrix to identify outliers
- Suggest adjustments to thresholds if paths too hard/easy
- Monitor playtest feedback on stat progression

---

## Change Log

### November 25, 2025
- Initial creation of STATS_MATRIX.md
- Documented all collaboration stat changes across all scenes
- Established ending threshold requirements
- Mapped relationship progression paths

### Future Updates
- Add playtest data (average Collaboration reached per path)
- Document any threshold adjustments based on testing
- Track which endings are most/least commonly achieved

---

**Last Updated**: November 25, 2025
**Maintained By**: Quality Balancer + Structural Reviewer
**Review Frequency**: After any scene modification or threshold change
