# 🏢 ENTERPRISE SETUP GUIDE
## The Avalon Codex - Solo Developer with AI Assistance

**Last Updated:** November 24, 2025  
**For:** One developer managing a creative narrative project with multiple GitHub accounts and AI assistance

---

## 📋 OVERVIEW

This guide helps you set up a professional "enterprise" environment for **The Avalon Codex** project, even as a solo developer. You'll configure:

1. **Dual GitHub Account Structure** (Personal + Organization)
2. **AI Assistant Integration** (GitHub Copilot Workspace Agent)
3. **Automation Workflows** (GitHub Actions)
4. **Development Environment** (Local setup)
5. **Multi-AI Collaboration System** (Coordinated AI assistants)

---

## 🎯 YOUR CURRENT SETUP

✅ **What You Already Have:**
- Repository: `issdandavis/Avalon`
- GitHub Copilot Workspace Agent configured
- Custom agent: "Avalon Lore Steward"
- GitHub Actions workflows (ChoiceScript tests, Jekyll)
- Comprehensive documentation
- Dual game versions (HTML + ChoiceScript)

🎯 **What We're Adding:**
- Structured account management
- Enhanced AI coordination
- Automated workflows
- Development best practices
- Collaboration tracking

---

## 1️⃣ GITHUB ACCOUNT STRUCTURE

### Your Two Accounts:

#### **Account 1: Personal Account** (`issdandavis`)
**Purpose:** Individual contributions, main development work  
**Access Level:** Owner  
**Responsibilities:**
- Day-to-day coding and writing
- Pull request reviews
- Issue management
- Direct commits to branches

#### **Account 2: Organization/Secondary Account**
**Purpose:** Project management, releases, automation  
**Access Level:** Collaborator or Organization member  
**Responsibilities:**
- Release management
- CI/CD oversight
- Documentation reviews
- Backup access

### How to Set Up Account #2:

```bash
# 1. Create/identify your second GitHub account
# 2. Go to https://github.com/issdandavis/Avalon/settings/access
# 3. Click "Add people"
# 4. Invite your second account
# 5. Grant "Maintain" or "Admin" access
```

### Benefits of Dual Account Setup:
- ✅ Separation of concerns (dev vs management)
- ✅ Better audit trail
- ✅ Practice enterprise workflows
- ✅ Backup access if one account locked
- ✅ Can simulate team collaboration

---

## 2️⃣ AI ASSISTANT CONFIGURATION

### GitHub Copilot Workspace Agent

**Already Configured:** ✅  
**Location:** `.github/agents/my-agent.agent.md`  
**Current Name:** "Avalon Lore Steward"

#### Verify It's Working:

```bash
# In VS Code with Copilot:
# 1. Open any .txt or .md file
# 2. Start typing a comment about Avalon lore
# 3. Copilot should suggest content aware of your universe
```

#### Enhance the Custom Agent:

Your agent should be updated to handle:
- **Lore Curation:** Validate new narrative against existing canon
- **File Organization:** Keep files categorized and labeled
- **Coding Assistance:** Help with ChoiceScript and JavaScript
- **Documentation:** Maintain consistency across docs

**See below for enhanced agent configuration.**

### Multi-AI Collaboration Setup

Create coordination files so multiple AI assistants can work together:

#### A. Status Context File
**Purpose:** Weekly snapshot of current work

```bash
# Will create: STATUS_CONTEXT.md
```

#### B. Scene Parity Checklist
**Purpose:** Track HTML vs ChoiceScript scene conversion

```bash
# Will create: SCENE_PARITY_CHECKLIST.md
```

#### C. Stats Matrix
**Purpose:** Track stat changes across choices

```bash
# Will create: STATS_MATRIX.md
```

---

## 3️⃣ ENVIRONMENT CONFIGURATION

### Local Development Setup

#### Step 1: Clone Repository (Both Accounts)

```bash
# On your main machine (Account 1)
git clone https://github.com/issdandavis/Avalon.git
cd Avalon

# Configure git for Account 1 (replace with your actual details)
git config user.name "Your Name"  # ← Your actual name
git config user.email "your.email@example.com"  # ← Your Account #1 email
```

```bash
# On secondary machine or profile (Account 2)
git clone https://github.com/issdandavis/Avalon.git
cd Avalon

# Configure git for Account 2 (replace with your actual details)
git config user.name "Your Name (Org)"  # ← Your actual name
git config user.email "your.other.email@example.com"  # ← Your Account #2 email
```

#### Step 2: Set Up Environment Variables

```bash
# Copy the template (this file exists in the repository)
cp config/.env.example config/.env

# Edit config/.env with your API keys
nano config/.env
```

**Add your keys:**
```bash
# Replace 'xxx' with your actual API keys:
ANTHROPIC_API_KEY=sk-ant-api03-xxx
OPENAI_API_KEY=sk-xxx
GITHUB_TOKEN=ghp_xxx  # For automation (optional)
```

⚠️ **NEVER commit `.env` to git** - it's already in `.gitignore`

#### Step 3: Install Dependencies

```bash
# If you add Node.js dependencies in future:
npm install

# No dependencies needed currently for basic HTML game
# ChoiceScript is standalone
```

---

## 4️⃣ AUTOMATED WORKFLOWS

### Current GitHub Actions

#### Workflow 1: ChoiceScript Tests
**File:** `.github/workflows/choicescript-tests.yml`  
**Triggers:** Pushes to `choicescript_game/scenes/**`  
**Status:** Placeholder (needs implementation)

#### Workflow 2: Jekyll Site CI
**File:** `.github/workflows/jekyll-docker.yml`  
**Triggers:** Pushes to `main` branch  
**Status:** Active

### Recommended Additional Workflows

#### A. Auto-Label PRs

Create `.github/workflows/auto-label.yml`:

```yaml
name: Auto Label PRs

on:
  pull_request:
    types: [opened, edited]

jobs:
  label:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/labeler@v4
        with:
          repo-token: "${{ secrets.GITHUB_TOKEN }}"
```

#### B. Weekly Status Report

Create `.github/workflows/weekly-status.yml`:

```yaml
name: Weekly Status Report

on:
  schedule:
    - cron: '0 9 * * 1'  # Every Monday at 9 AM
  workflow_dispatch:

jobs:
  status:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Generate Status
        run: |
          echo "# Weekly Status Report" > weekly-status.md
          echo "**Date:** $(date)" >> weekly-status.md
          echo "" >> weekly-status.md
          echo "## Recent Commits:" >> weekly-status.md
          git log --since="1 week ago" --pretty=format:"- %s (%an)" >> weekly-status.md
      - name: Create Issue
        uses: peter-evans/create-issue-from-file@v4
        with:
          title: "Weekly Status - $(date +%Y-%m-%d)"
          content-filepath: weekly-status.md
          labels: status, automated
```

#### C. ChoiceScript Validation (Enhanced)

Update `.github/workflows/choicescript-tests.yml`:

```yaml
name: ChoiceScript Tests

on:
  push:
    paths:
      - 'choicescript_game/scenes/**'
      - '.github/workflows/choicescript-tests.yml'
  pull_request:
    paths:
      - 'choicescript_game/scenes/**'
  workflow_dispatch:

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
      
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Check Scene Files Exist
        run: |
          echo "Checking required scene files..."
          required_scenes=(
            "startup.txt"
            "choicescript_stats.txt"
            "scenes/arrival.txt"
            "scenes/first_lesson.txt"
            "scenes/singing_dunes.txt"
            "scenes/verdant_tithe.txt"
            "scenes/rune_glacier.txt"
            "scenes/endings.txt"
          )
          
          for scene in "${required_scenes[@]}"; do
            if [ -f "choicescript_game/$scene" ]; then
              echo "✓ Found: $scene"
            else
              echo "✗ Missing: $scene"
              exit 1
            fi
          done
      
      - name: Check for Common Syntax Errors
        run: |
          echo "Checking for common ChoiceScript syntax errors..."
          cd choicescript_game/scenes
          
          # Check for unmatched *if statements
          for file in *.txt; do
            echo "Checking $file..."
            # Add basic syntax checks here
          done
          
          echo "Basic syntax check complete!"
      
      - name: Validate Stats Initialization
        run: |
          echo "Checking stats are properly initialized..."
          if grep -q "*create collaboration" choicescript_game/startup.txt; then
            echo "✓ Collaboration stat found"
          else
            echo "✗ Collaboration stat not initialized"
            exit 1
          fi
```

---

## 5️⃣ AI COORDINATION SYSTEM

### Multi-AI Workflow

When using multiple AI assistants (Claude, ChatGPT, Copilot, etc.):

#### Assign Clear Roles:

1. **Lore Curator** (Claude or creative-focused AI)
   - Validates narrative consistency
   - Checks character timelines
   - Maintains magic system rules

2. **Conversion Engineer** (GitHub Copilot)
   - Converts HTML to ChoiceScript
   - Implements stat tracking
   - Handles code structure

3. **Structural Reviewer** (Any code-focused AI)
   - Verifies branching logic
   - Checks scene parity
   - Validates stat progression

4. **Documentation Manager** (Any AI)
   - Updates roadmaps
   - Maintains guides
   - Tracks progress

#### Use Hand-off Conventions:

**Commit Message Prefixes:**
```
Lore: Added desert spirit backstory
Convert: HTML dunes scene → ChoiceScript
Struct: Fixed branching in glacier path
Docs: Updated roadmap Phase 2 status
Balance: Adjusted collaboration thresholds
```

**TODO Comments in Code:**
```choicescript
*comment TODO:[ROLE]: Description of what needs doing
*comment TODO:[Lore]: Verify Kael's age matches desert timeline
*comment TODO:[Balance]: Check if +15 collaboration too high here
```

---

## 6️⃣ PROJECT BOARD SETUP

### GitHub Projects (Recommended)

#### Create a Project Board:

1. Go to: https://github.com/issdandavis/Avalon/projects
2. Click "New project"
3. Choose "Board" template
4. Name it: "Avalon Development Tracker"

#### Suggested Columns:

```
📥 Backlog
│
├─ 🎯 Phase 2: ChoiceScript Completion
│
├─ 🔨 In Progress
│
├─ 👀 Review Needed
│
├─ 🧪 Testing
│
└─ ✅ Done
```

#### Add Issues for Each Task:

From `docs/PROJECT_ROADMAP.md`, create issues:

```bash
# Example issues to create:

1. "Complete Singing Dunes Expedition"
   - Labels: priority, choicescript, phase-2
   - Assigned to: Account #1

2. "Implement Verdant Tithe scenes"
   - Labels: choicescript, phase-2
   - Assigned to: Account #2 (or alternate)

3. "Write all 14 endings"
   - Labels: narrative, phase-2
   - Milestone: Phase 2 Complete
```

---

## 7️⃣ DEVELOPMENT WORKFLOW

### Daily Workflow (Solo Developer)

#### Morning Routine:
```bash
# 1. Pull latest changes
git pull origin main

# 2. Check project board
# Visit: github.com/issdandavis/Avalon/projects

# 3. Review STATUS_CONTEXT.md
cat STATUS_CONTEXT.md

# 4. Pick a task from "In Progress"
```

#### Working Session:
```bash
# 1. Create feature branch
git checkout -b feature/singing-dunes-expansion

# 2. Work on files (with AI assistance)
# - Use GitHub Copilot for code
# - Reference COPILOT_INSTRUCTIONS.md
# - Update STATUS_CONTEXT.md as you go

# 3. Test locally
# - Open game/index.html in browser
# - Or use ChoiceScript IDE for .txt files

# 4. Commit frequently
git add .
git commit -m "Convert: Added first 5 dunes scenes"
git push origin feature/singing-dunes-expansion
```

#### End of Day:
```bash
# 1. Create PR from feature branch
# Go to: github.com/issdandavis/Avalon/pulls
# Create PR: feature/singing-dunes-expansion → main

# 2. Switch to Account #2 to review
# - Read changes
# - Test if possible
# - Approve or request changes

# 3. Merge when ready
# Account #1 merges after Account #2 approves

# 4. Update project board
# Move cards to "Done"

# 5. Update STATUS_CONTEXT.md with tomorrow's plan
```

### Weekly Review (Both Accounts)

**Every Friday or Sunday:**

```bash
# 1. Review week's progress
git log --since="1 week ago" --pretty=format:"%h - %s"

# 2. Update PROJECT_ROADMAP.md checkboxes

# 3. Update SCENE_PARITY_CHECKLIST.md

# 4. Check STATS_MATRIX.md for balance issues

# 5. Plan next week's tasks

# 6. Commit documentation updates
git add docs/
git commit -m "Docs: Weekly progress update"
git push origin main
```

---

## 8️⃣ REPOSITORY SETTINGS

### Recommended Settings

#### Branch Protection (for `main`):

1. Go to: Settings → Branches → Add rule
2. Branch name pattern: `main`
3. Enable:
   - ✅ Require pull request before merging
   - ✅ Require approvals: 1 (your Account #2)
   - ✅ Dismiss stale approvals when new commits pushed
   - ✅ Require status checks to pass
   - ✅ Require branches to be up to date

#### Repository Settings:

```
General:
- ✅ Features: Issues, Projects, Wiki
- ✅ Pull Requests: Allow squash merging
- ❌ Allow merge commits (optional)
- ✅ Automatically delete head branches

Pages:
- Source: gh-pages branch (if hosting HTML game)
- Custom domain: (optional)

Security:
- ✅ Dependency graph
- ✅ Dependabot alerts
- ✅ Secret scanning
```

---

## 9️⃣ COLLABORATION FILES

### Create These Files:

#### A. STATUS_CONTEXT.md

```markdown
# Project Status Context

**Last Updated:** [Date]  
**Current Phase:** Phase 2 - ChoiceScript Completion  
**Active Scene:** singing_dunes.txt

## This Week's Focus:
- [ ] Complete dunes_arrival scene
- [ ] Add Kael introduction
- [ ] Implement truth-testing mechanic

## Pending Lore Updates:
- Desert spirit backstory (for dunes)
- Kael's relationship to Izack

## Next Up:
- Verdant Tithe forest expansion
```

#### B. SCENE_PARITY_CHECKLIST.md

```markdown
# Scene Parity Checklist
HTML vs ChoiceScript Scene Conversion Status

## Core Scenes
- [x] arrival.txt - Complete ✅
- [x] first_lesson.txt - Complete ✅
- [ ] dorm_room.txt - Missing
- [ ] academy_life.txt - Missing

## Expeditions
- [ ] singing_dunes.txt - Draft 🚧
- [ ] verdant_tithe.txt - Missing
- [ ] rune_glacier.txt - Missing

## Endings
- [ ] endings.txt - Placeholder only

**Legend:**
✅ Complete and verified
🚧 Draft/In Progress
❌ Has issues
⏸️ Blocked/Waiting
```

#### C. STATS_MATRIX.md

```markdown
# Stats Matrix
Track all stat modifications across scenes

| Scene File | Choice | Stat Change | Notes |
|------------|--------|-------------|-------|
| arrival.txt | Polite greeting | collaboration +5 | Baseline friendly |
| arrival.txt | Curious questions | collaboration +3 | Engagement |
| arrival.txt | Confident stance | collaboration +0 | Neutral |
| first_lesson.txt | Share power | collaboration +10 | Key moment |
| first_lesson.txt | Control power | collaboration -5 | Hierarchy |

## Balance Check:
- Minimum collaboration to reach endings: 60
- Maximum achievable by endings: ~120
- Current range: Good ✅
```

---

## 🔟 QUICK REFERENCE CHECKLIST

### ✅ Initial Setup (One Time)

- [ ] Add Account #2 to repository
- [ ] Set up branch protection on `main`
- [ ] Create GitHub Project board
- [ ] Copy `config/.env.example` to `config/.env`
- [ ] Add API keys to `.env`
- [ ] Verify GitHub Copilot agent works
- [ ] Create STATUS_CONTEXT.md
- [ ] Create SCENE_PARITY_CHECKLIST.md
- [ ] Create STATS_MATRIX.md
- [ ] Enable GitHub Actions
- [ ] Configure repository settings

### ✅ Daily Workflow

- [ ] Pull latest from `main`
- [ ] Check STATUS_CONTEXT.md
- [ ] Review project board
- [ ] Create feature branch
- [ ] Work with AI assistance
- [ ] Test changes locally
- [ ] Commit with role prefix
- [ ] Push and create PR
- [ ] Review with Account #2
- [ ] Merge after approval
- [ ] Update project board

### ✅ Weekly Maintenance

- [ ] Review week's commits
- [ ] Update PROJECT_ROADMAP.md
- [ ] Update SCENE_PARITY_CHECKLIST.md
- [ ] Balance check STATS_MATRIX.md
- [ ] Plan next week
- [ ] Commit documentation

---

## 🆘 TROUBLESHOOTING

### "Can't push to main"
**Solution:** You enabled branch protection. Create a branch and PR instead.

```bash
git checkout -b fix/issue-name
git push origin fix/issue-name
# Then create PR on GitHub
```

### "AI assistant not responding to my lore"
**Solution:** Check `.github/agents/my-agent.agent.md` and custom instructions.

### "Account #2 can't approve PRs"
**Solution:** Check repository access level. Needs "Write" or higher.

```
Settings → Collaborators → Check Account #2 access
```

### "GitHub Actions not running"
**Solution:** Check Actions are enabled.

```
Settings → Actions → General → Allow all actions
```

---

## 📚 ADDITIONAL RESOURCES

### Internal Documentation:
- `README.md` - Project overview
- `START_HERE.md` - Quick start for playing
- `QUICK_START.md` - Detailed game setup
- `docs/PROJECT_ROADMAP.md` - Development phases
- `docs/AUTOMATION_GUIDE.md` - Zapier integration ideas
- `.github/COPILOT_INSTRUCTIONS.md` - AI assistant guide

### External Resources:
- [GitHub Projects Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [ChoiceScript Wiki](https://choicescriptdev.fandom.com/)
- [Hosted Games Forum](https://forum.choiceofgames.com/)

---

## 🎯 NEXT STEPS

**Start Here:**

1. ✅ Add Account #2 as collaborator
2. ✅ Set up `.env` file with API keys
3. ✅ Create GitHub Project board
4. ✅ Create collaboration tracking files
5. ✅ Configure branch protection
6. ✅ Make first PR using new workflow
7. ✅ Test AI assistant coordination

**Then:**
- Continue Phase 2 development (ChoiceScript scenes)
- Use dual-account PR workflow
- Track progress in project board
- Coordinate multiple AI assistants
- Build toward publication

---

## 🎊 SUCCESS METRICS

You'll know the setup is working when:

✅ PRs require approval from Account #2  
✅ GitHub Actions run on every push  
✅ AI assistants reference your custom instructions  
✅ Project board stays updated  
✅ Collaboration files track progress  
✅ Development feels organized and professional

---

**Welcome to your enterprise setup! You're now running a professional development operation, even as a solo developer with AI assistance.** 🚀

*"The spiral continues. Every system you build makes the next step easier."*

---

**Questions?** Update this guide as you discover better workflows!
