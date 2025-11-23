# AI Task Queue - Multi-AI Coordination System

**Purpose:** This file coordinates work between multiple AI assistants working on the Avalon project simultaneously.

**Last Updated:** 2025-11-23 10:17 UTC

---

## 🚀 How This Works

1. **Tasks are added** to the queue below with priority, status, and assigned AI role
2. **AI assistants claim tasks** by updating status to "In Progress" and adding their name
3. **On completion**, AI updates status to "Complete" and commits with `./scripts/auto-commit.sh`
4. **Other AIs pick up** the next available task in their specialty area
5. **Human oversight** can intervene at any time to reprioritize or reassign

---

## 📊 Task Queue

### Priority 1: URGENT

#### TASK-001: Complete Multi-AI Coordination Framework ⏳
- **Status:** In Progress
- **Assigned To:** Copilot
- **Role:** Automation Planner
- **Estimated Time:** 2 hours
- **Description:** Set up complete AI-to-AI coordination system including task queue, handoff protocols, and shared context files
- **Dependencies:** None
- **Deliverables:**
  - [ ] Task queue system (this file)
  - [ ] Scene parity checklist
  - [ ] Stats matrix
  - [ ] AI handoff protocols
  - [ ] Webhook integration framework
- **Started:** 2025-11-23 10:17 UTC
- **Notes:** Foundation for all multi-AI collaboration

---

### Priority 2: HIGH

#### TASK-002: Convert Singing Dunes to ChoiceScript 📝
- **Status:** Not Started
- **Assigned To:** Unassigned (needs Conversion Engineer)
- **Role:** Conversion Engineer
- **Estimated Time:** 3-4 hours
- **Description:** Convert Singing Dunes expedition from HTML (`game/game.js`) to ChoiceScript format
- **Source:** `game/game.js` (search for "singingDunes")
- **Target:** `choicescript_game/scenes/singing_dunes.txt`
- **Dependencies:** None
- **Prerequisites:**
  - Read HTML source carefully
  - Review existing ChoiceScript scenes for format
  - Maintain stat tracking consistency
- **Lore Validation Needed:** Yes (Lore Curator should review after completion)
- **Notes:** See `docs/NEXT_TASKS.md` for detailed requirements

#### TASK-003: Convert Verdant Tithe to ChoiceScript 📝
- **Status:** Not Started
- **Assigned To:** Unassigned (needs Conversion Engineer)
- **Role:** Conversion Engineer
- **Estimated Time:** 3-4 hours
- **Description:** Convert Verdant Tithe expedition from HTML to ChoiceScript
- **Source:** `game/game.js` (search for "verdantTithe")
- **Target:** `choicescript_game/scenes/verdant_tithe.txt`
- **Dependencies:** TASK-002 (learn from Singing Dunes conversion)
- **Lore Validation Needed:** Yes
- **Notes:** Three paths: Dreamwillow, Thoughtvine, Heartwood

#### TASK-004: Convert Rune Glacier to ChoiceScript 📝
- **Status:** Not Started
- **Assigned To:** Unassigned (needs Conversion Engineer)
- **Role:** Conversion Engineer
- **Estimated Time:** 3-4 hours
- **Description:** Convert Rune Glacier expedition from HTML to ChoiceScript
- **Source:** `game/game.js` (search for "runeGlacier")
- **Target:** `choicescript_game/scenes/rune_glacier.txt`
- **Dependencies:** TASK-002, TASK-003
- **Lore Validation Needed:** Yes
- **Notes:** Control vs Harmony paths

---

### Priority 3: MEDIUM

#### TASK-005: Validate Scene Parity 🔍
- **Status:** Not Started
- **Assigned To:** Unassigned (needs Structural Reviewer)
- **Role:** Structural Reviewer
- **Estimated Time:** 2 hours
- **Description:** Verify all ChoiceScript scenes match HTML version in branching and endings
- **Dependencies:** TASK-002, TASK-003, TASK-004
- **Deliverables:**
  - Complete `SCENE_PARITY_CHECKLIST.md`
  - List any discrepancies
  - Flag missing content
- **Notes:** Use checklist to track scene-by-scene comparison

#### TASK-006: Balance Collaboration Stats 📊
- **Status:** Not Started
- **Assigned To:** Unassigned (needs Quality Balancer)
- **Role:** Quality Balancer
- **Estimated Time:** 2-3 hours
- **Description:** Review and balance Collaboration stat thresholds across all expeditions
- **Dependencies:** TASK-002, TASK-003, TASK-004, TASK-005
- **Deliverables:**
  - Complete `STATS_MATRIX.md`
  - Adjust thresholds for fairness
  - Test each path is achievable
- **Notes:** Ensure each ending is reachable with reasonable player choices

#### TASK-007: Implement All 14 Endings 🎬
- **Status:** Not Started
- **Assigned To:** Unassigned (needs Conversion Engineer)
- **Role:** Conversion Engineer
- **Estimated Time:** 3 hours
- **Description:** Port all 14 endings from HTML to ChoiceScript
- **Source:** `game/game.js` (search for endings)
- **Target:** `choicescript_game/scenes/endings.txt`
- **Dependencies:** TASK-005 (need to know all paths lead correctly)
- **Notes:** See `docs/NEXT_TASKS.md` for full ending list

---

### Priority 4: LOW

#### TASK-008: Polish Polly's Commentary ✨
- **Status:** Not Started
- **Assigned To:** Unassigned (needs Lore Curator or Writer)
- **Role:** Lore Curator
- **Estimated Time:** 2-3 hours
- **Description:** Add more sarcastic commentary from Polly throughout the game
- **Dependencies:** None (can be done anytime)
- **Notes:** Maintain Polly's voice - sarcastic but helpful

#### TASK-009: Create Beta Testing Infrastructure 🧪
- **Status:** Not Started
- **Assigned To:** Unassigned (needs Automation Planner)
- **Role:** Automation Planner
- **Estimated Time:** 1-2 hours
- **Description:** Set up beta testing forms, feedback collection, and bug tracking
- **Dependencies:** TASK-002, TASK-003, TASK-004, TASK-007 (need complete game first)
- **Notes:** Only needed when game content is complete

---

## 🤖 AI Role Assignments

### How to Claim a Task

1. Find a task matching your role that is "Not Started"
2. Update the task:
   ```markdown
   - **Status:** In Progress
   - **Assigned To:** [Your AI Name/Platform]
   - **Started:** [Current UTC timestamp]
   ```
3. Add a note in `STATUS_CONTEXT.md` about what you're working on
4. Commit your changes: `./scripts/auto-commit.sh -m "AI [Name]: Claimed TASK-XXX"`
5. Do the work!
6. When done, update status to "Complete" and commit

### Specialized AI Roles

**Lore Curator** (Claude/creative models)
- Validates narrative consistency
- Checks against master lore documents
- Flags timeline or magic rule conflicts
- Best for: TASK-008

**Conversion Engineer** (Copilot/Continue)
- Translates HTML to ChoiceScript
- Preserves choice logic and stats
- Maintains game mechanics
- Best for: TASK-002, TASK-003, TASK-004, TASK-007

**Structural Reviewer** (Cody/Codeium)
- Ensures scene parity
- Checks stat progression
- Verifies branching consistency
- Best for: TASK-005

**Quality Balancer** (Any analytical AI)
- Balances difficulty
- Tests stat thresholds
- Ensures fair progression
- Best for: TASK-006

**Automation Planner** (Any AI with system knowledge)
- Sets up workflows
- Creates automation
- Manages infrastructure
- Best for: TASK-001, TASK-009

---

## 📝 Task Template

When adding new tasks, use this template:

```markdown
#### TASK-XXX: [Task Name] [Emoji]
- **Status:** Not Started | In Progress | Complete | Blocked
- **Assigned To:** Unassigned | [AI Name]
- **Role:** [AI Role Type]
- **Estimated Time:** [Hours]
- **Description:** [What needs to be done]
- **Source:** [Source files if applicable]
- **Target:** [Target files/deliverables]
- **Dependencies:** [Other task numbers]
- **Prerequisites:** [Things that must be done first]
- **Lore Validation Needed:** Yes | No
- **Notes:** [Additional context]
```

---

## 🔔 Notification System

When completing a task:
1. Update task status to "Complete"
2. Add completion timestamp
3. Commit with: `./scripts/auto-commit.sh -m "AI [Name]: Completed TASK-XXX - [brief description]"`
4. This triggers auto-push, making work available to all other AIs
5. Update `STATUS_CONTEXT.md` with next steps

---

## 📊 Progress Dashboard

**Total Tasks:** 9  
**Completed:** 0  
**In Progress:** 1  
**Not Started:** 8  
**Blocked:** 0  

**Estimated Time Remaining:** ~20-25 hours of AI work

---

## 🚨 Blockers and Issues

*(AI assistants: Add blockers here)*

- None currently

---

## 💡 Tips for AI Collaboration

1. **Always pull latest before starting:** The repo updates frequently
2. **Use auto-commit frequently:** `./scripts/auto-commit.sh` after each milestone
3. **Communicate in STATUS_CONTEXT.md:** Tell other AIs what you're doing
4. **Mark TODO comments:** Use `// TODO:[ROLE]:` for handoffs
5. **Test your work:** Run the game before marking complete
6. **Update documentation:** Keep guides current as you work

---

*This queue is maintained by all AI assistants working on the project. Human oversight can intervene at any time.*
