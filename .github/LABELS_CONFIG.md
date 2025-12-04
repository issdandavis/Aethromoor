# Repository Labels Configuration

This file documents the labels used in the Avalon repository, including those used by AI automation.

## AI Automation Labels

### ai-automation
- **Color:** `#0052CC` (Blue)
- **Description:** Issues related to AI automation features and enhancements
- **Auto-applied when:** Issue mentions "ai", "automation", or "copilot"

### ai-task
- **Color:** `#1D76DB` (Light Blue)
- **Description:** Tasks that can be automated or AI-assisted
- **Auto-applied when:** Using AI-specific issue templates

## Content Type Labels

### game-development
- **Color:** `#5319E7` (Purple)
- **Description:** ChoiceScript game development and scene conversion
- **Auto-applied when:** Issue mentions "choicescript", "scene", or "expedition"

### lore
- **Color:** `#D93F0B` (Red)
- **Description:** Worldbuilding, character consistency, and narrative validation
- **Auto-applied when:** Issue mentions "lore", "character", or "worldbuilding"

### documentation
- **Color:** `#0E8A16` (Green)
- **Description:** Documentation updates, guides, and README changes
- **Auto-applied when:** Issue mentions "documentation", "readme", or "guide"

### bug
- **Color:** `#D73A4A` (Red)
- **Description:** Something isn't working correctly
- **Auto-applied when:** Issue mentions "bug", "error", or "broken"

## Priority Labels

### high-priority
- **Color:** `#B60205` (Dark Red)
- **Description:** Critical issues that need immediate attention
- **Auto-applied when:** Issue mentions "urgent", "critical", or "high priority"

### medium-priority
- **Color:** `#FBCA04` (Yellow)
- **Description:** Important but not critical tasks
- **Auto-applied when:** Manually applied

### low-priority
- **Color:** `#E4E669` (Light Yellow)
- **Description:** Tasks that can be addressed later
- **Auto-applied when:** Manually applied

## Task Type Labels

### conversion
- **Color:** `#C2E0C6` (Light Green)
- **Description:** HTML to ChoiceScript conversion tasks
- **Auto-applied when:** Using Scene Conversion template

### enhancement
- **Color:** `#A2EEEF` (Cyan)
- **Description:** New features or improvements
- **Auto-applied when:** Using AI Automation Task template

### question
- **Color:** `#D876E3` (Pink)
- **Description:** Questions or clarifications needed
- **Auto-applied when:** Manually applied

## Workflow Status Labels

### in-progress
- **Color:** `#0366D6` (Blue)
- **Description:** Work is currently being done
- **Auto-applied when:** Manually applied

### blocked
- **Color:** `#6A737D` (Gray)
- **Description:** Cannot proceed due to dependencies
- **Auto-applied when:** Manually applied

### needs-review
- **Color:** `#FBCA04` (Yellow)
- **Description:** Ready for review
- **Auto-applied when:** Manually applied

## Quality Labels

### validated
- **Color:** `#0E8A16` (Green)
- **Description:** Passed AI validation checks
- **Auto-applied when:** Content validation workflow succeeds

### needs-validation
- **Color:** `#F9D0C4` (Light Red)
- **Description:** Requires validation or verification
- **Auto-applied when:** Content validation workflow fails

## How to Create These Labels

### Via GitHub UI
1. Go to repository **Issues** tab
2. Click **Labels**
3. Click **New label**
4. Enter name, description, and color
5. Click **Create label**

### Via GitHub CLI
```bash
# Install GitHub CLI if needed: https://cli.github.com/

# Create labels
gh label create "ai-automation" --color "0052CC" --description "Issues related to AI automation features and enhancements"
gh label create "ai-task" --color "1D76DB" --description "Tasks that can be automated or AI-assisted"
gh label create "game-development" --color "5319E7" --description "ChoiceScript game development and scene conversion"
gh label create "lore" --color "D93F0B" --description "Worldbuilding, character consistency, and narrative validation"
gh label create "documentation" --color "0E8A16" --description "Documentation updates, guides, and README changes"
gh label create "high-priority" --color "B60205" --description "Critical issues that need immediate attention"
gh label create "medium-priority" --color "FBCA04" --description "Important but not critical tasks"
gh label create "low-priority" --color "E4E669" --description "Tasks that can be addressed later"
gh label create "conversion" --color "C2E0C6" --description "HTML to ChoiceScript conversion tasks"
gh label create "enhancement" --color "A2EEEF" --description "New features or improvements"
gh label create "validated" --color "0E8A16" --description "Passed AI validation checks"
gh label create "needs-validation" --color "F9D0C4" --description "Requires validation or verification"
```

### Via Labels Sync GitHub Action (Recommended)
Create `.github/labels.yml`:
```yaml
- name: ai-automation
  color: "0052CC"
  description: "Issues related to AI automation features and enhancements"
- name: ai-task
  color: "1D76DB"
  description: "Tasks that can be automated or AI-assisted"
- name: game-development
  color: "5319E7"
  description: "ChoiceScript game development and scene conversion"
- name: lore
  color: "D93F0B"
  description: "Worldbuilding, character consistency, and narrative validation"
- name: documentation
  color: "0E8A16"
  description: "Documentation updates, guides, and README changes"
- name: high-priority
  color: "B60205"
  description: "Critical issues that need immediate attention"
- name: conversion
  color: "C2E0C6"
  description: "HTML to ChoiceScript conversion tasks"
- name: enhancement
  color: "A2EEEF"
  description: "New features or improvements"
- name: validated
  color: "0E8A16"
  description: "Passed AI validation checks"
```

Then use [EndBug/label-sync](https://github.com/EndBug/label-sync) action to sync.

## Label Usage Guidelines

### For Contributors
- **Don't remove auto-applied labels** unless they're incorrect
- **Add additional labels** as needed (priority, status)
- **Use consistent labels** across similar issues

### For Maintainers
- **Review auto-labels** to ensure accuracy
- **Adjust automation rules** if labels are frequently wrong
- **Create new labels** when patterns emerge

### For AI Systems
- **Check labels** to determine appropriate assistance
- **Suggest agents** based on label combinations
- **Apply validation labels** after automated checks

## Auto-Labeling Logic

Current automation in `.github/workflows/ai-task-automation.yml`:

```javascript
// Content detection
if (title.includes('bug') || body.includes('error') || body.includes('broken')) {
  labels.push('bug');
}
if (title.includes('lore') || body.includes('character') || body.includes('worldbuilding')) {
  labels.push('lore');
}
if (title.includes('choicescript') || title.includes('scene') || body.includes('expedition')) {
  labels.push('game-development');
}
if (title.includes('documentation') || title.includes('readme') || title.includes('guide')) {
  labels.push('documentation');
}
if (title.includes('ai') || title.includes('automation') || body.includes('copilot')) {
  labels.push('ai-automation');
}

// Priority detection  
if (title.includes('urgent') || title.includes('critical') || body.includes('high priority')) {
  labels.push('high-priority');
}
```

## Future Label Ideas

Potential labels for future automation:
- `stat-balancing` - Issues related to game stat balance
- `scene-parity` - HTML vs ChoiceScript consistency
- `timeline-check` - Multi-generational timeline validation
- `agent-suggestion` - AI agent recommendation needed
- `workflow-enhancement` - Improvements to GitHub Actions
- `integration` - External tool integration (Zapier, etc.)

---

**Maintained by:** Repository maintainers and AI automation system
**Last Updated:** November 25, 2025
