# 🤖 AI Automation Quick Reference

**Fast reference for AI features in the Avalon repository**

---

## Custom Agents

| Agent | Purpose | Use When |
|-------|---------|----------|
| **Lore Steward** | File organization, general coding | Organizing files, general help |
| **Scene Converter** | HTML → ChoiceScript conversion | Converting game scenes |
| **Lore Guardian** | Narrative consistency validation | Checking lore, characters, timeline |

**Invoke:** `@copilot /agent [agent-name] [request]`

---

## Issue Templates

| Template | Label | Use For |
|----------|-------|---------|
| **Scene Conversion** | `game-development` | Converting HTML scenes to ChoiceScript |
| **Lore Consistency** | `lore` | Validating narrative consistency |
| **AI Automation** | `ai-automation` | Proposing new AI features |
| **Task** | - | General development tasks |

**Create:** Issues → New Issue → Choose Template

---

## Workflows (Automated)

| Workflow | Trigger | What It Does |
|----------|---------|--------------|
| **Content Validation** | PR to scenes/lore | Validates syntax, consistency, parity |
| **Task Automation** | New issues | Auto-labels, suggests AI help |
| **ChoiceScript Tests** | Push to scenes | Runs game tests (placeholder) |

**Manual Run:** Actions tab → Select workflow → Run workflow

---

## Commands (Issue Comments)

| Command | What It Does |
|---------|--------------|
| `/create-checklist` | Generates detailed task checklist |

**More commands coming soon!**

---

## Auto-Labels

Issues are automatically labeled based on content:

- `bug` - "bug", "error", "broken"
- `lore` - "lore", "character", "worldbuilding"  
- `game-development` - "choicescript", "scene", "expedition"
- `documentation` - "documentation", "readme", "guide"
- `ai-automation` - "ai", "automation", "copilot"
- `high-priority` - "urgent", "critical", "high priority"

---

## Multi-AI Roles

| Role | AI Type | Responsible For |
|------|---------|-----------------|
| **Lore Curator** | Creative | Narrative validation, consistency |
| **Conversion Engineer** | Code-focused | HTML→ChoiceScript translation |
| **Structural Reviewer** | Analysis | Scene parity, stat checking |
| **Quality Balancer** | - | Stat balancing, difficulty |

**Commit Prefixes:** `Lore:`, `Convert:`, `Struct:`, `Balance:`, `Auto:`

---

## Shared Context Files

Maintain for multi-AI coordination:

- `STATUS_CONTEXT.md` - Current work snapshot
- `SCENE_PARITY_CHECKLIST.md` - Scene status tracking
- `STATS_MATRIX.md` - Stat changes by choice

---

## Quick Validation Checks

**ChoiceScript Syntax:**
```bash
cd choicescript_game/scenes
grep "^\*goto " *.txt  # Check goto statements
grep "^\*label " *.txt  # Check label definitions
grep "\*set " *.txt     # Check stat modifications
```

**Character Consistency:**
```bash
grep -r "Izack" lore/ game/ choicescript_game/
grep -r "Aria" lore/ game/ choicescript_game/
```

---

## File Locations

| What | Where |
|------|-------|
| Agent configs | `.github/agents/` |
| Workflows | `.github/workflows/` |
| Issue templates | `.github/ISSUE_TEMPLATE/` |
| Full AI guide | `docs/AI_AUTOMATION_FEATURES.md` |
| Copilot instructions | `.github/COPILOT_INSTRUCTIONS.md` |

---

## Quick Start

1. Create issue using template
2. Auto-labels apply
3. AI suggests assistance
4. Use `/create-checklist` for task breakdown
5. Work with appropriate AI agent
6. PR triggers validation
7. Review automated feedback

---

## Common Tasks

**Convert a scene:**
1. Create "Scene Conversion" issue
2. Use Scene Converter agent
3. Reference `first_lesson.txt` for format
4. Create PR
5. Validation runs automatically

**Check lore:**
1. Create "Lore Consistency" issue
2. Use Lore Guardian agent
3. Cross-reference master chronicle
4. Document findings
5. Update files as needed

**Add automation:**
1. Create "AI Automation Task" issue
2. Specify what to automate
3. Choose: workflow, agent, or script
4. Implement and test
5. Document in AI_AUTOMATION_FEATURES.md

---

## Help & Documentation

- **Full Guide:** `docs/AI_AUTOMATION_FEATURES.md`
- **Project Context:** `.github/COPILOT_INSTRUCTIONS.md`
- **Roadmap:** `docs/PROJECT_ROADMAP.md`
- **Tasks:** `docs/NEXT_TASKS.md`

---

**Version:** 1.0 | **Updated:** Nov 25, 2025
