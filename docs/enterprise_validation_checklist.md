# Enterprise automation and security validation checklist

This checklist captures the manual steps to confirm your GitHub Enterprise automation and security setup is aligned with the plan for the Avalon repository.

## Advanced Security policies (enterprise)
- Go to **Profile → Enterprise (or Enterprises → select your enterprise) → Policies → Advanced Security**.
- Confirm repo admins are allowed/blocked from toggling Secret Protection, GitHub Advanced Security, AI detection in secret scanning, and Copilot Autofix according to your enforcement plan.
- Adjust policies if they do not match the intended defaults for your organizations.

## GitHub Actions governance
- Document the allowed third-party actions policy (verified creators/whitelists vs. GitHub-only) and confirm it matches enterprise/org settings.
- In an example org, open **Settings → Actions** and verify allowed actions, required verification, and runner strategy (GitHub-hosted vs. self-hosted, including any private networking such as Azure VNET).
- Ensure audit log/exporting is configured with the retention you need for Actions activity.

## Required workflow enforcement (rulesets)
- If a workflow must pass before merging (e.g., dependency review), create or update a branch ruleset: **Organization → Settings → Repository → Rulesets → Create/Edit → Enforcement: Active → Require workflows to pass before merging**.
- Add the required workflow(s) and confirm the referenced workflow file exists in the target repository/branch and is configured correctly.
- Test on a sample PR to confirm the required workflow blocks merges when failing/missing.

## Projects built-in automations
- Open the relevant project, click the menu (top-right), then **Workflows**.
- For each default workflow you rely on, click **Edit**, adjust fields as needed, **Save**, and ensure it is turned **On**.
- Confirm defaults such as automatically setting **Status** to **Done** when issues/PRs close, and any auto-add/archive rules you need.

## Deployment and environment protections
- Store sensitive credentials as repo/org/enterprise secrets; avoid embedding secrets in workflows.
- For protected environments, configure required reviewers or manual approvals and restrict secrets to those environments.

## Quick validation loop
- Spot-check **Enterprise → Policies → Advanced Security** against your intended enforcement matrix.
- Pick a sample org and check **Settings → Actions** to verify allowed actions/runners match the plan.
- Open a repo with a required workflow (e.g., dependency review) and confirm the rule exists, the workflow file is present, and it passes on a test PR.
- Open a project and ensure required built-in automations are enabled under **Workflows**.
- If any check is out of alignment, update the relevant enterprise policy, org/repo Actions settings, branch ruleset, workflow file, or project workflow via the UI paths above.
