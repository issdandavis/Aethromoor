# AI Automation Features Guide

This document outlines all AI-powered automation features available in the Avalon repository to help streamline development, maintain quality, and improve collaboration.

## Table of Contents
1. [Custom AI Agents](#custom-ai-agents)
2. [GitHub Actions Workflows](#github-actions-workflows)
3. [Issue Templates for AI Tasks](#issue-templates-for-ai-tasks)
4. [AI Commands](#ai-commands)
5. [Multi-AI Coordination](#multi-ai-coordination)
6. [Best Practices](#best-practices)

---

## Custom AI Agents

The repository includes specialized AI agents for different aspects of the project. These agents have deep context about the Avalon universe and specific technical expertise.

### Available Agents

#### 1. Avalon Lore Steward (`my-agent`)
**Location:** `.github/agents/my-agent.agent.md`

**Purpose:** Organizes files, maintains lore categorization, assists with coding

**Use when:**
- Organizing repository structure
- Managing file locations
- General coding assistance
- File management tasks

**Invoke with:** `@copilot /agent my-agent [your request]`

#### 2. Scene Conversion Engineer
**Location:** `.github/agents/scene-converter.agent.md`

**Purpose:** Expert in converting HTML game scenes to ChoiceScript format

**Specializations:**
- HTML to ChoiceScript translation
- Stat system implementation
- ChoiceScript syntax
- Narrative expansion
- Quality assurance

**Use when:**
- Converting scenes from `game/game.js` to `choicescript_game/scenes/`
- Implementing stat tracking
- Ensuring proper ChoiceScript syntax
- Expanding game content

**Best for:** Game development, scene conversion, ChoiceScript work

#### 3. Lore Guardian
**Location:** `.github/agents/lore-guardian.agent.md`

**Purpose:** Validates narrative consistency across the 150-year epic

**Specializations:**
- Character consistency checking
- Magic system integrity
- Timeline validation
- Geographic consistency
- Multi-generational tracking

**Use when:**
- Validating lore consistency
- Checking character details
- Verifying timeline accuracy
- Ensuring magic system compliance
- Cross-referencing narrative elements

**Best for:** Lore validation, consistency checks, narrative quality

---

## GitHub Actions Workflows

Automated workflows run on various triggers to validate content, assist with tasks, and maintain quality.

### 1. AI Content Validation
**File:** `.github/workflows/ai-content-validation.yml`

**Triggers:**
- Pull requests affecting `choicescript_game/scenes/`, `lore/`, or `writing_drafts/`
- Manual trigger via workflow_dispatch

**What it does:**
- ✅ Validates ChoiceScript syntax
- ✅ Checks for broken `*goto` statements
- ✅ Verifies stat modification syntax
- ✅ Ensures Polly commentary is present
- ✅ Validates character name consistency
- ✅ Checks magic system terminology
- ✅ Compares HTML vs ChoiceScript parity
- ✅ Identifies placeholder scenes

**How to use:**
- Automatically runs on relevant PRs
- Manually trigger from Actions tab
- Review job outputs for warnings

**Example output:**
```
✓ singing_dunes.txt exists (534 lines)
✗ verdant_tithe.txt missing
⚠ rune_glacier.txt may be placeholder (< 100 lines)
```

### 2. AI Task Automation
**File:** `.github/workflows/ai-task-automation.yml`

**Triggers:**
- New issues opened
- Issues labeled
- Issue comments created
- Manual trigger

**What it does:**
- 🏷️ Auto-labels issues based on content
- 💬 Provides AI assistance suggestions based on labels
- ✅ Generates task checklists on command

**Auto-labeling logic:**
- `bug` - Issues mentioning "bug", "error", or "broken"
- `lore` - Issues about characters, worldbuilding
- `game-development` - ChoiceScript, scenes, expeditions
- `documentation` - README, guides
- `ai-automation` - AI, automation, copilot
- `high-priority` - Urgent or critical issues

**AI assistance by label:**
- `game-development` → Suggests Scene Converter, provides references
- `lore` → Suggests Lore Guardian, lists key files
- `documentation` → Suggests documentation automation

**Commands:**
- `/create-checklist` - Generates detailed task checklist in issue comment

**Example:**
```
Comment: /create-checklist
Result: AI generates planning, implementation, validation, and finalization checklist
```

### 3. ChoiceScript Tests
**File:** `.github/workflows/choicescript-tests.yml`

**Triggers:**
- Pushes affecting `choicescript_game/scenes/`
- Manual trigger

**What it does:**
- Placeholder for ChoiceScript quicktest and randomtest
- Ready to be enhanced with actual test commands

**Future enhancements:**
- Run ChoiceScript's built-in test suite
- Validate all paths are playable
- Check for game-breaking errors

### 4. Jekyll Site CI
**File:** `.github/workflows/jekyll-docker.yml`

**Triggers:**
- Pushes to main branch
- Pull requests to main

**What it does:**
- Builds Jekyll site in Docker container
- Validates site builds successfully

---

## Issue Templates for AI Tasks

Specialized issue templates help structure AI-assisted work and ensure consistency.

### 1. Scene Conversion Template
**File:** `.github/ISSUE_TEMPLATE/scene-conversion.md`

**Use for:** Converting HTML scenes to ChoiceScript

**Includes:**
- Scene identification fields
- Conversion requirements checklist
- AI assistance planning
- Quality validation criteria
- Expected outcomes

**Labels:** `game-development`, `ai-task`, `conversion`

**When to use:**
- Converting Singing Dunes scenes
- Converting Verdant Tithe scenes
- Converting Rune Glacier scenes
- Converting any expedition content

### 2. Lore Consistency Check Template
**File:** `.github/ISSUE_TEMPLATE/lore-consistency.md`

**Use for:** Validating narrative consistency

**Includes:**
- Element type and name
- Consistency check requirements
- Character/magic/timeline/location validation
- AI assistance planning
- Findings documentation

**Labels:** `lore`, `ai-task`, `documentation`

**When to use:**
- Checking character consistency
- Validating timeline accuracy
- Ensuring magic system compliance
- Cross-referencing locations

### 3. AI Automation Task Template
**File:** `.github/ISSUE_TEMPLATE/ai-automation-task.md`

**Use for:** General AI automation tasks

**Includes:**
- Task description and category
- Current manual process
- Proposed automation solution
- Implementation plan (workflow/agent/script)
- Integration points
- Success criteria
- Testing plan

**Labels:** `ai-automation`, `enhancement`

**When to use:**
- Proposing new automations
- Enhancing existing workflows
- Creating new custom agents
- Adding new AI capabilities

### 4. Task Template (Original)
**File:** `.github/ISSUE_TEMPLATE/task.md`

**Use for:** General tasks

**Includes:**
- Goal description
- Acceptance criteria
- AI loop plan

**When to use:**
- Standard development tasks
- Non-AI-specific work

---

## AI Commands

Special commands you can use in issue comments to trigger AI assistance.

### `/create-checklist`
**Where:** Issue comments
**What it does:** Generates detailed task checklist
**Example:**
```
User comment: /create-checklist
Bot generates:
## AI-Generated Task Checklist
### Planning
- [ ] Review relevant documentation
- [ ] Identify affected files
...
```

### Future Commands (Planned)
- `/validate-lore [element]` - Run lore consistency check
- `/convert-scene [scene-name]` - Assist with scene conversion
- `/balance-stats` - Check stat threshold balance
- `/check-parity` - Verify HTML vs ChoiceScript parity

---

## Multi-AI Coordination

The repository supports coordinated work across multiple AI assistants with defined roles.

### AI Roles

#### Lore Curator (Creative AI)
**Examples:** Claude, GPT-4 creative variant
**Responsibilities:**
- Validates narrative against lore
- Flags timeline/magic conflicts
- Ensures character consistency
**Use for:** Lore validation, creative writing, consistency checks

#### Conversion Engineer (Code-focused AI)
**Examples:** GitHub Copilot, Continue
**Responsibilities:**
- Translates HTML to ChoiceScript
- Preserves choice logic and stats
- Maintains technical accuracy
**Use for:** Scene conversion, code translation, syntax

#### Structural Reviewer (Analysis AI)
**Examples:** Cody, Codeium
**Responsibilities:**
- Ensures scene parity
- Checks stat progression
- Validates branching structure
**Use for:** Cross-file analysis, consistency verification

#### Quality Balancer
**Responsibilities:**
- Equalizes difficulty
- Compares stat thresholds
- Ensures balanced gameplay
**Use for:** Game balance, stat tuning

### Shared Context Files

To coordinate multiple AIs, maintain these files:

#### STATUS_CONTEXT.md (Create if needed)
```markdown
# Current Status
**Week of:** [Date]
**Current Scene:** singing_dunes
**Pending Updates:** 
- Lore validation for Kael character
- Stat balancing for truth tests
```

#### SCENE_PARITY_CHECKLIST.md (Create if needed)
```markdown
# Scene Parity Status
| HTML Scene | ChoiceScript | Status |
|------------|--------------|--------|
| singing_dunes_arrival | singing_dunes.txt | Draft |
| verdant_tithe_entry | verdant_tithe.txt | Missing |
```

#### STATS_MATRIX.md (Create if needed)
```markdown
# Stat Changes by Choice
| File | Choice | Stat | Delta |
|------|--------|------|-------|
| first_lesson.txt | Ask Izack for help | collaboration | +10 |
| singing_dunes.txt | Tell truth | collaboration | +5 |
```

### Hand-off Conventions

**Inline TODOs:**
```choicescript
// TODO:[LORE]: Verify Kael's age aligns with timeline
// TODO:[BALANCE]: Adjust collaboration threshold for this path
```

**Commit Message Prefixes:**
- `Lore:` - Lore validation or updates
- `Convert:` - Scene conversion work
- `Struct:` - Structural review changes
- `Balance:` - Stat balancing adjustments
- `Auto:` - Automation updates

---

## Best Practices

### For Scene Conversion

1. **Always use Scene Conversion Engineer agent** for ChoiceScript work
2. **Reference `first_lesson.txt`** for formatting examples
3. **Validate with workflow** after conversion
4. **Check lore consistency** with Lore Guardian
5. **Test all paths** manually or with quicktest

### For Lore Validation

1. **Use Lore Guardian agent** for consistency checks
2. **Cross-reference master chronicle** (`IZACK_MASTER_CHRONICLE_UPDATED.txt`)
3. **Document findings** in issue template
4. **Update shared context** files
5. **Verify across all formats** (HTML, ChoiceScript, lore files)

### For Automation Tasks

1. **Create issue using AI Automation template**
2. **Specify clear success criteria**
3. **Test thoroughly** before deployment
4. **Document** in this guide
5. **Update AUTOMATION_GUIDE.md** for user-facing features

### For Multi-AI Coordination

1. **Define roles clearly** before starting
2. **Maintain shared context files**
3. **Use standard prefixes** in commits
4. **Hand off explicitly** with TODOs
5. **Document handoffs** in issues/PRs

### For Quality Assurance

1. **Run validation workflows** on all PRs
2. **Review automated feedback** carefully
3. **Address warnings** before merging
4. **Update tests** as features evolve
5. **Maintain documentation** current

---

## Getting Started

### For New Contributors

1. **Read this guide** to understand AI capabilities
2. **Review `.github/COPILOT_INSTRUCTIONS.md`** for project context
3. **Check `docs/PROJECT_ROADMAP.md`** for current phase
4. **Use issue templates** for structured work
5. **Leverage AI agents** for specialized tasks

### For AI Assistants

1. **Identify your role** (Lore, Conversion, Review, Balance)
2. **Read relevant agent documentation**
3. **Check shared context files**
4. **Follow hand-off conventions**
5. **Update documentation** as you work

### Quick Start Checklist

- [ ] Read START_HERE.md
- [ ] Review AI Automation Features (this file)
- [ ] Read COPILOT_INSTRUCTIONS.md
- [ ] Check PROJECT_ROADMAP.md for current phase
- [ ] Explore available custom agents
- [ ] Try creating an issue with templates
- [ ] Test `/create-checklist` command
- [ ] Review workflow outputs

---

## Troubleshooting

### Workflow Not Running
- Check trigger conditions in workflow file
- Verify paths match your changes
- Check GitHub Actions permissions
- Look at workflow run logs

### Agent Not Responding as Expected
- Ensure using correct agent name
- Check agent configuration file
- Provide sufficient context
- Try rephrasing request

### Labels Not Auto-Applied
- Check issue content includes keywords
- Verify workflow has issues:write permission
- Review workflow logs for errors

### Validation Failing
- Review specific failure in job output
- Check file syntax
- Verify paths and labels exist
- Test locally if possible

---

## Future Enhancements

Planned AI automation features:

- [ ] Automated stat balancing analysis
- [ ] Content quality scoring
- [ ] Automatic scene parity reporting
- [ ] Integration with ChoiceScript IDE
- [ ] Automated playtesting reports
- [ ] Lore contradiction detection with AI analysis
- [ ] Automatic generation of scene summaries
- [ ] AI-powered beta testing coordination
- [ ] Automated release notes generation

---

## Resources

**Documentation:**
- `.github/COPILOT_INSTRUCTIONS.md` - Detailed project guide
- `docs/AUTOMATION_GUIDE.md` - User automation (Zapier, etc.)
- `docs/PROJECT_ROADMAP.md` - Development roadmap
- `docs/NEXT_TASKS.md` - Task queue

**Agent Configurations:**
- `.github/agents/my-agent.agent.md` - Lore Steward
- `.github/agents/scene-converter.agent.md` - Scene Converter
- `.github/agents/lore-guardian.agent.md` - Lore Guardian

**Workflows:**
- `.github/workflows/ai-content-validation.yml`
- `.github/workflows/ai-task-automation.yml`
- `.github/workflows/choicescript-tests.yml`

**Issue Templates:**
- `.github/ISSUE_TEMPLATE/scene-conversion.md`
- `.github/ISSUE_TEMPLATE/lore-consistency.md`
- `.github/ISSUE_TEMPLATE/ai-automation-task.md`

---

## Support

For questions or issues with AI automation:
1. Check this guide first
2. Review relevant workflow logs
3. Consult agent documentation
4. Create issue using AI Automation Task template
5. Tag with `ai-automation` label

---

**Last Updated:** November 25, 2025
**Maintained By:** AI Automation System
**Version:** 1.0

*"The spiral continues. Every automation writes efficiency into our process."*
