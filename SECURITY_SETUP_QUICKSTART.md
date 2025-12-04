# 🚀 Quick Start - Secure API Keys Setup

## What Was Created

A complete secure API key management system for the Avalon repository, supporting:
- Payment processing (Stripe)
- AI services (OpenAI, Anthropic)
- Automation tools (Pipedream, Zapier, n8n)
- GitHub Actions and webhooks

## 📁 New Files and Directories

```
.auth/                                  ← New secure keys directory
├── README.md                           ← Full security guide (8KB)
├── keys.example.json                   ← Template for all API keys (4KB)
├── AUTOMATION_QUICK_START.md           ← Pipedream/Zapier guide (11KB)
├── SECURITY_INCIDENT_STRIPE_KEY.md     ← URGENT: Key rotation guide (7KB)
└── keys.json                           ← YOU CREATE THIS (gitignored)

docs/
├── SECURITY.md                         ← Complete security guide (16KB)
└── GITHUB_SECRETS_SETUP.md             ← GitHub Secrets setup (13KB)

config/
└── .env.example                        ← Updated with Stripe config

.gitignore                              ← Updated to protect secrets
README.md                               ← Updated with security section
```

## ⚠️ URGENT: First Steps

### 1. Rotate the Exposed Stripe Key (DO THIS FIRST!)

The Stripe API key from the issue **MUST be rotated immediately**:

```bash
# Follow these steps ASAP:
1. Go to: https://dashboard.stripe.com/apikeys
2. Find key starting with: sk_live_51SYHy3...
3. Click "Roll" button
4. Confirm rotation
5. Copy NEW secret key (you'll only see it once!)
6. Update production with new key
```

**Full instructions:** See `.auth/SECURITY_INCIDENT_STRIPE_KEY.md`

### 2. Set Up Local Development (5 minutes)

```bash
# Navigate to repository
cd /path/to/Aethromoor

# Copy templates
cp config/.env.example config/.env
cp .auth/keys.example.json .auth/keys.json

# Edit and add your TEST keys
nano config/.env
# Add: STRIPE_SECRET_KEY=sk_test_... (TEST key only!)

# Or use the centralized keys file
nano .auth/keys.json
# Fill in test keys for all services

# Verify git ignores your secrets
git status
# Should NOT show .env or keys.json
```

### 3. Configure GitHub Secrets (10 minutes)

**For automation and production:**

1. Go to: https://github.com/issdandavis/Aethromoor/settings/secrets/actions

2. Click "New repository secret"

3. Add these secrets:

| Secret Name | Where to Get It | Value Format |
|-------------|-----------------|--------------|
| `STRIPE_SECRET_KEY` | Stripe Dashboard (rotated!) | `sk_live_...` |
| `STRIPE_PUBLISHABLE_KEY` | Stripe Dashboard | `pk_live_...` |
| `STRIPE_WEBHOOK_SECRET` | Stripe Webhooks | `whsec_...` |
| `ANTHROPIC_API_KEY` | Anthropic Console | `sk-ant-...` |
| `OPENAI_API_KEY` | OpenAI Platform | `sk-...` |
| `PIPEDREAM_API_KEY` | Pipedream Settings | Your key |

**Full instructions:** See `docs/GITHUB_SECRETS_SETUP.md`

## 📖 Documentation Quick Links

### For Developers
- **Getting Started:** This file
- **Security Best Practices:** `docs/SECURITY.md`
- **Local Key Management:** `.auth/README.md`

### For Automation
- **Pipedream/Zapier Integration:** `.auth/AUTOMATION_QUICK_START.md`
- **GitHub Actions Setup:** `docs/GITHUB_SECRETS_SETUP.md`

### Emergency
- **Exposed Key Response:** `.auth/SECURITY_INCIDENT_STRIPE_KEY.md`
- **Incident Procedures:** `docs/SECURITY.md` (Section: Incident Response)

## 🔐 Security Architecture

### Three-Tier System

**Tier 1: Local Development (`.env` files)**
- Location: `config/.env`, `.env.local`
- Usage: Local development only
- Protection: Gitignored
- Keys: TEST keys only (sk_test_, pk_test_)

**Tier 2: Centralized Keys (`.auth/` directory)**
- Location: `.auth/keys.json`
- Usage: Shared by automation tools (Pipedream, Zapier)
- Protection: Gitignored except documentation
- Keys: TEST keys for dev, LIVE keys only if needed by automation

**Tier 3: Production (GitHub Secrets)**
- Location: GitHub Repository Secrets
- Usage: GitHub Actions, production deployment
- Protection: Encrypted, masked in logs
- Keys: LIVE keys only

## 🤖 Using with Automation Tools

### Pipedream Workflows

**Option 1: Environment Variables**
```javascript
const stripeKey = process.env.STRIPE_SECRET_KEY;
```

**Option 2: Read from keys.json**
```javascript
const keys = require('./.auth/keys.json');
const stripeKey = keys.stripe.secret_key;
```

**Option 3: Pipedream Connected Accounts** (recommended)
```javascript
// Connect Stripe account in Pipedream UI
// Access automatically via this.stripe
```

### Zapier Webhooks

**Trigger from code:**
```javascript
const webhookUrl = process.env.ZAPIER_WEBHOOK_URL;
await axios.post(webhookUrl, { data });
```

### GitHub Actions

**Access secrets:**
```yaml
- name: Deploy
  env:
    STRIPE_SECRET_KEY: ${{ secrets.STRIPE_SECRET_KEY }}
  run: ./deploy.sh
```

**Full examples:** See `.auth/AUTOMATION_QUICK_START.md`

## ✅ Verification Checklist

After setup, verify:

- [ ] **Stripe key rotated** (if exposed key was from this repo)
- [ ] **Local .env created** from template
- [ ] **Test keys added** to local config
- [ ] **Git ignores secrets** (`git status` clean)
- [ ] **GitHub Secrets configured** (all required keys)
- [ ] **Automation tested** (Pipedream/Zapier)
- [ ] **Documentation reviewed** (know where to find info)

## 🆘 Common Issues

### "Cannot find .env file"

**Solution:**
```bash
cp config/.env.example config/.env
nano config/.env  # Add your keys
```

### "Keys.json not found"

**Solution:**
```bash
cp .auth/keys.example.json .auth/keys.json
nano .auth/keys.json  # Fill in your keys
```

### "Git trying to commit .env"

**Solution:**
```bash
# Verify .gitignore
cat .gitignore | grep ".env"

# Should show:
# .env
# .env.local
# config/.env
```

### "Stripe API key invalid"

**Possible causes:**
1. Using test key in production (or vice versa)
2. Key not rotated after exposure
3. Extra whitespace when copying
4. Key revoked in Stripe Dashboard

**Solution:** Generate new key, verify format, check environment

## 📚 Learn More

### Service Dashboards
- **Stripe:** https://dashboard.stripe.com/
- **OpenAI:** https://platform.openai.com/
- **Anthropic:** https://console.anthropic.com/
- **Pipedream:** https://pipedream.com/
- **GitHub Secrets:** https://github.com/issdandavis/Aethromoor/settings/secrets

### Documentation
- [Stripe API Docs](https://stripe.com/docs/api)
- [GitHub Secrets Guide](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Pipedream Docs](https://pipedream.com/docs)
- [Zapier Webhooks](https://zapier.com/apps/webhook/help)

## 💡 Best Practices

1. **Always use test keys for development**
   - Stripe: `sk_test_...`, `pk_test_...`
   - Never use live keys locally

2. **Never commit secrets to Git**
   - Use `.env` files (gitignored)
   - Use GitHub Secrets for production
   - Double-check before committing

3. **Rotate keys regularly**
   - Every 90 days recommended
   - Immediately if exposed
   - Document rotation dates

4. **Monitor usage**
   - Check Stripe Dashboard logs weekly
   - Review GitHub Actions logs
   - Watch for unusual activity

5. **Use least privilege**
   - Only grant necessary permissions
   - Create separate keys per environment
   - Revoke unused keys

## 🎯 Next Steps

1. **Complete urgent actions:**
   - [ ] Rotate exposed Stripe key
   - [ ] Set up local development
   - [ ] Configure GitHub Secrets

2. **Test integration:**
   - [ ] Test local development setup
   - [ ] Test GitHub Actions workflow
   - [ ] Test Pipedream/Zapier integration

3. **Security review:**
   - [ ] Read `docs/SECURITY.md`
   - [ ] Understand incident response
   - [ ] Set up monitoring

4. **Team onboarding:**
   - [ ] Share this guide with team
   - [ ] Review security procedures
   - [ ] Establish key rotation schedule

## 📞 Need Help?

**Security Issue?**
- See: `.auth/SECURITY_INCIDENT_STRIPE_KEY.md`
- Read: `docs/SECURITY.md` (Incident Response section)

**Setup Questions?**
- Check: `.auth/README.md`
- Review: `docs/GITHUB_SECRETS_SETUP.md`

**Automation Questions?**
- Guide: `.auth/AUTOMATION_QUICK_START.md`

**Repository Issues:**
- Create GitHub issue with `security` label
- Contact: @issdandavis

---

## 🎉 Summary

You now have a complete, secure API key management system that:

✅ Protects secrets from being committed to Git  
✅ Provides clear templates and examples  
✅ Supports multiple automation platforms  
✅ Includes comprehensive documentation  
✅ Has incident response procedures  

**Start with the urgent Stripe key rotation, then set up your local environment!**

---

**Created:** December 2024  
**Repository:** Avalon/Aethromoor  
**Maintainer:** @issdandavis
