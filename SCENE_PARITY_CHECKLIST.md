# Scene Parity Checklist

**Purpose:** Track conversion status between HTML and ChoiceScript versions to ensure identical game experiences.

**Last Updated:** 2025-11-23 10:17 UTC

---

## 📋 Scene Comparison Status

| HTML Scene | ChoiceScript File | Status | Endings Count | Choices Match | Stats Match | Verified By |
|-----------|------------------|--------|---------------|---------------|-------------|-------------|
| Introduction | `startup.txt` | ✅ Complete | N/A | ✅ Yes | ✅ Yes | Initial |
| Polly Introduction | `startup.txt` | ✅ Complete | N/A | ✅ Yes | ✅ Yes | Initial |
| Arrival Paths (3) | `arrival.txt` | ✅ Complete | 3 | ✅ Yes | ✅ Yes | Initial |
| Dorm Room | `dorm_room.txt` | ✅ Complete | N/A | ✅ Yes | ✅ Yes | Initial |
| First Lesson | `first_lesson.txt` | ✅ Complete | N/A | ✅ Yes | ✅ Yes | Initial |
| Academy Life | `academy_life.txt` | ✅ Complete | N/A | ✅ Yes | ✅ Yes | Initial |
| Expedition Prep | `expedition_prep.txt` | ✅ Complete | N/A | ✅ Yes | ✅ Yes | Initial |
| **Singing Dunes** | `singing_dunes.txt` | ❌ Missing | Unknown | ❓ Unknown | ❓ Unknown | - |
| **Verdant Tithe** | `verdant_tithe.txt` | ❌ Missing | Unknown | ❓ Unknown | ❓ Unknown | - |
| **Rune Glacier** | `rune_glacier.txt` | ❌ Missing | Unknown | ❓ Unknown | ❓ Unknown | - |
| Character Bonds | `character_bonds.txt` | ⚠️ Draft | N/A | ❓ Unknown | ❓ Unknown | - |
| Final Trial | `final_trial.txt` | ⚠️ Draft | N/A | ❓ Unknown | ❓ Unknown | - |
| **All Endings (14)** | `endings.txt` | ❌ Missing | 14 | ❓ Unknown | ❓ Unknown | - |

---

## 🎯 Legend

- ✅ **Complete** - Scene fully converted and verified
- ⚠️ **Draft** - Scene exists but needs verification
- ❌ **Missing** - Scene not yet created
- ❓ **Unknown** - Status needs to be checked

---

## 📊 Detailed Scene Breakdown

### ✅ Completed Scenes

#### Startup & Introduction
- **HTML Location:** Beginning of `game/game.js`
- **ChoiceScript:** `startup.txt`
- **Choices:** Character creation, name, starting stats
- **Stats Initialized:** Collaboration, relationships (Izack, Aria, Zara, Kael, Polly)
- **Branches:** Linear introduction
- **Verified:** Initial setup

#### Arrival Paths
- **HTML Location:** `game/game.js` - arrival section
- **ChoiceScript:** `arrival.txt`
- **Choices:** 3 arrival methods (portal, guided, storm)
- **Stats Affected:** +3 Collaboration variations
- **Branches:** 3 unique paths that reconverge
- **Verified:** Initial setup

#### Dorm Room Customization
- **HTML Location:** `game/game.js` - dorm section
- **ChoiceScript:** `dorm_room.txt`
- **Choices:** Room features, color scheme, desk type
- **Stats Affected:** None (flavor choices)
- **Branches:** Customization only
- **Verified:** Initial setup

#### First Lesson
- **HTML Location:** `game/game.js` - first lesson
- **ChoiceScript:** `first_lesson.txt`
- **Choices:** How to handle collaboration exercise
- **Stats Affected:** Collaboration +5 to +10, relationships
- **Branches:** Success/failure paths
- **Verified:** Initial setup

---

### ❌ Priority Conversions Needed

#### Singing Dunes Expedition
- **HTML Location:** `game/game.js` (search: "singingDunes")
- **ChoiceScript Target:** `choicescript_game/scenes/singing_dunes.txt`
- **Expected Choices:** ~15-20
- **Expected Branches:** Truth acceptance vs rejection
- **Stats Required:** Collaboration threshold checks
- **Endings Connected:** Truthbound Mage
- **Key Elements:**
  - Truth-sworn sand mechanics
  - Kael (desert guide) interactions
  - Oath-magic learning
  - Honesty testing sequences
- **Assigned To:** Needs Conversion Engineer
- **Priority:** HIGH

#### Verdant Tithe Expedition
- **HTML Location:** `game/game.js` (search: "verdantTithe")
- **ChoiceScript Target:** `choicescript_game/scenes/verdant_tithe.txt`
- **Expected Choices:** ~20-25
- **Expected Branches:** 3 paths (Dreamwillow, Thoughtvine, Heartwood)
- **Stats Required:** Collaboration threshold checks
- **Endings Connected:** Forestbound Guardian, Heartwood Guardian
- **Key Elements:**
  - Sentient forest atmosphere
  - Thoughtvine thought-reading
  - Dreamwillow vision sequences
  - Heartwood Tree encounter
- **Assigned To:** Needs Conversion Engineer
- **Priority:** HIGH

#### Rune Glacier Expedition
- **HTML Location:** `game/game.js` (search: "runeGlacier")
- **ChoiceScript Target:** `choicescript_game/scenes/rune_glacier.txt`
- **Expected Choices:** ~15-20
- **Expected Branches:** Control vs Harmony paths
- **Stats Required:** Collaboration threshold checks
- **Endings Connected:** Runeweaver, Glacier Partner
- **Key Elements:**
  - Living ice mechanics
  - Adaptive rune system
  - Aria's teaching sequences
  - Frozen spell library
  - Partnership vs domination choice
- **Assigned To:** Needs Conversion Engineer
- **Priority:** HIGH

#### All 14 Endings
- **HTML Location:** `game/game.js` (search: "endings")
- **ChoiceScript Target:** `choicescript_game/scenes/endings.txt`
- **Expected Endings:** 14 unique outcomes
- **Stat Thresholds:** Variable (needs balancing)
- **Ending List:**
  1. Collaborative Master (high collaboration)
  2. Truthbound Mage (Singing Dunes)
  3. Forestbound Guardian (Verdant Tithe)
  4. Heartwood Guardian (Verdant Tithe - special)
  5. Runeweaver (Rune Glacier - control)
  6. Glacier Partner (Rune Glacier - harmony)
  7. Balanced Mage (mixed stats)
  8. Boundary Specialist
  9. Collaborative Scholar
  10. Humble Seeker
  11. Second Chance
  12. Humbled Student
  13. Expelled (failure)
  14. Standard Path (neutral)
- **Assigned To:** Needs Conversion Engineer
- **Priority:** MEDIUM (after expeditions)

---

## 🔍 Verification Checklist

When verifying a scene, check all of these:

### Narrative Elements
- [ ] All dialogue matches HTML version
- [ ] Scene descriptions are equivalent
- [ ] Character voices are consistent
- [ ] Polly's commentary is included
- [ ] No plot points are missing

### Choice Structure
- [ ] Same number of choices at each decision point
- [ ] Choice text matches or is equivalent
- [ ] All branches lead to correct next scenes
- [ ] Dead ends are intentional (if any)
- [ ] Hidden choices implemented correctly

### Stats & Variables
- [ ] Same stats are modified
- [ ] Stat changes are identical amounts
- [ ] Relationship changes match
- [ ] Variables are set/checked correctly
- [ ] Thresholds match HTML version

### Endings & Outcomes
- [ ] All endings are reachable
- [ ] Ending conditions match HTML
- [ ] Ending text is equivalent
- [ ] Achievement triggers work
- [ ] Stat requirements are fair

### Technical Quality
- [ ] No ChoiceScript syntax errors
- [ ] *goto statements link correctly
- [ ] *if/*else logic is sound
- [ ] Variables are properly scoped
- [ ] Comments explain complex logic

---

## 📝 Verification Process

1. **Conversion Engineer** creates the ChoiceScript scene
2. **Mark as Draft** in checklist above
3. **Structural Reviewer** compares scene to HTML source
4. **Run both versions** and compare gameplay
5. **Check all boxes** in verification checklist
6. **Mark as Complete** when verified
7. **Commit changes:** `./scripts/auto-commit.sh -m "Verified scene parity: [scene name]"`

---

## 🎯 Quick Status Summary

**Total Scenes:** 13  
**Complete:** 7 (54%)  
**Draft:** 2 (15%)  
**Missing:** 4 (31%)  

**Critical Path:** Need to complete Expeditions + Endings for full game

---

## 📊 Stat Tracking Reference

All scenes should track these stats consistently:

### Primary Stats
- **Collaboration** (0-100) - Central game mechanic
- **izack_relationship** (0-100) - Relationship with Izack
- **aria_relationship** (0-100) - Relationship with Aria
- **zara_relationship** (0-100) - Relationship with Zara
- **kael_relationship** (0-100) - Relationship with Kael
- **polly_relationship** (0-100) - Relationship with Polly

### Story Variables
- **chosen_expedition** - Which expedition player selected
- **arrival_method** - How player arrived at academy
- **dorm_style** - Room customization choices
- Various ending flags and achievement trackers

---

## 🤝 Notes for AI Collaborators

- **Conversion Engineers:** Focus on accuracy first, optimization later
- **Structural Reviewers:** Be thorough - missing choices break the game
- **Lore Curators:** Check that magic system rules are consistent
- **Quality Balancers:** Track stat changes in `STATS_MATRIX.md`

---

*This checklist is updated as scenes are converted and verified. Keep it current!*
