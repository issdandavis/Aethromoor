# 📊 STATS MATRIX
## Game Statistics Tracking & Balance

**Purpose:** Track all stat changes, thresholds, and balance across the game.

**Last Updated:** 2025-11-22 04:03 UTC  
**Updated By:** GitHub Copilot

---

## 🎮 CORE STATISTICS

### Primary Stat: Collaboration
**Range:** 0-100  
**Starting Value:** 50 (neutral)  
**Purpose:** Measures player's approach to magic (collaborative vs hierarchical)

**Thresholds:**
- **80-100:** Highly collaborative (best endings)
- **60-79:** Moderately collaborative (good endings)
- **40-59:** Neutral/balanced (mixed endings)
- **20-39:** Moderately hierarchical (challenging endings)
- **0-19:** Highly hierarchical (failure endings)

### Relationship Stats
**Range:** 0-100 each  
**Starting Value:** 0 (unknown)  
**Tracked Relationships:**
- Aria Ravencrest (mentor)
- Zara (peer student)
- Polly (companion)
- Kael (desert guide) - if Singing Dunes chosen
- Forest entities - if Verdant Tithe chosen
- Glacier - if Rune Glacier chosen

---

## 📋 STAT CHANGE LOG

### Opening Sequence
| Choice | Source File | Collaboration Δ | Relationships Δ | Notes |
|--------|-------------|-----------------|-----------------|-------|
| Polly introduction responses | startup.txt | 0 | Polly +5 to +10 | Flavor only, no major impact |
| Understanding dimensional theory | startup.txt | 0 | Polly +5 | Shows intellectual engagement |

### Arrival Paths
| Choice | Source File | Collaboration Δ | Relationships Δ | Notes |
|--------|-------------|-----------------|-----------------|-------|
| Diplomatic arrival | arrival.txt | +5 | Aria +10 | Respectful approach |
| Confident arrival | arrival.txt | 0 | Aria +5 | Neutral impression |
| Humble arrival | arrival.txt | +10 | Aria +15 | Shows openness to learning |

### First Lesson
| Choice | Source File | Collaboration Δ | Relationships Δ | Notes |
|--------|-------------|-----------------|-----------------|-------|
| Listen to Zara's ideas | first_lesson.txt | +10 | Zara +15 | Key collaborative moment |
| Ignore Zara's ideas | first_lesson.txt | -10 | Zara -15 | Hierarchical approach |
| Work together equally | first_lesson.txt | +15 | Zara +20 | Best collaborative outcome |
| Take control of spell | first_lesson.txt | -15 | Zara -20 | Hierarchical approach |
| Share control of spell | first_lesson.txt | +10 | Zara +15 | Collaborative approach |
| Acknowledge failure together | first_lesson.txt | +5 | Zara +10 | Graceful response |
| Blame Zara for failure | first_lesson.txt | -15 | Zara -25 | Toxic response |

### Expedition Selection
| Choice | Source File | Collaboration Δ | Relationships Δ | Notes |
|--------|-------------|-----------------|-----------------|-------|
| Choose Singing Dunes | expedition_choice.txt | 0 | 0 | Opens Kael relationship track |
| Choose Verdant Tithe | expedition_choice.txt | 0 | 0 | Opens forest relationship tracks |
| Choose Rune Glacier | expedition_choice.txt | 0 | 0 | Develops Aria relationship further |

---

## 🏜️ SINGING DUNES STAT CHANGES

**Status:** ⏳ Not yet implemented  
**Source File:** `choicescript_game/scenes/singing_dunes.txt` (to be created)

### Expected Stat Changes:
| Choice Point | Collaboration Δ | Relationships Δ | Notes |
|--------------|-----------------|-----------------|-------|
| First meeting with Kael | 0 | Kael +10 | Introduction |
| Truth-testing: Tell full truth | +15 | Kael +20 | Core collaborative moment |
| Truth-testing: Partial truth | 0 | Kael -10 | Hedging approach |
| Truth-testing: Lie | -20 | Kael -30 | Hierarchical/deceptive |
| Accept truth-sworn sand | +10 | Kael +15 | Shows trust |
| Refuse truth-sworn sand | -5 | Kael -15 | Shows distrust |
| Learn oath-magic collaboratively | +15 | Kael +20 | Collaborative learning |
| Try to control oath-magic | -15 | Kael -20 | Hierarchical approach |
| Desert accepts you | +20 | Kael +25 | Major success |
| Desert rejects you | -10 | Kael -10 | Learning moment |

**Threshold for Truthbound Mage Ending:**
- Collaboration >= 70
- Kael >= 60
- Truth-testing success required

---

## 🌲 VERDANT TITHE STAT CHANGES

**Status:** ⏳ Not yet implemented  
**Source File:** `choicescript_game/scenes/verdant_tithe.txt` (to be created)

### Expected Stat Changes:
| Choice Point | Collaboration Δ | Relationships Δ | Notes |
|--------------|-----------------|-----------------|-------|
| Enter forest respectfully | +10 | Forest +10 | Collaborative approach |
| Enter forest boldly | -5 | Forest -5 | Hierarchical approach |
| Listen to Thoughtvine | +15 | Thoughtvine +20 | Collaborative learning |
| Resist Thoughtvine | -10 | Thoughtvine -15 | Hierarchical resistance |
| Accept Dreamwillow vision | +10 | Dreamwillow +20 | Openness to experience |
| Reject Dreamwillow vision | -5 | Dreamwillow -10 | Closed approach |
| Protect Heartwood Tree | +15 | Heartwood +25 | Guardian role |
| Seek to use Heartwood | -15 | Heartwood -25 | Extractive approach |
| Choose Dreamwillow path | +5 | Dreamwillow +30 | Vision specialty |
| Choose Thoughtvine path | +10 | Thoughtvine +30 | Mind specialty |
| Choose Heartwood path | +15 | Heartwood +30 | Protection specialty |

**Thresholds for Forest Endings:**
- **Forestbound Guardian:** Collaboration >= 70, any forest relationship >= 50
- **Heartwood Guardian:** Heartwood >= 70, Heartwood path chosen
- **Dreamwillow Path:** Dreamwillow >= 60, vision focus

---

## ❄️ RUNE GLACIER STAT CHANGES

**Status:** ⏳ Not yet implemented  
**Source File:** `choicescript_game/scenes/rune_glacier.txt` (to be created)

### Expected Stat Changes:
| Choice Point | Collaboration Δ | Relationships Δ | Notes |
|--------------|-----------------|-----------------|-------|
| Approach glacier with respect | +10 | Glacier +10, Aria +5 | Collaborative start |
| Approach glacier with confidence | 0 | Aria +5 | Neutral start |
| Try to control living ice | -15 | Glacier -20, Aria -10 | Hierarchical approach |
| Work with living ice | +15 | Glacier +20, Aria +10 | Collaborative approach |
| Learn from Aria's guidance | +10 | Aria +15 | Mentorship acceptance |
| Ignore Aria's guidance | -10 | Aria -15 | Independent (hierarchical) |
| Study frozen spell library | +5 | Aria +10 | Academic approach |
| Seek glacier partnership | +20 | Glacier +30, Aria +15 | Major collaborative moment |
| Choose control path | -20 | Glacier -30, Aria -10 | Hierarchical mastery |
| Choose harmony path | +20 | Glacier +25, Aria +15 | Collaborative mastery |
| Choose partnership path | +25 | Glacier +40, Aria +20 | Ultimate collaborative path |

**Thresholds for Glacier Endings:**
- **Runeweaver:** Collaboration >= 60, rune mastery focus
- **Glacier Partner:** Glacier >= 80, partnership path chosen
- **Balanced Mage:** Collaboration 50-70, multiple approaches

---

## 🏆 ENDING REQUIREMENTS

### High Collaboration Endings

#### Collaborative Master
**Requirements:**
- Collaboration >= 85
- All three expeditions completed
- At least two relationships >= 70
**Source File:** `endings.txt` (to be created)

#### Collaborative Scholar
**Requirements:**
- Collaboration >= 75
- Academic achievements (library visits, study choices)
- Aria >= 60
**Source File:** `endings.txt`

### Specialty Endings

#### Truthbound Mage
**Requirements:**
- Collaboration >= 70
- Kael >= 60
- Singing Dunes expedition completed successfully
- Truth-testing passed
**Source File:** `endings.txt`

#### Forestbound Guardian
**Requirements:**
- Collaboration >= 70
- Any forest entity >= 50
- Verdant Tithe expedition completed
**Source File:** `endings.txt`

#### Heartwood Guardian
**Requirements:**
- Heartwood >= 70
- Heartwood path chosen in Verdant Tithe
- Protection focus
**Source File:** `endings.txt`

#### Runeweaver
**Requirements:**
- Collaboration >= 60
- Rune Glacier expedition completed
- Rune mastery focus
**Source File:** `endings.txt`

#### Glacier Partner
**Requirements:**
- Glacier >= 80
- Partnership path chosen in Rune Glacier
- Collaboration >= 75
**Source File:** `endings.txt`

### Balanced Endings

#### Balanced Mage
**Requirements:**
- Collaboration 50-70
- Multiple expedition paths experienced
- No extreme relationship scores
**Source File:** `endings.txt`

#### Boundary Specialist
**Requirements:**
- Aria >= 70
- Boundary magic focus
- Collaboration >= 60
**Source File:** `endings.txt`

### Humble Endings

#### Humble Seeker
**Requirements:**
- Humble arrival chosen
- Collaboration >= 60
- No hierarchical choices
**Source File:** `endings.txt`

#### Second Chance
**Requirements:**
- Failed at least one major challenge
- Recovered gracefully (acknowledged failure, learned)
- Collaboration >= 50
**Source File:** `endings.txt`

### Low Collaboration Endings

#### Humbled Student
**Requirements:**
- Collaboration 30-49
- At least one relationship >= 40 (shows growth)
- Learning moment acknowledged
**Source File:** `endings.txt`

#### Expelled (Failure)
**Requirements:**
- Collaboration < 30
- Multiple hierarchical choices
- Low relationships across the board
**Source File:** `endings.txt`

### Neutral Ending

#### Standard Path
**Requirements:**
- None of the above requirements met
- Collaboration 40-60
- Neutral choices throughout
**Source File:** `endings.txt`

---

## ⚖️ BALANCE ANALYSIS

### Current Balance Issues:
- ⏳ Not yet tested (expeditions not implemented)

### Balance Goals:
1. **No Impossible Paths:** Every ending should be achievable with consistent choices
2. **Clear Signaling:** Players should understand which path they're on
3. **Meaningful Choices:** Stat changes should feel impactful but not punishing
4. **Recovery Possible:** One bad choice shouldn't lock out good endings
5. **Failure Avoidable:** Expelled ending should require consistent poor choices

### Balance Testing Checklist:
- [ ] Play through with only collaborative choices - should reach Collaborative Master
- [ ] Play through with only hierarchical choices - should reach Expelled
- [ ] Play through with mixed choices - should reach Balanced Mage or similar
- [ ] Test each specialty path (Singing Dunes, Verdant Tithe, Rune Glacier)
- [ ] Verify all 14 endings are reachable with realistic stat combinations

---

## 🔢 STAT MATH

### Collaboration Stat Pathways

**Maximum Possible Collaboration (Perfect Collaborative Run):**
- Start: 50
- Humble arrival: +10 (60)
- First lesson (all collaborative): +35 (95)
- Singing Dunes (all collaborative): +60 (155, capped at 100)
- **Result:** 100 (easily achieves Collaborative Master)

**Minimum Possible Collaboration (Perfect Hierarchical Run):**
- Start: 50
- Confident arrival: 0 (50)
- First lesson (all hierarchical): -40 (10)
- Singing Dunes (all hierarchical): -50 (-40, capped at 0)
- **Result:** 0 (Expelled ending)

**Neutral Path:**
- Start: 50
- Mix of collaborative/hierarchical: 0 (50)
- **Result:** 40-60 range (Standard Path or Balanced Mage)

### Relationship Math

**Maximum Relationship (e.g., Aria):**
- Humble arrival: +15
- First lesson collaborative: +15
- Rune Glacier (all partnership): +60
- **Total:** 90 (achievable)

**Minimum Relationship:**
- Confident arrival: +5
- No interaction: 0
- **Total:** 5 (low but not negative)

---

## 📊 PLAYTESTING TRACKER

### Test Runs:
| Run # | Focus | Collaboration End | Key Relationships | Ending Achieved | Issues Found |
|-------|-------|-------------------|-------------------|-----------------|--------------|
| 1 | TBD | TBD | TBD | TBD | TBD |

*(To be filled in during playtesting)*

---

## 🔄 UPDATE LOG

**2025-11-22:** Initial stats matrix created with expected values  
**Next Update:** When Singing Dunes is implemented and tested

---

## 📝 NOTES FOR BALANCERS

### When Implementing Stat Changes:
1. Consider player intent (what feels collaborative vs hierarchical)
2. Make consequences clear in narrative
3. Don't punish exploration (minor stat hits acceptable)
4. Reward consistency (multiple collaborative choices should stack)
5. Allow recovery (one bad choice shouldn't doom run)

### When Testing Balance:
1. Play through multiple times with different approaches
2. Document actual Collaboration values at each point
3. Verify ending thresholds are appropriate
4. Adjust if paths feel impossible or too easy
5. Update this matrix with actual tested values

### When Updating This File:
1. Mark expected values vs tested values clearly
2. Document any threshold adjustments
3. Note balance issues found
4. Update ending requirements if needed
5. Cross-reference with SCENE_PARITY_CHECKLIST.md

---

**Remember:** Good balance means player choices matter, paths are achievable, and the story feels responsive to decisions.

*"Every choice shifts the spiral. Balance makes the story."* 🌀
