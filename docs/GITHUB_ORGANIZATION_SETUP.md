# GitHub Organization Setup Guide
## Complete Guide for Team Collaboration & Automation

This guide covers all the GitHub organizational tasks mentioned in the overview, tailored for the Avalon project and multi-repository AI automation.

---

## 🎯 Quick Start Checklist

### Essential Setup (Complete These First)
- [x] Repository created and organized
- [x] Issue templates configured
- [x] Pull request template configured
- [x] Labels system established
- [ ] Team members invited (see below)
- [ ] Branch protection rules configured
- [ ] Automated security scanning enabled
- [ ] CI/CD workflows active
- [ ] Auto-assignment for issues configured

---

## 👥 INVITE YOUR PEOPLE

### Step 1: Find Team Members

**By GitHub Username:**
1. Go to repository Settings → Collaborators
2. Click "Add people"
3. Enter GitHub username
4. Select permission level
5. Send invite

**By Email Address:**
1. Same process as above
2. Enter email address instead
3. They'll receive invitation email

### Step 2: Permission Levels

**Choose the right level for each member:**

#### Read
- Can view and discuss
- Cannot make changes
- Good for: Playtesters, reviewers

#### Triage
- Can manage issues and pull requests
- Cannot push to repository
- Good for: Community managers, beta coordinators

#### Write
- Can push to non-protected branches
- Can merge approved pull requests
- Good for: Writers, content contributors

#### Maintain
- Can manage repository settings
- Cannot delete repository
- Good for: Project managers, lead developers

#### Admin
- Full access to repository
- Can delete repository
- Good for: Repository owners only

### Recommended Team Structure for Avalon:
```
Owner (You) → Admin
AI Assistants → Write access (via automation)
Content Writers → Write access
Beta Testers → Read access
Community Managers → Triage access
```

---

## 🔐 ENTERPRISE SECURITY

### Enable SAML Single Sign-On (Organization Feature)

**Note:** Requires GitHub Organization (not individual repo)

If upgrading to Organization:
1. Convert repository to organization
2. Settings → Security → SAML single sign-on
3. Connect identity provider (Google Workspace, Azure AD, etc.)
4. Test with one account first
5. Enforce for all members

**For Individual Repositories:**
- Use 2FA requirement instead
- Settings → Security → Require two-factor authentication
- All collaborators must enable 2FA

### Get Automatic Security Updates

**Enable Dependabot (FREE and recommended):**

1. Settings → Security & analysis
2. Enable "Dependency graph" ✅
3. Enable "Dependabot alerts" ✅
4. Enable "Dependabot security updates" ✅

**What This Does:**
- Automatically scans dependencies
- Alerts you to vulnerabilities
- Auto-creates PRs to fix issues
- Works with package.json, requirements.txt, etc.

### Get Alerts for Vulnerabilities

**Enable Code Scanning:**

1. Settings → Security & analysis
2. Enable "Code scanning" ✅
3. Choose "CodeQL Analysis" (free)
4. Commit the generated workflow file

**Enable Secret Scanning:**

1. Settings → Security & analysis
2. Enable "Secret scanning" ✅ (if available)
3. Automatically detects committed secrets
4. Prevents API key leaks

**Configure Security Advisories:**

1. Security tab → Advisories
2. Enable "Private vulnerability reporting"
3. Allows responsible disclosure
4. Get notified of security issues

---

## 🤝 COLLABORATIVE CODING

### Create Pull Request Workflow

**Current Status:** ✅ Template exists at `.github/pull_request_template.md`

**Best Practices:**
1. Always create feature branch first
2. Make focused, single-purpose changes
3. Fill out PR template completely
4. Link related issues
5. Request review before merging

**PR Template Sections:**
- Summary (what changed)
- Linked Issue (reference)
- Change Notes (before/after)
- AI Review (if applicable)

### Create Branch Protection Rules

**Recommended Configuration:**

1. Go to Settings → Branches
2. Add rule for `main` branch
3. Enable these protections:

**Essential Protections:**
```
✅ Require pull request before merging
  ✅ Require approvals (1 reviewer minimum)
  ✅ Dismiss stale reviews on new commits
  
✅ Require status checks to pass
  ✅ Require branches to be up to date
  
✅ Include administrators (enforce rules for all)

✅ Restrict who can push (optional for small teams)
```

**Advanced Protections:**
```
✅ Require conversation resolution before merging
✅ Require signed commits (for security)
✅ Require linear history (cleaner git log)
✅ Lock branch (prevent any changes - for releases)
```

**For Development Branch:**
- Less strict than main
- Allow direct pushes for rapid iteration
- Still require CI checks to pass

---

## ⚙️ AUTOMATION AND CI/CD

### Auto-Assign New Issues

**Create Issue Auto-Assignment Workflow:**

File: `.github/workflows/auto-assign-issues.yml`

This workflow will:
- Automatically assign new issues to team members
- Rotate assignments for balance
- Add labels based on issue content
- Notify assignees via Discord/Slack

### Run Continuous Integration Tests

**Current Status:** 
- ✅ Jekyll CI (for documentation)
- ⚠️ ChoiceScript tests (placeholder, needs implementation)

**Recommended CI Tests:**
1. **ChoiceScript Validation**
   - Quicktest (verify all paths work)
   - Randomtest (stress test choices)
   - Word count validation
   - Achievement verification

2. **Content Validation**
   - Spell check
   - Consistency checks
   - Link validation
   - File structure validation

3. **Game Balance Testing**
   - Stat tracking validation
   - Ending accessibility check
   - Choice consequence verification

### Publish Members-Only Website

**GitHub Pages Configuration:**

1. Settings → Pages
2. Source: Deploy from branch
3. Branch: `main` or `gh-pages`
4. Folder: `/docs` or `/ (root)`

**For Private Repository:**
- GitHub Pages only public on free tier
- Consider: Netlify, Vercel (free private deployments)
- Or: Keep repository public, game free

**Automated Deployment:**
- Current Jekyll workflow builds documentation
- Can add game deployment workflow
- Auto-deploy on merge to main

---

## 🔄 MULTI-REPOSITORY AI AUTOMATION

### Testing AI Across Multiple Repositories

**Strategy for Multi-Repo AI Access:**

#### Option 1: GitHub App (Recommended)
- Create custom GitHub App
- Grant access to all repositories
- Use App credentials for AI automation
- Scoped permissions per repository

#### Option 2: Personal Access Token
- Create classic PAT with repo scope
- Works across all your repositories
- Store in automation system (Zapier, etc.)
- Rotate regularly for security

#### Option 3: Fine-Grained Tokens (NEW)
- More secure than classic PAT
- Specific repository access
- Granular permissions
- Expiration dates

### Testing Checklist for AI Automation:

**Repository 1 (Avalon):**
- [ ] AI can read issues
- [ ] AI can create branches
- [ ] AI can create pull requests
- [ ] AI can update documentation
- [ ] AI can trigger workflows

**Repository 2 (If you have others):**
- [ ] Same permissions work across repos
- [ ] Automation can access both
- [ ] Cross-repo references work
- [ ] Unified workflow triggers

**Repository 3 & 4 (If applicable):**
- [ ] Test same features
- [ ] Verify permission consistency
- [ ] Check automation scalability

---

## 📋 RECOMMENDED GITHUB FEATURES

### GitHub Projects
**Set up project board:**
1. Projects tab → New project
2. Template: "Automated kanban"
3. Connect to issues and PRs
4. Columns: To Do, In Progress, Review, Done

### GitHub Discussions
**Enable for community:**
1. Settings → Features
2. Enable Discussions ✅
3. Categories: Announcements, Ideas, Q&A, Show and Tell

### GitHub Wiki
**For documentation:**
1. Settings → Features
2. Enable Wiki ✅
3. Use for: Lore, gameplay guides, worldbuilding

### GitHub Releases
**Version management:**
1. Code tab → Releases
2. Create release tags (v1.0, v1.1, etc.)
3. Attach compiled game files
4. Write release notes
5. Mark pre-releases for beta versions

---

## 🤖 AI AUTOMATION WORKFLOWS

### Recommended Automation Setup

**1. Issue Triage Bot**
```yaml
Trigger: New issue created
Actions:
  - Add labels based on content
  - Assign to team member (round-robin)
  - Add to project board
  - Notify in Discord
```

**2. PR Review Bot**
```yaml
Trigger: Pull request opened
Actions:
  - Run automated tests
  - Check for required reviews
  - Verify branch is up to date
  - Add size label (S/M/L/XL)
```

**3. Content Sync Bot**
```yaml
Trigger: Changes to lore/ directory
Actions:
  - Validate consistency
  - Update character databases
  - Notify writers
  - Create changelog entry
```

**4. Release Bot**
```yaml
Trigger: Tag pushed (v*)
Actions:
  - Create GitHub release
  - Build game files
  - Post to social media
  - Update documentation
  - Notify testers
```

---

## 🎮 AVALON-SPECIFIC WORKFLOWS

### Game Development Workflow

```
Lore Update → Writing → Scene Development → Testing → Release
     ↓            ↓             ↓              ↓         ↓
  (Validate) (Consistency) (Quicktest)  (Beta Test) (Publish)
```

### Automated Content Pipeline

1. **Lore Changes** (in `lore/`)
   - Trigger consistency check
   - Update character tracking
   - Notify game developers

2. **Scene Updates** (in `choicescript_game/scenes/`)
   - Run ChoiceScript tests
   - Verify stat tracking
   - Check for broken paths
   - Update word count

3. **Documentation Updates** (in `docs/`)
   - Build and deploy via Jekyll
   - Update project status
   - Sync with README

---

## 📊 METRICS & MONITORING

### What to Track

**Development Metrics:**
- Issues opened vs closed
- PR merge time
- Code review coverage
- Test pass rate
- Build success rate

**Content Metrics:**
- Word count by scene
- Number of endings
- Choice complexity
- Achievement coverage

**Community Metrics:**
- Contributor count
- Discussion engagement
- Bug report rate
- Feature request trends

### Tools to Use

**GitHub Insights (Built-in):**
- Contributors graph
- Commit activity
- Code frequency
- Pulse overview

**External Tools:**
- Codecov (test coverage)
- SonarCloud (code quality)
- Snyk (security scanning)
- Better Uptime (monitoring)

---

## 🔧 IMPLEMENTATION CHECKLIST

### Week 1: Foundation
- [ ] Invite first team member
- [ ] Set up branch protection on `main`
- [ ] Enable Dependabot alerts
- [ ] Create first project board

### Week 2: Automation
- [ ] Implement issue auto-assignment
- [ ] Set up CI tests for ChoiceScript
- [ ] Configure automated releases
- [ ] Add security scanning

### Week 3: Enhancement
- [ ] Enable Discussions
- [ ] Set up Wiki for lore
- [ ] Create automation workflows
- [ ] Document processes

### Week 4: Testing
- [ ] Test multi-repo AI access
- [ ] Verify all automations
- [ ] Train team on workflows
- [ ] Gather feedback and iterate

---

## 🆘 TROUBLESHOOTING

### Common Issues

**"I can't enable Dependabot"**
- Check if repository is private
- Verify you have admin access
- Try enabling dependency graph first

**"Branch protection isn't working"**
- Verify rule pattern matches branch name
- Check if "Include administrators" is enabled
- Ensure you have admin permissions

**"CI tests aren't running"**
- Check workflow file syntax
- Verify triggers are correct
- Look at Actions tab for errors
- Check if Actions are enabled

**"Can't invite collaborators"**
- Verify repository isn't organization-owned
- Check invitation didn't go to spam
- Try inviting by username instead of email

---

## 🚀 QUICK WINS

### Implement These Now for Immediate Value

1. **Enable Dependabot** (5 minutes)
   - Free security scanning
   - Auto-fix vulnerabilities
   - Zero maintenance

2. **Add Branch Protection** (10 minutes)
   - Prevent accidental changes
   - Require reviews
   - Maintain quality

3. **Set Up Auto-Assignment** (15 minutes)
   - Distribute work evenly
   - Never miss an issue
   - Clear ownership

4. **Create Project Board** (10 minutes)
   - Visual workflow
   - Track progress
   - Team transparency

---

## 📚 ADDITIONAL RESOURCES

### GitHub Documentation
- [GitHub Actions](https://docs.github.com/en/actions)
- [Branch Protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches)
- [Security Features](https://docs.github.com/en/code-security)
- [GitHub Apps](https://docs.github.com/en/apps)

### Community Resources
- [GitHub Community Forum](https://github.community/)
- [GitHub Skills](https://skills.github.com/)
- [GitHub Blog](https://github.blog/)

### Project-Specific
- See `AUTOMATION_GUIDE.md` for Zapier integration
- See `CONTRIBUTING.md` for contribution guidelines
- See `PROJECT_ROADMAP.md` for development status

---

## 🎊 SUCCESS METRICS

**You'll know your setup is working when:**
- ✅ Issues are automatically assigned
- ✅ All PRs require reviews
- ✅ Tests run on every commit
- ✅ Security alerts appear promptly
- ✅ Team collaborates smoothly
- ✅ Documentation stays current
- ✅ Releases are automated
- ✅ Multi-repo automation works seamlessly

---

**This guide is your complete reference for GitHub organization and automation.**

*Updated: November 2025*
*Branch: copilot/invite-first-member*
