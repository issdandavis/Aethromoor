# Stats Matrix - Collaboration & Relationship Tracking

**Purpose:** Track all stat changes across scenes to ensure balanced progression and fair difficulty.

**Last Updated:** 2025-11-23 10:17 UTC

---

## 📊 Primary Stats Overview

| Stat Name | Range | Starting Value | Purpose |
|-----------|-------|----------------|---------|
| **collaboration** | 0-100 | 50 | Core mechanic - collaborative vs hierarchical magic |
| **izack_relationship** | 0-100 | 30 | Relationship with Headmaster Izack |
| **aria_relationship** | 0-100 | 30 | Relationship with Aria (ice mage) |
| **zara_relationship** | 0-100 | 30 | Relationship with Zara (researcher) |
| **kael_relationship** | 0-100 | 30 | Relationship with Kael (desert guide) |
| **polly_relationship** | 0-100 | 50 | Relationship with Polly (familiar) |

---

## 🎯 Stat Changes by Scene

### Startup & Character Creation
| Choice | Collaboration Δ | Relationships Δ | Source File |
|--------|-----------------|-----------------|-------------|
| Create character | 0 | All start at 30 (Polly at 50) | `startup.txt` |

---

### Arrival Scenes
| Choice | Collaboration Δ | Relationships Δ | Source File |
|--------|-----------------|-----------------|-------------|
| Portal arrival (confident) | +3 | Izack +5 | `arrival.txt` |
| Guided arrival (cautious) | +5 | Aria +5 | `arrival.txt` |
| Storm arrival (adaptable) | +5 | Zara +5 | `arrival.txt` |

**Analysis:** All paths give +3 to +5 Collaboration, balanced start

---

### Dorm Room Customization
| Choice | Collaboration Δ | Relationships Δ | Source File |
|--------|-----------------|-----------------|-------------|
| All choices | 0 | 0 | `dorm_room.txt` |

**Analysis:** Flavor choices only, no stat impact

---

### First Lesson
| Choice | Collaboration Δ | Relationships Δ | Source File |
|--------|-----------------|-----------------|-------------|
| Listen first (collaborative) | +10 | Aria +5 | `first_lesson.txt` |
| Speak up (assertive) | +5 | Izack +5 | `first_lesson.txt` |
| Force magic (hierarchical) | +0 | Aria -5 | `first_lesson.txt` |
| Perfect collaboration | +15 | Aria +10, Izack +5 | `first_lesson.txt` |

**Analysis:** Strong incentive for collaboration (+15 max), penalties for forcing (-5 relationship)

**Running Total After First Lesson:**
- **Best path:** 50 + 5 (arrival) + 15 (lesson) = **70 Collaboration**
- **Worst path:** 50 + 3 (arrival) + 0 (lesson) = **53 Collaboration**

---

### Singing Dunes Expedition
| Choice | Collaboration Δ | Relationships Δ | Source File | Status |
|--------|-----------------|-----------------|-------------|---------|
| *To be mapped* | ❓ | ❓ | `singing_dunes.txt` | ❌ Not Created |

**Expected Thresholds:**
- **Truth Acceptance:** Collaboration > 60 required
- **Kael Partnership:** Kael relationship > 40
- **Truthbound Ending:** Collaboration > 70 + complete oath sequence

**TODO:** Conversion Engineer should map all stat changes when creating scene

---

### Verdant Tithe Expedition
| Choice | Collaboration Δ | Relationships Δ | Source File | Status |
|--------|-----------------|-----------------|-------------|---------|
| *To be mapped* | ❓ | ❓ | `verdant_tithe.txt` | ❌ Not Created |

**Expected Thresholds:**
- **Thoughtvine Path:** Collaboration > 55
- **Dreamwillow Path:** Collaboration > 65
- **Heartwood Path:** Collaboration > 75 (highest requirement)

**TODO:** Map three distinct paths with different stat requirements

---

### Rune Glacier Expedition
| Choice | Collaboration Δ | Relationships Δ | Source File | Status |
|--------|-----------------|-----------------|-------------|---------|
| *To be mapped* | ❓ | ❓ | `rune_glacier.txt` | ❌ Not Created |

**Expected Thresholds:**
- **Control Path (Runeweaver):** Collaboration < 50
- **Harmony Path (Partner):** Collaboration > 70
- **Aria Mentorship:** Aria relationship > 50

**TODO:** Ensure control/harmony paths have clear stat divergence

---

## 🎯 Ending Requirements

### High Collaboration Endings

| Ending Name | Collaboration Required | Other Requirements | Priority |
|-------------|------------------------|-------------------|----------|
| **Collaborative Master** | > 85 | All relationships > 60 | Highest achievement |
| **Heartwood Guardian** | > 75 | Verdant Tithe + special choice | Expedition-specific |
| **Glacier Partner** | > 70 | Rune Glacier harmony path | Expedition-specific |
| **Truthbound Mage** | > 70 | Singing Dunes oath path | Expedition-specific |
| **Collaborative Scholar** | > 65 | No specific expedition | General good ending |
| **Balanced Mage** | 55-70 | Balanced relationships | Neutral ending |

### Low Collaboration Endings

| Ending Name | Collaboration Required | Other Requirements | Type |
|-------------|------------------------|-------------------|------|
| **Runeweaver** | < 50 | Rune Glacier control path | Hierarchical success |
| **Boundary Specialist** | 40-55 | Independent choices | Solo practitioner |
| **Humble Seeker** | 30-50 | Low but not failing | Learning path |
| **Second Chance** | 25-40 | Failed then recovered | Redemption |
| **Humbled Student** | 15-30 | Multiple failures | Warning ending |
| **Expelled** | < 15 | Critical failures | Bad ending |

### Special Endings

| Ending Name | Requirements | Notes |
|-------------|--------------|-------|
| **Forestbound Guardian** | Verdant Tithe + Collab > 60 | Expedition-specific |
| **Standard Path** | Any middle-range stats | Default ending |

---

## 📈 Progression Analysis

### Ideal Collaborative Path
```
Start: 50
+ Arrival (guided): 50 + 5 = 55
+ First Lesson (perfect): 55 + 15 = 70
+ Expedition choices: 70 + 10-15 = 80-85
= Eligible for top endings
```

### Balanced Path
```
Start: 50
+ Arrival (portal): 50 + 3 = 53
+ First Lesson (speak): 53 + 5 = 58
+ Expedition choices: 58 + 7-10 = 65-68
= Eligible for middle endings
```

### Hierarchical Path
```
Start: 50
+ Arrival (confident): 50 + 3 = 53
+ First Lesson (force): 53 + 0 = 53
+ Expedition (control): 53 - 5 = 48
= Eligible for control/solo endings
```

---

## ⚖️ Balance Recommendations

### For Quality Balancer Role

**Current Analysis:**
- Starting value (50) is good midpoint
- First lesson offers biggest single boost (+15)
- Need expedition scenes to provide 15-20 points total
- Endings span full range (0-100) appropriately

**Recommendations:**
1. **Expeditions should offer:** 15-20 points total across all choices
2. **Each expedition path:** Should have 3-5 major stat changes
3. **Penalties:** Should be rare but meaningful (-5 max per choice)
4. **Hidden bonuses:** For especially clever collaborative solutions

**Threshold Testing:**
- [ ] Test all 14 endings are reachable
- [ ] Verify no ending requires perfect play
- [ ] Check that collaborative path isn't too easy
- [ ] Ensure hierarchical path is viable alternative

---

## 🔢 Stat Change Patterns

### Small Changes (1-3 points)
- Minor dialogue choices
- Flavor text selections
- Low-stakes decisions
- **Example:** Asking Polly for advice (+2)

### Medium Changes (5-10 points)
- Significant choices
- Expedition decision points
- Character interactions
- **Example:** First lesson collaboration (+10)

### Large Changes (10-15 points)
- Major story beats
- Perfect execution bonuses
- Critical decisions
- **Example:** First lesson perfect collab (+15)

### Penalties (-5 to -10 points)
- Rejecting collaboration
- Forcing hierarchical magic
- Betraying trust
- **Example:** Forcing magic in lesson (-5 Aria)

---

## 📝 Template for Adding New Stat Changes

When creating/converting scenes, use this format:

```markdown
### [Scene Name]
| Choice | Collaboration Δ | Relationships Δ | Source File |
|--------|-----------------|-----------------|-------------|
| [Choice text] | +X | [Character] +Y | `scene.txt` |
| [Choice text] | -X | [Character] -Y | `scene.txt` |
```

**Then update:**
1. Running totals section
2. Ending requirements if affected
3. Balance recommendations

---

## 🎮 Playtesting Scenarios

### Scenario 1: Maximum Collaboration
- All collaborative choices
- Expected final score: 85-90
- Should unlock: Collaborative Master

### Scenario 2: Balanced Player
- Mix of collaborative and independent
- Expected final score: 60-70
- Should unlock: Balanced Mage or Collaborative Scholar

### Scenario 3: Hierarchical Approach
- Control-focused choices
- Expected final score: 40-50
- Should unlock: Runeweaver or Boundary Specialist

### Scenario 4: Struggling Student
- Mistakes but trying
- Expected final score: 30-40
- Should unlock: Humble Seeker or Second Chance

---

## 🚨 Red Flags to Watch For

- **Too Easy:** Player reaches 85+ without trying
- **Too Hard:** Player can't reach 70 with best choices
- **Dead Zone:** Stat ranges that don't lead to any ending
- **Soft Lock:** Expedition requires stats impossible to have at that point
- **Runaway:** Early choices make later choices meaningless

---

## 🤝 Collaboration Notes

**For Conversion Engineers:**
- Log ALL stat changes as you convert scenes
- Mark "❓" for estimated values, update after testing
- Note any thresholds you add

**For Quality Balancers:**
- Review this matrix after all expeditions converted
- Test each ending is achievable
- Adjust thresholds as needed
- Update recommendations section

**For Structural Reviewers:**
- Verify stat changes match HTML source
- Flag any missing stat tracking
- Check threshold logic is sound

---

*This matrix grows as scenes are converted. Keep it updated!*
