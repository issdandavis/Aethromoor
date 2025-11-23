# Documentation - AI Agent Instructions

## 📚 Purpose
This directory contains **project documentation** including roadmaps, automation guides, development plans, and tracking documents for the Avalon Codex project.

## 📁 Directory Structure

```
docs/
├── PROJECT_ROADMAP.md          → Development phases and current status
├── AUTOMATION_GUIDE.md         → Zapier workflows and automation setup
├── NEXT_TASKS.md              → Immediate priority tasks
├── CONSOLIDATION_SUMMARY.md   → Repository organization history
├── COMPLETE_MATERIALS_SUMMARY.md → Content inventory
├── AETHERMOOR_CHRONICLES.md   → Future project planning
├── TRACING.md                 → Analytics and tracking documentation
└── [Future tracking docs]     → STATUS_CONTEXT, SCENE_PARITY_CHECKLIST, STATS_MATRIX
```

## 🎯 Documentation Standards

### When to Create New Documentation
- ✅ New development phase begins
- ✅ New automation workflow implemented
- ✅ Major architectural decision made
- ✅ Tracking system established
- ✅ Process change affects multiple contributors

### When to Update Existing Documentation
- ✅ Development phase milestone reached
- ✅ Task priority changes
- ✅ Automation workflow modified
- ✅ New features added to tracking systems
- ✅ Deadlines or timelines shift

### Documentation Writing Style
**Be:**
- Clear and concise
- Action-oriented (use checklists)
- Up-to-date (document changes immediately)
- Consistent in formatting
- Practical and useful for future reference

**Avoid:**
- Vague language ("maybe", "possibly")
- Outdated information (update or remove)
- Redundancy (link to other docs instead of duplicating)
- Overly technical jargon (explain when necessary)
- Missing context (assume reader hasn't been following along)

## 📋 Key Documents Explained

### PROJECT_ROADMAP.md - The Master Plan
**Purpose**: Track development progress across all phases
**Update frequency**: Weekly or after major milestones
**Owned by**: Project lead / Structural Reviewer

**Required sections:**
- Current status with completion checkboxes
- Active phase with priority tasks
- Next milestone clearly defined
- Timeline estimates (realistic)
- Success metrics for each phase

**Update triggers:**
- Major task completed
- Phase transition
- Timeline adjustment
- Scope change
- New milestone added

### AUTOMATION_GUIDE.md - Workflow Documentation
**Purpose**: Document all automated processes (Zapier, scripts, etc.)
**Update frequency**: When automation changes
**Owned by**: Automation Planner role

**Required sections:**
- Each automation with clear purpose
- Setup instructions (reproducible)
- Trigger conditions
- Expected outcomes
- Troubleshooting common issues

**Update triggers:**
- New automation created
- Existing workflow modified
- Integration point added
- Automation disabled/removed
- Bug fix applied

### NEXT_TASKS.md - Immediate Priorities
**Purpose**: Track current week's tasks and immediate priorities
**Update frequency**: Daily to weekly
**Owned by**: All contributors

**Required sections:**
- High-priority tasks (do this week)
- Medium-priority tasks (do this month)
- Low-priority / future tasks
- Blocked tasks (waiting on something)

**Update triggers:**
- Task completed
- Priority shift
- Blocker encountered
- New urgent task identified

## 🔄 Multi-AI Collaboration Tracking Docs

### STATUS_CONTEXT.md (Create if Missing)
**Purpose**: Weekly snapshot for AI agent context synchronization
**Format**:
```markdown
# Status Context - Week of [Date]

## Current Work
- **Active Scene**: singing_dunes.txt conversion
- **Assigned Role**: Conversion Engineer
- **Blocker**: Waiting on lore verification for Kael's dialogue

## Recent Changes
- Completed first_lesson.txt ChoiceScript conversion
- Updated SCENE_PARITY_CHECKLIST.md
- Fixed stat threshold in arrival_walk.txt

## Pending Tasks
- [ ] Complete Singing Dunes conversion
- [ ] Lore check on desert magic system
- [ ] Update STATS_MATRIX with new choices

## Known Issues
- Collaboration stat may be too easy in forest expedition
- Need to verify ending_truthbound_mage.txt logic
```

**Update frequency**: Start of each work session
**Owned by**: Current active AI agent

### SCENE_PARITY_CHECKLIST.md (Create if Missing)
**Purpose**: Track HTML vs ChoiceScript scene conversion status
**Format**:
```markdown
# Scene Parity Checklist

## Opening Sequence
- [x] polly_intro.txt - Verified, 1,200 words
- [x] character_creation.txt - Verified, 800 words

## Arrival Paths
- [x] arrival_teleport.txt - Verified, 600 words
- [x] arrival_walk.txt - Verified, 650 words
- [x] arrival_fly.txt - Verified, 620 words

## First Lesson
- [x] first_lesson.txt - Verified, 3,500 words
- [x] All branching paths match HTML
- [x] Stat tracking verified

## Expeditions
- [ ] singing_dunes.txt - Draft, ~70% complete
- [ ] verdant_tithe.txt - Missing
- [ ] rune_glacier.txt - Missing

## Endings
- [ ] ending_collaborative_master.txt - Missing
- [ ] ending_truthbound_mage.txt - Missing
[... all 14 endings listed ...]
```

**Update frequency**: After each scene conversion or verification
**Owned by**: Structural Reviewer role

### STATS_MATRIX.md (Create if Missing)
**Purpose**: Track all stat-affecting choices across both versions
**Format**:
```markdown
# Stats Matrix - Choice Impact Tracking

## First Lesson
| Source File | Choice Description | Collaboration | Aria | Zara | Polly | Notes |
|------------|-------------------|---------------|------|------|-------|-------|
| first_lesson.txt | Work with magic collaboratively | +5 | +1 | 0 | +1 | Major positive |
| first_lesson.txt | Force magic to obey | -5 | -1 | 0 | 0 | Major negative |
| first_lesson.txt | Ask Aria for guidance | +2 | +2 | 0 | +1 | Relationship builder |

## Singing Dunes
| Source File | Choice Description | Collaboration | Kael | Notes |
|------------|-------------------|---------------|------|-------|
| singing_dunes.txt | Speak truth to sand | +5 | +2 | Truth path |
| singing_dunes.txt | Try to control desert | -5 | -2 | Control path |
| singing_dunes.txt | Reject oath-magic | -3 | -3 | Rejection path |

## Ending Thresholds
| Ending | Required Stats | Required Flags |
|--------|---------------|----------------|
| Collaborative Master | Collaboration >= 85, all expeditions complete | glacier_path = "harmony" |
| Truthbound Mage | Collaboration >= 60 | dunes_path = "truth" |
```

**Update frequency**: After each choice implementation or stat adjustment
**Owned by**: Quality Balancer role

## ✏️ Documentation Editing Guidelines

### Updating PROJECT_ROADMAP.md
**When checking off tasks:**
```markdown
<!-- BEFORE -->
- [ ] Complete Singing Dunes expedition

<!-- AFTER -->
- [x] Complete Singing Dunes expedition
```

**When adding new tasks:**
- Add to appropriate phase section
- Include clear acceptance criteria
- Estimate time/effort if known
- Note dependencies

**When changing phases:**
- Update "CURRENT STATUS" section at top
- Add completion date to finished phase
- Move active tasks to current phase
- Archive completed checklists

### Updating AUTOMATION_GUIDE.md
**When documenting new automation:**
```markdown
## [Automation Name]

**Purpose**: [What does this do and why?]

**Trigger**: [What starts this automation?]

**Actions**:
1. [Step-by-step process]
2. [With specific details]
3. [That someone could reproduce]

**Expected Outcome**: [What should happen when successful?]

**Troubleshooting**:
- **Issue**: [Common problem]
  **Solution**: [How to fix]
```

### Creating Tracking Documents
**For STATUS_CONTEXT.md:**
- Create in `/docs/` directory
- Update at start of each work session
- Keep concise (one page maximum)
- Focus on current context, not history

**For SCENE_PARITY_CHECKLIST.md:**
- Create in `/docs/` directory
- List ALL scenes (HTML and ChoiceScript)
- Use consistent status labels: Missing / Draft / Verified
- Include word counts for parity checking
- Update after every conversion or verification

**For STATS_MATRIX.md:**
- Create in `/docs/` directory
- Use tables for clarity
- Include source file, choice text, and all stat impacts
- Document ending thresholds separately
- Update after implementing any stat-affecting choice

## 🎯 Automation Planner Role

**When acting as Automation Planner:**

**Your responsibilities:**
- ✅ Document all automation workflows
- ✅ Update guides when processes change
- ✅ Identify automation opportunities
- ✅ Maintain AUTOMATION_GUIDE.md accuracy
- ✅ Track analytics requirements

**Your process:**
1. Identify repeated manual task
2. Research automation solution (Zapier, script, etc.)
3. Document workflow BEFORE implementing
4. Implement and test
5. Document in AUTOMATION_GUIDE.md
6. Add to NEXT_TASKS.md for monitoring

**Your communication format:**
```
AUTOMATION UPDATE: [Workflow Name]

📋 WHAT CHANGED:
[Describe modification to existing automation OR new automation created]

📝 DOCUMENTATION UPDATED:
- Updated AUTOMATION_GUIDE.md section [X]
- Added troubleshooting for [issue]
- Included setup instructions for [tool]

🎯 IMPACT:
[What this automation saves / improves / enables]

✅ TESTING:
[How you verified it works as expected]
```

## ✅ Documentation Quality Checklist

Before committing documentation updates:

- [ ] All information is current and accurate
- [ ] Checklists updated with latest status
- [ ] Dates reflect actual completion times
- [ ] No broken links to other documents
- [ ] Formatting is consistent (headings, lists, code blocks)
- [ ] Technical terms are explained or linked
- [ ] Contact info / ownership is clear if applicable
- [ ] Changes are reflected in related documents
- [ ] Commit message clearly states what was updated
- [ ] Future readers could follow without prior context

## 🚨 Documentation Red Flags

**Watch out for:**
- ❌ Outdated status (says "in progress" but actually complete)
- ❌ Conflicting information across different docs
- ❌ Missing context (assumes reader knows backstory)
- ❌ Vague action items ("improve game" - improve *what* exactly?)
- ❌ Orphaned references (mentions doc that doesn't exist)
- ❌ No ownership (unclear who maintains this)
- ❌ Stale timestamps (last update 6 months ago but claims "current")
- ❌ Duplicate information (copy-pasted across multiple docs)

## 📚 Documentation Resources

**Style Guides:**
- GitHub Flavored Markdown (for formatting)
- Microsoft Writing Style Guide (for tone/clarity)
- Plain Language Guidelines (for accessibility)

**Tools:**
- Markdown linters (for consistency)
- Grammarly or LanguageTool (for prose)
- Link checkers (for broken references)

**Project-Specific References:**
- Root AGENTS.md (for overall project context)
- PROJECT_ROADMAP.md (for current development phase)
- Repository README.md (for project overview)

## 🎊 Success Metrics

Your documentation is successful if:
- ✅ New contributors can onboard from docs alone
- ✅ Current status is always accurate
- ✅ Automation workflows are reproducible
- ✅ Tracking documents enable coordination
- ✅ Decisions are documented with rationale
- ✅ Progress is visible and measurable
- ✅ Blockers are identified early
- ✅ Future you can pick up where you left off

---

*Good documentation is a love letter to your future self and your collaborators.*
