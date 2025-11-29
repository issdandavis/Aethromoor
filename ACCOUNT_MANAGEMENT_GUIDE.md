# Account Management Guide

## 📋 Overview

This guide helps you manage **personal accounts**, **organizational accounts**, and **business integrations** for your projects. Everything is clearly labeled and organized.

---

## 🏗️ Account Structure

### Personal Accounts
**What they are:** Your individual GitHub accounts  
**Primary:** issdandavis  
**Configuration:** `config/account-settings.json` → `personal_accounts`

### Organizational Accounts  
**What they are:** GitHub Organizations you own/manage  
**Current:** issdandavis (personal organization)  
**Configuration:** `config/account-settings.json` → `organizational_accounts`

### Business Integrations
**What they are:** Third-party services (Stripe, PayPal, analytics, etc.)  
**Configuration:** `config/account-settings.json` → `business_integrations`

---

## 📁 Configuration Files

### Main Files
- **`config/account-settings.json`** - All account types, business integrations, payment processing
- **`config/automation-monitoring-settings.json`** (renamed from enterprise-settings.json) - Workflow monitoring only
- **`config/automation-settings.json`** - General automation settings

### Key Distinction
- ✅ **Account Settings** = Who you are (personal/org accounts, business integrations)
- ✅ **Automation Monitoring** = How systems are monitored (workflows, 2FA validation)
- ✅ **Automation Settings** = What automations run (AI agents, inbox management)

---

## 💳 Setting Up Stripe Payment Processing

### 1. Create Stripe Account
1. Go to https://stripe.com
2. Sign up with your business email
3. Complete business verification (for live payments)

### 2. Get API Keys
1. Log into Stripe Dashboard
2. Go to **Developers** → **API Keys**
3. Copy:
   - **Publishable key** (starts with `pk_test_` or `pk_live_`)
   - **Secret key** (starts with `sk_test_` or `sk_live_`)

### 3. Add to GitHub Secrets
```bash
# Go to your repository
# Settings → Secrets and variables → Actions → New repository secret

# Add these secrets:
STRIPE_TEST_SECRET_KEY = sk_test_...
STRIPE_LIVE_SECRET_KEY = sk_live_...  (when ready for production)
STRIPE_WEBHOOK_SECRET = whsec_...     (for webhook verification)
```

### 4. Update Configuration
Edit `config/account-settings.json`:
```json
{
  "business_integrations": {
    "payment_processing": {
      "stripe": {
        "enabled": true,
        "mode": "test",  // Change to "live" when ready
        "api_keys": {
          "test_publishable_key": "pk_test_YOUR_KEY_HERE",
          "live_publishable_key": "pk_live_YOUR_KEY_HERE"
        }
      }
    }
  }
}
```

### 5. Create Products in Stripe
1. Stripe Dashboard → **Products** → **Add Product**
2. Create products:
   - Game Purchase ($X.XX one-time)
   - Premium Subscription ($X.XX/month)
   - Donation (customer sets amount)
3. Copy the **Price ID** for each (starts with `price_...`)
4. Add to `account-settings.json` under `products`

---

## 🏢 Managing Organizations

### Current Setup
- **Personal Organization:** issdandavis
- **Repositories:** Aethromoor (this repo)

### Adding Sub-Organizations

**When to use:**
- Separate business entity
- Different project types (personal vs commercial)
- Team collaboration needs

**How to add:**
1. Create organization on GitHub
2. Add to `config/account-settings.json`:
```json
{
  "organizational_accounts": {
    "sub_organizations": {
      "enabled": true,
      "list": [
        {
          "name": "my-game-studio",
          "type": "business",
          "enabled": true,
          "purpose": "Commercial game publishing",
          "auto_approve_workflows": true,
          "trusted": true
        }
      ]
    }
  }
}
```
3. Update `.github/workflows/auto-approve-workflows.yml` to include new org

---

## 🔐 Security Best Practices

### Secrets Management
✅ **ALWAYS** store API keys in GitHub Secrets  
✅ **NEVER** commit keys to repository  
✅ Use test/sandbox mode until ready for production  
✅ Rotate keys every 90 days

### Account Access
✅ Enable 2FA on all accounts  
✅ Use strong, unique passwords  
✅ Review access permissions quarterly  
✅ Limit auto-approval to trusted accounts only

---

## 🚀 Quick Start Checklist

### For Stripe Setup
- [ ] Create Stripe account
- [ ] Get test API keys
- [ ] Add secrets to GitHub
- [ ] Update `account-settings.json`
- [ ] Create products in Stripe
- [ ] Add product price IDs to config
- [ ] Test with test mode first
- [ ] Switch to live mode when ready

### For New Organization
- [ ] Create GitHub organization
- [ ] Add to `account-settings.json`
- [ ] Update workflow auto-approval list
- [ ] Configure organization settings
- [ ] Add team members (if any)
- [ ] Set up repository permissions

---

## 📊 Account Types Reference

| Account Type | Purpose | Auto-Approve | Config Location |
|-------------|---------|--------------|-----------------|
| Personal Primary | Your main GitHub account | ✅ Yes | `personal_accounts.primary` |
| Personal Secondary | Additional accounts | ⚠️ Optional | `personal_accounts.secondary` |
| Main Organization | Your primary org | ✅ Yes | `organizational_accounts.main_organization` |
| Sub-Organizations | Business/project orgs | ⚠️ Per org | `organizational_accounts.sub_organizations` |
| Stripe | Payment processing | N/A | `business_integrations.payment_processing.stripe` |
| Other Services | Analytics, email, etc | N/A | `business_integrations.*` |

---

## 🔄 Workflow Auto-Approval

### Who Gets Auto-Approved
✅ Personal accounts (you)  
✅ Organizational accounts (your orgs)  
✅ Trusted bots (Dependabot, Copilot)

### Who Requires Manual Approval
❌ External contributors  
❌ Unknown accounts  
❌ Untrusted bots

### Configuration
Edit `config/account-settings.json`:
```json
{
  "workflow_automation": {
    "auto_approval_rules": {
      "personal_accounts": true,
      "organizational_accounts": true,
      "external_contributors": false
    }
  }
}
```

---

## 📈 Business Integration Examples

### Payment Processing
- **Stripe** - Credit card payments, subscriptions
- **PayPal** - Alternative payment method
- **Ko-fi** - Donations and tips

### Analytics
- **Google Analytics** - Website traffic
- **Plausible** - Privacy-friendly analytics

### Email & Communication
- **SendGrid** - Transactional emails
- **Mailchimp** - Newsletter and marketing

### Hosting & CDN
- **Cloudflare** - CDN and DDoS protection
- **AWS S3** - File storage
- **GitHub Pages** - Free website hosting

---

## 🆘 Common Scenarios

### "I want to sell my game"
1. Set up Stripe (see above)
2. Create product in Stripe
3. Enable in `account-settings.json`
4. Integrate payment form in your game/website

### "I want to accept donations"
1. Option 1: Stripe (setup above)
2. Option 2: Ko-fi (easier, takes small fee)
3. Option 3: PayPal Donate button

### "I want to start a game studio"
1. Create new GitHub organization
2. Add to sub-organizations in config
3. Set up business Stripe account
4. Configure organizational permissions

### "I have multiple projects"
1. Create sub-organization per project type
2. Or use repository-level settings within one org
3. Configure auto-approval per org

---

## 📞 Support & Resources

### Stripe Resources
- Dashboard: https://dashboard.stripe.com
- Documentation: https://stripe.com/docs
- Test Cards: https://stripe.com/docs/testing

### GitHub Resources
- Organizations: https://docs.github.com/en/organizations
- Secrets: https://docs.github.com/en/actions/security-guides/encrypted-secrets
- Workflows: https://docs.github.com/en/actions

---

## 🎯 Next Steps

1. **Review** `config/account-settings.json`
2. **Set up** Stripe account (if selling/accepting payments)
3. **Add** API keys to GitHub Secrets
4. **Test** with sandbox/test mode
5. **Launch** when ready!

---

*This guide is part of the account management system. For automation monitoring (not account management), see `docs/AUTOMATION_MONITORING.md` (renamed from ENTERPRISE_MONITORING.md).*
