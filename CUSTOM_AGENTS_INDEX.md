# 🤖 CUSTOM AGENTS INDEX
**Complete Guide to Specialized AI Agents for Avalon Development**

Last Updated: December 2, 2025

---

## 📚 QUICK NAVIGATION

| Agent | Priority | Purpose | When to Use |
|-------|----------|---------|-------------|
| [ChoiceScript Converter](#choicescript-conversion-specialist) | ⚡ Phase 1 | HTML→ChoiceScript conversion | Converting game scenes |
| [Lore Guardian](#lore-consistency-guardian) | ⚡ Phase 1 | Canon validation | Before publishing content |
| [ChoiceScript Validator](#choicescript-technical-validator) | ⭐ Phase 2 | Technical QA | After scene completion |
| [Polly's Voice Architect](#pollys-voice-architect) | ⭐ Phase 2 | Polly commentary enhancement | Polishing scenes |
| [Romance Orchestrator](#romance-system-orchestrator) | 💕 Phase 3 | Romance system design | Creating relationship content |

---

## 🎯 PHASE 1: CRITICAL AGENTS (Deploy Immediately)

### ChoiceScript Conversion Specialist

**File:** `.github/agents/choicescript-converter.agent.md`

**What It Does:**
- Converts HTML game scenes to ChoiceScript format
- Preserves 100% narrative parity between versions
- Maintains all player choices and stat modifications
- Validates syntax automatically

**When to Use:**
- Converting any HTML scene from `game/scenes/` to `choicescript_game/scenes/`
- Implementing expeditions (Singing Dunes, Verdant Tithe, Rune Glacier)
- Porting endings from HTML to ChoiceScript

**Example Task:**
```
"Convert singing_dunes.html scenes 1-3 to ChoiceScript format, 
preserving all truth-testing mechanics and Kael dialogue."
```

**Success Metrics:**
- Conversion time: 30-45 minutes per scene
- 100% QuickTest pass rate
- Identical choice trees to HTML source

**ROI:** Saves 45+ hours of manual conversion work

---

### Lore Consistency Guardian

**File:** `.github/agents/lore-guardian.agent.md`

**What It Does:**
- Validates content against 8 lore documents
- Catches timeline contradictions (4 generations, 150+ years)
- Verifies character voices match established patterns
- Ensures magic system consistency

**When to Use:**
- Before publishing any new scene
- After major content additions
- When introducing new character dialogue
- Before merging PRs with narrative changes

**Example Task:**
```
"Validate the new Verdant Tithe scenes against character chronicles 
and magic system rules. Check for timeline consistency."
```

**Success Metrics:**
- Zero canon violations in published content
- 95%+ catch rate for inconsistencies
- 10-15 minutes validation per scene

**ROI:** Prevents expensive rewrites from canon violations

---

## ⭐ PHASE 2: QUALITY AGENTS (Deploy After Phase 1)

### ChoiceScript Technical Validator

**File:** `.github/agents/choicescript-validator.agent.md`

**What It Does:**
- Runs QuickTest (syntax validation)
- Runs RandomTest (1000 iterations, path coverage)
- Analyzes stat progression fairness
- Detects unreachable endings or achievements

**When to Use:**
- After completing a major section (expedition, endings)
- Before beta testing
- When debugging player reports of unreachable content
- Monthly quality assurance checks

**Example Task:**
```
"Run RandomTest on all scenes and verify all 14 endings are 
reachable. Check if Truthbound Mage ending threshold is achievable."
```

**Success Metrics:**
- 100% QuickTest pass rate
- All endings reached in 1000 RandomTest iterations
- Stat thresholds achievable by 50%+ of players

**ROI:** Saves 6+ hours of manual QA testing

---

### Polly's Voice Architect

**File:** `.github/agents/polly-voice-architect.agent.md`

**What It Does:**
- Enhances scenes with Polly's meta-commentary
- Explains dimensional magic accessibly
- Balances sarcasm and helpfulness (60/30/10 ratio)
- Maintains consistent voice with existing scenes

**When to Use:**
- After initial scene writing is complete
- When dimensional magic concepts need explanation
- To add humor without breaking immersion
- During content polish phase

**Example Task:**
```
"Add Polly commentary to Rune Glacier scenes, focusing on 
explaining control vs harmony magic approaches with humor."
```

**Success Metrics:**
- 2-3 Polly comments per scene
- Voice matches first_lesson.txt patterns
- Commentary in 60-70% of scenes

**ROI:** Saves 2+ hours of voice consistency work

---

## 💕 PHASE 3: ENHANCEMENT AGENTS (Deploy Later)

### Romance System Orchestrator

**File:** `.github/agents/romance-orchestrator.agent.md`

**What It Does:**
- Designs ethical polyamory system
- Creates character-specific romance arcs (Aria, Zara, Alexander)
- Implements consent-first mechanics
- Balances monogamy and polyamory paths

**When to Use:**
- When implementing romance content
- Creating relationship progression scenes
- Designing romance endings
- Adding optional romantic subplots to expeditions

**Example Task:**
```
"Design Aria's slow-burn romance arc with trust-building mechanics 
and create 3 romance scenes for library encounters."
```

**Success Metrics:**
- 3 fully developed romance arcs
- Equal content quality for mono/poly paths
- Player choice respected (no forced romance)

**ROI:** Saves 3+ hours of specialized romance design

---

## 📊 AGENT COMPARISON

### How They Differ from Generic Workers

| Generic Workers | Custom Agents |
|-----------------|---------------|
| Create new content | Transform/validate existing content |
| General purpose | Domain-specialized |
| Good enough quality | Professional-grade quality |
| No lore context | Deep canon knowledge |
| Standard tools | Specialized tools (conversion, validation) |

### Agent Coordination

**No Overlap:** Each agent has exclusive domain
- Converter: Format translation only
- Lore Guardian: Canon validation only
- Validator: Technical QA only
- Polly Architect: Voice enhancement only
- Romance Orchestrator: Relationship content only

**Workflow Integration:**
1. Generic worker writes scene → 
2. Converter translates format → 
3. Lore Guardian validates canon → 
4. Polly Architect adds commentary → 
5. Validator runs QA tests → 
6. Ready for human review

---

## 🚀 DEPLOYMENT GUIDE

### Phase 1: Week 1
**Deploy:** ChoiceScript Converter + Lore Guardian

**Why First:**
- Biggest bottleneck (72-hour conversion)
- Highest ROI (60+ hours saved)
- Low risk (test on 1-2 scenes first)

**Test With:**
- Convert singing_dunes scenes 1-3
- Validate against lore documents
- Verify syntax passes QuickTest

**Success = Deploy Phase 2**

---

### Phase 2: Week 2-3
**Deploy:** ChoiceScript Validator + Polly's Voice Architect

**Why Second:**
- Phase 1 agents generating content that needs QA
- Polly enhancement ready after conversion complete
- Quality improvements before beta testing

**Test With:**
- Run RandomTest on converted scenes
- Add Polly commentary to 3 scenes
- Verify voice consistency

**Success = Deploy Phase 3**

---

### Phase 3: Week 4+
**Deploy:** Romance System Orchestrator

**Why Last:**
- Enhancement, not critical path
- Requires completed expedition content
- Can be iterated based on player feedback

**Test With:**
- Create 1 romance arc (Aria)
- Test mono and poly paths
- Verify consent mechanics work

---

## 💰 ROI SUMMARY

| Agent | Time Saved | API Cost/Month | ROI |
|-------|------------|----------------|-----|
| ChoiceScript Converter | 45 hours | $30 | 75x |
| Lore Guardian | 15 hours | $20 | 37x |
| ChoiceScript Validator | 6 hours | $15 | 20x |
| Polly's Voice Architect | 2 hours | $15 | 6x |
| Romance Orchestrator | 3 hours | $20 | 7x |
| **TOTAL** | **71 hours** | **$100** | **35-71x** |

*ROI calculated at $50-100/hour human labor rate*

---

## 🆘 TROUBLESHOOTING

### Agent Not Found
**Issue:** Agent name not recognized  
**Fix:** Check file is in `.github/agents/` and merged to main branch

### Agent Produces Low Quality Output
**Issue:** Output doesn't meet standards  
**Fix:** Review agent's success metrics, refine task description, test on smaller scope

### Agent Conflicts with Worker
**Issue:** Agent and worker editing same file  
**Fix:** Coordinate timing - run agents sequentially, not in parallel

### Agent Validation Fails
**Issue:** Content flagged incorrectly  
**Fix:** Review validation report, check if false positive, update canon sources if needed

---

## 📖 RELATED DOCUMENTATION

- **Full Strategy:** `docs/CUSTOM_AGENT_RECOMMENDATIONS.md` (17KB)
- **Implementation Guide:** `docs/CUSTOM_AGENT_IMPLEMENTATION_GUIDE.md` (20KB)
- **Quick Reference:** `docs/CUSTOM_AGENT_QUICK_REFERENCE.md` (6KB)
- **Agent Management:** `AGENT_MANAGEMENT_README.md`
- **Task Queue:** `docs/AI_TASK_QUEUE.md`

---

## ✅ NEXT STEPS

1. **Read:** `docs/CUSTOM_AGENT_QUICK_REFERENCE.md` (2 min)
2. **Deploy Phase 1:** ChoiceScript Converter + Lore Guardian
3. **Test:** Convert 1-2 scenes, validate output
4. **Monitor:** Check success metrics
5. **Scale:** Deploy Phase 2 if Phase 1 succeeds

---

**Status:** ✅ 5 agents created and ready for deployment  
**Expected Impact:** 50-60% reduction in development time  
**Timeline:** Phase 1 deploy within 1-2 days

---

*"Specialized agents. Accelerated development. Professional quality."*  
**Caw.** 🪶
