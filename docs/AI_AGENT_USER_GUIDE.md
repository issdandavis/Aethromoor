# 🤖 AI Agent System - User Guide
## Avalon Codex Automated Workflow System

## Welcome!

This guide will help you understand and use the AI agent system that works 24/7 to grow, organize, and maintain your Avalon Codex project.

## Quick Start

### What This System Does

Your AI agents work around the clock to:

1. **📁 Organize Files** - Automatically categorize and file new content
2. **📚 Maintain Lore** - Check for consistency and expand worldbuilding
3. **✍️ Generate Content** - Create new scenes, lore entries, and dialogue
4. **🔍 Validate Quality** - Ensure everything meets your standards

### How to Use It

**The system runs automatically!** You don't need to do anything special. Just:

1. Add content to your repository (anywhere)
2. AI agents will organize, validate, and expand it
3. Review the Pull Requests they create
4. Merge what you like!

---

## Understanding Your Agents

### 🗂️ Content Organizer Agent

**What it does:**
- Watches for new files in your repository
- Automatically moves them to the right folders
- Keeps your project tidy and easy to navigate

**When it runs:**
- Immediately when new files are detected
- Weekly cleanup every Sunday
- Manual trigger anytime you want

**What you'll see:**
- Issues tagged `organization` if files need manual review
- PRs with organization changes
- Weekly organization reports

**How to use:**
```bash
# Trigger manual organization
gh workflow run weekly-organization.yml

# Check organization reports
ls .github/reports/organization-*.md
```

### 📖 Lore Curator Agent

**What it does:**
- Checks new content against established canon
- Identifies lore gaps and contradictions
- Validates character consistency and timeline accuracy

**When it runs:**
- On every Pull Request that changes lore
- Weekly deep scan for canon issues
- Manual trigger when you add major lore

**What you'll see:**
- Comments on PRs about lore consistency
- Reports on canon compliance
- Suggestions for lore expansion

**How to use:**
```bash
# Trigger lore check manually
gh workflow run lore-consistency-check.yml

# Review lore reports
cat .github/lore-validation-report.md
```

### ✨ Content Generator Agent

**What it does:**
- Creates new game scenes from outlines
- Generates lore entries to fill gaps
- Writes dialogue variations
- Expands placeholder content

**When it runs:**
- Daily at 2 AM UTC
- Weekly expansion sprint on Sundays
- Manual trigger for specific content types

**What you'll see:**
- PRs labeled `ai-generated` with new content
- Quality reports showing metrics
- Content organized in `generated_content/` folder

**How to use:**
```bash
# Generate specific content type
gh workflow run daily-content-generation.yml -f content_type=scene

# Generate all types
gh workflow run daily-content-generation.yml -f content_type=all

# Check generated content
ls generated_content/*/
```

---

## Daily Workflows

### What Happens Each Day (Automatically)

**2:00 AM UTC - Daily Content Generation**
```
1. Content Generator creates new material:
   - 1 new lore entry
   - 100-200 lines of scene expansion
   - 3-5 dialogue variations
   
2. Lore Curator validates everything:
   - Checks character consistency
   - Verifies canon compliance
   - Validates timeline accuracy
   
3. Content Organizer files it properly:
   - Categorizes content
   - Tags with metadata
   - Updates indexes
   
4. Pull Request created for your review
```

**Your Action:** Review the PR and merge if you like the content!

### What Happens Each Week (Automatically)

**Sunday Midnight UTC - Weekly Expansion Sprint**
```
1. Content Generator completes major work:
   - 1 full expedition scene (500+ lines)
   - 2-3 character development moments
   - 1 new ending variation
   - 5 expanded lore entries
   
2. Content Organizer deep cleans:
   - Scans entire repository
   - Moves misplaced files
   - Regenerates all indexes
   - Creates organization report
   
3. Lore Curator performs full audit:
   - Timeline validation
   - Character relationship map update
   - Canon consistency check
   - Gap identification report
```

**Your Action:** Review the comprehensive weekly PRs and reports!

---

## Manual Controls

### Trigger Workflows Manually

You can run any agent workflow manually using GitHub Actions:

**Via GitHub Web Interface:**
1. Go to your repository on GitHub
2. Click "Actions" tab
3. Select the workflow you want
4. Click "Run workflow" button
5. Choose options and click green "Run workflow"

**Via Command Line:**
```bash
# Daily content generation (all types)
gh workflow run daily-content-generation.yml

# Specific content type
gh workflow run daily-content-generation.yml -f content_type=lore

# Weekly organization
gh workflow run weekly-organization.yml

# Lore consistency check
gh workflow run lore-consistency-check.yml
```

### Content Generation Options

When triggering content generation manually, you can specify what type:

- `all` - Generate everything (default)
- `scene` - Only game scenes
- `lore` - Only lore entries
- `dialogue` - Only dialogue variations

**Example:**
```bash
# Generate only lore
gh workflow run daily-content-generation.yml -f content_type=lore

# Generate only scenes
gh workflow run daily-content-generation.yml -f content_type=scene
```

---

## Reviewing AI-Generated Content

### What to Look For

When reviewing PRs from AI agents, check:

✅ **Character Voice Consistency**
- Does Polly sound sarcastic but caring?
- Is Izack humble and wise?
- Are character personalities maintained?

✅ **Canon Compliance**
- No contradictions with established lore?
- Timeline makes sense?
- Magic system rules followed?

✅ **Quality Standards**
- Writing is engaging and vivid?
- Choices are meaningful?
- Proper ChoiceScript syntax?

✅ **Integration**
- Fits well with existing content?
- Cross-references make sense?
- File organization correct?

### Approval Process

1. **Review the PR** - Read through generated content
2. **Check quality reports** - See validation results
3. **Test if needed** - For game scenes, test in ChoiceScript
4. **Request changes** - Comment if something needs adjustment
5. **Approve and merge** - If everything looks good!

### Requesting Changes

If you need adjustments, comment on the PR:

```
@github-actions This scene needs:
- More Polly commentary
- Adjust Izack's dialogue to be more humble
- Add sensory details to the desert description
```

The agents will learn from your feedback over time!

---

## Configuration

### Agent Settings

Agent behavior is controlled by config files in `.github/agents/config/`:

**content_organizer_config.yml**
```yaml
confidence_threshold: 0.85  # How confident before auto-organizing
auto_organize_threshold: 0.85
manual_review_threshold: 0.60
```

**lore_curator_config.yml**
```yaml
strictness_level: high  # How strict with canon (low/medium/high)
auto_expand_gaps: true  # Auto-generate lore for gaps?
max_daily_expansions: 3  # Limit expansions per day
```

**content_generator_config.yml**
```yaml
daily_scene_lines: 200  # Lines to generate daily
weekly_scene_lines: 500  # Lines for weekly sprint
min_quality_score: 70  # Minimum quality threshold
```

### API Keys

The system needs API keys to work. Set them in GitHub Secrets:

1. Go to repository Settings
2. Navigate to Secrets and variables → Actions
3. Add these secrets:
   - `ANTHROPIC_API_KEY` - For Claude-based agents
   - `OPENAI_API_KEY` - For GPT-based agents (optional)

**Never commit API keys to the repository!**

---

## Monitoring & Reports

### Daily Reports

Check `generated_content/[DATE]/GENERATION_LOG.md` for:
- What was generated
- Quality metrics
- Validation results

### Weekly Reports

Check `.github/reports/organization-[DATE].md` for:
- Organization status
- Files processed
- Improvement suggestions
- Content map

### GitHub Issues

Agents create issues when they need help:
- `organization` label - Files need manual categorization
- `canon-decision-needed` - Lore conflict requires human decision
- `quality-review` - Content below automatic threshold

---

## Common Scenarios

### "I want more lore about [topic]"

Create an issue:
```
Title: Generate lore for Midnight Council
Labels: generate-content, lore

Description:
Please generate detailed lore about the Midnight Council mentioned in Aria's backstory. Include:
- History and founding
- Current structure
- Relationship to Avalon Academy
- Key members
```

The Content Generator will process this and create a PR!

### "I need this scene expanded"

Comment on the scene file or create issue:
```
Title: Expand singing_dunes_arrival scene
Labels: generate-content, scene

Description:
Expand singing_dunes_arrival to 500+ lines with:
- More environmental description
- Kael's introduction
- Truth-testing mechanics
- 3-5 meaningful choices
```

### "A file is in the wrong place"

Don't worry! The Content Organizer will catch it in the next weekly scan. Or trigger manually:

```bash
gh workflow run weekly-organization.yml
```

### "The lore seems contradictory"

The Lore Curator checks this automatically on PRs. If you notice an issue:

```bash
# Run lore check manually
gh workflow run lore-consistency-check.yml
```

Review the report at `.github/lore-validation-report.md`

---

## Best Practices

### 🎯 Let the Agents Work

- Don't manually organize files - let Content Organizer do it
- Don't check canon manually - let Lore Curator validate
- Review and approve rather than generate yourself

### 📝 Provide Clear Feedback

When requesting changes on PRs:
- Be specific about what needs adjustment
- Explain why (helps agents learn)
- Provide examples of what you want

### 🔄 Regular Review Cadence

Set up a review schedule:
- **Daily:** Quick check of generation PRs
- **Weekly:** Review weekly sprint content
- **Monthly:** Check agent performance metrics

### 🎨 Maintain Quality

Approve content that:
- Matches established voice and tone
- Complies with canon
- Meets quality standards
- Integrates well with existing content

### 💾 Keep Backups

Agents work in branches and PRs, so:
- Main branch is always protected
- You can reject any PR
- Nothing is lost if you don't like it
- All history is preserved

---

## Troubleshooting

### "No PRs are being created"

**Check:**
1. GitHub Actions are enabled (Settings → Actions)
2. Workflows are not disabled
3. API keys are set in Secrets
4. Check Actions tab for errors

**Solution:**
```bash
# View recent workflow runs
gh run list

# View specific run details
gh run view [RUN_ID]
```

### "Content quality is low"

**Adjust settings:**
1. Edit `.github/agents/config/content_generator_config.yml`
2. Increase `min_quality_score`
3. Adjust creativity vs consistency weights

**Provide feedback:**
- Comment on PRs with specific issues
- Agents learn from your edits

### "Too many PRs to review"

**Adjust frequency:**
1. Edit workflow schedule in `.github/workflows/`
2. Change daily to weekly, or vice versa
3. Adjust `max_daily_expansions` in config

**Batch review:**
- Let PRs accumulate
- Review in batches weekly
- Merge similar changes together

### "Lore inconsistencies detected"

**Review the report:**
1. Check `.github/lore-validation-report.md`
2. Decide which version is correct
3. Update master chronicle if needed

**Fix conflicts:**
- Edit the conflicting file
- Update IZACK_MASTER_CHRONICLE_UPDATED.txt
- Commit changes

---

## Advanced Usage

### Creating Custom Workflows

You can create custom agent workflows:

```yaml
# .github/workflows/custom-generation.yml
name: Custom Content Generation

on:
  workflow_dispatch:
    inputs:
      topic:
        description: 'Topic to generate about'
        required: true

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      # Your custom generation logic
```

### Integrating External Tools

Connect agents to external automation:

**Zapier Integration:**
- Trigger: New Google Doc in lore folder
- Action: Run content organization workflow
- Result: Auto-filed in repository

**Discord Integration:**
- Post daily generation summary
- Alert on quality issues
- Share weekly reports

### Extending Agent Capabilities

To add new agent capabilities:

1. Edit the agent markdown file in `.github/agents/`
2. Update workflows in `.github/workflows/`
3. Add new config options in `.github/agents/config/`
4. Document changes in this guide

---

## Getting Help

### Documentation
- **Agent Specs:** `.github/agents/*.agent.md`
- **Orchestrator:** `.github/agents/ORCHESTRATOR.md`
- **Workflows:** `.github/workflows/*.yml`

### Support
- **Issues:** Create issue with `agent-help` label
- **Discussions:** Use GitHub Discussions for questions
- **Email:** Contact repository maintainer

### Community
- Share tips and tricks in Discussions
- Report bugs via Issues
- Suggest improvements via PRs

---

## Success Metrics

Track your system's performance:

### Productivity
- ✅ Content generated per week
- ✅ Scenes completed per month
- ✅ Lore entries created

### Quality
- ✅ Acceptance rate of generated content
- ✅ Canon compliance score
- ✅ Time saved on manual tasks

### Organization
- ✅ Files properly organized
- ✅ Reduced time finding content
- ✅ Cleaner repository structure

---

## Quick Reference

### Most Common Commands

```bash
# Generate content
gh workflow run daily-content-generation.yml

# Organize repository
gh workflow run weekly-organization.yml

# Check lore consistency
gh workflow run lore-consistency-check.yml

# View recent runs
gh run list

# View workflow details
gh run view [RUN_ID]
```

### Most Important Files

```
.github/agents/ORCHESTRATOR.md         - System overview
.github/agents/content-generator.agent.md  - Generation rules
.github/agents/lore-curator.agent.md       - Canon validation
.github/agents/content-organizer.agent.md  - Organization logic
.github/workflows/                     - Automation workflows
.github/agents/config/                 - Agent settings
```

### Quick Checks

```bash
# See what's been generated today
ls generated_content/$(date +%Y-%m-%d)*/

# Check latest organization report
cat .github/reports/organization-*.md | tail -100

# View lore validation
cat .github/lore-validation-report.md
```

---

## Conclusion

Your AI agent system is designed to:
- 🚀 Accelerate content creation
- 🎯 Maintain quality and consistency
- 📁 Keep everything organized
- ⏰ Work 24/7 while you're away

**Just review, approve, and enjoy watching your project grow!**

---

*Last Updated: [Auto-generated]*
*Version: 1.0*
*For updates, see `.github/agents/ORCHESTRATOR.md`*
