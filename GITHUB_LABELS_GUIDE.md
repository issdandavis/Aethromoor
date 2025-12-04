# 🏷️ GITHUB LABELS & ORGANIZATION GUIDE

**Purpose:** Organize issues, PRs, and tasks for better repository management

---

## 📋 RECOMMENDED LABEL SYSTEM

### 🎯 Priority Labels

| Label | Color | Description | When to Use |
|-------|-------|-------------|-------------|
| `priority: critical` | #d73a4a (red) | Blocking issues, game-breaking bugs | Game won't run, data loss risk |
| `priority: high` | #ff9800 (orange) | Important features, major bugs | Affects core gameplay |
| `priority: medium` | #ffd700 (yellow) | Standard improvements | Nice to have features |
| `priority: low` | #90ee90 (light green) | Minor enhancements | Polish, small tweaks |

### 📦 Type Labels

| Label | Color | Description | When to Use |
|-------|-------|-------------|-------------|
| `type: bug` | #ee0701 (red) | Something isn't working | Errors, crashes, incorrect behavior |
| `type: feature` | #0e8a16 (green) | New feature request | New capabilities, additions |
| `type: enhancement` | #84b6eb (blue) | Improvement to existing feature | Make something better |
| `type: documentation` | #0075ca (dark blue) | Documentation improvements | README updates, guides |
| `type: content` | #c5def5 (light blue) | Game content, lore, writing | Story scenes, worldbuilding |
| `type: automation` | #5319e7 (purple) | AI/automation related | Workflow changes, bot updates |

### 🎮 Component Labels

| Label | Color | Description | When to Use |
|-------|-------|-------------|-------------|
| `component: game-html` | #fbca04 (yellow) | HTML browser game | Issues with `game/` directory |
| `component: game-choicescript` | #d4c5f9 (purple) | ChoiceScript version | Issues with `choicescript_game/` |
| `component: lore` | #c2e0c6 (light green) | Worldbuilding & lore | `lore/` directory content |
| `component: writing` | #fef2c0 (cream) | Manuscripts & drafts | `writing_drafts/` content |
| `component: docs` | #0366d6 (blue) | Documentation | `docs/` directory |
| `component: automation` | #5319e7 (purple) | AI workers & workflows | `.github/` directory |
| `component: config` | #d93f0b (orange) | Configuration | `config/` directory |

### 🔄 Status Labels

| Label | Color | Description | When to Use |
|-------|-------|-------------|-------------|
| `status: blocked` | #b60205 (dark red) | Cannot proceed | Waiting on something |
| `status: in-progress` | #0e8a16 (green) | Actively being worked on | PR open, work started |
| `status: needs-review` | #fbca04 (yellow) | Ready for review | Awaiting feedback |
| `status: on-hold` | #d4c5f9 (purple) | Paused temporarily | Deprioritized |
| `status: wontfix` | #ffffff (white) | Will not be addressed | Not aligned with goals |

### 🎨 Work Category Labels

| Label | Color | Description | When to Use |
|-------|-------|-------------|-------------|
| `work: creative` | #ff69b4 (pink) | Creative writing, storytelling | Story content, dialogue |
| `work: technical` | #1d76db (blue) | Code, scripting, programming | Bug fixes, features |
| `work: design` | #f9d0c4 (peach) | UI/UX, visual design | Styling, layout |
| `work: testing` | #bfd4f2 (light blue) | QA, validation | Testing, verification |
| `work: planning` | #d4c5f9 (purple) | Strategy, roadmap | Planning, organization |

### 🤖 AI Worker Labels

| Label | Color | Description | When to Use |
|-------|-------|-------------|-------------|
| `ai: scene-writer` | #5319e7 (purple) | Scene Writer agent | Auto-generated scenes |
| `ai: content-polisher` | #7057ff (violet) | Content Polisher agent | Polished content |
| `ai: stat-balancer` | #8b7dff (lavender) | Stat Balancer agent | Game balance changes |
| `ai: game-tester` | #a699ff (light purple) | Game Tester agent | Automated test results |
| `ai: inbox-manager` | #c2b5ff (pale purple) | Inbox Manager agent | Auto-replies |
| `ai: generated` | #d1c4e9 (very light purple) | AI-generated content | Any AI-created content |

### 👥 Collaboration Labels

| Label | Color | Description | When to Use |
|-------|-------|-------------|-------------|
| `help-wanted` | #008672 (teal) | Community help needed | Open for contributions |
| `good-first-issue` | #7057ff (violet) | Good for newcomers | Easy starter tasks |
| `question` | #cc317c (pink) | Questions, clarifications | Need information |
| `discussion` | #d4c5f9 (purple) | Open discussion | Ideas, proposals |
| `feedback-needed` | #fbca04 (yellow) | Seeking feedback | Need opinions |

### 🎯 Special Labels

| Label | Color | Description | When to Use |
|-------|-------|-------------|-------------|
| `phase-1` | #c5def5 (light blue) | Phase 1: Foundation | Initial game scenes |
| `phase-2` | #bfd4f2 (sky blue) | Phase 2: Expansion | Additional content |
| `phase-3` | #84b6eb (medium blue) | Phase 3: Polish | Final polish |
| `ready-to-merge` | #0e8a16 (green) | Approved, ready to merge | Final approval |
| `breaking-change` | #d73a4a (red) | Breaking change | Major changes |
| `dependencies` | #0366d6 (blue) | Dependency updates | External libraries |

---

## 📊 LABEL USAGE GUIDE

### For Issues

#### Bug Report Example
```
Labels: type: bug, priority: high, component: game-html, status: needs-review
```

#### Feature Request Example
```
Labels: type: feature, priority: medium, component: game-choicescript, work: technical
```

#### Content Addition Example
```
Labels: type: content, priority: low, component: lore, work: creative
```

### For Pull Requests

#### AI-Generated Content PR
```
Labels: ai: generated, ai: scene-writer, component: game-choicescript, phase-2
```

#### Bug Fix PR
```
Labels: type: bug, priority: high, component: game-html, ready-to-merge
```

#### Documentation Update PR
```
Labels: type: documentation, priority: low, component: docs, ready-to-merge
```

---

## 🎯 LABEL COMBINATIONS

### Common Patterns

#### Critical Bug
- `priority: critical`
- `type: bug`
- `component: [affected component]`
- `status: in-progress`

#### AI-Generated Scene
- `ai: generated`
- `ai: scene-writer`
- `type: content`
- `component: game-choicescript`
- `phase-2`

#### Community Contribution
- `help-wanted`
- `good-first-issue`
- `type: [type]`
- `component: [component]`
- `priority: low`

#### Content Review
- `type: content`
- `status: needs-review`
- `feedback-needed`
- `component: lore` or `component: writing`
- `work: creative`

---

## 🔧 LABEL AUTOMATION

### Auto-Applied Labels

The following labels are automatically applied by GitHub Actions:

1. **`ai: generated`** - All PRs from AI workers
2. **`ai: [worker-name]`** - Specific AI worker that created PR
3. **`status: in-progress`** - When PR is opened
4. **`ready-to-merge`** - When all checks pass

### Label Triggers

Certain labels trigger automated actions:

| Label | Action |
|-------|--------|
| `ready-to-merge` | Auto-approve if all checks pass |
| `ai: generated` | Skip certain validation checks |
| `priority: critical` | Notify repository owner |
| `status: blocked` | Add to blocked issues board |

---

## 📱 LABEL FILTERS

### Quick Filter Commands

Use these in GitHub's issue search:

```
# All bugs
label:"type: bug"

# All AI-generated content
label:"ai: generated"

# All critical priority items
label:"priority: critical"

# All ChoiceScript game issues
label:"component: game-choicescript"

# All items needing review
label:"status: needs-review"

# Good first issues for newcomers
label:"good-first-issue"

# All Phase 2 work
label:"phase-2"

# All creative work
label:"work: creative"
```

### Combined Filters

```
# Critical bugs in HTML game
label:"priority: critical" label:"type: bug" label:"component: game-html"

# Content needing feedback
label:"type: content" label:"feedback-needed"

# AI-generated scenes in Phase 2
label:"ai: scene-writer" label:"phase-2"

# All blocked items
label:"status: blocked"
```

---

## 🎨 COLOR SCHEME RATIONALE

### Red Family (#d73a4a, #b60205)
- Critical issues
- Bugs
- Breaking changes

### Orange Family (#ff9800, #d93f0b)
- High priority
- Configuration
- Important items

### Yellow Family (#fbca04, #ffd700)
- Medium priority
- Needs review
- Feedback needed

### Green Family (#0e8a16, #90ee90)
- Features
- In progress
- Ready to merge

### Blue Family (#0075ca, #0366d6, #84b6eb)
- Documentation
- Components
- Enhancement

### Purple Family (#5319e7, #7057ff, #d4c5f9)
- AI/Automation
- Planning
- Discussions

### Pink Family (#ff69b4, #cc317c)
- Creative work
- Questions
- Community

---

## 📋 LABEL MAINTENANCE

### Monthly Review
- Remove unused labels
- Update label descriptions
- Adjust colors if needed
- Archive completed phase labels

### Label Consistency
- Use lowercase
- Use hyphens for spaces
- Keep names concise
- Be descriptive

### Adding New Labels
1. Check if existing label works
2. Propose in discussion
3. Add with consistent naming
4. Document in this guide

---

## 🎯 CURRENT REPOSITORY LABELS

### Existing Labels (From .github/LABELS.md)
The repository currently has these labels configured:
- Type labels (bug, feature, enhancement, etc.)
- Priority labels (critical, high, medium, low)
- Component labels
- Status labels

**Note:** See `.github/LABELS.md` for the complete technical list.

---

## 💡 BEST PRACTICES

### DO:
✅ Use multiple labels for context
✅ Update labels as work progresses
✅ Be consistent with naming
✅ Use priority labels on all issues
✅ Label PRs immediately

### DON'T:
❌ Over-label (max 5-6 labels per issue)
❌ Create duplicate labels
❌ Use vague labels
❌ Forget to update status labels
❌ Create one-off labels

---

## 🔄 WORKFLOW INTEGRATION

### Issue Lifecycle Labels

```
New Issue → priority: [level] + type: [type] + component: [area]
    ↓
Accepted → + status: in-progress
    ↓
Review → + status: needs-review
    ↓
Done → + ready-to-merge or status: wontfix
```

### PR Lifecycle Labels

```
PR Opened → ai: generated (if applicable) + component: [area]
    ↓
Tests Pass → + status: in-progress
    ↓
Review Complete → + status: needs-review
    ↓
Approved → + ready-to-merge
    ↓
Merged → (labels archived with issue/PR)
```

---

## 📞 QUICK REFERENCE

| Need | Use These Labels |
|------|------------------|
| **Report bug** | `type: bug` + `priority: [level]` + `component: [area]` |
| **Request feature** | `type: feature` + `priority: [level]` + `component: [area]` |
| **Add content** | `type: content` + `work: creative` + `component: lore/writing` |
| **Update docs** | `type: documentation` + `component: docs` |
| **AI task** | `ai: [worker]` + `type: [type]` + `component: [area]` |
| **Help wanted** | `help-wanted` + `good-first-issue` + `priority: low` |

---

**Last Updated:** December 2, 2025  
**Maintained By:** Repository maintainers  
**See Also:** `.github/LABELS.md` for technical label definitions
