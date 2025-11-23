# SCENE_PARITY_CHECKLIST.md
## HTML ↔ ChoiceScript Scene Alignment Tracker

**Purpose:** Ensure both game versions tell the same story with equivalent content  
**Last Updated:** November 23, 2025  
**Version:** 1.0 (Stage1 Initialization)

---

## 📋 Scene Status Legend

- ✅ **Verified** - Scene fully implemented and tested in ChoiceScript, matches HTML version
- 🟢 **Complete** - Scene implemented, needs final verification
- 🟡 **Draft** - Scene exists but needs expansion/refinement
- 🔴 **Missing** - HTML content not yet converted to ChoiceScript
- ⚪ **N/A** - ChoiceScript-only content (no HTML equivalent)

---

## 🎬 Opening Sequences

| HTML Scene | ChoiceScript File | Status | Notes |
|------------|-------------------|--------|-------|
| Character Creation | `startup.txt` | ✅ Verified | Enhanced with more options |
| Polly's Introduction | `startup.txt` | ✅ Verified | Matches tone perfectly |
| Three Arrival Paths | `arrival.txt` (231 lines) | ✅ Verified | Portal/Carriage/Flight |
| First Day Setup | `academy_life.txt` | ✅ Verified | Tutorial intro |

---

## 📚 Tutorial & Introduction

| HTML Scene | ChoiceScript File | Status | Branches | Endings |
|------------|-------------------|--------|----------|---------|
| First Lesson (Dimensional Magic) | `first_lesson.txt` (289 lines) | ✅ Verified | 3 paths | Intro to collaboration |
| Familiar Selection | `familiar_selection.txt` (164 lines) | ✅ Verified | 4 choices | Companion bond |
| Dorm Room Setup | `dorm_room.txt` (124 lines) | ✅ Verified | Customization | Home base established |

---

## 🗺️ MAIN EXPEDITIONS (Critical Content)

### Singing Dunes Expedition

| HTML Scene Node | ChoiceScript Label | Status | Line Count | Branches | Quality Check |
|-----------------|-------------------|--------|------------|----------|---------------|
| `singingDunes_arrival` | `dunes_arrival` | ✅ Verified | ~60 | 3 choices | Production-ready |
| `dunes_kael_intro` | `kael_introduction` | ✅ Verified | ~80 | Meet guide | Matches tone |
| `dunes_truth_test` | `first_truth_test` | ✅ Verified | ~120 | Truth/Safe/Avoid | Stat tracking works |
| `dunes_honest_path` | `truth_embraced` | ✅ Verified | ~90 | Vulnerability reward | Emotionally resonant |
| `dunes_safe_path` | `truth_shared_safely` | ✅ Verified | ~70 | Caution approach | Balanced outcome |
| `dunes_oasis` | `ironwood_oasis` | ✅ Verified | ~85 | Discovery | Vivid description |
| `dunes_spirits` | `oath_spirits_encounter` | ✅ Verified | ~110 | Spirit interaction | Lore-accurate |
| `dunes_oath_magic` | `oath_binding_lesson` | ✅ Verified | ~95 | Learn mechanics | Educational |
| `dunes_final_test` | `desert_final_truth` | ✅ Verified | ~130 | Climax choice | High stakes |
| `dunes_blessing` | `truthbound_achievement` | ✅ Verified | ~60 | Success path | Satisfying |
| `dunes_rejection` | `desert_rejection` | ✅ Verified | ~50 | Failure path | Consequence clear |

**Total Lines:** 931  
**Overall Status:** ✅ Complete & Verified  
**Parity Check:** Matches HTML version with enhanced detail

---

### Verdant Tithe Expedition

| HTML Scene Node | ChoiceScript Label | Status | Line Count | Branches | Quality Check |
|-----------------|-------------------|--------|------------|----------|---------------|
| `verdantTithe_arrival` | `forest_arrival` | 🟡 Draft | ~30 | Basic | Needs expansion |
| `forest_thoughts` | `thoughtvine_introduction` | 🟡 Draft | ~40 | Minimal | Underdeveloped |
| `dreamwillow_grove` | `dreamwillow_encounter` | 🟡 Draft | ~35 | Basic | Placeholder |
| `dreamwillow_vision` | `vision_sequence` | 🔴 Missing | 0 | N/A | Not implemented |
| `thoughtvine_merge` | `thoughtvine_communion` | 🔴 Missing | 0 | N/A | Not implemented |
| `heartwood_tree` | `heartwood_approach` | 🟡 Draft | ~25 | Minimal | Needs depth |
| `heartwood_test` | `tithe_payment` | 🟡 Draft | ~30 | Basic | Underdeveloped |
| `heartwood_guardian` | `heartwood_guardian_path` | 🔴 Missing | 0 | N/A | Rare ending path missing |
| `forest_departure` | `forest_conclusion` | 🟡 Draft | ~23 | Basic | Needs closure |

**Total Lines:** 183 (TARGET: 600+)  
**Overall Status:** 🟡 Needs Major Expansion  
**Priority:** HIGH - Next conversion target  
**Missing Content:** Vision sequences, Thoughtvine deep merge, Guardian path

---

### Rune Glacier Expedition

| HTML Scene Node | ChoiceScript Label | Status | Line Count | Branches | Quality Check |
|-----------------|-------------------|--------|------------|----------|---------------|
| `runeGlacier_arrival` | `glacier_arrival` | ✅ Verified | ~95 | Vivid intro | Production-ready |
| `glacier_runes_awaken` | `rune_awakening` | ✅ Verified | ~110 | Living ice | Atmospheric |
| `aria_lesson` | `aria_boundary_teaching` | ✅ Verified | ~130 | Control vs Harmony | Educational |
| `glacier_control_path` | `ice_domination_attempt` | ✅ Verified | ~140 | Force approach | Consequence-rich |
| `glacier_harmony_path` | `ice_partnership` | ✅ Verified | ~150 | Collaboration | Rewarding |
| `spell_library` | `frozen_knowledge` | ✅ Verified | ~120 | Discovery | Lore integration |
| `ancient_runes` | `primordial_inscriptions` | ✅ Verified | ~105 | Deep lore | Ancient feel |
| `boundary_test` | `magical_limits_test` | ✅ Verified | ~115 | Challenge | Balanced difficulty |
| `runeweaver_path` | `control_mastery_ending` | ✅ Verified | ~90 | Domination end | Clear outcome |
| `glacier_partner_path` | `partnership_bond` | ✅ Verified | ~130 | Harmony end | Satisfying |
| `glacier_departure` | `ice_blessing` | ✅ Verified | ~80 | Closure | Respectful farewell |

**Total Lines:** 1,266  
**Overall Status:** ✅ Complete & Verified  
**Parity Check:** Exceeds HTML version with enhanced mechanics

---

## 🎭 Character & Relationship Scenes

| Scene Type | ChoiceScript File | Status | Notes |
|------------|-------------------|--------|-------|
| Character Bonds | `character_bonds.txt` (196 lines) | ✅ Verified | Izack, Aria, Zara interactions |
| Romance Options | `romance_scenes.txt` (213 lines) | ⚪ N/A | Optional ChoiceScript enhancement |
| Academy Life | `academy_life.txt` (167 lines) | ✅ Verified | Daily activities |

---

## 🏆 ENDINGS (14 Total)

| Ending Name | HTML Node | ChoiceScript Label | Status | Requirements | Verification |
|-------------|-----------|-------------------|--------|--------------|--------------|
| Collaborative Master | `ending_collaborative_master` | `collaborative_master` | ✅ Verified | Collab > 80 + Partnership | Tested |
| Truthbound Mage | `ending_truthbound` | `truthbound_mage_ending` | ✅ Verified | Truth-Sworn Sand + Collab > 70 | Tested |
| Forestbound Guardian | `ending_forestbound` | `forestbound_guardian_ending` | ✅ Verified | Forest artifacts | Tested |
| Heartwood Guardian | `ending_heartwood` | `heartwood_guardian_ending` | 🟡 Draft | Ancient Wisdom artifact | Needs Verdant expansion |
| Runeweaver | `ending_runeweaver` | `runeweaver_ending` | ✅ Verified | Runeweaver's Mark | Tested |
| Glacier Partner | `ending_glacier_partner` | `glacier_partner_ending` | ✅ Verified | Glacier Partnership | Tested |
| Balanced Mage | `ending_balanced` | `balanced_mage_ending` | ✅ Verified | Harmony Bracelet | Tested |
| Boundary Specialist | `ending_boundary` | `boundary_specialist_ending` | ✅ Verified | Collab 50-74 | Tested |
| Collaborative Scholar | `ending_scholar` | `collaborative_scholar_ending` | ✅ Verified | Collab > 75 | Tested |
| Humble Seeker | `ending_humble` | `humble_seeker_ending` | ✅ Verified | Rune of Mystery | Tested |
| Second Chance | `ending_second_chance` | `second_chance_ending` | ✅ Verified | Low collab but recovery | Tested |
| Humbled Student | `ending_humbled` | `humbled_student_ending` | ✅ Verified | Learned from failure | Tested |
| Expelled | `ending_expelled` | `expelled_ending` | ✅ Verified | Collab < 20 | Tested |
| Standard Path | `ending_standard` | `standard_path_ending` | ✅ Verified | Default completion | Tested |

**Endings Status:** 13/14 Fully Verified, 1 Needs Verdant Tithe completion  
**All ending logic:** ✅ Implemented in `endings.txt`

---

## 🎁 Optional/Enhancement Content

| Scene Type | ChoiceScript File | Status | Notes |
|------------|-------------------|--------|-------|
| Secret Paths | `secret_paths.txt` (295 lines) | ⚪ N/A | Hidden discoveries |
| Golem Workshop | `golem_workshop.txt` (174 lines) | ⚪ N/A | Crafting minigame |
| Final Trial | `final_trial.txt` (622 lines) | ⚪ N/A | Climactic challenge |
| Expedition Prep | `expedition_prep.txt` (108 lines) | ✅ Verified | Pre-journey setup |

---

## 📊 Overall Parity Status

### Completion Metrics
- **Core Scenes:** 95% complete (Verdant Tithe needs expansion)
- **Endings:** 93% verified (1 depends on Verdant Tithe)
- **Total Content:** 6,139 lines ChoiceScript vs ~4,000 lines HTML
- **Enhancement Factor:** ChoiceScript version has ~50% more detail

### Quality Assurance
- [x] Singing Dunes matches HTML quality
- [x] Rune Glacier matches HTML quality
- [ ] Verdant Tithe needs expansion to match
- [x] All endings accessible (except Heartwood Guardian pending Verdant)
- [x] Stat tracking consistent across versions
- [x] Character voices maintained

---

## 🎯 Next Steps for Parity

### Critical
1. **Expand Verdant Tithe** to 600+ lines
   - Add Thoughtvine deep merge scenes
   - Implement Dreamwillow vision sequences
   - Develop Heartwood Guardian path
   - Match detail level of other expeditions

### Nice-to-Have
2. Polish Polly's commentary consistency
3. Add more stat-based variations
4. Enhance environmental descriptions

---

## 🔄 Update Protocol

When modifying scenes:
1. Update this checklist status
2. Note line count changes
3. Mark verification status
4. Update STATUS_CONTEXT.md
5. Cross-reference STATS_MATRIX.md if stats changed

---

**Maintained by:** Structural Reviewer role (Multi-AI Collaboration)  
**Update Frequency:** After each scene modification  
**Version:** 1.0 (Stage1 Initialization)
