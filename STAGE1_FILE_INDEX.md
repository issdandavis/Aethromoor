# 📚 STAGE1_FILE_INDEX.md
## Complete Guide to Stage1 Framework Files

**Created:** November 23, 2025  
**Purpose:** Navigate the multi-AI collaboration framework

---

## 🎯 START HERE

### New to the Project?
👉 **[STAGE1_QUICK_START.md](STAGE1_QUICK_START.md)** - 30-second orientation

### Want the Full Story?
👉 **[STAGE1_COMPLETION_REPORT.md](STAGE1_COMPLETION_REPORT.md)** - Complete framework documentation

### Need a Summary?
👉 **[STAGE1_SUMMARY.txt](STAGE1_SUMMARY.txt)** - ASCII art summary for quick review

---

## 📋 FILE DIRECTORY

### 🔄 Living Documents (Update Frequently)

**[STATUS_CONTEXT.md](STATUS_CONTEXT.md)** - 4.4K
- **Update:** Weekly or after milestones
- **Purpose:** Current development snapshot
- **Users:** All roles
- **Contains:**
  - What's being worked on RIGHT NOW
  - Scene completion metrics
  - Pending lore updates
  - Next session priorities
  - Quick links to key files

**[SCENE_PARITY_CHECKLIST.md](SCENE_PARITY_CHECKLIST.md)** - 9.9K
- **Update:** After each scene modification
- **Purpose:** HTML ↔ ChoiceScript alignment tracking
- **Users:** Structural Reviewer (primary), Conversion Engineer
- **Contains:**
  - Scene-by-scene status (✅ Verified, 🟡 Draft, 🔴 Missing)
  - Line count tracking
  - Quality verification checklists
  - Branch and ending count verification
  - Overall parity metrics

**[STATS_MATRIX.md](STATS_MATRIX.md)** - 14K
- **Update:** After any stat-affecting changes
- **Purpose:** Comprehensive stat tracking & balance
- **Users:** Quality Balancer (primary), Conversion Engineer
- **Contains:**
  - Scene-by-scene stat modifications
  - Collaboration score progression
  - Relationship stat tracking
  - Artifact acquisition thresholds
  - Ending requirement calculations
  - Balance analysis & recommendations

---

### 📖 Reference Documents (Stable)

**[MULTI_AI_ROLES.md](MULTI_AI_ROLES.md)** - 13K
- **Update:** As needed when roles evolve
- **Purpose:** Role definitions & collaboration protocols
- **Users:** All roles
- **Contains:**
  - 5 specialized role definitions
  - Responsibilities and boundaries
  - Tools & reference materials
  - Handoff protocols
  - Git commit prefix conventions
  - Conflict resolution procedures
  - Workflow diagrams

**[STAGE1_COMPLETION_REPORT.md](STAGE1_COMPLETION_REPORT.md)** - 14K
- **Update:** Historical record (no updates)
- **Purpose:** Document Stage1 initialization outcomes
- **Users:** Reference, onboarding
- **Contains:**
  - What Stage1 achieved
  - Success criteria verification
  - Framework architecture
  - Benefits analysis
  - Next steps for each role
  - Complete deliverables list

**[STAGE1_QUICK_START.md](STAGE1_QUICK_START.md)** - 6.9K
- **Update:** When priorities change
- **Purpose:** Fastest onboarding for new AI assistants
- **Users:** Any AI joining the project
- **Contains:**
  - 30-second orientation
  - Essential files in reading order
  - Current priority (Verdant Tithe)
  - Role-specific quick starts
  - Quick answers to common questions

**[STAGE1_SUMMARY.txt](STAGE1_SUMMARY.txt)** - 5.2K
- **Update:** Historical snapshot
- **Purpose:** ASCII art summary for quick terminal viewing
- **Users:** Quick reference
- **Contains:**
  - Files created list
  - Framework capabilities
  - Current status
  - Role definitions
  - Success metrics

---

## 🗺️ NAVIGATION FLOWCHART

```
Are you NEW to the project?
    ↓ YES
    Read: STAGE1_QUICK_START.md (30 sec)
    Then: STATUS_CONTEXT.md (current state)
    Then: MULTI_AI_ROLES.md (find your role)
    ↓
    Ready to work!

Are you CONTINUING work?
    ↓ YES
    Check: STATUS_CONTEXT.md (what's current?)
    Check: Your role's artifact
        → Lore Curator: lore/ directory
        → Conversion Engineer: SCENE_PARITY_CHECKLIST.md
        → Structural Reviewer: SCENE_PARITY_CHECKLIST.md
        → Quality Balancer: STATS_MATRIX.md
        → Automation Planner: docs/AUTOMATION_GUIDE.md
    ↓
    Continue work, update artifacts

Want to UNDERSTAND the framework?
    ↓ YES
    Read: STAGE1_COMPLETION_REPORT.md (full details)
    Skim: STAGE1_SUMMARY.txt (quick overview)
    ↓
    Framework expert!
```

---

## 🎭 FILE USAGE BY ROLE

### 🎨 Lore Curator
**Primary Files:**
- `lore/` directory (worldbuilding)
- `writing_drafts/IZACK_MASTER_CHRONICLE_UPDATED.txt`

**Coordination Files:**
- STATUS_CONTEXT.md - Check pending lore updates
- SCENE_PARITY_CHECKLIST.md - See what scenes need approval

**Update Responsibility:**
- STATUS_CONTEXT.md - Mark lore items as approved/addressed

---

### 🔧 Conversion Engineer
**Primary Files:**
- `game/game.js` (HTML source)
- `choicescript_game/scenes/*.txt` (target files)

**Coordination Files:**
- SCENE_PARITY_CHECKLIST.md - **PRIMARY** - Track conversion status
- STATS_MATRIX.md - Reference for stat changes
- STATUS_CONTEXT.md - Check current priority

**Update Responsibility:**
- SCENE_PARITY_CHECKLIST.md - Mark scenes as "Draft" when done
- STATUS_CONTEXT.md - Note major progress

---

### 🏗️ Structural Reviewer
**Primary Files:**
- SCENE_PARITY_CHECKLIST.md - **PRIMARY** - Verification tracking

**Coordination Files:**
- `choicescript_game/scenes/*.txt` - Files to review
- STATUS_CONTEXT.md - Check what's ready for review

**Update Responsibility:**
- SCENE_PARITY_CHECKLIST.md - Mark scenes "Complete" or return to Engineer
- STATUS_CONTEXT.md - Note structural issues found

---

### ⚖️ Quality Balancer
**Primary Files:**
- STATS_MATRIX.md - **PRIMARY** - Balance tracking

**Coordination Files:**
- SCENE_PARITY_CHECKLIST.md - See what's ready for balancing
- STATUS_CONTEXT.md - Check balance priorities

**Update Responsibility:**
- STATS_MATRIX.md - Document all stat changes, recalculate thresholds
- SCENE_PARITY_CHECKLIST.md - Mark scenes "Verified" when balanced
- STATUS_CONTEXT.md - Note balance adjustments

---

### 🤖 Automation Planner
**Primary Files:**
- `docs/AUTOMATION_GUIDE.md`

**Coordination Files:**
- STATUS_CONTEXT.md - Monitor for automation opportunities

**Update Responsibility:**
- `docs/AUTOMATION_GUIDE.md` - Document new workflows
- STATUS_CONTEXT.md - Note automation added (optional)

---

## 📊 FILE RELATIONSHIPS

```
STAGE1_QUICK_START.md
    ├─→ Points newcomers to STATUS_CONTEXT.md
    └─→ References MULTI_AI_ROLES.md

STATUS_CONTEXT.md (weekly snapshot)
    ├─→ Links to SCENE_PARITY_CHECKLIST.md
    ├─→ Links to STATS_MATRIX.md
    └─→ Points to current work files

MULTI_AI_ROLES.md (coordination)
    ├─→ Defines how to use STATUS_CONTEXT.md
    ├─→ Defines how to use SCENE_PARITY_CHECKLIST.md
    └─→ Defines how to use STATS_MATRIX.md

SCENE_PARITY_CHECKLIST.md
    ├─→ Updated by Conversion Engineer (Draft)
    ├─→ Updated by Structural Reviewer (Complete)
    └─→ Updated by Quality Balancer (Verified)

STATS_MATRIX.md
    ├─→ Read by Conversion Engineer
    └─→ Updated by Quality Balancer

STAGE1_COMPLETION_REPORT.md
    └─→ Historical reference for framework design

STAGE1_SUMMARY.txt
    └─→ Quick terminal-friendly overview
```

---

## 🔍 FIND WHAT YOU NEED

### "What should I work on?"
→ **STATUS_CONTEXT.md** - Current focus section

### "How do I convert a scene?"
→ **MULTI_AI_ROLES.md** - Conversion Engineer role
→ **SCENE_PARITY_CHECKLIST.md** - See what's missing

### "Is this scene complete?"
→ **SCENE_PARITY_CHECKLIST.md** - Status column

### "How many points should this choice give?"
→ **STATS_MATRIX.md** - Stat balancing guidelines

### "What's my role's job?"
→ **MULTI_AI_ROLES.md** - Your role section

### "How do I hand off work?"
→ **MULTI_AI_ROLES.md** - Handoff protocols

### "What did Stage1 achieve?"
→ **STAGE1_COMPLETION_REPORT.md** - Full documentation
→ **STAGE1_SUMMARY.txt** - Quick overview

### "How do I start contributing?"
→ **STAGE1_QUICK_START.md** - 30-second onboarding

---

## 💾 FILE MAINTENANCE

### Update Frequency

| File | Frequency | Trigger |
|------|-----------|---------|
| STATUS_CONTEXT.md | Weekly | Major milestones |
| SCENE_PARITY_CHECKLIST.md | Per scene | Scene status changes |
| STATS_MATRIX.md | Per change | Stat modifications |
| MULTI_AI_ROLES.md | Rare | Role evolution |
| STAGE1_QUICK_START.md | Rare | Priority shifts |
| STAGE1_COMPLETION_REPORT.md | Never | Historical record |
| STAGE1_SUMMARY.txt | Never | Snapshot |

---

## 🎯 QUALITY CHECKS

### Before Committing Changes

- [ ] Updated relevant living document?
- [ ] STATUS_CONTEXT.md reflects changes if milestone?
- [ ] SCENE_PARITY_CHECKLIST.md updated if scene changed?
- [ ] STATS_MATRIX.md updated if stats changed?
- [ ] Git commit has role prefix (Lore:/Convert:/Struct:/Balance:/Auto:)?

---

## 📦 FILE PACKAGE SUMMARY

**Total Stage1 Files:** 7 (6 markdown + 1 txt)
**Total Documentation:** ~62K characters
**Living Documents:** 3 (frequent updates)
**Reference Documents:** 4 (stable)

**Core Trio (Most Important):**
1. STATUS_CONTEXT.md - Current state
2. SCENE_PARITY_CHECKLIST.md - Scene tracking
3. STATS_MATRIX.md - Balance tracking

**Onboarding Pair:**
1. STAGE1_QUICK_START.md - Fast start
2. MULTI_AI_ROLES.md - Role guide

**Documentation Pair:**
1. STAGE1_COMPLETION_REPORT.md - Full details
2. STAGE1_SUMMARY.txt - Quick overview

---

## 🚀 QUICK ACTIONS

### I'm starting work on Verdant Tithe
1. Check STATUS_CONTEXT.md (confirms it's the priority)
2. Read SCENE_PARITY_CHECKLIST.md (see current 183 lines status)
3. Review STATS_MATRIX.md (understand stat needs)
4. Get Lore Curator approval (if Conversion Engineer)
5. Expand the scene
6. Update SCENE_PARITY_CHECKLIST.md to "Draft"

### I'm verifying a scene
1. Check SCENE_PARITY_CHECKLIST.md (which scene is "Draft"?)
2. Verify all gotos, branches, syntax
3. Update SCENE_PARITY_CHECKLIST.md to "Complete" or return feedback
4. Hand off to Quality Balancer

### I'm balancing stats
1. Check STATS_MATRIX.md (current thresholds)
2. Review completed scene stat changes
3. Adjust for balance
4. Update STATS_MATRIX.md with changes
5. Mark scene "Verified" in SCENE_PARITY_CHECKLIST.md

---

## 📞 HELP & SUPPORT

**Can't find what you need?**
- Check this index again
- Read STAGE1_QUICK_START.md
- Consult MULTI_AI_ROLES.md
- Leave question in STATUS_CONTEXT.md

**Confused about roles?**
→ MULTI_AI_ROLES.md has detailed definitions

**Need project context?**
→ README.md + docs/PROJECT_ROADMAP.md

**Want to understand Stage1?**
→ STAGE1_COMPLETION_REPORT.md

---

**Maintained by:** Stage1 Framework  
**Last Updated:** November 23, 2025  
**Version:** 1.0  
**Purpose:** Navigate multi-AI collaboration files efficiently
