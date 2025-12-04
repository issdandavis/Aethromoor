# 🔐 Secure API Keys Repository

## ⚠️ CRITICAL SECURITY WARNING

**This directory is for LOCAL DEVELOPMENT ONLY and is excluded from Git via `.gitignore`.**

- **NEVER commit actual API keys to version control**
- **NEVER share your `.env` or `keys.json` files**
- **ALWAYS rotate keys immediately if they are exposed**

---

## 📁 Directory Purpose

This `.auth/` directory provides a centralized, secure location for storing authentication credentials used by:
- **Automation tools** (Pipedream, Zapier, Make.com)
- **AI services** (ChatGPT, Claude, other LLMs)
- **Payment processors** (Stripe, PayPal)
- **APIs and webhooks**
- **Development tools**

---

## 🔒 Security Best Practices

### 1. **Never Commit Secrets**
All files in this directory (except `README.md` and `.example` files) are automatically excluded from Git.

### 2. **Use Environment Variables**
For local development, use `.env` files. For production/CI:
- **GitHub Actions:** Use [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- **Vercel/Netlify:** Use platform environment variables
- **Docker:** Use secrets management or encrypted environment files

### 3. **Rotate Exposed Keys Immediately**
If a key is ever committed or exposed:
1. **Immediately rotate** the key in the service dashboard
2. **Revoke** the exposed key
3. **Update** your local configuration with the new key
4. **Audit** access logs to check for unauthorized usage

### 4. **Use Key Expiration**
Where possible:
- Set expiration dates on API keys
- Use time-limited tokens
- Implement regular key rotation schedules

---

## 📋 File Structure

```
.auth/
├── README.md              ← This file (tracked in Git)
├── keys.example.json      ← Template (tracked in Git)
├── keys.json              ← YOUR ACTUAL KEYS (NEVER COMMITTED)
├── .env.local             ← Local overrides (NEVER COMMITTED)
└── service-accounts/      ← Service-specific configs (NEVER COMMITTED)
    ├── stripe.json
    ├── openai.json
    └── pipedream.json
```

---

## 🚀 Quick Start

### Step 1: Copy the Example File
```bash
cp .auth/keys.example.json .auth/keys.json
```

### Step 2: Fill In Your Keys
Edit `.auth/keys.json` with your actual credentials:
```json
{
  "stripe": {
    "publishable_key": "pk_live_...",
    "secret_key": "sk_live_...",
    "webhook_secret": "whsec_..."
  }
}
```

### Step 3: Verify Git Ignores Your Secrets
```bash
git status
# Should NOT show .auth/keys.json or .auth/.env.local
```

---

## 🔑 Supported Services

### Payment Processors
- **Stripe:** API keys, webhook secrets
- **PayPal:** Client ID, secret
- **Square:** Access tokens

### AI Services
- **OpenAI:** API keys for GPT models
- **Anthropic:** API keys for Claude
- **Cohere:** API keys
- **Hugging Face:** Access tokens

### Automation Platforms
- **Pipedream:** API keys, workflow tokens
- **Zapier:** Webhook URLs, API keys
- **Make.com:** API tokens
- **n8n:** Credentials

### Development Tools
- **GitHub:** Personal access tokens, OAuth apps
- **GitLab:** Access tokens
- **Bitbucket:** App passwords
- **Vercel:** Deploy tokens
- **Netlify:** Access tokens

### Communication
- **Discord:** Webhook URLs, bot tokens
- **Slack:** Webhook URLs, OAuth tokens
- **Twilio:** Account SID, auth tokens
- **SendGrid:** API keys

---

## 🤖 Accessing Keys in Automation

### For Pipedream Workflows
```javascript
// Option 1: Environment variables
const stripeKey = process.env.STRIPE_SECRET_KEY;

// Option 2: Read from file (if mounted)
const fs = require('fs');
const keys = JSON.parse(fs.readFileSync('.auth/keys.json', 'utf8'));
const stripeKey = keys.stripe.secret_key;
```

### For GitHub Actions
```yaml
# Use GitHub Secrets instead of local files
- name: Use Stripe API
  env:
    STRIPE_SECRET_KEY: ${{ secrets.STRIPE_SECRET_KEY }}
  run: |
    # Your automation script
```

### For Local Scripts
```python
# Python example
import json
import os

# Load from JSON file
with open('.auth/keys.json', 'r') as f:
    keys = json.load(f)
    stripe_key = keys['stripe']['secret_key']

# Or use environment variables
stripe_key = os.environ.get('STRIPE_SECRET_KEY')
```

---

## 📖 Key Management by Service

### Stripe
**Where to find keys:**
1. Go to [Stripe Dashboard](https://dashboard.stripe.com/)
2. Navigate to **Developers → API Keys**
3. Copy your keys (use Test keys for development)

**Key types:**
- `pk_live_...` / `pk_test_...` - Publishable key (safe for client-side)
- `sk_live_...` / `sk_test_...` - Secret key (NEVER expose to clients)
- `whsec_...` - Webhook signing secret

**Security notes:**
- Use test keys (`pk_test_`, `sk_test_`) for development
- Only use live keys (`pk_live_`, `sk_live_`) in production
- Rotate keys every 90 days
- Monitor key usage in dashboard

### OpenAI
**Where to find keys:**
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Navigate to **API Keys**
3. Create a new secret key

**Key format:** `sk-...`

**Security notes:**
- Set usage limits on each key
- Create separate keys for different environments
- Monitor usage in dashboard

### GitHub Personal Access Tokens
**Where to create:**
1. Go to **Settings → Developer settings → Personal access tokens**
2. Choose **Tokens (classic)** or **Fine-grained tokens**
3. Set appropriate scopes/permissions

**Security notes:**
- Use fine-grained tokens with minimal permissions
- Set expiration dates (max 90 days recommended)
- Use different tokens for different tools

---

## 🚨 What To Do If Keys Are Exposed

### Immediate Actions (within 5 minutes)
1. **Revoke the exposed key** in the service dashboard
2. **Generate a new key** with a different value
3. **Update your local configuration** with the new key

### Investigation (within 1 hour)
4. **Check access logs** for unauthorized usage
5. **Review recent transactions** (for payment processors)
6. **Scan Git history** to see where exposure occurred

### Prevention (within 24 hours)
7. **Update `.gitignore`** if needed
8. **Implement pre-commit hooks** to catch secrets
9. **Add automated secret scanning** (GitHub Advanced Security)
10. **Document the incident** for future reference

### For Stripe Keys Specifically
- **Check Stripe Dashboard → Logs** for unusual activity
- **Review payments and refunds**
- **Consider enabling fraud detection rules**
- **Contact Stripe support** if unauthorized charges occurred

---

## 🛡️ Advanced Security

### Secret Scanning Tools
```bash
# Install gitleaks for local secret scanning
brew install gitleaks  # macOS
# or download from https://github.com/gitleaks/gitleaks

# Scan your repository
gitleaks detect --source . --verbose

# Scan before committing
gitleaks protect --staged
```

### Pre-commit Hooks
Create `.git/hooks/pre-commit`:
```bash
#!/bin/bash
# Check for potential secrets before committing

if gitleaks protect --staged; then
    echo "✅ No secrets detected"
    exit 0
else
    echo "❌ Potential secrets found! Commit blocked."
    exit 1
fi
```

### Environment-Specific Keys
```bash
# Development
cp .auth/keys.example.json .auth/keys.dev.json

# Staging
cp .auth/keys.example.json .auth/keys.staging.json

# Production (use GitHub Secrets instead)
```

---

## 📚 Additional Resources

- [GitHub Secrets Documentation](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Stripe API Key Best Practices](https://stripe.com/docs/keys)
- [OpenAI API Key Safety](https://platform.openai.com/docs/guides/safety-best-practices)
- [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [12-Factor App Config](https://12factor.net/config)

---

## 🆘 Support

If you're unsure about:
- Whether a key should be committed
- How to rotate a specific type of key
- Setting up automation access

**Default rule: When in doubt, DON'T commit it. Use GitHub Secrets instead.**

---

**Last Updated:** December 2024  
**Repository:** Avalon/Spiral of Pollyoneth  
**Maintainer:** @issdandavis
