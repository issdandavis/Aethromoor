# MULTI_AI_ROLES.md
## Role Definitions for Collaborative Development

**Purpose:** Define clear responsibilities for different AI assistants working on Avalon  
**Last Updated:** November 23, 2025  
**Version:** 1.0 (Stage1 Initialization)

---

## 🎭 Role System Overview

The Avalon project uses a **multi-AI collaboration model** where different AI assistants take specialized roles to avoid overlap and maximize efficiency. Each role has specific tools, responsibilities, and coordination protocols.

### Core Principles
1. **Separation of Concerns** - Each role has distinct responsibilities
2. **Shared Context** - All roles use the same anchor artifacts
3. **Clear Handoffs** - Defined protocols for passing work between roles
4. **Version Control** - Git commit prefixes identify which role made changes
5. **No Overlap** - Roles trust each other's expertise

---

## 👥 ROLE DEFINITIONS

### 🎨 Lore Curator (Claude/Creative Model)

**Primary Responsibility:** Maintain narrative consistency and world-building integrity

**Key Duties:**
- Validate new narrative content against existing lore
- Check timeline consistency across generations
- Ensure magic system rules are followed
- Verify character personality consistency
- Flag contradictions with established canon
- Approve thematic coherence

**Tools & References:**
- `lore/` directory (all worldbuilding documents)
- `writing_drafts/IZACK_MASTER_CHRONICLE_UPDATED.txt`
- `lore/Unified Worldbuilding Master Framew.txt`
- `docs/AETHERMOOR_CHRONICLES.md`
- Character personality guides

**When to Engage:**
- Before implementing new narrative content
- When expanding character dialogue
- When creating new magical mechanics
- If timeline questions arise
- When adding new locations or lore elements

**Handoff Protocol:**
- Reviews scene drafts for lore accuracy
- Provides "Lore Approved ✓" or requests changes
- Documents any new lore in appropriate files
- Updates STATUS_CONTEXT.md with lore decisions

**Git Commit Prefix:** `Lore:`

**Example Tasks:**
- Verify that Thoughtvine mechanics match established forest lore
- Ensure Polly's sarcasm level is consistent with character
- Check that Izack's teaching methods align with collaborative magic philosophy
- Validate timeline: Does this event fit the generation structure?

---

### 🔧 Conversion Engineer (Copilot/Continue)

**Primary Responsibility:** Convert HTML scenes to ChoiceScript format

**Key Duties:**
- Translate HTML game content to ChoiceScript syntax
- Preserve choice logic and branching
- Implement stat modifications correctly
- Maintain narrative flow
- Expand placeholder content to full scenes
- Match target line counts (600+ for expeditions)

**Tools & References:**
- `game/game.js` (HTML source)
- `choicescript_game/scenes/` (target files)
- `choicescript_game/scenes/first_lesson.txt` (format example)
- `.github/COPILOT_INSTRUCTIONS.md` (ChoiceScript syntax guide)
- SCENE_PARITY_CHECKLIST.md

**When to Engage:**
- Converting HTML scenes to ChoiceScript
- Expanding placeholder scenes
- Implementing new choices and branches
- Writing narrative prose
- Creating scene transitions

**Handoff Protocol:**
- Receives "Lore Approved ✓" scenes
- Drafts ChoiceScript implementation
- Adds `// TODO:[ROLE]` comments for stat balancing
- Updates SCENE_PARITY_CHECKLIST.md to "Draft" status
- Hands off to Structural Reviewer

**Git Commit Prefix:** `Convert:`

**Example Tasks:**
- Expand verdant_tithe.txt from 183 to 600+ lines
- Convert Dreamwillow vision sequence from HTML
- Implement Thoughtvine deep merge scene
- Add environmental descriptions and Polly commentary

---

### 🏗️ Structural Reviewer (Cody/Codeium)

**Primary Responsibility:** Ensure technical correctness and scene parity

**Key Duties:**
- Verify all `*goto` targets exist
- Ensure scene has same branching as HTML version
- Check ending count matches
- Validate stat progression logic
- Test scene flow and transitions
- Confirm no dead ends exist
- Verify syntax correctness

**Tools & References:**
- SCENE_PARITY_CHECKLIST.md (main tracking document)
- `game/game.js` (HTML reference)
- ChoiceScript syntax validator
- Codebase indexing tools

**When to Engage:**
- After Conversion Engineer completes draft
- Before stat balancing begins
- When verifying bug fixes
- During final quality checks

**Handoff Protocol:**
- Receives "Draft" scenes from Conversion Engineer
- Runs structural checks (gotos, labels, branches)
- Updates SCENE_PARITY_CHECKLIST.md with findings
- Marks "Complete" if structure sound, or returns to Engineer
- Hands off to Quality Balancer for stat tuning

**Git Commit Prefix:** `Struct:`

**Verification Checklist:**
- [ ] All `*goto` statements point to valid labels
- [ ] All `*label` names are unique
- [ ] Scene has same number of choices as HTML version
- [ ] Branches lead to correct endpoints
- [ ] No orphaned code sections
- [ ] Page breaks placed appropriately
- [ ] Syntax follows ChoiceScript standards

---

### ⚖️ Quality Balancer

**Primary Responsibility:** Balance stat progression and difficulty

**Key Duties:**
- Adjust collaboration stat thresholds
- Ensure ending accessibility is fair
- Balance relationship stat gains/losses
- Equalize difficulty across expeditions
- Verify artifact acquisition feels earned
- Test edge cases for stat requirements
- Update STATS_MATRIX.md

**Tools & References:**
- STATS_MATRIX.md (primary reference)
- Ending threshold calculations
- Playtest data (when available)
- Difficulty curve guidelines

**When to Engage:**
- After structural review complete
- When balancing expedition difficulty
- If ending accessibility seems off
- During final polish phase
- After beta testing feedback

**Handoff Protocol:**
- Receives "Complete" scenes from Structural Reviewer
- Reviews all stat modifications
- Adjusts thresholds for balance
- Updates STATS_MATRIX.md with changes
- Marks scene "Verified" in SCENE_PARITY_CHECKLIST.md
- Approves for final testing

**Git Commit Prefix:** `Balance:`

**Balance Guidelines:**
- No single choice should swing > 25 collaboration points
- Each expedition should offer similar total stat ranges
- Multiple paths to each ending tier
- Failure endings should be hard but possible to avoid
- Artifact acquisition: meaningful but achievable

---

### 🤖 Automation Planner (Any Model)

**Primary Responsibility:** Document automation workflows and triggers

**Key Duties:**
- Update Zapier workflow documentation
- Plan analytics triggers
- Document new content types for automation
- Maintain deployment procedures
- Track integration points
- Update CI/CD documentation

**Tools & References:**
- `docs/AUTOMATION_GUIDE.md`
- Zapier workflow configurations
- GitHub Actions (if any)
- Analytics tracking plans

**When to Engage:**
- When new content types are added
- If expedition structure changes
- During deployment planning
- When setting up beta testing infrastructure
- For analytics implementation

**Handoff Protocol:**
- Monitors development for automation opportunities
- Documents new workflows in AUTOMATION_GUIDE.md
- Coordinates with other roles for trigger points
- No blocking dependencies on other roles

**Git Commit Prefix:** `Auto:`

**Scope:**
- Analytics event triggers
- Content deployment automation
- Beta testing workflows
- Social media integration (if planned)
- Save file migration (if needed)

---

## 📋 SHARED CONTEXT ARTIFACTS

All roles reference these files to maintain synchronized state:

### STATUS_CONTEXT.md
**Owner:** All roles (collaborative)  
**Update Frequency:** Weekly or after milestones  
**Purpose:** Current development snapshot

### SCENE_PARITY_CHECKLIST.md
**Owner:** Structural Reviewer (primary)  
**Update Frequency:** After each scene modification  
**Purpose:** Track HTML ↔ ChoiceScript alignment

### STATS_MATRIX.md
**Owner:** Quality Balancer (primary)  
**Update Frequency:** After stat-affecting changes  
**Purpose:** Comprehensive stat tracking

### PROJECT_ROADMAP.md
**Owner:** Project management  
**Update Frequency:** Phase transitions  
**Purpose:** Overall development plan

### NEXT_TASKS.md
**Owner:** All roles (collaborative)  
**Update Frequency:** As tasks completed  
**Purpose:** Priority queue

---

## 🔄 COLLABORATION WORKFLOW

### Standard Development Flow

```
1. LORE CURATOR
   ↓ (Approves narrative integrity)
   
2. CONVERSION ENGINEER
   ↓ (Drafts ChoiceScript scene)
   
3. STRUCTURAL REVIEWER
   ↓ (Verifies technical correctness)
   
4. QUALITY BALANCER
   ↓ (Adjusts stat balance)
   
5. FINAL VERIFICATION
   (Scene marked "Verified" - ready for play)
```

### Parallel Workflows

- **Automation Planner** works independently, updates docs
- **Lore Curator** can review multiple drafts simultaneously
- **Quality Balancer** can adjust multiple scenes in batch

### Handoff Markers

**In-File Comments:**
```choicescript
*comment TODO:Struct: Verify this goto target exists
*comment TODO:Balance: Adjust this threshold if Glacier too hard
*comment LORE-APPROVED: 2025-11-23
```

**Remove TODOs before marking "Verified"**

### Git Workflow

1. Create branch: `role/task-name-date`
2. Commit with prefix: `Role: Description`
3. Update relevant shared artifact
4. Push and notify next role (if sequential)

---

## 🎯 ROLE SELECTION GUIDE

### When You're Starting Work

**Ask yourself:**
1. **Is this a narrative/lore question?** → Lore Curator
2. **Am I converting HTML to ChoiceScript?** → Conversion Engineer
3. **Am I checking structure/syntax?** → Structural Reviewer
4. **Am I balancing stats/difficulty?** → Quality Balancer
5. **Am I documenting automation?** → Automation Planner

### Multi-Role Sessions

Some tasks require multiple roles:
- **New scene expansion:** Curator → Engineer → Reviewer → Balancer
- **Bug fix:** Reviewer → (Balancer if stat-related)
- **Lore addition:** Curator → Engineer (if affects scenes)

### Role Boundaries

**Lore Curator should NOT:**
- Write ChoiceScript syntax
- Balance stat numbers
- Verify goto statements

**Conversion Engineer should NOT:**
- Make lore decisions without approval
- Balance stat thresholds
- Verify all gotos exist (Reviewer's job)

**Structural Reviewer should NOT:**
- Rewrite narrative content
- Make major stat adjustments
- Create new lore

**Quality Balancer should NOT:**
- Change narrative flow
- Add new scenes
- Make lore decisions

---

## 📊 ROLE ACCOUNTABILITY

### Success Metrics

**Lore Curator:**
- Zero lore contradictions in final content
- Character voices remain consistent
- Timeline coherence maintained

**Conversion Engineer:**
- All HTML scenes converted to ChoiceScript
- Target line counts achieved
- Narrative quality maintained or exceeded

**Structural Reviewer:**
- Zero broken goto statements
- All branches verified
- Scene parity 100%

**Quality Balancer:**
- All endings accessible through reasonable play
- Stat progression feels fair
- Difficulty balanced across expeditions

---

## 🆘 CONFLICT RESOLUTION

### If Roles Disagree

1. **Document the conflict** in relevant artifact
2. **Consult source material** (lore docs, HTML game)
3. **Defer to specialty:** Lore questions → Curator, Balance questions → Balancer
4. **Escalate if needed** to project owner (@issdandavis)

### Common Conflicts

- **"This stat change breaks lore!"** → Lore Curator has final say on thematic fit, Balancer adjusts numbers
- **"This branch doesn't exist in HTML!"** → Check SCENE_PARITY for intentional enhancement vs mistake
- **"This ending is too hard to reach!"** → Quality Balancer analyzes, may adjust thresholds

---

## 📚 QUICK REFERENCE

### Role Priority Order (for conflicts)
1. **Lore Curator** - Narrative integrity is paramount
2. **Quality Balancer** - Player experience matters
3. **Structural Reviewer** - Technical correctness required
4. **Conversion Engineer** - Prose can be adjusted
5. **Automation Planner** - Non-blocking enhancements

### Communication Protocol
- **Blocking issues:** Add BLOCKED tag to STATUS_CONTEXT.md
- **Questions:** Add QUESTION tag with @role mention
- **Approvals:** Add APPROVED tag with role signature
- **Handoffs:** Update checklist status and notify

---

**Maintained by:** Multi-AI Collaboration System  
**Version:** 1.0 (Stage1 Initialization)  
**Review Date:** After first full collaboration cycle
