# GitHub Labels Guide
## Avalon Repository Label System

This document describes the comprehensive label system used in the Avalon repository to organize issues, pull requests, and facilitate automated workflows.

---

## 🚀 Quick Setup

Run this script to create all labels automatically:
```bash
.github/scripts/create-labels.sh
```

Or manually create labels using GitHub UI or CLI.

---

## 📊 Label Categories

### Priority Labels
Used to indicate urgency and importance of issues.

| Label | Color | Description | When to Use |
|-------|-------|-------------|-------------|
| `priority: critical` | 🔴 Red | Critical issue requiring immediate attention | Security issues, broken main functionality, blocking bugs |
| `priority: high` | 🟠 Orange | High priority issue | Important features, significant bugs, approaching deadlines |
| `priority: medium` | 🟡 Yellow | Medium priority issue | Standard features, moderate bugs, normal workflow |
| `priority: low` | 🟢 Green | Low priority issue | Nice-to-haves, minor improvements, future enhancements |

### Type Labels
Categorize the nature of the issue or PR.

| Label | Color | Description | Auto-Applied By |
|-------|-------|-------------|-----------------|
| `bug` | 🔴 Red | Something isn't working | Issue auto-assignment workflow |
| `enhancement` | 🔵 Blue | New feature or request | Issue auto-assignment workflow |
| `documentation` | 📘 Blue | Improvements or additions to documentation | Issue auto-assignment, PR management |
| `question` | 🟣 Purple | Further information is requested | Issue auto-assignment workflow |
| `duplicate` | ⚪ Gray | This issue or pull request already exists | Manual |
| `invalid` | 🟡 Yellow | This doesn't seem right | Manual |
| `wontfix` | ⚪ White | This will not be worked on | Manual |

### Content Labels
Specific to the Avalon project content.

| Label | Color | Description | Auto-Applied By |
|-------|-------|-------------|-----------------|
| `game-content` | 🟣 Purple | Related to game scenes and gameplay | PR management workflow |
| `lore` | 🔵 Light Blue | Related to worldbuilding and lore | Issue auto-assignment, PR management |
| `writing` | 📝 Blue | Related to narrative and writing | PR management workflow |
| `choicescript` | 🟠 Orange | Related to ChoiceScript implementation | PR management workflow |

### Technical Labels
For technical aspects of the project.

| Label | Color | Description | Auto-Applied By |
|-------|-------|-------------|-----------------|
| `github-actions` | ⚫ Black | Related to GitHub Actions workflows | PR management workflow |
| `security` | 🔴 Red | Security-related issue or improvement | Security scanning workflow |
| `dependencies` | 🔵 Blue | Pull requests that update a dependency file | Dependabot |
| `tests` | 🟢 Green | Related to testing | Manual, PR management |
| `automation` | 🟡 Yellow | Related to automation and CI/CD | PR management workflow |

### Size Labels (Pull Requests)
Automatically applied based on lines changed.

| Label | Color | Lines Changed | Description |
|-------|-------|---------------|-------------|
| `size: XS` | 🟢 Light Green | < 10 | Extra small PR |
| `size: S` | 🟢 Green | < 50 | Small PR |
| `size: M` | 🟠 Orange | < 200 | Medium PR |
| `size: L` | 🔴 Red-Orange | < 500 | Large PR |
| `size: XL` | 🔴 Dark Red | 500+ | Extra large PR |

### Status Labels
Track progress and blockers.

| Label | Color | Description | When to Apply |
|-------|-------|-------------|---------------|
| `status: in progress` | 🔵 Blue | Work is currently in progress | When actively working on issue/PR |
| `status: blocked` | 🔴 Red | Blocked by dependencies or issues | When can't proceed due to external factors |
| `status: needs review` | 🟡 Yellow | Needs review from maintainers | When PR is ready for review |
| `status: ready to merge` | 🟢 Green | Approved and ready to merge | After review approval |

### AI & Collaboration Labels
For AI-assisted development.

| Label | Color | Description | When to Use |
|-------|-------|-------------|-------------|
| `ai-generated` | 🟣 Pink | Content or code generated with AI assistance | For AI-created content |
| `ai-review` | 🟠 Light Orange | Needs AI review or validation | When requiring AI assistance |
| `good first issue` | 🟣 Purple | Good for newcomers | Simple, well-defined tasks |
| `help wanted` | 🟢 Green | Extra attention is needed | Community contributions welcome |

### Project-Specific Labels
For Avalon development phases.

| Label | Color | Description | Phase Focus |
|-------|-------|-------------|-------------|
| `phase-1` | 🔵 Blue | Phase 1 development tasks | Initial game scenes |
| `phase-2` | 🟣 Purple | Phase 2 development tasks | Expanded content |
| `phase-3` | 🔴 Red | Phase 3 development tasks | Polish & publication |
| `polish` | 🟡 Light Yellow | Polish and refinement work | Final improvements |
| `beta-testing` | 🟠 Orange | Related to beta testing | Testing phase |

---

## 🤖 Automated Label Application

### When Issues Are Created:
**Workflow:** `.github/workflows/auto-assign-issues.yml`

Automatically adds labels based on keywords:
- `bug` → Keywords: "bug", "error", "broken"
- `enhancement` → Keywords: "feature", "enhancement", "feature request"
- `documentation` → Keywords: "doc", "documentation"
- `question` → Keywords: "question", "help", "how to"
- `game-content` → Keywords: "game", "choicescript", "scene"
- `lore` → Keywords: "lore", "worldbuilding", "character"
- `priority: high` → Keywords: "urgent", "critical", "security"

### When Pull Requests Are Opened:
**Workflow:** `.github/workflows/pr-management.yml`

Automatically adds labels based on:

**By Size:**
- Lines changed < 10 → `size: XS`
- Lines changed < 50 → `size: S`
- Lines changed < 200 → `size: M`
- Lines changed < 500 → `size: L`
- Lines changed 500+ → `size: XL`

**By Files Changed:**
- Files in `choicescript_game/` or `game/` → `game-content`
- Files in `lore/` → `lore`
- Files in `docs/` or `.md` files → `documentation`
- Files in `writing_drafts/` → `writing`
- Files in `.github/workflows/` → `github-actions`
- Files containing "test" → `tests`

---

## 📋 Label Usage Best Practices

### For Issues:
1. **Always apply at least one type label** (bug, enhancement, documentation, question)
2. **Add a priority label** if it's time-sensitive or critical
3. **Add content labels** to help categorize (game-content, lore, writing)
4. **Update status labels** as work progresses
5. **Use AI labels** when requesting or providing AI assistance

### For Pull Requests:
1. **Size labels are automatic** - don't add manually
2. **Content labels are automatic** - verify they're correct
3. **Add status labels** as PR progresses through review
4. **Link to issues** for automatic label inheritance
5. **Use `ready to merge`** when approved and ready

### For Automation:
1. **Don't remove auto-applied labels** unless incorrect
2. **Report issues** if auto-labeling isn't working correctly
3. **Update workflows** if new label patterns are needed
4. **Review labels regularly** to ensure they're still relevant

---

## 🔧 Managing Labels

### Creating New Labels:
```bash
# Using GitHub CLI
gh label create "label-name" --color "color-hex" --description "Description"

# Example
gh label create "urgent-fix" --color "d73a4a" --description "Requires urgent attention"
```

### Editing Existing Labels:
```bash
gh label edit "label-name" --color "new-color" --description "New description"
```

### Deleting Labels:
```bash
gh label delete "label-name"
```

### Listing All Labels:
```bash
gh label list
```

---

## 🎯 Label Strategies for Different Scenarios

### Bug Reports:
```
Required: bug
Recommended: priority: [level], game-content/lore/etc
Optional: good first issue (if suitable for new contributors)
```

### Feature Requests:
```
Required: enhancement
Recommended: phase-1/2/3, game-content/lore/etc
Optional: help wanted (if community input desired)
```

### Documentation Updates:
```
Required: documentation
Recommended: size: [auto-applied]
Optional: good first issue
```

### Security Issues:
```
Required: security, priority: critical
Recommended: status: in progress (when being addressed)
Action: Review immediately
```

### AI-Assisted Work:
```
Required: ai-generated (for AI-created content)
Recommended: ai-review (if needs validation)
Optional: Content-specific labels
```

---

## 📈 Label Analytics

Use labels to track:
- **Development velocity**: Count of `status: completed` per week
- **Bug rate**: Ratio of `bug` to `enhancement`
- **AI contribution**: Percentage of `ai-generated` work
- **Phase progress**: Distribution across `phase-1/2/3` labels
- **Community engagement**: Count of `good first issue` + `help wanted`

---

## 🔄 Label Lifecycle

### Issue Lifecycle:
```
Created → [type label] → [priority label] → status: in progress → 
status: needs review → status: completed → Closed
```

### PR Lifecycle:
```
Opened → [size label] → [content labels] → status: needs review → 
status: ready to merge → Merged
```

---

## 🆘 Troubleshooting

**Labels not auto-applying?**
- Check workflow runs in Actions tab
- Verify workflow files are correct
- Check keyword matching in issue/PR content

**Wrong labels applied?**
- Manually edit labels
- Update workflow patterns if systematic issue
- Report bug if workflow malfunction

**Missing needed labels?**
- Run `.github/scripts/create-labels.sh`
- Or create manually via GitHub UI
- Update this guide with new labels

---

## 📚 Related Documentation

- **Automation Guide**: `docs/AUTOMATION_GUIDE.md`
- **GitHub Organization Setup**: `docs/GITHUB_ORGANIZATION_SETUP.md`
- **Contributing Guide**: `CONTRIBUTING.md`
- **Project Roadmap**: `docs/PROJECT_ROADMAP.md`

---

**All labels work together to create an organized, efficient workflow for the Avalon project.**

*Last updated: November 2025*