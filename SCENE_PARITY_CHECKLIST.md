# SCENE_PARITY_CHECKLIST.md
**HTML to ChoiceScript Scene Conversion Tracking**

## Purpose
This checklist ensures that every scene in the HTML version (`game/`) has a corresponding ChoiceScript implementation (`choicescript_game/scenes/`) with matching narrative content, choice points, and endings.

---

## Conversion Status Legend
- ✅ **Verified** - ChoiceScript scene exists, tested, matches HTML narrative
- 📝 **Draft** - ChoiceScript scene exists but needs review/testing
- ❌ **Missing** - No ChoiceScript equivalent exists yet
- 🔄 **In Progress** - Currently being converted
- ⚠️ **Needs Update** - Exists but HTML version changed, needs sync

---

## Core Game Sequence

| HTML Scene | ChoiceScript Scene | Status | Notes |
|------------|-------------------|--------|-------|
| Game Start | `startup.txt` | ✅ Verified | Title screen, stat initialization, achievements |
| Opening/Polly Intro | `arrival.txt` | ✅ Verified | 3 arrival paths (boat/carriage/teleport), matches HTML |
| Familiar Selection | `familiar_selection.txt` | ✅ Verified | All familiar types implemented |
| Dorm Room | `dorm_room.txt` | ✅ Verified | Initial settling in, Polly banter |
| First Lesson | `first_lesson.txt` | ✅ Verified | Collaborative magic tutorial, dimensional theory |
| Academy Life | `academy_life.txt` | ✅ Verified | Daily activities, character interactions |
| Golem Workshop | `golem_workshop.txt` | ✅ Verified | Optional golem creation |

---

## Expedition Scenes

| HTML Scene | ChoiceScript Scene | Status | Notes |
|------------|-------------------|--------|-------|
| Expedition Prep | `expedition_prep.txt` | ✅ Verified | Selection of which biome to explore |
| Singing Dunes | `singing_dunes.txt` | ✅ Verified | Desert truth-testing, Kael guide, truth-sworn sand artifact |
| Verdant Tithe | `verdant_tithe.txt` | ✅ Verified | Forest exploration, Thoughtvine/Dreamwillow/Heartwood paths |
| Rune Glacier | `rune_glacier.txt` | ✅ Verified | Ice magic, control vs harmony, glacier partnership |

### Expedition Choice Tracking
Each expedition must lead to specific ending types:
- **Singing Dunes** → Truthbound Mage ending (+ others based on Collaboration)
- **Verdant Tithe** → 3 forest endings (Forestbound/Heartwood/Dreamwillow)
- **Rune Glacier** → 3 glacier endings (Runeweaver/Partner/Control Master)

---

## Character & Relationship Scenes

| HTML Scene | ChoiceScript Scene | Status | Notes |
|------------|-------------------|--------|-------|
| Character Bonding | `character_bonds.txt` | ✅ Verified | Deepening relationships with Izack/Aria/Zara |
| Romance Scenes | `romance_scenes.txt` | ✅ Verified | Optional romance paths (if enabled) |
| Secret Paths | `secret_paths.txt` | ✅ Verified | Hidden lore discoveries, special areas |

---

## Endgame Sequences

| HTML Scene | ChoiceScript Scene | Status | Notes |
|------------|-------------------|--------|-------|
| Final Trial | `final_trial.txt` | ✅ Verified | Culminating test of skills |
| All 14 Endings | `endings.txt` | ✅ Verified | See endings matrix below |

---

## Endings Matrix
**Total Endings: 14**

| Ending Name | Requirement | ChoiceScript Implementation | HTML Equivalent |
|-------------|-------------|----------------------------|-----------------|
| Collaborative Master | Collaboration > 85 + Partnership artifact | ✅ Verified | ✅ Match |
| Truthbound Mage | Truth-Sworn Sand artifact + Collaboration > 60 | ✅ Verified | ✅ Match |
| Forestbound Guardian | Forest artifact (general) + Collaboration > 50 | ✅ Verified | ✅ Match |
| Heartwood Guardian | Heartwood Guardian artifact + High empathy | ✅ Verified | ✅ Match |
| Runeweaver | Glacier artifact + Collaboration > 60 | ✅ Verified | ✅ Match |
| Glacier Partner | Glacier Partnership artifact + Very high Collaboration | ✅ Verified | ✅ Match |
| Balanced Mage | Balanced stats, no extreme artifact | ✅ Verified | ✅ Match |
| Boundary Specialist | High knowledge, worked with Aria | ✅ Verified | ✅ Match |
| Collaborative Scholar | Good Collaboration, academic focus | ✅ Verified | ✅ Match |
| Humble Seeker | Lower stats but positive attitude | ✅ Verified | ✅ Match |
| Second Chance | Failed but given opportunity to improve | ✅ Verified | ✅ Match |
| Humbled Student | Low Collaboration, learned lesson | ✅ Verified | ✅ Match |
| Expelled | Critical failures, kicked out | ✅ Verified | ✅ Match |
| Standard Path | Completed but no special achievements | ✅ Verified | ✅ Match |

---

## Choice Point Verification

### Critical Branching Points
Each major choice point must have identical options between HTML and ChoiceScript:

1. **Arrival Method** (3 paths)
   - 🌊 Boat (humble, collaborative start)
   - 🐴 Carriage (traditional arrival)
   - ⚡ Teleportation (powerful entrance)
   - Status: ✅ All paths match

2. **Familiar Selection**
   - 🦅 Eagle (bold, ambitious)
   - 🐈 Cat (curious, independent)
   - 🦉 Owl (wise, thoughtful)
   - 🦊 Fox (clever, adaptable)
   - 🐦‍⬛ Polly (unique, sarcastic)
   - Status: ✅ All options match

3. **Expedition Choice**
   - 🏜️ Singing Dunes (truth/honesty focus)
   - 🌲 Verdant Tithe (empathy/connection focus)
   - ❄️ Rune Glacier (control/harmony focus)
   - Status: ✅ All paths match

4. **First Lesson Approach**
   - Collaborative (high Collaboration boost)
   - Individual (Power boost)
   - Balanced (moderate both)
   - Status: ✅ All approaches match

---

## Scene Flow Validation

### HTML Game Flow
```
index.html → [game.js renders scenes dynamically]
```

### ChoiceScript Game Flow
```
startup.txt
  ↓
arrival.txt (3 paths converge)
  ↓
familiar_selection.txt
  ↓
dorm_room.txt
  ↓
first_lesson.txt
  ↓
academy_life.txt
  ↓
[Optional: golem_workshop.txt]
  ↓
expedition_prep.txt
  ↓
[One of: singing_dunes.txt / verdant_tithe.txt / rune_glacier.txt]
  ↓
[Optional: character_bonds.txt, romance_scenes.txt, secret_paths.txt]
  ↓
final_trial.txt
  ↓
endings.txt
```

Status: ✅ Flow matches HTML version narrative progression

---

## Content Completeness Check

### Scene Word Count Comparison
| Scene | HTML (approx) | ChoiceScript | Parity |
|-------|---------------|--------------|--------|
| Arrival | ~2,000 words | ~2,400 words | ✅ |
| First Lesson | ~3,500 words | ~3,800 words | ✅ |
| Singing Dunes | ~8,000 words | ~8,500 words | ✅ |
| Verdant Tithe | ~6,000 words | ~6,200 words | ✅ |
| Rune Glacier | ~9,000 words | ~9,500 words | ✅ |
| Endings | ~7,000 words | ~7,200 words | ✅ |

**Total Word Count:**
- HTML Version: ~40,000 words
- ChoiceScript Version: ~42,000 words
- Status: ✅ ChoiceScript has slight expansion for clarity/stat tracking

---

## Testing Checklist

### Path Testing (All paths must be playable)
- ✅ Boat → Eagle → Singing Dunes → Truthbound Mage
- ✅ Carriage → Cat → Verdant Tithe → Heartwood Guardian
- ✅ Teleport → Owl → Rune Glacier → Glacier Partner
- ✅ Any path → Polly → Any expedition → Collaborative Master
- ✅ Low Collaboration path → Expelled ending
- ✅ Balanced approach → Balanced Mage ending

### Choice Consistency Testing
- ✅ Same choices produce same stat changes
- ✅ Same endings requirements between versions
- ✅ Same character personalities and dialogue tone
- ✅ Same lore reveals and worldbuilding

---

## Maintenance Notes

### When to Update This File
- After converting a new scene from HTML to ChoiceScript
- After making significant changes to an existing ChoiceScript scene
- After testing reveals discrepancies between versions
- Weekly during active development
- Before each beta testing phase

### Responsible AI Roles
- **Conversion Engineer**: Updates scene status during conversion
- **Structural Reviewer**: Verifies parity and updates status to "Verified"
- **Lore Curator**: Confirms narrative consistency
- **Quality Balancer**: Notes any stat threshold adjustments needed

---

## Current Status Summary

**Overall Conversion Progress: 100% Complete ✅**

- Core Sequence: 7/7 scenes ✅
- Expeditions: 4/4 scenes ✅
- Character/Romance: 3/3 scenes ✅
- Endgame: 2/2 scenes ✅
- Endings: 14/14 endings ✅

**Ready for:** Beta testing and polish phase

**Last Verified:** November 25, 2025
