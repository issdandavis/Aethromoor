# 🤖 Avalon AI Agent System - Quick Start

## What is This?

An automated AI system that works 24/7 to:
- ✍️ Generate new game content (scenes, lore, dialogue)
- 📁 Organize your files automatically
- 🔍 Check for lore consistency
- 📊 Maintain quality standards

**It's like having a team of assistants working around the clock!**

---

## Setup (5 Minutes)

### 1. Add API Keys

Go to your repository → **Settings** → **Secrets and variables** → **Actions**

Add these secrets:
- `ANTHROPIC_API_KEY` - Your Claude API key ([Get one here](https://console.anthropic.com/))
- `OPENAI_API_KEY` - Your OpenAI API key ([Get one here](https://platform.openai.com/)) *(Optional)*

### 2. Enable Workflows

Go to **Actions** tab → Click **"I understand my workflows, go ahead and enable them"**

### 3. Done!

The system will now run automatically:
- **Every day at 2 AM UTC** - Generates new content
- **Every Sunday** - Deep organization and cleanup
- **On every PR** - Checks lore consistency

---

## How to Use It

### Let It Work Automatically

Just add content to your repository normally. The AI agents will:
1. Detect new files
2. Organize them properly
3. Validate against canon
4. Generate related content
5. Create Pull Requests for your review

### Manual Triggers

Want to generate content now? Use GitHub Actions:

**Via Web:**
1. Go to **Actions** tab
2. Select **"Daily Content Generation"**
3. Click **"Run workflow"**
4. Choose content type (scene/lore/dialogue/all)
5. Click green **"Run workflow"** button

**Via Command Line:**
```bash
# Generate all content types
gh workflow run daily-content-generation.yml

# Generate only scenes
gh workflow run daily-content-generation.yml -f content_type=scene

# Generate only lore
gh workflow run daily-content-generation.yml -f content_type=lore

# Run organization
gh workflow run weekly-organization.yml

# Check lore consistency
gh workflow run lore-consistency-check.yml
```

---

## What You'll See

### Pull Requests
- **Label:** `ai-generated` - Content created by AI
- **Label:** `organization` - Files organized
- **Label:** `needs-review` - Awaiting your approval

### Issues
- **Label:** `canon-decision-needed` - Lore conflict needs human decision
- **Label:** `quality-review` - Content below automatic threshold
- **Label:** `organization` - Files need manual categorization

### Reports
- `generated_content/[DATE]/` - Daily generated content
- `.github/reports/organization-[DATE].md` - Weekly organization reports
- `.github/lore-validation-report.md` - Lore consistency checks

---

## Reviewing AI Content

When you see a PR labeled `ai-generated`:

1. **Read the content** - Check generated scenes, lore, or dialogue
2. **Verify quality** - Does it match character voices and style?
3. **Check canon** - Does it fit with established lore?
4. **Test if needed** - For game scenes, test in ChoiceScript
5. **Approve or request changes** - Merge if good, comment if needs work

### Acceptance Criteria

✅ **Good to Merge:**
- Character voices sound right
- No lore contradictions
- Quality meets standards
- Integrates well with existing content

❌ **Request Changes:**
- Character feels off
- Contradicts canon
- Below quality standards
- Doesn't fit story flow

---

## Customization

### Adjust Agent Behavior

Edit config files in `.github/agents/config/`:

**content_generator_config.yml** - How much content to generate
```yaml
daily_generation:
  scene_lines: 200  # Change to 100 or 400
  lore_entries: 1   # Change to 2 or 3
```

**lore_curator_config.yml** - How strict to be with canon
```yaml
strictness_level: high  # Change to medium or low
```

**content_organizer_config.yml** - Organization behavior
```yaml
confidence_threshold: 0.85  # Change to 0.70 or 0.95
```

### Change Schedule

Edit workflow files in `.github/workflows/`:

**daily-content-generation.yml**
```yaml
schedule:
  - cron: '0 2 * * *'  # Change time (currently 2 AM UTC)
```

**weekly-organization.yml**
```yaml
schedule:
  - cron: '0 0 * * 0'  # Change day (currently Sunday)
```

---

## Common Tasks

### "I want more lore about X"

Create an issue:
```
Title: Generate lore for [topic]
Labels: generate-content, lore

Description:
Please generate lore about [topic]. Include:
- [What you want]
- [Specific details]
- [How it connects to existing lore]
```

The Content Generator will create it and submit a PR!

### "This file is in the wrong place"

Just wait! The weekly organization run will catch it. Or trigger manually:
```bash
gh workflow run weekly-organization.yml
```

### "Expand this scene"

Create an issue or comment on the file:
```
Title: Expand [scene_name]
Labels: generate-content, scene

Expand to 500+ lines with:
- More environmental detail
- Character interactions
- Meaningful choices
- Polly commentary
```

### "Check if this is consistent with canon"

Trigger lore check:
```bash
gh workflow run lore-consistency-check.yml
```

---

## System Overview

### The Agents

**🗂️ Content Organizer** - Keeps files tidy
- Monitors for new files
- Categorizes and files them
- Updates indexes
- Prevents duplicates

**📖 Lore Curator** - Protects canon
- Validates consistency
- Checks timelines
- Ensures character voices
- Identifies gaps

**✨ Content Generator** - Creates content
- Generates scenes
- Writes lore entries
- Creates dialogue
- Expands placeholders

### The Workflows

**Daily (2 AM UTC)**
- Generate new content
- Validate with lore curator
- Organize and tag
- Create PR for review

**Weekly (Sunday Midnight UTC)**
- Deep repository scan
- Organization cleanup
- Full lore audit
- Comprehensive reports

**On Pull Requests**
- Validate lore changes
- Check character consistency
- Ensure quality standards
- Comment with findings

---

## Troubleshooting

### "Workflows aren't running"

1. Check Actions are enabled (Settings → Actions)
2. Verify API keys are set in Secrets
3. Check workflow syntax in `.github/workflows/`
4. View error logs in Actions tab

### "Content quality is low"

1. Adjust thresholds in config files
2. Provide feedback on PRs (agents learn!)
3. Increase `min_quality_score` in generator config

### "Too many PRs"

1. Reduce generation frequency in workflow schedules
2. Lower daily quotas in generator config
3. Review PRs in batches weekly

### "Lore conflicts detected"

1. Read the validation report
2. Decide which version is correct
3. Update master chronicle
4. Re-run validation

---

## Need Help?

### Documentation
- **Full Guide:** `docs/AI_AGENT_USER_GUIDE.md`
- **System Overview:** `.github/agents/ORCHESTRATOR.md`
- **Agent Details:** `.github/agents/*.agent.md`

### Support
- **Create Issue:** Use label `agent-help`
- **GitHub Discussions:** Ask questions
- **Contact:** Repository maintainer

---

## Quick Commands Reference

```bash
# Content generation
gh workflow run daily-content-generation.yml
gh workflow run daily-content-generation.yml -f content_type=scene
gh workflow run daily-content-generation.yml -f content_type=lore

# Organization
gh workflow run weekly-organization.yml

# Validation
gh workflow run lore-consistency-check.yml

# Check status
gh run list
gh run view [RUN_ID]

# View generated content
ls generated_content/
cat generated_content/*/GENERATION_LOG.md

# View reports
cat .github/reports/organization-*.md
cat .github/lore-validation-report.md
```

---

## What's Next?

1. ✅ **Set up API keys** (see step 1 above)
2. ✅ **Enable workflows** (see step 2 above)
3. ✅ **Wait for first run** (daily at 2 AM UTC)
4. ✅ **Review first PR** (check quality and approve)
5. ✅ **Customize configs** (adjust to your preferences)
6. ✅ **Enjoy automated content** (watch your project grow!)

---

**Welcome to automated content creation!**

Your AI agents are ready to work 24/7.
Just review, approve, and watch your world expand.

🚀

---

*For the complete guide, see `docs/AI_AGENT_USER_GUIDE.md`*
*For technical details, see `.github/agents/ORCHESTRATOR.md`*
