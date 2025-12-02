# 🔧 REPOSITORY MAINTENANCE GUIDE

**Purpose:** Keep the Aethromoor repository organized, healthy, and efficient

---

## 📅 MAINTENANCE SCHEDULE

### Daily (Automated by AI)
✅ **Scene Writing** - Every 3 hours
- AI Scene Writer generates new content
- Auto-commits to repository

✅ **Content Polish** - Every 4 hours
- AI Content Polisher adds sensory details
- Improves narrative quality

✅ **Inbox Management** - Every 30 seconds
- Auto-replies to GitHub notifications
- Categorizes issues and PRs

✅ **System Validation** - Every 4 hours
- Enterprise monitoring validates all functions
- Health reports generated

### Weekly (Manual)
⏰ **System Health Check** (5 minutes)
```bash
# Check AI agent status
python .github/scripts/agent_manager_cli.py health

# Or open visual dashboard
open agent-dashboard.html
```

⏰ **Review Changelog** (10 minutes)
- Check `CHANGELOG.md` for AI-generated updates
- Verify changes are appropriate
- Roll back if needed

⏰ **Review Recent Commits** (10 minutes)
```bash
git log --oneline --since="7 days ago"
```

⏰ **Check Open Issues** (15 minutes)
- Review new issues
- Apply appropriate labels
- Respond to questions

⏰ **Review Pull Requests** (15 minutes)
- Check AI-generated PRs
- Merge approved changes
- Close stale PRs

### Monthly (Manual)
📅 **Repository Organization** (30 minutes)
- [ ] Clean up `archive/` if over 20 MB
- [ ] Review and update `docs/PROJECT_ROADMAP.md`
- [ ] Update `CHANGELOG.md` with monthly summary
- [ ] Review file organization in all directories

📅 **Documentation Review** (45 minutes)
- [ ] Update README.md if needed
- [ ] Review all top-level guides
- [ ] Check for broken links
- [ ] Update screenshots if UI changed

📅 **Label Management** (15 minutes)
- [ ] Review label usage
- [ ] Remove unused labels
- [ ] Update label descriptions
- [ ] Archive completed phase labels

📅 **Backup Verification** (10 minutes)
- [ ] Verify GitHub backups are working
- [ ] Check local clones are up to date
- [ ] Verify important files not in `.gitignore`

### Quarterly (Manual)
🗓️ **Deep Review** (2-3 hours)
- [ ] Full repository audit
- [ ] Review all automation workflows
- [ ] Update all documentation
- [ ] Plan next phase of development
- [ ] Archive completed phases
- [ ] Update project roadmap

🗓️ **Security Review** (1 hour)
- [ ] Rotate API keys if needed
- [ ] Review `.env.example` template
- [ ] Check for exposed secrets
- [ ] Verify workflow permissions
- [ ] Update dependencies

---

## 🧹 CLEANING TASKS

### When Archive Gets Large (>20 MB)
1. Review files in `archive/`
2. Delete truly unnecessary files
3. Compress remaining files into dated .zip
4. Keep only last 2 years of archives

### When Docs Get Cluttered
1. Review all files in `docs/`
2. Consolidate duplicate information
3. Move outdated docs to `docs/archive/`
4. Update table of contents

### When Root Gets Messy
1. Review all root-level files
2. Move detailed guides to `docs/`
3. Keep only essential entry points
4. Update `FILE_LOCATIONS.txt`

---

## 📊 HEALTH CHECKS

### Repository Health Indicators

#### ✅ Healthy Repository
- No merge conflicts
- All CI/CD workflows passing
- AI agents running on schedule
- Issues labeled and organized
- PRs reviewed within 1 week
- Documentation up to date
- File organization clear

#### ⚠️ Needs Attention
- 1-2 failing workflows
- Some unlabeled issues
- PRs older than 2 weeks
- Minor documentation gaps
- Slight file disorganization

#### ❌ Unhealthy Repository
- Multiple failing workflows
- Many unlabeled issues
- PRs older than 1 month
- Outdated documentation
- Major file disorganization
- Archive over 30 MB

### Quick Health Check Commands

```bash
# Check recent commits
git log --oneline -10

# Check repository status
git status

# Check for uncommitted changes
git diff

# List open issues (requires gh CLI)
gh issue list --state open

# List open PRs (requires gh CLI)
gh pr list --state open

# Check workflow status (requires gh CLI)
gh workflow list

# View recent workflow runs
gh run list --limit 10
```

---

## 🤖 AI WORKER MAINTENANCE

### Verify AI Workers Are Running

**Dashboard Check:**
```bash
open agent-dashboard.html
```

**CLI Check:**
```bash
python .github/scripts/agent_manager_cli.py health
```

### Common AI Worker Issues

#### Worker Not Running
**Symptom:** No recent commits from AI worker

**Solution:**
1. Check GitHub Actions tab
2. Verify `ANTHROPIC_API_KEY` is set
3. Re-run failed workflow
4. Check workflow logs

#### Worker Generating Bad Content
**Symptom:** Low-quality or incorrect content

**Solution:**
1. Review recent commits
2. Revert bad commit: `git revert <commit-hash>`
3. Adjust worker prompt in `.github/workflows/`
4. Monitor next generation

#### Worker Consuming Too Many API Calls
**Symptom:** High API usage

**Solution:**
1. Check workflow schedules
2. Reduce frequency if needed
3. Add rate limiting
4. Monitor usage

### Manual AI Worker Triggers

```bash
# Trigger Scene Writer manually
gh workflow run ai-scene-writer.yml

# Trigger Content Polisher manually
gh workflow run ai-content-polish.yml

# Trigger Stat Balancer manually
gh workflow run ai-stat-balancer.yml

# Trigger Game Tester manually
gh workflow run ai-game-tester.yml
```

---

## 📁 FILE ORGANIZATION CHECKLIST

### Monthly Review

#### ✅ lore/
- [ ] All files are lore-related
- [ ] No duplicates
- [ ] Files clearly named
- [ ] README.md up to date

#### ✅ writing_drafts/
- [ ] Latest manuscripts present
- [ ] Old versions moved to archive
- [ ] Files clearly named
- [ ] README.md up to date

#### ✅ game/
- [ ] Game is playable
- [ ] No broken scenes
- [ ] All assets present
- [ ] README.md up to date

#### ✅ choicescript_game/
- [ ] Scenes properly formatted
- [ ] No syntax errors
- [ ] Stats correctly defined
- [ ] README.md up to date

#### ✅ docs/
- [ ] Documentation current
- [ ] No outdated guides
- [ ] Links working
- [ ] README.md up to date

#### ✅ archive/
- [ ] Size under 20 MB
- [ ] Only historical files
- [ ] README.md explains contents

#### ✅ config/
- [ ] No exposed secrets
- [ ] .env.example up to date
- [ ] Templates current

#### ✅ .github/
- [ ] Workflows functioning
- [ ] Scripts working
- [ ] Documentation current

---

## 🏷️ LABEL HYGIENE

### Weekly Label Check
- [ ] All new issues labeled
- [ ] All new PRs labeled
- [ ] Priority labels applied
- [ ] Component labels applied
- [ ] Status labels updated

### Monthly Label Audit
- [ ] Remove unused labels
- [ ] Update label descriptions
- [ ] Archive phase labels when complete
- [ ] Check color consistency
- [ ] Update GITHUB_LABELS_GUIDE.md

---

## 📝 DOCUMENTATION MAINTENANCE

### Keep These Updated

#### After Major Changes
- [ ] README.md
- [ ] CHANGELOG.md
- [ ] docs/PROJECT_ROADMAP.md
- [ ] FILE_LOCATIONS.txt

#### Monthly
- [ ] REPOSITORY_INVENTORY.md
- [ ] docs/FEATURES_COMPLETE.md
- [ ] WORKFLOW_STATUS.md

#### Quarterly
- [ ] All root-level guides
- [ ] All docs/ documentation
- [ ] .github/ documentation
- [ ] Component READMEs

### Documentation Quality Check
- [ ] No broken links
- [ ] Screenshots current
- [ ] Examples work
- [ ] Dates updated
- [ ] TOC updated
- [ ] Grammar/spelling checked

---

## 🔐 SECURITY MAINTENANCE

### Monthly Security Check
- [ ] No API keys in code
- [ ] .env.example is template only
- [ ] Secrets in GitHub Secrets
- [ ] No sensitive data in commits
- [ ] Dependencies up to date

### Quarterly Security Audit
- [ ] Rotate API keys
- [ ] Review access permissions
- [ ] Check workflow permissions
- [ ] Review collaborator access
- [ ] Update security documentation

---

## 📈 GROWTH MANAGEMENT

### When Repository Gets Large (>100 MB)

1. **Analyze Size:**
```bash
du -sh * | sort -h
```

2. **Identify Large Files:**
```bash
find . -type f -size +1M -not -path "./.git/*"
```

3. **Clean Up:**
- Move large files to external storage
- Compress PDFs if possible
- Archive old versions
- Use Git LFS for large files if needed

### When Issue Count Gets High (>50 open)

1. **Triage:**
- Close stale issues (>6 months old)
- Merge duplicate issues
- Convert some to discussions

2. **Organize:**
- Apply better labels
- Create milestones
- Use project boards

3. **Delegate:**
- Mark good first issues
- Add help-wanted labels
- Create issue templates

---

## 🎯 QUICK MAINTENANCE COMMANDS

### Daily Quick Check (2 minutes)
```bash
# Pull latest changes
git pull

# Check status
git status

# View recent activity
git log --oneline -5

# Check if AI workers ran
git log --oneline --author="github-actions" --since="24 hours ago"
```

### Weekly Quick Check (5 minutes)
```bash
# Open dashboard
open agent-dashboard.html

# Check health
python .github/scripts/agent_manager_cli.py health

# List open issues
gh issue list --state open | wc -l

# List open PRs
gh pr list --state open | wc -l
```

### Monthly Quick Check (15 minutes)
```bash
# Full health check
python .github/scripts/agent_manager_cli.py health

# Repository size
du -sh .

# Archive size
du -sh archive/

# Check for large files
find . -type f -size +1M -not -path "./.git/*"

# Recent activity summary
git log --oneline --since="30 days ago" | wc -l
```

---

## 📞 TROUBLESHOOTING

### Common Issues

#### "Repository is messy"
**Solution:** Follow "File Organization Checklist" above

#### "AI workers not running"
**Solution:** Check GitHub Actions, verify API key

#### "Too many open issues"
**Solution:** Triage and close stale issues

#### "Documentation outdated"
**Solution:** Follow "Documentation Maintenance" schedule

#### "Repository too large"
**Solution:** Follow "Growth Management" steps

#### "Workflows failing"
**Solution:** Check workflow logs, fix errors

---

## ✅ MAINTENANCE CHECKLIST TEMPLATE

### Copy This for Monthly Review

```markdown
## Monthly Maintenance - [Month] [Year]

### System Health ✅
- [ ] AI agents running
- [ ] No failing workflows
- [ ] Repository under 100 MB
- [ ] Archive under 20 MB

### Organization ✅
- [ ] All issues labeled
- [ ] All PRs reviewed
- [ ] Files properly organized
- [ ] No duplicate files

### Documentation ✅
- [ ] README.md current
- [ ] CHANGELOG.md updated
- [ ] PROJECT_ROADMAP.md current
- [ ] FILE_LOCATIONS.txt current

### Security ✅
- [ ] No exposed secrets
- [ ] API keys rotated (if needed)
- [ ] Dependencies updated
- [ ] Permissions reviewed

### Notes:
[Add any observations or actions taken]
```

---

## 🎉 MAINTENANCE SUCCESS CRITERIA

Your repository is well-maintained if:

✅ **Organization (5/5)**
- Clear file structure
- Everything easy to find
- No duplicate files
- Good documentation

✅ **Health (5/5)**
- All workflows passing
- AI workers running
- No merge conflicts
- Recent activity

✅ **Documentation (5/5)**
- Up to date
- Complete
- Easy to understand
- No broken links

✅ **Security (5/5)**
- No exposed secrets
- Current dependencies
- Proper permissions
- Regular audits

✅ **Automation (5/5)**
- AI workers functioning
- Workflows running
- Auto-management working
- Good coverage

---

**Last Updated:** December 2, 2025  
**Review Frequency:** Monthly  
**Next Review:** January 2, 2026  

**Maintained By:** Repository maintainers + AI autonomous workers  
**Questions?** See CONTRIBUTING.md or open an issue
