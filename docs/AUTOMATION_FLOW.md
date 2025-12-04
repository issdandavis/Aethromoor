# Avalon GitHub Automation Flow

This document visualizes how all the automated workflows work together.

---

## 🔄 Complete Automation Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     AVALON REPOSITORY                            │
│                  (issdandavis/Avalon)                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │         TRIGGER EVENTS                  │
        │  • New Issue                           │
        │  • New Pull Request                    │
        │  • Push to main/develop                │
        │  • Weekly schedule                     │
        │  • Manual trigger                      │
        └─────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
    ┌─────────────┐  ┌──────────────┐  ┌──────────────┐
    │   ISSUES    │  │  PULL REQ    │  │   COMMITS    │
    └─────────────┘  └──────────────┘  └──────────────┘
              │               │               │
              ▼               ▼               ▼
    ┌─────────────────────────────────────────────────┐
    │         AUTOMATED WORKFLOWS                     │
    │                                                 │
    │  1. auto-assign-issues.yml                    │
    │  2. pr-management.yml                         │
    │  3. choicescript-tests.yml                    │
    │  4. security-scanning.yml                     │
    │  5. deploy-pages.yml                          │
    │  6. jekyll-docker.yml (existing)              │
    └─────────────────────────────────────────────────┘
              │
              └──────┬─────────┬─────────┬─────────┐
                     ▼         ▼         ▼         ▼
            ┌────────────┬──────────┬─────────┬─────────┐
            │  Assign &  │ Validate │ Security│ Deploy  │
            │   Label    │  Content │  Scan   │  Site   │
            └────────────┴──────────┴─────────┴─────────┘
                     │         │         │         │
                     └─────────┴────┬────┴─────────┘
                                   ▼
                        ┌────────────────────┐
                        │   NOTIFICATIONS    │
                        │ • GitHub UI        │
                        │ • Email            │
                        │ • Actions Tab      │
                        └────────────────────┘
```

---

## 📊 Workflow Details

### 1️⃣ Issue Auto-Assignment
**Trigger:** New issue created

```
New Issue Created
       ↓
Analyze title & body
       ↓
Apply labels (bug/enhancement/docs/lore/etc)
       ↓
Assign to repository owner
       ↓
Add welcome comment
       ↓
✓ Issue organized & assigned
```

**Auto-applied labels:**
- `bug` - Keywords: bug, error, broken
- `enhancement` - Keywords: feature, enhancement
- `documentation` - Keywords: doc, documentation
- `question` - Keywords: question, help
- `game-content` - Keywords: game, scene
- `lore` - Keywords: lore, character
- `priority: high` - Keywords: urgent, critical

---

### 2️⃣ Pull Request Management
**Trigger:** Pull request opened/updated

```
PR Opened
    ↓
Calculate size (lines changed)
    ↓
Apply size label (XS/S/M/L/XL)
    ↓
Analyze changed files
    ↓
Apply content labels
    ↓
Check PR description completeness
    ↓
Comment if missing info
    ↓
✓ PR categorized & reviewed
```

**Size labels:**
- XS: < 10 lines
- S: < 50 lines
- M: < 200 lines
- L: < 500 lines
- XL: 500+ lines

**Content labels:**
- `game-content` - Files in game/ or choicescript_game/
- `lore` - Files in lore/
- `documentation` - Files in docs/ or .md
- `writing` - Files in writing_drafts/
- `github-actions` - Files in .github/workflows/

---

### 3️⃣ ChoiceScript Testing
**Trigger:** Changes to game files

```
Game Files Changed
       ↓
Validate scene files exist
       ↓
Check startup.txt structure
       ↓
Scan for syntax issues
       ↓
Calculate word count
       ↓
Validate HTML version
       ↓
Check content consistency
       ↓
✓ Game validated
```

**Checks performed:**
- ✓ Scene files present
- ✓ startup.txt contains *create and *scene_list
- ✓ No obvious syntax errors
- ✓ Word count meets minimum (30,000)
- ✓ HTML files intact
- ✓ JavaScript syntax valid

---

### 4️⃣ Security Scanning
**Trigger:** Push to main/develop, weekly, manual

```
Code Changes / Weekly Run
          ↓
    CodeQL Analysis
          ↓
    Secret Scanning (TruffleHog)
          ↓
    Dependency Review
          ↓
    File Validation
          ↓
    Generate Report
          ↓
✓ Security verified
```

**Security checks:**
- ✓ Code vulnerabilities (CodeQL)
- ✓ Exposed secrets (TruffleHog)
- ✓ Vulnerable dependencies (Dependency Review)
- ✓ Sensitive files (.env, .key, etc.)

---

### 5️⃣ GitHub Pages Deployment
**Trigger:** Push to main branch

```
Push to Main
     ↓
Build site structure
     ↓
Copy game files
     ↓
Copy documentation
     ↓
Create landing page
     ↓
Upload artifact
     ↓
Deploy to GitHub Pages
     ↓
✓ Live site updated
```

**Deployed content:**
- game/ → Your playable game
- docs/ → All documentation
- README, guides → Info pages
- index.html → Auto-redirect to game

---

## 🎯 Integration Points

### GitHub Features Used:
```
┌─────────────────────────────────────┐
│        GitHub Features              │
│                                     │
│  ✓ Actions (CI/CD)                 │
│  ✓ Issues (Task tracking)          │
│  ✓ Pull Requests (Code review)     │
│  ✓ Labels (Organization)           │
│  ✓ Pages (Deployment)              │
│  ✓ Security (Scanning)             │
│  ✓ Dependabot (Updates)            │
└─────────────────────────────────────┘
```

### External Tools Integration:
```
┌─────────────────────────────────────┐
│      Available Integrations         │
│                                     │
│  ⏳ Zapier (automation)             │
│  ⏳ Discord (notifications)         │
│  ⏳ Slack (team chat)               │
│  ⏳ Trello (project mgmt)           │
│  ⏳ Email (updates)                 │
└─────────────────────────────────────┘
```

---

## 🔄 Multi-Repository Flow

### Testing AI Across Multiple Repos:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Repo 1     │     │   Repo 2     │     │   Repo 3     │
│  (Avalon)    │     │  (Other)     │     │  (Other)     │
└──────────────┘     └──────────────┘     └──────────────┘
       ↓                    ↓                    ↓
       └────────────────────┼────────────────────┘
                           ▼
              ┌─────────────────────────┐
              │   Access Method         │
              │                         │
              │  • Personal Access      │
              │    Token (Classic)      │
              │  • Fine-Grained PAT     │
              │  • GitHub App           │
              └─────────────────────────┘
                           ▼
              ┌─────────────────────────┐
              │   AI Automation         │
              │                         │
              │  • Read all repos       │
              │  • Write to all repos   │
              │  • Cross-repo refs      │
              │  • Coordinated updates  │
              └─────────────────────────┘
```

**Test protocol in:** `docs/MULTI_REPO_AI_TESTING.md`

---

## 📈 Workflow Execution Frequency

```
┌────────────────────┬──────────────┬──────────────┐
│     Workflow       │   Frequency  │   Duration   │
├────────────────────┼──────────────┼──────────────┤
│ Auto-assign Issues │ Per issue    │ ~10 seconds  │
│ PR Management      │ Per PR       │ ~15 seconds  │
│ ChoiceScript Tests │ Per push     │ ~30 seconds  │
│ Security Scanning  │ Weekly + PR  │ ~2 minutes   │
│ Pages Deployment   │ Per push     │ ~1 minute    │
│ Jekyll CI          │ Per push     │ ~30 seconds  │
└────────────────────┴──────────────┴──────────────┘
```

---

## 🎮 Game-Specific Automation

### Content Pipeline:
```
Writer Updates Lore
       ↓
Commits to lore/ directory
       ↓
Git push
       ↓
Triggers workflows:
  • Security scan (check for sensitive data)
  • Jekyll build (update docs)
  • Auto-label PR (add 'lore' label)
       ↓
Merge to main
       ↓
Deploy to GitHub Pages
       ↓
✓ Lore publicly available
```

### Scene Development:
```
Add New Scene
       ↓
Edit choicescript_game/scenes/newscene.txt
       ↓
Git push
       ↓
Triggers workflows:
  • ChoiceScript Tests (validate scene)
  • Security scan (check code)
  • PR Management (label & size)
       ↓
Tests pass
       ↓
Review & approve
       ↓
Merge to main
       ↓
Deploy to Pages
       ↓
✓ New scene live
```

---

## 🔐 Security Flow

```
Code Committed
      ↓
┌─────────────┐
│  CodeQL     │ → Scans for vulnerabilities
└─────────────┘
      ↓
┌─────────────┐
│ TruffleHog  │ → Detects secrets
└─────────────┘
      ↓
┌─────────────┐
│ Dep Review  │ → Checks dependencies
└─────────────┘
      ↓
┌─────────────┐
│ File Check  │ → Validates files
└─────────────┘
      ↓
  All Pass?
   ↙     ↘
 Yes     No
  ↓       ↓
Merge   Block & Alert
```

---

## 📊 Status Dashboard

### Current Automation Status:

```
✅ ACTIVE:
├─ Issue auto-assignment
├─ PR labeling
├─ Content validation
├─ Security scanning
└─ Documentation builds

⏳ READY (needs user action):
├─ GitHub Pages deployment
├─ Dependabot alerts
└─ Branch protection

🔄 CONFIGURABLE:
├─ Notification targets
├─ Label patterns
├─ Test criteria
└─ Deployment settings
```

---

## 🎊 Success Indicators

When automation is working correctly, you'll see:

✅ **On Issue Creation:**
- Issue automatically assigned to you
- Labels applied based on content
- Welcome comment added
- Visible in Actions tab

✅ **On Pull Request:**
- Size label applied immediately
- Content labels added
- PR checklist verified
- Tests run automatically

✅ **On Push to Main:**
- Security scans complete
- Tests validate content
- Site deploys to Pages
- All checks pass

✅ **Weekly:**
- Security scan runs Monday 00:00 UTC
- Results in Actions tab
- Alerts if issues found

---

## 🔧 Customization Points

You can customize:

1. **Issue Assignment** → Edit `.github/workflows/auto-assign-issues.yml`
   - Change assignee
   - Modify label keywords
   - Customize welcome message

2. **PR Management** → Edit `.github/workflows/pr-management.yml`
   - Adjust size thresholds
   - Add new content categories
   - Change label colors

3. **Security Scanning** → Edit `.github/workflows/security-scanning.yml`
   - Add more security tools
   - Adjust scan frequency
   - Customize alert levels

4. **Deployment** → Edit `.github/workflows/deploy-pages.yml`
   - Change what gets deployed
   - Modify landing page
   - Add build steps

---

**All workflows are documented in their respective YAML files.**

**See `docs/GITHUB_ORGANIZATION_SETUP.md` for full configuration guide.**

*Last updated: November 2025*
