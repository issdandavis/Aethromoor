# Quick Setup: Branch Protection Rules

This is a quick-reference guide for setting up branch protection rules through the GitHub web interface.

## Setup Instructions (5 minutes)

### Step 1: Navigate to Branch Protection Settings

1. Go to your repository on GitHub
2. Click **Settings** (top navigation)
3. Click **Branches** (left sidebar)
4. Under "Branch protection rules", click **Add rule**

### Step 2: Configure Main Branch Protection

**Branch name pattern**: `main`

#### Protect Matching Branches

✅ **Require a pull request before merging**
   - ✅ Require approvals: **1**
   - ✅ Dismiss stale pull request approvals when new commits are pushed
   - ✅ Require review from Code Owners

✅ **Require status checks to pass before merging**
   - ✅ Require branches to be up to date before merging
   - Search for and select any required status checks:
     - `check-review-status` (from pr-review-requirements workflow)
     - Any other CI/CD checks you want to require

⬜ **Require conversation resolution before merging** (optional but recommended)

⬜ **Require signed commits** (optional, for extra security)

⬜ **Require linear history** (optional, prevents merge commits)

⬜ **Include administrators** (optional, applies rules to admins too)

#### Rules Applied to Everyone

⬜ **Allow force pushes** (leave unchecked)

⬜ **Allow deletions** (leave unchecked)

### Step 3: Save

Click **Create** or **Save changes**

## What This Does

With these settings:
- No one can push directly to `main` (all changes via PR)
- All PRs require at least 1 approval from a code owner
- Code owners are automatically requested for review
- Status checks must pass before merging
- Stale approvals are dismissed when new commits are pushed

## Verification

To verify it's working:

1. Create a test branch
2. Make a small change
3. Open a pull request to `main`
4. You should see:
   - Review required from code owners
   - Status checks running
   - Merge button disabled until approved

## For Owner (@issdandavis)

The `auto-approve-workflows.yml` will automatically approve your own PRs, so you can still merge quickly while requiring reviews from external contributors.

## Troubleshooting

**"Status check not found"**
- The workflow must run at least once before it appears in the list
- Create a test PR to trigger it, then add it to required checks

**"Can't require Code Owners review"**
- Ensure `.github/CODEOWNERS` file exists and is correctly formatted
- Code owner must have write access to the repository

**"Rules don't seem to apply"**
- Check that the branch name pattern matches exactly (`main`)
- Verify your role has the restrictions (if "Include administrators" is checked)
- It may take a moment for rules to take effect

## Additional Resources

- [GitHub Docs: About Branch Protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [Full Branch Protection Guide](BRANCH_PROTECTION_GUIDE.md)
- [Contributing Guide](../CONTRIBUTING.md)

---

*This is a companion to the automated workflows in `.github/workflows/pr-review-requirements.yml`*
