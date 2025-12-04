# 🛡️ Security Guide - Avalon Project

## Table of Contents
1. [Critical Security Notice](#critical-security-notice)
2. [API Keys Management](#api-keys-management)
3. [Stripe Integration](#stripe-integration)
4. [GitHub Secrets Setup](#github-secrets-setup)
5. [Local Development](#local-development)
6. [Production Deployment](#production-deployment)
7. [Incident Response](#incident-response)
8. [Security Checklist](#security-checklist)

---

## ⚠️ Critical Security Notice

### Never Commit Secrets to Git

**The following should NEVER be committed to version control:**
- API keys (Stripe, OpenAI, Anthropic, etc.)
- Webhook secrets
- Personal access tokens
- OAuth credentials
- Database credentials
- Encryption keys
- SSL certificates (private keys)

**Already committed a secret?** See [Incident Response](#incident-response) immediately.

---

## 🔑 API Keys Management

### Three-Tier Security Architecture

This repository uses a three-tier approach to managing secrets:

#### Tier 1: Local Development (`.env` files)
- **Location:** Project root and `config/` directory
- **Usage:** Local development only
- **Protection:** Listed in `.gitignore`
- **Example:** `config/.env.example`

#### Tier 2: Centralized Keys (`.auth/` directory)
- **Location:** `.auth/` directory
- **Usage:** Shared between multiple automation tools
- **Protection:** Fully excluded from Git (except documentation)
- **Documentation:** [.auth/README.md](.auth/README.md)
- **Template:** [.auth/keys.example.json](.auth/keys.example.json)

#### Tier 3: Production/CI (GitHub Secrets)
- **Location:** GitHub Repository → Settings → Secrets and Variables → Actions
- **Usage:** GitHub Actions workflows and production deployments
- **Protection:** Encrypted at rest, masked in logs
- **Documentation:** See [GitHub Secrets Setup](#github-secrets-setup)

### Which Tier to Use?

| Use Case | Recommended Tier | Why |
|----------|------------------|-----|
| Local script development | Tier 1 (`.env`) | Simple, tool-agnostic |
| Multi-tool automation (Pipedream, Zapier) | Tier 2 (`.auth/`) | Centralized management |
| GitHub Actions workflows | Tier 3 (GitHub Secrets) | Encrypted, secure |
| Production deployment | Tier 3 (Platform secrets) | Platform-managed security |
| Shared between team members | **Never commit!** Use password manager | Security |

---

## 💳 Stripe Integration

### Getting Your Stripe Keys

1. **Log in to Stripe Dashboard:** https://dashboard.stripe.com/
2. **Navigate to:** Developers → API Keys
3. **Key Types:**
   - **Publishable Key** (`pk_test_...` or `pk_live_...`) - Safe for client-side code
   - **Secret Key** (`sk_test_...` or `sk_live_...`) - NEVER expose to clients
   - **Webhook Secret** (`whsec_...`) - For verifying webhook signatures

### Test vs. Live Keys

#### Development (Use Test Keys)
```bash
# In your .env file
STRIPE_PUBLISHABLE_KEY=pk_test_51AbCdEfGhIjKlMnOpQrStUvWxYz...
STRIPE_SECRET_KEY=sk_test_51AbCdEfGhIjKlMnOpQrStUvWxYz...
STRIPE_WEBHOOK_SECRET=whsec_AbCdEfGhIjKlMnOpQrStUvWxYz...
```

**Test keys characteristics:**
- No real charges are processed
- Test credit card numbers work (4242 4242 4242 4242)
- Safe to use for development and testing
- Visible in Stripe Dashboard's "Test Mode"

#### Production (Use Live Keys)
```bash
# In GitHub Secrets (NOT in .env)
STRIPE_PUBLISHABLE_KEY=pk_live_YOUR_ACTUAL_LIVE_KEY_HERE
STRIPE_SECRET_KEY=sk_live_YOUR_ACTUAL_LIVE_KEY_HERE
STRIPE_WEBHOOK_SECRET=whsec_YOUR_WEBHOOK_SECRET_HERE
```

**Live keys characteristics:**
- Real charges are processed
- Real credit cards are charged
- **NEVER commit to version control**
- **NEVER use in local development**
- Only use in production environment

### ⚠️ CRITICAL: Key Rotation After Exposure

**If you've exposed a Stripe key (committed to Git, posted in issue, etc.):**

1. **Immediate Action (within 5 minutes):**
   ```
   1. Go to Stripe Dashboard → Developers → API Keys
   2. Click "Roll" next to the exposed key
   3. Confirm key rotation
   4. Update your production environment immediately
   ```

2. **Investigation (within 1 hour):**
   ```
   1. Check Stripe Dashboard → Logs for suspicious activity
   2. Review recent payments and refunds
   3. Check webhook events for unusual patterns
   4. Document when and how the exposure occurred
   ```

3. **Prevention (within 24 hours):**
   ```
   1. Ensure .gitignore properly excludes secret files
   2. Run secret scanning tools (see below)
   3. Update team security procedures
   4. Consider enabling Stripe Radar for fraud detection
   ```

### Stripe Webhook Configuration

1. **Create Webhook Endpoint:**
   - Go to Stripe Dashboard → Developers → Webhooks
   - Click "Add endpoint"
   - Enter your endpoint URL (e.g., `https://yourdomain.com/webhook/stripe`)

2. **Select Events:**
   - `payment_intent.succeeded`
   - `payment_intent.payment_failed`
   - `customer.created`
   - `charge.refunded`
   - (Add others as needed)

3. **Save Webhook Secret:**
   ```bash
   # Add to .env (local) or GitHub Secrets (production)
   STRIPE_WEBHOOK_SECRET=whsec_...
   ```

4. **Verify Webhook Signatures:**
   ```javascript
   const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
   const endpointSecret = process.env.STRIPE_WEBHOOK_SECRET;

   // In your webhook handler
   const sig = req.headers['stripe-signature'];
   let event;

   try {
     event = stripe.webhooks.constructEvent(req.body, sig, endpointSecret);
   } catch (err) {
     return res.status(400).send(`Webhook Error: ${err.message}`);
   }
   ```

---

## 🔐 GitHub Secrets Setup

### Adding Secrets to GitHub

1. **Navigate to Repository Settings:**
   ```
   Repository → Settings → Secrets and variables → Actions
   ```

2. **Click "New repository secret"**

3. **Add Required Secrets:**

   | Secret Name | Description | Where to Get It |
   |-------------|-------------|-----------------|
   | `STRIPE_SECRET_KEY` | Stripe secret key | [Stripe Dashboard](https://dashboard.stripe.com/apikeys) |
   | `STRIPE_WEBHOOK_SECRET` | Stripe webhook secret | Stripe → Webhooks → Endpoint |
   | `ANTHROPIC_API_KEY` | Claude API key | [Anthropic Console](https://console.anthropic.com/) |
   | `OPENAI_API_KEY` | OpenAI API key | [OpenAI Platform](https://platform.openai.com/api-keys) |
   | `PIPEDREAM_API_KEY` | Pipedream API key | [Pipedream Settings](https://pipedream.com/settings/account) |

4. **Access in GitHub Actions:**
   ```yaml
   # .github/workflows/your-workflow.yml
   name: Deploy with Stripe
   
   on:
     push:
       branches: [main]
   
   jobs:
     deploy:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Deploy to production
           env:
             STRIPE_SECRET_KEY: ${{ secrets.STRIPE_SECRET_KEY }}
             STRIPE_WEBHOOK_SECRET: ${{ secrets.STRIPE_WEBHOOK_SECRET }}
           run: |
             # Your deployment script
             ./deploy.sh
   ```

### Secret Security in Workflows

**GitHub automatically:**
- ✅ Masks secrets in log output
- ✅ Encrypts secrets at rest
- ✅ Prevents secrets from being read by forked repositories
- ✅ Limits secret access to selected workflows

**You should:**
- ❌ Never `echo` or `console.log()` secrets
- ❌ Never pass secrets as command-line arguments
- ❌ Never commit GitHub Actions logs
- ✅ Use environment variables, not direct substitution
- ✅ Regularly rotate secrets (every 90 days)

---

## 💻 Local Development

### Initial Setup

1. **Copy Example Files:**
   ```bash
   # Copy environment template
   cp config/.env.example config/.env
   
   # Copy keys template
   cp .auth/keys.example.json .auth/keys.json
   ```

2. **Fill in Development Keys:**
   ```bash
   # Edit config/.env
   nano config/.env
   
   # Add your TEST Stripe keys
   STRIPE_SECRET_KEY=sk_test_...
   STRIPE_PUBLISHABLE_KEY=pk_test_...
   ```

3. **Verify Git Ignores Secrets:**
   ```bash
   git status
   # Should NOT show:
   # - config/.env
   # - .auth/keys.json
   # - Any files with credentials
   ```

### Loading Environment Variables

#### For Node.js:
```javascript
require('dotenv').config({ path: './config/.env' });

const stripeKey = process.env.STRIPE_SECRET_KEY;
```

#### For Python:
```python
from dotenv import load_dotenv
import os

load_dotenv('config/.env')

stripe_key = os.getenv('STRIPE_SECRET_KEY')
```

#### For Shell Scripts:
```bash
source config/.env
echo "Stripe key loaded: ${STRIPE_SECRET_KEY:0:10}..."
```

### Reading from .auth/keys.json

#### For Node.js:
```javascript
const fs = require('fs');
const path = require('path');

const keysPath = path.join(__dirname, '.auth', 'keys.json');
const keys = JSON.parse(fs.readFileSync(keysPath, 'utf8'));

const stripeKey = keys.stripe.secret_key;
```

#### For Python:
```python
import json
import os

keys_path = os.path.join('.auth', 'keys.json')
with open(keys_path, 'r') as f:
    keys = json.load(f)

stripe_key = keys['stripe']['secret_key']
```

---

## 🚀 Production Deployment

### Deployment Checklist

- [ ] **All secrets stored in platform-specific secrets management**
  - GitHub Actions: GitHub Secrets
  - Vercel: Environment Variables
  - Netlify: Environment Variables
  - AWS: Secrets Manager or Parameter Store
  
- [ ] **Using LIVE Stripe keys (pk_live_, sk_live_)**

- [ ] **Webhook endpoints configured correctly**
  - HTTPS enabled
  - Signature verification implemented
  - Error handling in place

- [ ] **Environment variables loaded correctly**
  - No hardcoded secrets in code
  - No .env files in production
  - Secrets injected at runtime

- [ ] **Logging configured safely**
  - No secrets in logs
  - Sensitive data masked
  - Log rotation enabled

- [ ] **Access control configured**
  - Least privilege principle
  - Service accounts used where appropriate
  - Regular access audits

### Platform-Specific Guides

#### Vercel
```bash
# Install Vercel CLI
npm i -g vercel

# Add secrets
vercel secrets add stripe-secret-key sk_live_...
vercel secrets add stripe-webhook-secret whsec_...

# Link in vercel.json
{
  "env": {
    "STRIPE_SECRET_KEY": "@stripe-secret-key",
    "STRIPE_WEBHOOK_SECRET": "@stripe-webhook-secret"
  }
}
```

#### Netlify
```bash
# Install Netlify CLI
npm i -g netlify-cli

# Add environment variables in Netlify UI
# Site settings → Build & deploy → Environment → Environment variables

# Or via CLI
netlify env:set STRIPE_SECRET_KEY sk_live_...
```

#### Heroku
```bash
# Set config vars
heroku config:set STRIPE_SECRET_KEY=sk_live_...
heroku config:set STRIPE_WEBHOOK_SECRET=whsec_...

# Verify
heroku config
```

---

## 🚨 Incident Response

### If You've Committed a Secret to Git

**Severity: CRITICAL - Act immediately!**

#### Step 1: Stop Everything (0-5 minutes)
1. **Do NOT push more commits** trying to "fix" it
2. **Do NOT delete the repository** (secrets remain in Git history)
3. **Do NOT panic** - follow this checklist

#### Step 2: Rotate the Secret (5-10 minutes)
1. **Go to the service dashboard:**
   - Stripe: Dashboard → Developers → API Keys → Roll key
   - OpenAI: Platform → API Keys → Revoke key
   - GitHub: Settings → Developer settings → Revoke token

2. **Generate new secret** with different value

3. **Update production immediately:**
   - GitHub Secrets
   - Vercel/Netlify environment variables
   - Any running services

#### Step 3: Clean Git History (10-30 minutes)

**WARNING: This rewrites Git history. Coordinate with team!**

```bash
# Install BFG Repo Cleaner
brew install bfg  # macOS
# or download from https://rtyley.github.io/bfg-repo-cleaner/

# Clone a fresh copy
git clone --mirror https://github.com/yourusername/Aethromoor.git

# Remove the secret (replace with your actual secret)
bfg --replace-text secrets.txt Aethromoor.git

# Cleanup
cd Aethromoor.git
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# Force push (requires coordination with team)
git push --force
```

**Alternative: GitHub's Secret Scanning**
- GitHub automatically detects many types of secrets
- Will alert repository admins
- Contact service providers directly

#### Step 4: Investigate Impact (30-60 minutes)
1. **Check service logs** for unauthorized access
2. **Review usage metrics** for anomalies
3. **Check for financial impact** (especially Stripe)
4. **Document timeline** of exposure

#### Step 5: Prevent Future Incidents (1-24 hours)
1. **Enable GitHub secret scanning:**
   ```
   Repository → Settings → Code security and analysis
   → Enable "Secret scanning"
   ```

2. **Add pre-commit hooks:**
   ```bash
   # Install gitleaks
   brew install gitleaks
   
   # Add to .git/hooks/pre-commit
   #!/bin/bash
   gitleaks protect --staged
   ```

3. **Review and update .gitignore:**
   ```bash
   # Ensure all secret patterns are covered
   git status --ignored
   ```

4. **Team training:**
   - Share this guide
   - Conduct security review
   - Update procedures

### Secret Scanning Tools

#### Gitleaks (Recommended)
```bash
# Install
brew install gitleaks

# Scan entire repository
gitleaks detect --source . --verbose

# Scan before committing
gitleaks protect --staged

# Scan with custom rules
gitleaks detect --config .gitleaks.toml
```

#### TruffleHog
```bash
# Install
pip install truffleHog

# Scan repository
trufflehog https://github.com/yourusername/Aethromoor.git

# Scan local directory
trufflehog filesystem .
```

#### Git-secrets
```bash
# Install (AWS tool)
brew install git-secrets

# Setup in repository
git secrets --install
git secrets --register-aws

# Scan commits
git secrets --scan-history
```

---

## ✅ Security Checklist

### Before Every Commit
- [ ] Run `git status` and review staged files
- [ ] No `.env` files staged
- [ ] No `keys.json` or similar staged
- [ ] No hardcoded credentials in code
- [ ] Run `gitleaks protect --staged` (if installed)

### Weekly
- [ ] Review repository for new `.env` patterns
- [ ] Check GitHub Secrets are up to date
- [ ] Verify webhook endpoints are responding
- [ ] Review service logs for anomalies

### Monthly
- [ ] Rotate API keys (following service best practices)
- [ ] Audit access logs on all services
- [ ] Review team member access
- [ ] Update `.gitignore` if needed

### Quarterly
- [ ] Full security audit
- [ ] Rotate all API keys
- [ ] Review and update this security guide
- [ ] Team security training review

### Before Production Deploy
- [ ] All secrets in platform secrets management
- [ ] Using production API keys (not test keys)
- [ ] Webhooks configured with signature verification
- [ ] No secrets in logs
- [ ] Error handling in place
- [ ] Monitoring and alerting configured

---

## 📚 Additional Resources

### Official Documentation
- [Stripe API Security](https://stripe.com/docs/security)
- [GitHub Secrets Documentation](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [12-Factor App: Config](https://12factor.net/config)

### Tools
- [Gitleaks](https://github.com/gitleaks/gitleaks) - Secret scanning
- [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/) - Git history cleanup
- [git-secrets](https://github.com/awslabs/git-secrets) - Prevent committing secrets
- [TruffleHog](https://github.com/trufflesecurity/trufflehog) - Find exposed secrets

### Security Standards
- [PCI DSS](https://www.pcisecuritystandards.org/) - Payment card security
- [SOC 2](https://www.aicpa.org/soc) - Service organization controls
- [GDPR](https://gdpr.eu/) - Data protection (EU)
- [CCPA](https://oag.ca.gov/privacy/ccpa) - Consumer privacy (California)

---

## 🆘 Emergency Contacts

### If you detect a security incident:

1. **Rotate compromised credentials immediately** (see service dashboards above)
2. **Contact repository maintainer:** @issdandavis
3. **Document the incident** in GitHub Issues (use `security` label)
4. **Follow incident response plan** (above)

### Service Support Contacts

- **Stripe Support:** https://support.stripe.com/
- **GitHub Support:** https://support.github.com/
- **OpenAI Support:** https://help.openai.com/
- **Anthropic Support:** https://support.anthropic.com/

---

**Remember: When in doubt, don't commit it. Use GitHub Secrets instead.**

**Last Updated:** December 2024  
**Version:** 1.0.0  
**Maintainer:** @issdandavis
