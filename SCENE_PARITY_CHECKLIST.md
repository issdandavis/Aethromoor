# 🎮 SCENE PARITY CHECKLIST
## HTML vs ChoiceScript Scene Comparison

**Purpose:** Track conversion status and ensure story parity between HTML and ChoiceScript versions.

**Last Updated:** 2025-11-22 04:03 UTC  
**Updated By:** GitHub Copilot

---

## 📋 PARITY RULES

### Both Versions Must Have:
✅ Same story beats and narrative moments  
✅ Same character interactions and dialogue themes  
✅ Same choice points (may differ in technical implementation)  
✅ Same endings (all 14 must be reachable)  
✅ Same stat changes (Collaboration + relationships)  
✅ Equivalent emotional impact and player agency  

### Versions May Differ In:
- Technical implementation (HTML buttons vs ChoiceScript commands)
- Exact wording (can be refined for ChoiceScript)
- UI presentation (ChoiceScript has standard interface)
- Code structure (different languages/frameworks)

---

## 🎯 CORE GAME STRUCTURE

### Opening Sequence
| Component | HTML Status | ChoiceScript Status | Parity |
|-----------|-------------|---------------------|--------|
| Polly's Introduction | ✅ Complete | ✅ Complete | ✅ Verified |
| Dimensional theory explanation | ✅ Complete | ✅ Complete | ✅ Verified |
| Journey to Avalon | ✅ Complete | ✅ Complete | ✅ Verified |

### Arrival Paths
| Path | HTML Status | ChoiceScript Status | Parity |
|------|-------------|---------------------|--------|
| Diplomatic arrival | ✅ Complete | ✅ Complete | ✅ Verified |
| Confident arrival | ✅ Complete | ✅ Complete | ✅ Verified |
| Humble arrival | ✅ Complete | ✅ Complete | ✅ Verified |

### First Lesson
| Component | HTML Status | ChoiceScript Status | Parity |
|-----------|-------------|---------------------|--------|
| Classroom scene | ✅ Complete | ✅ Complete | ✅ Verified |
| Aria Ravencrest introduction | ✅ Complete | ✅ Complete | ✅ Verified |
| Collaborative casting mechanics | ✅ Complete | ✅ Complete | ✅ Verified |
| Partner interactions (Zara, others) | ✅ Complete | ✅ Complete | ✅ Verified |
| Lesson success/failure paths | ✅ Complete | ✅ Complete | ✅ Verified |

### Expedition Selection
| Component | HTML Status | ChoiceScript Status | Parity |
|-----------|-------------|---------------------|--------|
| Three expedition choices | ✅ Complete | ✅ Complete | ✅ Verified |
| Expedition descriptions | ✅ Complete | ✅ Complete | ✅ Verified |
| Choice tracking | ✅ Complete | ✅ Complete | ✅ Verified |

---

## 🏜️ SINGING DUNES EXPEDITION

**Priority:** HIGH (Next to convert)  
**HTML File:** `game/scenes/singing_dunes.html` (if exists, or integrated in main HTML)  
**ChoiceScript File:** `choicescript_game/scenes/singing_dunes.txt`  
**Overall Status:** ⏳ Not yet started

| Scene Component | HTML | ChoiceScript | Parity | Notes |
|-----------------|------|--------------|--------|-------|
| Desert arrival | ✅ | ❌ Missing | ❌ | Needs conversion |
| Kael introduction | ✅ | ❌ Missing | ❌ | Desert guide character |
| Truth-testing mechanics | ✅ | ❌ Missing | ❌ | Core desert magic |
| Truth-sworn sand artifact | ✅ | ❌ Missing | ❌ | Key item system |
| Oath-magic learning | ✅ | ❌ Missing | ❌ | Magic system teaching |
| Desert acceptance path | ✅ | ❌ Missing | ❌ | Success route |
| Desert rejection path | ✅ | ❌ Missing | ❌ | Alternative route |
| Connection to Truthbound Mage ending | ✅ | ❌ Missing | ❌ | Ending linkage |

**Stat Changes in This Scene:**
- Collaboration +/- based on truth-telling choices
- Kael relationship established
- Possible Truth specialty unlocked

**Choices Count:** TBD (count from HTML version)  
**Endings Linked:** Truthbound Mage (primary), possibly others

---

## 🌲 VERDANT TITHE EXPEDITION

**Priority:** MEDIUM (After Singing Dunes)  
**HTML File:** `game/scenes/verdant_tithe.html` (if exists)  
**ChoiceScript File:** `choicescript_game/scenes/verdant_tithe.txt`  
**Overall Status:** ⏳ Planned, not yet started

| Scene Component | HTML | ChoiceScript | Parity | Notes |
|-----------------|------|--------------|--------|-------|
| Forest arrival | ✅ | ❌ Missing | ❌ | Needs conversion |
| Sentient forest atmosphere | ✅ | ❌ Missing | ❌ | Environmental storytelling |
| Thoughtvine interactions | ✅ | ❌ Missing | ❌ | Mind-reading plants |
| Dreamwillow vision sequence | ✅ | ❌ Missing | ❌ | Dream/vision mechanics |
| Heartwood Tree encounter | ✅ | ❌ Missing | ❌ | Central tree guardian |
| Dreamwillow path | ✅ | ❌ Missing | ❌ | Vision-focused route |
| Thoughtvine path | ✅ | ❌ Missing | ❌ | Mind-focused route |
| Heartwood path | ✅ | ❌ Missing | ❌ | Protection-focused route |
| Connection to forest endings (3) | ✅ | ❌ Missing | ❌ | Multiple ending linkages |

**Stat Changes in This Scene:**
- Collaboration +/- based on plant cooperation
- Multiple relationship tracks (Dreamwillow, Thoughtvine, Heartwood)
- Forest specialty potential

**Choices Count:** TBD (count from HTML version)  
**Endings Linked:** Forestbound Guardian, Heartwood Guardian, possibly Dreamwillow path

---

## ❄️ RUNE GLACIER EXPEDITION

**Priority:** MEDIUM (After Verdant Tithe)  
**HTML File:** `game/scenes/rune_glacier.html` (if exists)  
**ChoiceScript File:** `choicescript_game/scenes/rune_glacier.txt`  
**Overall Status:** ⏳ Planned, not yet started

| Scene Component | HTML | ChoiceScript | Parity | Notes |
|-----------------|------|--------------|--------|-------|
| Glacier arrival | ✅ | ❌ Missing | ❌ | Needs conversion |
| Living ice mechanics | ✅ | ❌ Missing | ❌ | Animated ice entities |
| Control vs Harmony paths | ✅ | ❌ Missing | ❌ | Core philosophical choice |
| Mystery partnership path | ✅ | ❌ Missing | ❌ | Glacier partnership route |
| Aria's teaching sequences | ✅ | ❌ Missing | ❌ | Mentor involvement |
| Frozen spell library | ✅ | ❌ Missing | ❌ | Knowledge discovery |
| Control path | ✅ | ❌ Missing | ❌ | Hierarchical magic route |
| Harmony path | ✅ | ❌ Missing | ❌ | Collaborative magic route |
| Partnership path | ✅ | ❌ Missing | ❌ | Glacier alliance route |
| Connection to glacier endings (3) | ✅ | ❌ Missing | ❌ | Multiple ending linkages |

**Stat Changes in This Scene:**
- Collaboration +/- based on approach (harmony vs control)
- Aria relationship development
- Glacier partnership tracking
- Runeweaver specialty potential

**Choices Count:** TBD (count from HTML version)  
**Endings Linked:** Runeweaver, Glacier Partner, possibly Balanced Mage

---

## 🏆 ENDINGS

**Total Endings:** 14  
**HTML Implementation:** 14/14 ✅  
**ChoiceScript Implementation:** 1/14 ⏳

| Ending | HTML | ChoiceScript | Parity | Requirements | Linked Expedition |
|--------|------|--------------|--------|--------------|-------------------|
| Collaborative Master | ✅ | ❌ | ❌ | High Collaboration, all expeditions | All |
| Truthbound Mage | ✅ | ❌ | ❌ | Singing Dunes success, truth focus | Singing Dunes |
| Forestbound Guardian | ✅ | ❌ | ❌ | Verdant Tithe, protection path | Verdant Tithe |
| Heartwood Guardian | ✅ | ❌ | ❌ | Verdant Tithe, Heartwood path | Verdant Tithe |
| Runeweaver | ✅ | ❌ | ❌ | Rune Glacier, rune mastery | Rune Glacier |
| Glacier Partner | ✅ | ❌ | ❌ | Rune Glacier, partnership path | Rune Glacier |
| Balanced Mage | ✅ | ❌ | ❌ | Medium Collaboration, multiple paths | Multiple |
| Boundary Specialist | ✅ | ❌ | ❌ | Aria relationship, boundary magic | Any |
| Collaborative Scholar | ✅ | ❌ | ❌ | High Collaboration, academic focus | Any |
| Humble Seeker | ✅ | ❌ | ❌ | Low confidence, high openness | Any |
| Second Chance | ✅ | ❌ | ❌ | Failed but recovered | Any |
| Humbled Student | ✅ | ❌ | ❌ | Low Collaboration, learning moment | Any |
| Expelled | ✅ | ❌ | ❌ | Very low Collaboration | Any (failure) |
| Standard Path | ✅ | ✅ | ✅ | Default/neutral stats | Any (neutral) |

**Notes:**
- All endings must be implemented in ChoiceScript
- Stat thresholds must match HTML version (or be balanced equivalently)
- Each ending should feel earned and meaningful

---

## 📊 PARITY VERIFICATION CHECKLIST

### For Each Converted Scene:

**Narrative Parity:**
- [ ] Same story beats occur
- [ ] Same character interactions
- [ ] Same emotional moments
- [ ] Equivalent dialogue quality

**Mechanical Parity:**
- [ ] Same number of meaningful choices
- [ ] Same stat changes (tracked in STATS_MATRIX.md)
- [ ] Same branching structure
- [ ] Same ending connections

**Testing:**
- [ ] ChoiceScript scene runs without errors
- [ ] All choices lead to expected outcomes
- [ ] Stats update correctly
- [ ] Progression feels equivalent to HTML

**Documentation:**
- [ ] This checklist updated
- [ ] STATS_MATRIX.md updated
- [ ] HANDOFF.md noted conversion
- [ ] .VERSION incremented

---

## 🔍 HOW TO VERIFY PARITY

### Step 1: Play HTML Version
- Note all choice points
- Track stat changes
- Document story beats
- List character interactions

### Step 2: Review ChoiceScript Version
- Compare choice points
- Verify stat changes match
- Check story beats included
- Confirm character moments present

### Step 3: Side-by-Side Comparison
- Create comparison table
- Note any differences
- Justify intentional changes
- Fix unintentional differences

### Step 4: Update This File
- Mark scene as verified
- Note any acceptable differences
- Document conversion decisions
- Update status indicators

---

## 📝 CONVERSION NOTES

### Singing Dunes:
- (Notes to be added during conversion)

### Verdant Tithe:
- (Notes to be added during conversion)

### Rune Glacier:
- (Notes to be added during conversion)

### Endings:
- (Notes to be added during implementation)

---

## 🚨 PARITY ISSUES

### Current Issues:
- None (conversion not yet started)

### Resolved Issues:
- (To be documented as issues are found and resolved)

---

## 📊 PROGRESS SUMMARY

**Overall Conversion Progress:**
- **Foundation:** ✅ 100% (5/5 scenes)
- **Expeditions:** ❌ 0% (0/3 expeditions)
- **Endings:** ⏳ 7% (1/14 endings)
- **Total Game:** ⏳ ~15% estimated

**Next Milestone:** Singing Dunes Complete (target: +33% expedition progress)

---

## 🔄 UPDATE LOG

**2025-11-22:** Initial checklist created with baseline status  
**Next Update:** When Singing Dunes conversion begins

---

**Remember:** Parity doesn't mean identical - it means equivalent story, choices, and impact. Document intentional differences and justify them.

*"Two versions, one story. The spiral continues."* 🌀
