# Automation Scripts

This directory contains automation scripts for managing Avalon content.

## Available Scripts

### Content Health Check
**File:** `content-health.sh`

Generates a comprehensive health report of all game content:
- Total word counts and scene metrics
- Scene breakdown with quality indicators
- Character mention balance
- Recent activity tracking
- Recommendations for next steps

**Usage:**
```bash
./scripts/content-health.sh
# or
bash scripts/content-health.sh
```

**When to run:** Daily or before major work sessions

---

### Weekly Growth Report
**File:** `weekly-growth.sh`

Tracks content growth and suggests expansion priorities:
- Progress toward publication goals
- Identifies shortest scenes
- Finds scenes needing more choices
- Suggests weekly word count targets

**Usage:**
```bash
./scripts/weekly-growth.sh
```

**When to run:** Weekly on Monday mornings

---

### Content Organizer
**File:** `organize-content.sh`

Analyzes and organizes lore files:
- Finds uncategorized files
- Suggests proper directory placement
- Reports current organization status

**Usage:**
```bash
./scripts/organize-content.sh
```

**When to run:** After adding new lore files

---

## Automation Strategy

These scripts work together with the AI tools documented in:
- `docs/AI_CONTENT_AUTOMATION.md` - Full AI automation strategy
- `docs/GITHUB_COPILOT_CLI_GUIDE.md` - Command-line AI assistance
- `docs/AUTOMATION_GUIDE.md` - External tool integration

## Setting Up Automation

### Daily Workflow
```bash
# Morning: Check content health
./scripts/content-health.sh

# Use GitHub Copilot CLI for tasks
gh copilot suggest "find scenes needing expansion"

# End of day: Review progress
git status
```

### Weekly Workflow
```bash
# Monday: Growth review
./scripts/weekly-growth.sh > reports/week-$(date +%Y%m%d).txt

# Plan week's content
gh copilot suggest "suggest priority scenes for this week"
```

## Tips

- **Save Reports:** Redirect output to save reports
  ```bash
  ./scripts/content-health.sh > reports/daily-$(date +%Y%m%d).txt
  ```

- **Compare Over Time:** Save weekly reports to track progress
  ```bash
  mkdir -p reports
  ./scripts/weekly-growth.sh > reports/weekly-$(date +%Y%m%d).txt
  ```

- **Combine with AI:** Use script output with Copilot CLI
  ```bash
  ./scripts/content-health.sh | grep "🔴" | gh copilot explain
  ```

## Future Enhancements

Potential additions:
- [ ] Automated lore consistency checking
- [ ] Character arc tracking
- [ ] Scene dependency mapping
- [ ] Statistical analysis of player choices
- [ ] Integration with GitHub Actions for CI/CD

---

*For more automation ideas, see `docs/AI_CONTENT_AUTOMATION.md`*
