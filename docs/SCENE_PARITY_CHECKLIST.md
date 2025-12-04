# Scene Parity Checklist

**Purpose**: Track conversion status of HTML game scenes → ChoiceScript format

**Status Legend**:
- ✅ **Verified** - ChoiceScript version complete and tested, matches HTML
- ⏳ **Draft** - ChoiceScript version exists but needs review/completion
- ❌ **Missing** - ChoiceScript version not yet created
- 🔄 **Needs Update** - HTML version changed, ChoiceScript needs sync

---

## Opening Sequence

| Scene | HTML | ChoiceScript | Status | Word Count (CS) | Notes |
|-------|------|--------------|--------|-----------------|-------|
| Polly Introduction | ✅ | ✅ | Verified | ~1,200 | Complete, voice accurate |
| Character Creation | ✅ | ✅ | Verified | ~800 | Stats initialized correctly |

## Arrival Paths

| Scene | HTML | ChoiceScript | Status | Word Count (CS) | Notes |
|-------|------|--------------|--------|-----------------|-------|
| Arrival - Teleport | ✅ | ✅ | Verified | ~600 | All paths working |
| Arrival - Walk | ✅ | ✅ | Verified | ~650 | Stat tracking correct |
| Arrival - Fly | ✅ | ✅ | Verified | ~620 | Polly commentary preserved |

## Tutorial / First Lesson

| Scene | HTML | ChoiceScript | Status | Word Count (CS) | Notes |
|-------|------|--------------|--------|-----------------|-------|
| First Lesson (complete) | ✅ | ✅ | Verified | ~3,500 | All branching paths match |
| - Introduction | ✅ | ✅ | Verified | - | Izack's teaching style correct |
| - Collaboration Choice | ✅ | ✅ | Verified | - | Stat impacts match (+5/-5) |
| - Aria Guidance | ✅ | ✅ | Verified | - | Character voice authentic |
| - Resolution | ✅ | ✅ | Verified | - | Routes correctly to expedition choice |

## Expedition Selection

| Scene | HTML | ChoiceScript | Status | Word Count (CS) | Notes |
|-------|------|--------------|--------|-----------------|-------|
| Expedition Choice Screen | ✅ | ✅ | Verified | ~500 | All three expeditions presented |

## Singing Dunes Expedition

| Scene | HTML | ChoiceScript | Status | Word Count (CS) | Notes |
|-------|------|--------------|--------|-----------------|-------|
| Desert Arrival | ✅ | ⏳ | Draft | ~800 | Needs Kael introduction review |
| Kael Introduction | ✅ | ⏳ | Draft | ~600 | Character voice needs validation |
| Truth Test 1 | ✅ | ⏳ | Draft | ~700 | Oath-magic mechanics need checking |
| Truth vs Control Choice | ✅ | ⏳ | Draft | ~500 | Major stat impact (verify thresholds) |
| Truth Path Resolution | ✅ | ❌ | Missing | - | Not yet implemented |
| Control Path Resolution | ✅ | ❌ | Missing | - | Not yet implemented |
| Rejection Path | ✅ | ❌ | Missing | - | Not yet implemented |
| Desert Conclusion | ✅ | ❌ | Missing | - | Routes to endings |

**Estimated Completion**: ~70% (draft content exists, needs finishing + validation)

## Verdant Tithe Expedition

| Scene | HTML | ChoiceScript | Status | Word Count (CS) | Notes |
|-------|------|--------------|--------|-----------------|-------|
| Forest Arrival | ✅ | ❌ | Missing | - | Sentient plants intro needed |
| Thoughtvine Encounter | ✅ | ❌ | Missing | - | Intellectual connection path |
| Dreamwillow Encounter | ✅ | ❌ | Missing | - | Emotional/subconscious path |
| Heartwood Encounter | ✅ | ❌ | Missing | - | Heart/core truth path |
| Plant Affinity Choice | ✅ | ❌ | Missing | - | Three-way branching |
| Thoughtvine Path Resolution | ✅ | ❌ | Missing | - | |
| Dreamwillow Path Resolution | ✅ | ❌ | Missing | - | |
| Heartwood Path Resolution | ✅ | ❌ | Missing | - | |
| Forest Conclusion | ✅ | ❌ | Missing | - | Routes to endings |

**Estimated Completion**: 0% (not yet started)

## Rune Glacier Expedition

| Scene | HTML | ChoiceScript | Status | Word Count (CS) | Notes |
|-------|------|--------------|--------|-----------------|-------|
| Glacier Arrival | ✅ | ❌ | Missing | - | Living ice introduction |
| Memory Crystal Discovery | ✅ | ❌ | Missing | - | Frozen spell library |
| Aria's Teaching Moment | ✅ | ❌ | Missing | - | Precision vs Partnership |
| Ice Awakening | ✅ | ❌ | Missing | - | Glacier consciousness emerges |
| Control vs Harmony Choice | ✅ | ❌ | Missing | - | Three-way branching |
| Control Path Resolution | ✅ | ❌ | Missing | - | |
| Harmony Path Resolution | ✅ | ❌ | Missing | - | |
| Mystery Path Resolution | ✅ | ❌ | Missing | - | Glacier partnership |
| Glacier Conclusion | ✅ | ❌ | Missing | - | Routes to endings |

**Estimated Completion**: 0% (not yet started)

## Endings (14 Total)

| Ending | HTML | ChoiceScript | Status | Required Stats | Notes |
|--------|------|--------------|--------|----------------|-------|
| Collaborative Master | ✅ | ❌ | Missing | Collab ≥85, all expeditions, glacier="harmony" | Ultimate positive |
| Truthbound Mage | ✅ | ❌ | Missing | Collab ≥60, dunes="truth" | Desert specialist |
| Forestbound Guardian | ✅ | ❌ | Missing | Collab ≥60, forest="thoughtvine" | Intellectual path |
| Heartwood Guardian | ✅ | ❌ | Missing | Collab ≥60, forest="heartwood" | Emotional path |
| Dreamweaver | ✅ | ❌ | Missing | Collab ≥60, forest="dreamwillow" | Subconscious path |
| Runeweaver | ✅ | ❌ | Missing | Collab ≥60, glacier="control" | Control mastery |
| Glacier Partner | ✅ | ❌ | Missing | Collab ≥70, glacier="mystery" | Partnership path |
| Balanced Mage | ✅ | ❌ | Missing | Collab 40-60, 2+ expeditions | Balanced approach |
| Boundary Specialist | ✅ | ❌ | Missing | High Aria relationship | Aria's protégé |
| Collaborative Scholar | ✅ | ❌ | Missing | Collab 50-70, focus on learning | Research path |
| Humble Seeker | ✅ | ❌ | Missing | Collab 30-50, acknowledges limits | Growth mindset |
| Second Chance | ✅ | ❌ | Missing | Low collab but recovers | Redemption arc |
| Humbled Student | ✅ | ❌ | Missing | Collab <30, recognizes need to improve | Learning humility |
| Standard Path | ✅ | ❌ | Missing | Neutral stats, completed academy | Neutral ending |

## Statistics Summary

### Overall Progress
- **Total Scenes**: ~35-40 scenes (estimated)
- **Verified**: 8 scenes (opening + first lesson)
- **Draft**: 4 scenes (partial Singing Dunes)
- **Missing**: ~23-28 scenes (expeditions + endings)
- **Completion**: ~25% overall

### By Section
- **Opening**: ✅ 100% complete (8/8 scenes verified)
- **Singing Dunes**: ⏳ 70% draft (4/8 scenes in progress)
- **Verdant Tithe**: ❌ 0% (0/9 scenes)
- **Rune Glacier**: ❌ 0% (0/9 scenes)
- **Endings**: ❌ 0% (0/14 endings)

### Word Count Tracking
- **HTML Version**: ~40,000 words
- **ChoiceScript Verified**: ~7,370 words
- **ChoiceScript Draft**: ~2,600 words (Singing Dunes partial)
- **Total ChoiceScript**: ~9,970 words (~25% of target)

## Next Priorities

1. **Complete Singing Dunes** (⏳ Draft → ✅ Verified)
   - Finish missing scenes (4 scenes)
   - Validate Kael character voice (Lore Curator)
   - Test all three path branches
   - Verify stat impacts match HTML

2. **Start Verdant Tithe** (❌ Missing → ⏳ Draft)
   - Convert forest arrival and plant introductions
   - Implement three-way branching (Thoughtvine/Dreamwillow/Heartwood)
   - Ensure sentient plant consciousness is conveyed

3. **Then Rune Glacier** (❌ Missing → ⏳ Draft)
   - Convert glacier arrival and memory crystal scenes
   - Implement Aria's teaching sequences
   - Create three-way branching (Control/Harmony/Mystery)

4. **Finally, All Endings** (❌ Missing → ⏳ Draft)
   - Implement stat-based routing logic
   - Ensure all 14 endings are reachable
   - Test ending triggers with various stat combinations

---

**Last Updated**: November 23, 2025  
**Next Review**: After Singing Dunes completion  
**Maintained By**: Structural Reviewer role
