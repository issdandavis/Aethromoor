# Multi-Repository AI Automation Guide
## Testing AI Access Across Multiple GitHub Repositories

This guide helps you test and verify that AI automation can access and work with multiple GitHub repositories simultaneously.

---

## 🎯 Testing Objectives

### What We're Testing:
1. **Repository Access** - Can AI access all repositories?
2. **Cross-Repo Operations** - Can AI coordinate across repos?
3. **Automation Consistency** - Do workflows work the same everywhere?
4. **Permission Management** - Are permissions configured correctly?

---

## 📋 Pre-Test Checklist

### Required Setup:
- [ ] Identify all repositories to test (you mentioned 3-4 repos)
- [ ] Verify GitHub access credentials
- [ ] Confirm permission levels on each repo
- [ ] Document current automation setup
- [ ] Create test plan for each repository

### Information to Gather:
```
Repository 1: [Name]
- Purpose: [What is it for?]
- Access Level: [Owner/Admin/Write/Read]
- Current Automation: [Yes/No - what kind?]

Repository 2: [Name]
- Purpose: [What is it for?]
- Access Level: [Owner/Admin/Write/Read]
- Current Automation: [Yes/No - what kind?]

Repository 3: [Name]
- Purpose: [What is it for?]
- Access Level: [Owner/Admin/Write/Read]
- Current Automation: [Yes/No - what kind?]

Repository 4: [Name] (if applicable)
- Purpose: [What is it for?]
- Access Level: [Owner/Admin/Write/Read]
- Current Automation: [Yes/No - what kind?]
```

---

## 🔑 Access Methods for Multi-Repo Automation

### Method 1: Personal Access Token (Classic)
**Best for: Individual developers managing multiple personal repos**

**Setup:**
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes:
   - `repo` (full repository access)
   - `workflow` (manage GitHub Actions)
   - `read:org` (if using organization)
4. Copy token and store securely
5. Use in automation tools (Zapier, custom scripts, etc.)

**Pros:**
- Works across all your repositories
- Simple setup
- Good for personal use

**Cons:**
- High privilege level (all repos)
- No fine-grained control
- Expires (need rotation)

### Method 2: Fine-Grained Personal Access Token (NEW)
**Best for: Security-conscious setups**

**Setup:**
1. Go to GitHub Settings → Developer settings → Personal access tokens → Fine-grained tokens
2. Generate new token
3. Select specific repositories
4. Choose permissions per resource type:
   - Contents: Read/Write
   - Issues: Read/Write
   - Pull requests: Read/Write
   - Workflows: Read/Write
5. Set expiration date (max 1 year)
6. Copy token and store securely

**Pros:**
- Specific repository access only
- Granular permissions
- Better security
- Mandatory expiration

**Cons:**
- More complex setup
- Need to update when adding repos
- Relatively new (fewer tool integrations)

### Method 3: GitHub App
**Best for: Team automation and production systems**

**Setup:**
1. Settings → Developer settings → GitHub Apps → New GitHub App
2. Configure:
   - Name: "Avalon AI Automation"
   - Homepage URL: Your GitHub profile or repo
   - Webhook: Optional (for real-time events)
3. Set permissions:
   - Repository permissions (as needed)
   - Organization permissions (if applicable)
4. Install on repositories
5. Generate private key
6. Use App ID + Private key for authentication

**Pros:**
- Best security model
- Scoped to specific repositories
- Auditable actions
- No expiration
- Can act as itself (not as you)

**Cons:**
- Most complex setup
- Requires server for webhook handling
- Overkill for simple use cases

---

## 🧪 Testing Protocol

### Phase 1: Individual Repository Tests

**Test Each Repository Separately:**

#### Test 1: Read Access
```bash
# Can AI read repository contents?
- List files in repository
- Read README.md
- Access issue list
- View workflow runs
```

**Expected Result:** ✅ All content accessible

#### Test 2: Write Access
```bash
# Can AI make changes?
- Create a branch
- Add/edit a file
- Create a commit
- Push to repository
```

**Expected Result:** ✅ Changes pushed successfully

#### Test 3: Issue Management
```bash
# Can AI work with issues?
- List existing issues
- Create new issue
- Comment on issue
- Apply labels
- Close issue
```

**Expected Result:** ✅ All operations successful

#### Test 4: Pull Request Operations
```bash
# Can AI work with PRs?
- List pull requests
- Create pull request
- Comment on PR
- Request review
- Merge PR (if permissions allow)
```

**Expected Result:** ✅ All operations successful

#### Test 5: Workflow Triggers
```bash
# Can AI trigger workflows?
- Trigger workflow_dispatch
- View workflow run results
- Download artifacts
- Read logs
```

**Expected Result:** ✅ Workflows trigger and accessible

### Phase 2: Cross-Repository Tests

**Test Coordination Across Repositories:**

#### Test 6: Multi-Repo Operations
```bash
# Can AI work with multiple repos simultaneously?
Task: Create issues in all repositories
Expected: Issues created in all repos with consistent formatting
```

#### Test 7: Cross-Repository References
```bash
# Can AI reference content across repos?
Task: Create PR in Repo 1 that references issue in Repo 2
Expected: Cross-repo link works correctly
```

#### Test 8: Consistent Automation
```bash
# Do similar workflows work the same way?
Task: Trigger same workflow type in all repos
Expected: Consistent behavior across all repositories
```

#### Test 9: Coordinated Updates
```bash
# Can AI make coordinated changes?
Task: Update README.md in all repos with consistent section
Expected: All READMEs updated with same pattern
```

---

## 📊 Test Results Template

### Repository Test Results

**Repository:** [Name]
**Date:** [Date of test]
**Access Method:** [Token type used]

| Test | Status | Notes |
|------|--------|-------|
| Read Access | ✅/❌ | |
| Write Access | ✅/❌ | |
| Issue Management | ✅/❌ | |
| PR Operations | ✅/❌ | |
| Workflow Triggers | ✅/❌ | |

**Overall Score:** X/5 tests passed

### Multi-Repo Test Results

| Test | Repo 1 | Repo 2 | Repo 3 | Repo 4 | Status |
|------|--------|--------|--------|--------|--------|
| Multi-Repo Operations | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Cross-Repo References | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Consistent Automation | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Coordinated Updates | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |

---

## 🔧 Configuration Examples

### Zapier Multi-Repo Configuration

**Example Zap: "Update All Repos on New Release"**

```
Trigger: GitHub - New Release (Repo 1)
↓
Action 1: GitHub - Create Issue (Repo 2)
  Title: "Update for {{release.name}}"
  Body: "New version released in main repo"
↓
Action 2: GitHub - Create Issue (Repo 3)
  [Same as Action 1]
↓
Action 3: GitHub - Create Issue (Repo 4)
  [Same as Action 1]
```

### GitHub Actions Cross-Repo Workflow

**Example: Trigger workflow in another repo**

```yaml
name: Trigger Other Repos

on:
  push:
    branches: [ "main" ]

jobs:
  trigger-repos:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Repo 2
        uses: actions/github-script@v7
        with:
          github-token: ${{ secrets.CROSS_REPO_TOKEN }}
          script: |
            await github.rest.actions.createWorkflowDispatch({
              owner: 'YOUR_USERNAME',
              repo: 'repo-2',
              workflow_id: 'sync.yml',
              ref: 'main'
            });
      
      - name: Trigger Repo 3
        uses: actions/github-script@v7
        with:
          github-token: ${{ secrets.CROSS_REPO_TOKEN }}
          script: |
            await github.rest.actions.createWorkflowDispatch({
              owner: 'YOUR_USERNAME',
              repo: 'repo-3',
              workflow_id: 'sync.yml',
              ref: 'main'
            });
```

---

## 🚨 Troubleshooting Common Issues

### Issue: "Resource not accessible by integration"
**Cause:** Insufficient permissions
**Solution:** Check token scopes or App permissions

### Issue: "Repository not found"
**Cause:** Token doesn't have access to specific repo
**Solution:** 
- For classic PAT: Verify `repo` scope is enabled
- For fine-grained PAT: Add repository to allowed list
- For GitHub App: Install app on repository

### Issue: "Workflow dispatch failed"
**Cause:** Workflow doesn't exist or isn't configured for manual trigger
**Solution:** Add `workflow_dispatch:` to workflow triggers

### Issue: "Rate limit exceeded"
**Cause:** Too many API calls
**Solution:** 
- Use authenticated requests (higher limits)
- Implement exponential backoff
- Cache results where possible
- Consider GitHub Enterprise for unlimited API

### Issue: "Cross-repo references not working"
**Cause:** Using short-hand reference in wrong context
**Solution:** Use full reference format: `owner/repo#issue_number`

---

## 📈 Success Criteria

### Your multi-repo AI automation is successful when:

✅ **All repositories are accessible**
- AI can read from all repos
- AI can write to all repos (where permitted)
- No "access denied" errors

✅ **Operations are consistent**
- Same commands work the same way across repos
- Automation produces consistent results
- Error handling works uniformly

✅ **Cross-repo coordination works**
- Can reference issues/PRs across repos
- Can trigger workflows in other repos
- Can maintain related content in sync

✅ **Security is maintained**
- Permissions are minimal required
- Tokens are stored securely
- Audit trail is clear

✅ **Automation is reliable**
- Workflows run consistently
- Error recovery works
- Notifications are sent properly

---

## 🎯 Recommended Test Sequence

### Day 1: Setup & Individual Tests
1. Configure access method (choose token type)
2. Test read access on all repos
3. Test write access on all repos
4. Document any issues

### Day 2: Advanced Individual Tests
1. Test issue management on each repo
2. Test PR operations on each repo
3. Test workflow triggers on each repo
4. Create test results document

### Day 3: Cross-Repo Tests
1. Test multi-repo operations
2. Test cross-repo references
3. Test coordinated updates
4. Verify consistency

### Day 4: Automation Setup
1. Implement chosen automation (Zapier/Actions)
2. Test end-to-end workflows
3. Verify notifications
4. Document configuration

### Day 5: Production Validation
1. Run full test suite again
2. Verify all success criteria
3. Create runbook for maintenance
4. Plan for ongoing monitoring

---

## 📝 Test Execution Template

### For Each Repository:

**Repository Name:** ________________

**Test Date:** ________________

**Tester:** ________________

**Access Method:** ☐ Classic PAT  ☐ Fine-grained PAT  ☐ GitHub App

**Tests:**

1. ☐ List repository files
2. ☐ Read README.md
3. ☐ Create test branch
4. ☐ Create test file
5. ☐ Commit changes
6. ☐ Push to repository
7. ☐ Create issue
8. ☐ Comment on issue
9. ☐ Add labels
10. ☐ Create pull request
11. ☐ Comment on PR
12. ☐ Trigger workflow
13. ☐ View workflow results

**Notes:**
________________________________
________________________________
________________________________

**Overall Result:** ☐ Pass  ☐ Fail  ☐ Partial

---

## 🔄 Ongoing Maintenance

### Weekly Tasks:
- [ ] Review automation logs
- [ ] Check for failed workflows
- [ ] Verify token hasn't expired
- [ ] Test critical paths

### Monthly Tasks:
- [ ] Full test suite run
- [ ] Review and update documentation
- [ ] Rotate credentials (if needed)
- [ ] Update automation for new features

### Quarterly Tasks:
- [ ] Comprehensive security audit
- [ ] Review access permissions
- [ ] Update automation patterns
- [ ] Plan improvements

---

## 📚 Additional Resources

### GitHub API Documentation
- [REST API](https://docs.github.com/en/rest)
- [GraphQL API](https://docs.github.com/en/graphql)
- [Webhooks](https://docs.github.com/en/webhooks)

### Automation Tools
- [GitHub Actions](https://docs.github.com/en/actions)
- [Zapier GitHub Integration](https://zapier.com/apps/github/integrations)
- [Octokit (GitHub API client)](https://github.com/octokit)

### Security Best Practices
- [Token Security](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure)
- [GitHub Apps Best Practices](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/best-practices-for-creating-a-github-app)

---

## 🎊 Next Steps After Testing

Once all tests pass:

1. **Document your configuration**
   - Token types used
   - Permissions granted
   - Repository access list

2. **Set up monitoring**
   - Workflow run notifications
   - Error alerting
   - Usage tracking

3. **Create runbooks**
   - How to add new repository
   - How to rotate credentials
   - How to troubleshoot issues

4. **Share with team**
   - Training documentation
   - Access procedures
   - Best practices

---

**You're now ready to test AI automation across all your GitHub repositories!**

*This guide is specific to testing multi-repo AI access for the Avalon project and related repositories.*

*Last updated: November 2025*
