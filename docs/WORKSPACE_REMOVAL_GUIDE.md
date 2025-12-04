# Workspace Removal Troubleshooting Guide

Use this checklist when you need to remove (delete) a workspace from your account and the usual UI path is failing. It is platform-agnostic, so adapt the terms (workspace/organization/tenant) to your service.

## Quick removal checklist
- Confirm your role. Only owners/admins can delete workspaces; members can usually **leave** but not delete.
- Export what you need first (repos, projects, billing receipts). Deletion is often irreversible.
- Cancel or transfer active subscriptions tied to the workspace to clear billing blocks.
- Remove required security gates (SSO/SCIM/enterprise policies) that prevent ownership changes or deletion.
- If you only want it off your account and you are not the owner, choose **Leave workspace** instead of **Delete**.

## Standard removal steps (owner/admin)
1. Open **Settings → Workspace/Organization → Danger Zone** (names vary).
2. Look for **Delete workspace**, **Deactivate**, or **Archive**.
3. Complete any required confirmations (typing the workspace name, re-entering your password, or MFA approval).
4. If the button is disabled, look for an explanatory banner (e.g., active subscription, outstanding invoices, pending transfer) and resolve it.

## When deletion is blocked
- **Active subscription**: Cancel the plan, wait for it to show as canceled, then retry deletion.
- **Outstanding invoices**: Pay or dispute the invoices; some platforms block deletion until the balance is zero.
- **Ownership lock**: If you are not the sole owner, transfer ownership or ask another owner to delete it. Remove yourself with **Leave workspace** if you just need it gone from your account.
- **Enterprise SSO/SCIM**: Temporarily disable enforcement or remove the workspace from the identity provider if the platform requires it for deletion.
- **Compliance holds/retention**: Check for legal holds, retention policies, or audit requirements that prevent deletion; you may need admin-level approval to clear these.

## Support escalation
If UI options fail, contact support with the details below to speed up resolution:
- Workspace name/URL and your role (owner/admin/member).
- Confirmation whether you want **Delete** or simply **Leave** the workspace.
- Subscription status (active/canceled), outstanding invoice numbers, and renewal date.
- Whether SSO/SCIM is enforced and if you can temporarily disable it.
- The exact error message or screenshot of the blocked deletion button.
- Target date/time you need the removal completed.

### Support request template
```
Subject: Workspace removal assistance

Hello Support,
I need to remove the workspace "<workspace-name>" from my account. My role: <owner/admin/member>.

Requested action: <Delete workspace entirely | Remove me from the workspace>.

Billing: <active plan / canceled on <date>; outstanding invoice numbers if any>.
SSO/SCIM: <enforced/not enforced>. I can <temporarily disable / cannot disable> it.
Error: <paste exact error text or describe disabled button>.
Deadline: <preferred completion time>.

Please process the removal or advise on the next required step.
Thank you.
```

## Optional pre-deletion data steps
- Export repositories, documents, and audit logs you might need later.
- Transfer ownership of assets you want to keep alive elsewhere (projects, domains, API keys).
- Reassign integrations/webhooks to another workspace to avoid downtime.

## After removal
- Verify the workspace no longer appears in your switcher or organization list.
- Confirm recurring charges stopped (check billing page and payment method).
- If you left instead of deleting, ensure role removal propagated (log out/in or clear cache if the workspace still appears).
