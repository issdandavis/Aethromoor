# License Application Workflow Guide

This document explains how to use the automated workflow to apply the Apache 2.0 License to your other repositories.

## 📋 Prerequisites

Before using this workflow, you need to create a **Personal Access Token (PAT)** with the right permissions.

### Creating a Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Name it: `License Application Token`
4. Set expiration: 90 days (or your preference)
5. Select these scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (Update GitHub Action workflows)
6. Click "Generate token"
7. **Copy the token immediately** (you won't see it again!)

### Adding the Token to This Repository

1. Go to this repository's Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `PAT_TOKEN`
4. Value: Paste your Personal Access Token
5. Click "Add secret"

## 🚀 How to Use the Workflow

### Step 1: Navigate to Actions

1. Go to the "Actions" tab in this repository
2. Click on "Apply License to Other Repositories" in the left sidebar

### Step 2: Run the Workflow

1. Click the "Run workflow" button (top right)
2. You'll see two input fields:

#### Input 1: Repositories
Enter a comma-separated list of repositories you want to add the license to.

**Format:** `owner/repo-name` (e.g., `issdandavis/repo-name`)

**Examples:**
- Single repo: `issdandavis/my-project`
- Multiple repos: `issdandavis/project1,issdandavis/project2,issdandavis/project3`
- With spaces (ok): `issdandavis/repo1, issdandavis/repo2, issdandavis/repo3`

#### Input 2: Create PR instead of direct commit
- **Checked (default):** Creates a Pull Request in each repository (recommended)
- **Unchecked:** Commits the LICENSE file directly to the default branch

**Recommendation:** Leave this checked! It's safer to review PRs before merging.

### Step 3: Run and Monitor

1. Click the green "Run workflow" button
2. The workflow will start running
3. Click on the running workflow to see progress
4. Watch as it processes each repository

## 📊 What Happens

The workflow will:

1. ✅ Clone each target repository
2. ✅ Check if a LICENSE file already exists (skips if yes)
3. ✅ Copy the LICENSE file from this repository
4. ✅ Create a PR (or commit directly) with the license
5. ✅ Provide a summary of successes and failures

### If Creating PRs (Recommended)

For each repository, the workflow creates a PR with:
- **Title:** "Add Apache 2.0 License"
- **Description:** Full explanation of what's being added and why
- **Branch:** `add-apache-license-{timestamp}`

**You'll need to:**
1. Go to each repository
2. Review the PR
3. Merge it to activate the license

### If Committing Directly

The LICENSE file is committed immediately to the default branch.

**No further action needed** - the license is active immediately.

## 🎯 Example Usage

### Scenario: Add License to 3 Repositories

1. You have these repos:
   - `issdandavis/GameProject`
   - `issdandavis/WebApp`
   - `issdandavis/Tools`

2. Go to Actions → Apply License to Other Repositories → Run workflow

3. Enter in "Repositories" field:
   ```
   issdandavis/GameProject,issdandavis/WebApp,issdandavis/Tools
   ```

4. Leave "Create PR" checked

5. Click "Run workflow"

6. Wait for workflow to complete (usually 1-2 minutes)

7. Go to each repository and merge the PR

8. Done! All three repositories now have the Apache 2.0 License

## ⚠️ Important Notes

### What Gets Skipped

The workflow will **skip** repositories that:
- Already have a LICENSE file (to avoid overwriting)
- Cannot be accessed (permissions issue)
- Don't exist or are misspelled

### Token Permissions

Your PAT needs:
- Write access to the repositories you're targeting
- The `repo` and `workflow` scopes

If the workflow fails with "permission denied", check that:
1. The PAT is correctly added as `PAT_TOKEN` secret
2. The PAT has the right scopes
3. You have write access to the target repositories

### Private Repositories

This workflow works with both public and private repositories, as long as:
- Your PAT has access to private repos (`repo` scope)
- You own the repositories or have write access

## 🔍 Troubleshooting

### "Failed to clone repository"
- Check that the repository name is correct
- Verify you have access to the repository
- Ensure your PAT has the `repo` scope

### "LICENSE file already exists"
- The repository already has a license
- If you want to replace it, you'll need to do that manually

### "Permission denied"
- Your PAT may not have the right scopes
- You may not have write access to the repository
- Check that PAT_TOKEN secret is set correctly

### Workflow doesn't appear
- Make sure this workflow file is on your default branch
- Check that Actions are enabled in repository settings

## 📝 Quick Reference

**Workflow Location:** `.github/workflows/apply-license-to-repos.yml`

**Required Secret:** `PAT_TOKEN` (Personal Access Token with `repo` and `workflow` scopes)

**Input Format:** `owner/repo1,owner/repo2,owner/repo3`

**Recommended Setting:** Create PR = ✅ (checked)

## 🎓 Best Practices

1. **Start Small:** Test with 1-2 repositories first
2. **Use PRs:** Always use PR mode to review before merging
3. **Verify Access:** Make sure you can access all target repos
4. **Check Results:** Review the workflow logs for any errors
5. **Rotate Tokens:** Update your PAT every 90 days for security

## 📚 Related Documentation

- [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
- [GitHub Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [GitHub Actions Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

---

**Need Help?** Check the workflow run logs in the Actions tab for detailed error messages.
