# Stats Matrix - Choice Impact Tracking

**Purpose**: Document all stat-affecting choices and ending thresholds for gameplay balance

**Stat Key**:
- **Collaboration**: 0-100 (main gameplay stat)
- **Relationships**: -10 to +10 (Aria, Zara, Polly, Kael, etc.)

---

## Opening Sequence

### Character Creation
| Source File | Choice Description | Collab | Aria | Zara | Polly | Notes |
|------------|-------------------|--------|------|------|-------|-------|
| character_creation.txt | Initial stats | 50 | 0 | 0 | 0 | Starting baseline |

### Arrival Paths
| Source File | Choice Description | Collab | Aria | Zara | Polly | Notes |
|------------|-------------------|--------|------|------|-------|-------|
| arrival_teleport.txt | Arrive via teleport | 0 | +1 | 0 | +1 | Precision approach |
| arrival_walk.txt | Walk through dimension | +2 | 0 | 0 | +1 | Patient, observant |
| arrival_fly.txt | Fly with dimensional aid | +1 | 0 | 0 | +2 | Partnership with magic |

---

## First Lesson (Tutorial)

### Core Collaboration Choices
| Source File | Choice Description | Collab | Aria | Zara | Polly | Notes |
|------------|-------------------|--------|------|------|-------|-------|
| first_lesson.txt | Collaborate with magic | +5 | +1 | 0 | +1 | Major positive, teaches philosophy |
| first_lesson.txt | Command/force magic | -5 | -1 | 0 | 0 | Major negative, hierarchical approach |
| first_lesson.txt | Ask Aria for help | +2 | +2 | 0 | +1 | Seeking guidance, builds relationship |
| first_lesson.txt | Experiment independently | +1 | 0 | +1 | +1 | Shows initiative, Zara approves |
| first_lesson.txt | Listen to Polly's advice | +3 | 0 | 0 | +2 | Trusts mentor wisdom |
| first_lesson.txt | Ignore Polly's advice | -2 | 0 | 0 | -1 | Polly is slightly annoyed |

### Recovery/Redemption Options
| Source File | Choice Description | Collab | Aria | Zara | Polly | Notes |
|------------|-------------------|--------|------|------|-------|-------|
| first_lesson.txt | Acknowledge mistake after forcing | +3 | +1 | 0 | +1 | Redemption opportunity |
| first_lesson.txt | Double down on control | -3 | -2 | 0 | -1 | Refuses to learn |

---

## Singing Dunes Expedition

### Desert Approach Choices
| Source File | Choice Description | Collab | Kael | Notes |
|------------|-------------------|--------|------|-------|
| singing_dunes.txt | Respect desert's truth-magic | +5 | +2 | Sets up "truth" path |
| singing_dunes.txt | Try to control desert magic | -5 | -2 | Sets up "control" path |
| singing_dunes.txt | Reject oath-magic entirely | -3 | -3 | Sets up "rejection" path |

### Truth-Testing Challenges
| Source File | Choice Description | Collab | Kael | Notes |
|------------|-------------------|--------|------|-------|
| singing_dunes.txt | Speak honest truth (difficult) | +5 | +3 | Truth path, high reward |
| singing_dunes.txt | Speak partial truth (easier) | +2 | +1 | Compromise, less impact |
| singing_dunes.txt | Attempt deception | -7 | -4 | Desert punishes lies |

### Kael Relationship Builders
| Source File | Choice Description | Collab | Kael | Notes |
|------------|-------------------|--------|------|-------|
| singing_dunes.txt | Ask about desert culture | +1 | +2 | Shows respect, builds rapport |
| singing_dunes.txt | Work collaboratively with Kael | +3 | +2 | Partnership approach |
| singing_dunes.txt | Dismiss Kael's guidance | -2 | -3 | Arrogance, damages relationship |

**Path Outcome Impact**:
- **Truth Path** (Kael +6 or more): Access to `ending_truthbound_mage.txt`
- **Control Path** (Collab negative net): Access to control-based endings
- **Rejection Path** (Kael -5 or worse): Access to `ending_humbled_student.txt`

---

## Verdant Tithe Expedition

### Forest Entry Choices
| Source File | Choice Description | Collab | Plant Affinity | Notes |
|------------|-------------------|--------|----------------|-------|
| verdant_tithe.txt | Open mind to forest consciousness | +4 | Thoughtvine +1 | Intellectual connection |
| verdant_tithe.txt | Open heart to forest | +4 | Dreamwillow +1 | Emotional connection |
| verdant_tithe.txt | Seek forest's core truth | +4 | Heartwood +1 | Deep authenticity |
| verdant_tithe.txt | Maintain emotional distance | 0 | All -1 | Forest senses disconnection |

### Plant Entity Partnerships
| Source File | Choice Description | Collab | Outcome | Notes |
|------------|-------------------|--------|---------|-------|
| verdant_tithe.txt | Partner with Thoughtvine | +5 | Thoughtvine path | Intellectual collaboration |
| verdant_tithe.txt | Partner with Dreamwillow | +5 | Dreamwillow path | Subconscious collaboration |
| verdant_tithe.txt | Partner with Heartwood | +5 | Heartwood path | Core truth collaboration |
| verdant_tithe.txt | Refuse forest partnership | -6 | Rejection | Forest turns away |

**Path Outcome Impact**:
- **Thoughtvine Path**: Access to `ending_forestbound_guardian.txt`
- **Dreamwillow Path**: Access to `ending_dreamweaver.txt`
- **Heartwood Path**: Access to `ending_heartwood_guardian.txt`

---

## Rune Glacier Expedition

### Ice Approach Choices
| Source File | Choice Description | Collab | Aria | Notes |
|------------|-------------------|--------|------|-------|
| rune_glacier.txt | Work with living ice collaboratively | +5 | +2 | Harmony path |
| rune_glacier.txt | Master ice through precision control | +2 | +3 | Control path (Aria approves precision) |
| rune_glacier.txt | Seek glacier's mysterious partnership | +6 | +1 | Mystery path, deepest collaboration |
| rune_glacier.txt | Force ice to obey | -5 | -2 | Hierarchical, fails Aria's teaching |

### Memory Crystal Interaction
| Source File | Choice Description | Collab | Outcome | Notes |
|------------|-------------------|--------|---------|-------|
| rune_glacier.txt | Study with respect | +3 | Knowledge +2 | Learns from frozen library |
| rune_glacier.txt | Try to take/possess knowledge | -4 | Knowledge +0 | Glacier resists theft |
| rune_glacier.txt | Ask glacier to share | +5 | Knowledge +3 | Partnership yields more |

### Aria's Lessons
| Source File | Choice Description | Collab | Aria | Notes |
|------------|-------------------|--------|------|-------|
| rune_glacier.txt | Apply Aria's precision teaching | +3 | +3 | Demonstrates learning |
| rune_glacier.txt | Blend precision with partnership | +5 | +2 | Synthesizes teachings |
| rune_glacier.txt | Ignore precision for pure collaboration | +2 | -1 | Well-intentioned but misses lesson |

**Path Outcome Impact**:
- **Control Path** (high Aria, medium Collab): Access to `ending_runeweaver.txt`
- **Harmony Path** (high Collab, all expeditions): Access to `ending_collaborative_master.txt`
- **Mystery Path** (very high Collab, glacier partnership): Access to `ending_glacier_partner.txt`

---

## Ending Thresholds

### Major Endings (Specialist Paths)

| Ending Name | Collaboration | Relationships | Expedition Flags | Additional Requirements |
|------------|---------------|---------------|------------------|------------------------|
| **Collaborative Master** | ≥85 | N/A | All 3 complete | glacier_path = "harmony" |
| **Truthbound Mage** | ≥60 | Kael ≥6 | Dunes complete | dunes_path = "truth" |
| **Forestbound Guardian** | ≥60 | N/A | Forest complete | forest_path = "thoughtvine" |
| **Heartwood Guardian** | ≥60 | N/A | Forest complete | forest_path = "heartwood" |
| **Dreamweaver** | ≥60 | N/A | Forest complete | forest_path = "dreamwillow" |
| **Runeweaver** | ≥60 | Aria ≥6 | Glacier complete | glacier_path = "control" |
| **Glacier Partner** | ≥70 | N/A | Glacier complete | glacier_path = "mystery" |

### Balanced/Growth Endings

| Ending Name | Collaboration | Relationships | Expedition Flags | Notes |
|------------|---------------|---------------|------------------|-------|
| **Balanced Mage** | 40-60 | N/A | 2+ complete | No extreme paths chosen |
| **Boundary Specialist** | ≥50 | Aria ≥8 | 1+ complete | Aria's protégé |
| **Collaborative Scholar** | 50-70 | Polly ≥6 | 1+ complete | Research-focused |
| **Humble Seeker** | 30-50 | N/A | 1+ complete | Acknowledges limitations |

### Redemption/Learning Endings

| Ending Name | Collaboration | Relationships | Expedition Flags | Notes |
|------------|---------------|---------------|------------------|-------|
| **Second Chance** | <40 but improving | N/A | 1+ complete | Showed growth from failures |
| **Humbled Student** | <30 | Any negative | 1+ complete | Learned humility through struggle |
| **Standard Path** | 35-65 | Neutral (±2) | 1+ complete | Completed but unremarkable |

### Failure State
| Ending Name | Collaboration | Relationships | Expedition Flags | Notes |
|------------|---------------|---------------|------------------|-------|
| **Expelled** | <20 | Multiple -5 | 0 complete | Refused to learn, expelled from academy |

---

## Stat Progression Balance Analysis

### Collaboration Opportunities by Expedition

**First Lesson (Tutorial)**:
- Maximum gain: +16 (all positive choices)
- Maximum loss: -17 (all negative choices)
- Typical range: +8 to +12 (mixed choices)

**Singing Dunes**:
- Maximum gain: +15 (truth path, all positive)
- Maximum loss: -15 (rejection/control path)
- Typical range: +5 to +10 (truth-leaning)

**Verdant Tithe**:
- Maximum gain: +18 (partnership path)
- Maximum loss: -10 (rejection path)
- Typical range: +10 to +15 (partnership-oriented)

**Rune Glacier**:
- Maximum gain: +19 (mystery/harmony path)
- Maximum loss: -9 (force/control path)
- Typical range: +8 to +14 (precision-collaboration blend)

### Reaching Key Thresholds

**For Collaborative Master (85+)**:
- Starting: 50
- Need: +35
- Requires: Consistently positive choices across all expeditions
- Achievable: Yes, with ~75% positive choices

**For Balanced Mage (40-60)**:
- Starting: 50
- Need: -10 to +10
- Requires: Mixed choices or neutral path
- Achievable: Yes, natural for exploratory players

**For Humbled Student (<30)**:
- Starting: 50
- Need: -20 or more
- Requires: Consistently negative choices
- Achievable: Yes, but requires deliberate poor choices

### Balance Recommendations

✅ **Well-Balanced**:
- Multiple paths to each ending
- Redemption opportunities exist
- No ending impossible to reach
- Player agency respected

⚠️ **Watch Areas**:
- Verdant Tithe may give too many positive points (consider reducing some +4 to +3)
- Collaborative Master threshold might be slightly too easy (consider raising to 88-90)
- Expelled threshold might be too harsh (consider -5 relationship requirement instead of multiple)

---

## Testing Scenarios

### Scenario 1: "Pure Collaborator"
- All positive collaboration choices
- Expected end Collaboration: ~98
- Expected ending: Collaborative Master (if glacier="harmony")

### Scenario 2: "Balanced Explorer"
- Mix of choices, mostly neutral
- Expected end Collaboration: ~55
- Expected ending: Balanced Mage or Standard Path

### Scenario 3: "Redemption Arc"
- Start with control/force choices (Collab drops to ~35)
- Switch to collaborative after First Lesson
- Expected end Collaboration: ~65
- Expected ending: Second Chance or Humble Seeker

### Scenario 4: "Specialist"
- Focus on one expedition path (e.g., Truth in Dunes)
- Moderate collaboration overall (~65)
- Expected ending: Truthbound Mage

---

**Last Updated**: November 23, 2025  
**Next Review**: After Singing Dunes balancing pass  
**Maintained By**: Quality Balancer role
