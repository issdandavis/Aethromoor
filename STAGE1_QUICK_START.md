# 🚀 STAGE1_QUICK_START.md
## Quick Reference Card for Multi-AI Collaboration

**For AI assistants joining the project:** Start here!

---

## ⚡ 30-Second Orientation

**Project:** Polly's Wingscroll - Choice-based fantasy game  
**Phase:** 2 of 5 (Content completion - 97% done)  
**Your First Task:** Check which role you're filling, then read that role's section

---

## 📋 ESSENTIAL FILES (Read in Order)

### 1. **STATUS_CONTEXT.md** ← Read THIS FIRST
Current development snapshot. Tells you:
- What's being worked on RIGHT NOW
- What's complete vs incomplete
- What needs attention next

### 2. **MULTI_AI_ROLES.md** ← Then read THIS
Find your role:
- 🎨 **Lore Curator** - Keeping narrative consistent
- 🔧 **Conversion Engineer** - Writing ChoiceScript scenes
- 🏗️ **Structural Reviewer** - Verifying technical correctness
- ⚖️ **Quality Balancer** - Balancing stats and difficulty
- 🤖 **Automation Planner** - Documenting workflows

### 3. **Your Role's Artifact**
- Lore Curator → `lore/` directory + character docs
- Conversion Engineer → SCENE_PARITY_CHECKLIST.md
- Structural Reviewer → SCENE_PARITY_CHECKLIST.md
- Quality Balancer → STATS_MATRIX.md
- Automation Planner → `docs/AUTOMATION_GUIDE.md`

---

## 🎯 CURRENT PRIORITY (Week of Nov 23, 2025)

**EXPAND VERDANT TITHE EXPEDITION**

**Current state:** 183 lines (placeholder)  
**Target:** 600+ lines (production-ready)  
**Location:** `/home/runner/work/Avalon/Avalon/choicescript_game/scenes/verdant_tithe.txt`

**Needs:**
- Thoughtvine deep merge scene
- Dreamwillow vision sequence
- Heartwood Tree communion
- Environmental descriptions
- Polly commentary
- Stat modifications

**Reference:**
- HTML version: `game/game.js` (search "verdantTithe")
- Quality example: `choicescript_game/scenes/singing_dunes.txt` (931 lines)

---

## 🔄 QUICK WORKFLOW

```
1. Read STATUS_CONTEXT.md
2. Identify your role
3. Check your artifact for details
4. Do your work
5. Update your artifact
6. Update STATUS_CONTEXT.md if milestone
7. Commit with role prefix: "Role: description"
```

---

## 📊 PROJECT AT A GLANCE

| Metric | Status |
|--------|--------|
| **Singing Dunes** | ✅ 931 lines - Complete |
| **Rune Glacier** | ✅ 1,266 lines - Complete |
| **Verdant Tithe** | 🟡 183 lines - NEEDS WORK |
| **Endings** | ✅ 1,118 lines - 13/14 done |
| **Overall** | 🟢 97% complete |

**Next milestone:** Verdant Tithe → 600+ lines → Phase 2 complete!

---

## 🆘 QUICK ANSWERS

**Q: I'm lost, where do I start?**  
A: Read STATUS_CONTEXT.md, then MULTI_AI_ROLES.md

**Q: What should I work on?**  
A: Expand Verdant Tithe (if Conversion Engineer role)

**Q: How do I know if I'm doing it right?**  
A: Check SCENE_PARITY_CHECKLIST.md for structure, STATS_MATRIX.md for balance

**Q: Can I change [X]?**  
A: Check your role boundaries in MULTI_AI_ROLES.md

**Q: Where's the lore reference?**  
A: `lore/` directory, especially `Unified Worldbuilding Master Framew.txt`

**Q: How do I test my changes?**  
A: ChoiceScript IDE needed (see `QUICK_START.md` in repo)

---

## 📁 KEY FILE LOCATIONS

```
Avalon/
├── STATUS_CONTEXT.md ← CURRENT STATE
├── SCENE_PARITY_CHECKLIST.md ← SCENE TRACKING
├── STATS_MATRIX.md ← STAT BALANCE
├── MULTI_AI_ROLES.md ← ROLE DEFINITIONS
├── STAGE1_COMPLETION_REPORT.md ← WHAT STAGE1 ACHIEVED
│
├── choicescript_game/scenes/
│   ├── verdant_tithe.txt ← NEEDS EXPANSION
│   ├── singing_dunes.txt ← REFERENCE (complete)
│   ├── rune_glacier.txt ← REFERENCE (complete)
│   └── endings.txt ← ENDINGS (nearly complete)
│
├── game/game.js ← HTML SOURCE (for conversion reference)
│
├── lore/ ← WORLDBUILDING
│   └── Unified Worldbuilding Master Framew.txt
│
└── docs/
    ├── PROJECT_ROADMAP.md ← OVERALL PLAN
    ├── NEXT_TASKS.md ← TASK QUEUE
    └── AUTOMATION_GUIDE.md ← WORKFLOWS
```

---

## ✅ ROLE-SPECIFIC QUICK STARTS

### 🎨 If You're LORE CURATOR:
1. Read `lore/Unified Worldbuilding Master Framew.txt`
2. Review `writing_drafts/IZACK_MASTER_CHRONICLE_UPDATED.txt`
3. Check `choicescript_game/scenes/verdant_tithe.txt`
4. Verify Thoughtvine mechanics match established lore
5. Approve or request changes

### 🔧 If You're CONVERSION ENGINEER:
1. Read `game/game.js` - search "verdantTithe"
2. Look at `choicescript_game/scenes/singing_dunes.txt` for format
3. Expand `choicescript_game/scenes/verdant_tithe.txt`
4. Target 600+ lines with rich descriptions
5. Update SCENE_PARITY_CHECKLIST.md to "Draft"

### 🏗️ If You're STRUCTURAL REVIEWER:
1. Wait for Conversion Engineer to finish Verdant draft
2. Verify all `*goto` statements point to valid labels
3. Check branching matches HTML version
4. Update SCENE_PARITY_CHECKLIST.md with findings
5. Hand off to Quality Balancer

### ⚖️ If You're QUALITY BALANCER:
1. Review STATS_MATRIX.md current state
2. Plan stat distribution for Verdant Tithe expansion
3. Calculate Heartwood Guardian ending accessibility
4. Adjust thresholds if needed
5. Update STATS_MATRIX.md

### 🤖 If You're AUTOMATION PLANNER:
1. Review `docs/AUTOMATION_GUIDE.md`
2. Monitor for new content types
3. No immediate blocking tasks
4. Document any new workflows

---

## 🎯 SUCCESS CRITERIA

**You'll know you succeeded when:**
- [x] You updated the relevant artifact
- [x] Your changes align with your role boundaries
- [x] You didn't step on another role's toes
- [x] STATUS_CONTEXT.md reflects changes (if milestone)
- [x] Git commit has correct role prefix

---

## 💡 PRO TIPS

✨ **Always read STATUS_CONTEXT.md first** - saves time  
✨ **Trust other roles' expertise** - don't redo their work  
✨ **Update artifacts as you go** - not at the end  
✨ **Use role prefixes in commits** - easy to track  
✨ **Ask in STATUS_CONTEXT.md** - leave questions for next AI

---

## 🚦 TRAFFIC LIGHT STATUS

🔴 **BLOCKED** - Something prevents progress (note in STATUS_CONTEXT)  
🟡 **IN PROGRESS** - Active development  
🟢 **COMPLETE** - Ready for next role/phase  
✅ **VERIFIED** - Tested and approved

Current Verdant Tithe status: 🟡 IN PROGRESS

---

## 📞 ESCALATION PATH

1. **Check STATUS_CONTEXT.md** - might be answered there
2. **Check your role's artifact** - detailed guidance
3. **Check MULTI_AI_ROLES.md** - role boundaries
4. **Leave note in STATUS_CONTEXT.md** - for next AI
5. **Contact project owner** - @issdandavis (GitHub)

---

## 🎊 YOU'RE READY!

You now know:
- ✅ What Stage1 achieved (organizational framework)
- ✅ Where to find current state (STATUS_CONTEXT.md)
- ✅ Your role and responsibilities (MULTI_AI_ROLES.md)
- ✅ What needs work right now (Verdant Tithe expansion)
- ✅ How to coordinate with other roles (handoff protocols)

**Go forth and code!** 🚀

---

**Created:** Stage1 Initialization  
**Purpose:** Fastest onboarding for multi-AI collaboration  
**Next Update:** When priorities change
