# Branch Protection and Merge Review Requirements

This document describes the review and approval requirements for all pull requests in the Aethromoor repository.

## Overview

All pull requests to the main branch require review and approval before they can be merged. This ensures code quality, maintains project consistency, and provides opportunities for knowledge sharing.

## Review Requirements

### For Pull Requests from External Contributors

1. **Automatic Review Request**: When a PR is opened, code owners (defined in `.github/CODEOWNERS`) are automatically requested for review
2. **Approval Required**: At least one approval from @issdandavis is required before merging
3. **Status Checks**: All automated tests and checks must pass
4. **Labels**: PRs are automatically labeled:
   - `awaiting-review` - When first opened and needs review
   - `approved-for-merge` - When approved and ready to merge

### For Pull Requests from Repository Owner (@issdandavis)

- **Auto-approved**: PRs from the owner are automatically approved
- **Can merge immediately** after automated checks pass
- This streamlines the workflow for the primary maintainer

## Workflow Process

### 1. Opening a Pull Request

When you open a PR:
- The PR review workflow automatically triggers
- Code owners are notified and requested for review
- An automated comment is added explaining the review process
- The `awaiting-review` label is added

### 2. During Review

- Reviewers will examine your code, documentation, and tests
- You may receive feedback or requests for changes
- Update your PR by pushing new commits to your branch
- The review process repeats for significant changes

### 3. After Approval

- Once approved, the `approved-for-merge` label is added
- The `awaiting-review` label is removed
- The PR can be merged by a maintainer
- Automated checks must still pass

### 4. Stale PR Reminders

- PRs waiting for review for more than 24 hours get automatic reminders
- This helps ensure timely reviews and keeps development moving

## Setting Up Branch Protection Rules

**Note**: Branch protection rules must be configured through GitHub's web interface by a repository administrator.

### Recommended Settings for Main Branch

To fully enforce these requirements, configure the following on the `main` branch:

1. **Navigate to**: Repository Settings → Branches → Branch protection rules
2. **Add rule for**: `main`
3. **Configure**:
   - ✅ Require a pull request before merging
   - ✅ Require approvals: 1
   - ✅ Dismiss stale pull request approvals when new commits are pushed
   - ✅ Require review from Code Owners
   - ✅ Require status checks to pass before merging
   - ✅ Require branches to be up to date before merging
   - ✅ Include administrators (optional, for strictest security)

4. **Status checks to require**:
   - Any CI/CD workflows (e.g., `ChoiceScript Tests`, `Build Check`)
   - Security scanning (if configured)
   - Linting and code quality checks

### Optional: Additional Protection

For extra security:
- ✅ Require signed commits
- ✅ Require linear history
- ✅ Lock branch (prevents any direct pushes)
- ✅ Do not allow bypassing the above settings

## Code Owners

Code owners are automatically requested to review PRs that touch files they own. See `.github/CODEOWNERS` for the current ownership mapping.

Current code owners:
- **@issdandavis**: All files (default owner)

## Labels

The review workflow uses these labels to track PR status:

| Label | Meaning |
|-------|---------|
| `awaiting-review` | PR needs review from code owner |
| `approved-for-merge` | PR has been approved and can be merged |

## Automated Workflows

### PR Review Requirements (`pr-review-requirements.yml`)

- Triggers on PR open, sync, and review events
- Checks review status for non-owner PRs
- Adds helpful comments and labels
- Sends reminders for stale PRs

### Auto-Approve Workflows (`auto-approve-workflows.yml`)

- Auto-approves PRs from the repository owner (@issdandavis)
- Enables workflow runs for enterprise accounts
- Streamlines the owner's workflow

## For Contributors

### Before Creating a PR

1. Ensure your code follows the project's style guidelines
2. Add or update tests as appropriate
3. Update documentation for any new features
4. Test your changes locally
5. Review your own changes first

### Writing Good PR Descriptions

Use the PR template to provide:
- Clear summary of changes
- Link to related issues
- Description of what was changed and why
- Any next steps or follow-up work needed

### Responding to Reviews

- Be responsive to reviewer feedback
- Ask questions if feedback is unclear
- Make requested changes promptly
- Update your PR with clear commit messages
- Request re-review after making changes

## For Reviewers

### Review Checklist

- [ ] Code is clear and well-documented
- [ ] Changes match the described purpose
- [ ] No obvious bugs or security issues
- [ ] Tests are included and pass
- [ ] Documentation is updated
- [ ] Follows project conventions and style
- [ ] Lore/narrative consistency (for game content)
- [ ] No secrets or sensitive data exposed

### Providing Feedback

- Be constructive and specific
- Explain the "why" behind suggestions
- Distinguish between required changes and nice-to-haves
- Acknowledge good work
- Use GitHub's suggestion feature for specific code changes

## Emergency Procedures

### Critical Bug Fixes

For critical security or bug fixes:
1. Mark the PR with `priority:critical` label
2. Notify reviewers via @mention
3. Reviewers will prioritize these PRs
4. Can be fast-tracked if necessary

### Hotfix Process

For urgent production issues:
1. Create branch from `main`
2. Make minimal fix
3. Open PR with `hotfix` label
4. Request expedited review
5. Merge after approval and checks pass

## Questions or Issues?

If you have questions about the review process:
- Check this documentation first
- Review the [Contributing Guide](../../CONTRIBUTING.md)
- Ask in your PR comments
- Open a discussion or issue

---

## Related Files

- `.github/CODEOWNERS` - Defines code ownership
- `.github/workflows/pr-review-requirements.yml` - Review workflow
- `.github/workflows/auto-approve-workflows.yml` - Auto-approval for owner
- `.github/pull_request_template.md` - PR template

---

*Last updated: 2025*
*This document ensures quality and consistency across all contributions to the Aethromoor project.*
