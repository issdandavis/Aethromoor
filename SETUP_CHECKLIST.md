# ✅ Enterprise Setup Quickstart Checklist

**For:** Solo developer setting up professional development environment  
**Time:** ~30-60 minutes  
**Result:** Fully functional enterprise-style workflow

---

## 🚀 DO THIS FIRST (5 minutes)

### 1. Add Your Second GitHub Account
```
□ Go to: https://github.com/issdandavis/Avalon/settings/access
□ Click "Add people"
□ Enter your second GitHub account email
□ Grant "Maintain" or "Admin" access
□ Accept invitation on Account #2
```

### 2. Verify Repository Access
```
□ Log in with Account #2
□ Visit: https://github.com/issdandavis/Avalon
□ Confirm you can see repository
□ Test: Create a test issue and close it
```

---

## ⚙️ LOCAL SETUP (10 minutes)

### 3. Clone Repository (Both Accounts)

**On Main Machine (Account #1):**
```bash
cd ~/projects  # or your projects folder
git clone https://github.com/issdandavis/Avalon.git
cd Avalon
git config user.name "Your Name"  # ← Replace with your actual name
git config user.email "your.email@example.com"  # ← Replace with your Account #1 email
```

**On Secondary Machine/Profile (Account #2) - OPTIONAL:**
```bash
cd ~/projects
git clone https://github.com/issdandavis/Avalon.git
cd Avalon
git config user.name "Your Name (Org)"  # ← Replace with your name
git config user.email "your.other.email@example.com"  # ← Replace with your Account #2 email
```

### 4. Set Up Environment Variables
```bash
□ cp config/.env.example config/.env
□ Edit config/.env with your API keys:
  - ANTHROPIC_API_KEY (if using Claude)
  - OPENAI_API_KEY (if using ChatGPT)
  - GITHUB_TOKEN (for automation - optional)
□ Save and close
□ Verify .env is in .gitignore
```

---

## 🔧 GITHUB CONFIGURATION (15 minutes)

### 5. Enable Branch Protection
```
□ Go to: Settings → Branches
□ Click "Add rule"
□ Branch name pattern: main
□ Check:
  ✓ Require a pull request before merging
  ✓ Require approvals: 1
  ✓ Dismiss stale approvals when new commits are pushed
  ✓ Require status checks to pass before merging
□ Save changes
```

### 6. Create GitHub Project Board
```
□ Go to: Projects → New project
□ Choose: "Board" template
□ Name: "Avalon Development Tracker"
□ Create columns:
  - 📥 Backlog
  - 🎯 Phase 2: ChoiceScript
  - 🔨 In Progress
  - 👀 Review
  - 🧪 Testing
  - ✅ Done
□ Click "Create"
```

### 7. Enable GitHub Actions
```
□ Go to: Settings → Actions → General
□ Select: "Allow all actions and reusable workflows"
□ Check: "Allow GitHub Actions to create and approve pull requests"
□ Save
```

---

## 📝 CREATE INITIAL ISSUES (10 minutes)

### 8. Add Issues from Roadmap

Create these issues (use GitHub web interface):

**Issue #1: Complete Singing Dunes Expansion**
```
Title: Complete Singing Dunes Expedition
Labels: priority, choicescript, phase-2
Assignee: Account #1
Description:
Convert HTML Singing Dunes content to ChoiceScript format.

Tasks:
- [ ] Create 15-20 scenes (500+ lines)
- [ ] Implement truth-testing mechanics
- [ ] Add Kael character interactions
- [ ] Connect to Truthbound Mage ending
- [ ] Test all branches

Reference: game/game.js for content
Template: choicescript_game/scenes/first_lesson.txt
```

**Issue #2: Implement Verdant Tithe**
```
Title: Complete Verdant Tithe Expedition
Labels: choicescript, phase-2
Assignee: Account #2
Description: Create sentient forest expedition scenes
```

**Issue #3: Implement Rune Glacier**
```
Title: Complete Rune Glacier Expedition
Labels: choicescript, phase-2
Description: Create living ice expedition with control/harmony paths
```

**Issue #4: Write All 14 Endings**
```
Title: Implement All 14 Game Endings
Labels: narrative, phase-2
Description: Write 30-50 lines for each ending
```

### 9. Add Issues to Project Board
```
□ Go to your Project board
□ Add all 4 issues to "Phase 2: ChoiceScript" column
□ Move Issue #1 to "In Progress"
□ Others stay in "Phase 2" column
```

---

## 🤖 VERIFY AI SETUP (5 minutes)

### 10. Check GitHub Copilot Agent
```
□ Open VS Code in Avalon folder
□ Open any .md or .txt file
□ Start typing about Avalon or Polly
□ Verify Copilot suggests context-aware content
□ Check: .github/agents/my-agent.agent.md exists
```

### 11. Test AI Coordination Files
```
□ Open STATUS_CONTEXT.md
□ Read current status
□ Open SCENE_PARITY_CHECKLIST.md
□ Understand scene conversion status
□ Open STATS_MATRIX.md
□ Review stat balance information
```

---

## 🎯 FIRST WORKFLOW TEST (10 minutes)

### 12. Create Your First Feature Branch
```bash
cd ~/projects/Avalon
git checkout -b test/enterprise-setup-complete
```

### 13. Make a Test Change
```bash
# Edit STATUS_CONTEXT.md - add your name under "Current Work Status"
nano STATUS_CONTEXT.md

# Add a line like:
# - **Setup Complete:** [Your Name] verified enterprise environment

# Save and exit
```

### 14. Commit and Push
```bash
git add STATUS_CONTEXT.md
git commit -m "Docs: Verified enterprise setup complete"
git push origin test/enterprise-setup-complete
```

### 15. Create Pull Request
```
□ Go to: https://github.com/issdandavis/Avalon/pulls
□ Click "Compare & pull request"
□ Title: "Test: Enterprise Setup Verification"
□ Description: "Testing dual-account PR workflow"
□ Create pull request
```

### 16. Review and Merge (Account #2)
```
□ Switch to Account #2 (new browser tab/profile)
□ Go to the PR
□ Click "Files changed"
□ Review changes
□ Click "Review changes" → Approve
□ Add comment: "LGTM! Setup verified ✅"
□ Submit review
```

### 17. Merge (Account #1)
```
□ Switch back to Account #1
□ Go to the PR
□ See the approval from Account #2
□ Click "Merge pull request"
□ Confirm merge
□ Delete branch
```

### 18. Update Local Repository
```bash
git checkout main
git pull origin main
git branch -d test/enterprise-setup-complete
```

---

## 🎉 VERIFICATION (5 minutes)

### 19. Confirm Everything Works

**Check these are true:**
```
✓ Account #2 has access to repository
✓ Branch protection enabled on main
✓ Can't push directly to main without PR
✓ PRs require Account #2 approval
✓ GitHub Actions enabled
✓ Project board created with issues
✓ AI coordination files exist
✓ .env file created (not committed)
✓ First PR successfully completed
✓ GitHub Copilot aware of project
```

**If all ✓, you're done! 🎊**

---

## 📚 DAILY WORKFLOW REFERENCE

### Every Development Session:

**1. Start (2 min)**
```bash
git pull origin main
cat STATUS_CONTEXT.md  # Read current status
```

**2. Work (varies)**
```bash
git checkout -b feature/your-feature-name
# Make changes
# Use AI assistants (Copilot, Claude, etc.)
# Test locally
```

**3. Commit (2 min)**
```bash
git add .
git commit -m "Convert: Added singing dunes scenes"
git push origin feature/your-feature-name
```

**4. PR & Review (5 min)**
```
- Create PR on GitHub
- Switch to Account #2
- Review and approve
- Switch to Account #1
- Merge PR
- Update project board
```

**5. End (1 min)**
```bash
git checkout main
git pull origin main
# Update STATUS_CONTEXT.md with tomorrow's plan
```

---

## 🆘 TROUBLESHOOTING

### "Can't push to main"
✅ **Expected behavior!** Branch protection is working.  
**Solution:** Create a feature branch and PR instead.

### "Account #2 can't see repository"
❌ **Problem:** Invitation not accepted  
**Solution:** Check Account #2 email for invitation

### "Copilot doesn't know about Avalon"
❌ **Problem:** Not using workspace context  
**Solution:** Open entire Avalon folder in VS Code, not individual files

### "GitHub Actions not running"
❌ **Problem:** Actions disabled  
**Solution:** Settings → Actions → Enable

---

## 📖 NEXT STEPS

**After Setup Complete:**

1. Read: `ENTERPRISE_SETUP_GUIDE.md` (full documentation)
2. Review: `.github/COPILOT_INSTRUCTIONS.md` (AI guide)
3. Check: `docs/PROJECT_ROADMAP.md` (Phase 2 tasks)
4. Start: Issue #1 - Singing Dunes expansion

**Your First Real Task:**
```
□ Create branch: feature/singing-dunes-expansion
□ Open: choicescript_game/scenes/singing_dunes.txt
□ Reference: game/game.js for content
□ Use: .github/COPILOT_INSTRUCTIONS.md for format
□ Expand: From 12 lines to 500+ lines
□ Commit, PR, review, merge!
```

---

## 🎯 QUICK LINKS

**Repository:**
- Main: https://github.com/issdandavis/Avalon
- Settings: https://github.com/issdandavis/Avalon/settings
- Actions: https://github.com/issdandavis/Avalon/actions
- Projects: https://github.com/issdandavis/Avalon/projects

**Documentation:**
- Full Guide: `ENTERPRISE_SETUP_GUIDE.md`
- AI Instructions: `.github/COPILOT_INSTRUCTIONS.md`
- Project Roadmap: `docs/PROJECT_ROADMAP.md`
- Automation: `docs/AUTOMATION_GUIDE.md`

**Tracking Files:**
- Status: `STATUS_CONTEXT.md`
- Scenes: `SCENE_PARITY_CHECKLIST.md`
- Stats: `STATS_MATRIX.md`

---

## ✅ COMPLETION CHECKLIST

**You've successfully set up enterprise infrastructure when:**

- [x] Created ENTERPRISE_SETUP_GUIDE.md
- [x] Created STATUS_CONTEXT.md
- [x] Created SCENE_PARITY_CHECKLIST.md
- [x] Created STATS_MATRIX.md
- [ ] Added Account #2 as collaborator
- [ ] Enabled branch protection on main
- [ ] Created GitHub Project board
- [ ] Set up .env file locally
- [ ] Enabled GitHub Actions
- [ ] Created initial issues
- [ ] Completed first test PR workflow
- [ ] Verified AI assistants work

**When all checked, you're ready to develop! 🚀**

---

*"The spiral continues. Your enterprise is ready."*

**Total Setup Time:** 30-60 minutes  
**Complexity:** Beginner-friendly  
**Result:** Professional development environment

---

**Questions?** Refer to full guide: `ENTERPRISE_SETUP_GUIDE.md`
