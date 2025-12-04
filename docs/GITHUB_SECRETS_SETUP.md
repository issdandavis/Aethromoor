# 🤖 GitHub Secrets Setup for Automation Tools

This guide shows you how to configure GitHub Secrets so that automation tools like Pipedream, Zapier, and AI agents can access your API keys securely.

---

## 📋 Quick Reference

| Secret Name | Description | Used By |
|-------------|-------------|---------|
| `STRIPE_SECRET_KEY` | Stripe API secret key | Payment workflows, webhooks |
| `STRIPE_PUBLISHABLE_KEY` | Stripe publishable key | Client-side checkout |
| `STRIPE_WEBHOOK_SECRET` | Stripe webhook signature | Webhook verification |
| `ANTHROPIC_API_KEY` | Claude API key | AI workers, content generation |
| `OPENAI_API_KEY` | OpenAI API key | GPT integrations, AI tools |
| `PIPEDREAM_API_KEY` | Pipedream account key | Pipedream workflows |
| `ZAPIER_WEBHOOK_URL` | Zapier webhook endpoint | Zapier integrations |
| `DISCORD_WEBHOOK_URL` | Discord channel webhook | Notifications |
| `GITHUB_TOKEN` | Personal access token | Repository operations |

---

## 🎯 Adding Secrets to GitHub

### Step-by-Step Guide

1. **Navigate to Repository Settings**
   ```
   Go to: https://github.com/issdandavis/Aethromoor/settings/secrets/actions
   
   Or manually:
   Repository → Settings → Secrets and variables → Actions
   ```

2. **Click "New repository secret"**

3. **Add Secret Information**
   - **Name:** Enter secret name (e.g., `STRIPE_SECRET_KEY`)
   - **Secret:** Paste the actual key value
   - **Note:** Add optional description for team context

4. **Click "Add secret"**

5. **Repeat for all required secrets**

---

## 🔑 Stripe Configuration

### Required Secrets

#### 1. STRIPE_SECRET_KEY
- **Where to get:** [Stripe Dashboard](https://dashboard.stripe.com/apikeys)
- **Format:** `sk_live_...` (production) or `sk_test_...` (development)
- **Usage:** Server-side payment processing
- **⚠️ Critical:** Use test keys until ready for production

**Add to GitHub:**
```
Name: STRIPE_SECRET_KEY
Value: sk_live_YOUR_NEW_ROTATED_KEY_HERE
```
**⚠️ CRITICAL:** DO NOT use the key from the issue - it was exposed and must be rotated first!

#### 2. STRIPE_PUBLISHABLE_KEY
- **Where to get:** [Stripe Dashboard](https://dashboard.stripe.com/apikeys)
- **Format:** `pk_live_...` or `pk_test_...`
- **Usage:** Client-side Stripe.js initialization
- **Note:** Safe to expose in frontend code

**Add to GitHub:**
```
Name: STRIPE_PUBLISHABLE_KEY
Value: pk_live_YOUR_PUBLISHABLE_KEY_HERE
```

#### 3. STRIPE_WEBHOOK_SECRET
- **Where to get:** Stripe Dashboard → Developers → Webhooks → Your endpoint
- **Format:** `whsec_...`
- **Usage:** Verifying webhook signatures
- **Critical:** Prevents webhook spoofing

**Add to GitHub:**
```
Name: STRIPE_WEBHOOK_SECRET
Value: whsec_YOUR_WEBHOOK_SECRET_HERE
```

---

## 🤖 AI Services Configuration

### Anthropic (Claude)

**Where to get:** [Anthropic Console](https://console.anthropic.com/)

```
Name: ANTHROPIC_API_KEY
Value: sk-ant-YOUR_API_KEY_HERE
```

**Usage in workflows:**
```yaml
- name: Run AI content generation
  env:
    ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
  run: |
    python .github/scripts/content_generator.py
```

### OpenAI (GPT)

**Where to get:** [OpenAI Platform](https://platform.openai.com/api-keys)

```
Name: OPENAI_API_KEY
Value: sk-YOUR_OPENAI_API_KEY_HERE
```

**Usage in workflows:**
```yaml
- name: Run GPT integration
  env:
    OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
  run: |
    node scripts/gpt-assistant.js
```

---

## 🔗 Automation Platform Configuration

### Pipedream

#### Required Secrets

**1. API Key (for workflow management)**
```
Name: PIPEDREAM_API_KEY
Value: YOUR_PIPEDREAM_API_KEY
```

**Where to get:**
1. Go to [Pipedream Settings](https://pipedream.com/settings/account)
2. Create new API key
3. Copy the key value

**2. Webhook URLs (for triggering workflows)**
```
Name: PIPEDREAM_WEBHOOK_STRIPE
Value: https://eoxxxxxxxxxxx.m.pipedream.net

Name: PIPEDREAM_WEBHOOK_GITHUB
Value: https://eoyyyyyyyyyy.m.pipedream.net
```

**Where to get:**
1. Create workflow in Pipedream
2. Add HTTP trigger
3. Copy the endpoint URL

#### Using in GitHub Actions

```yaml
name: Trigger Pipedream Workflow

on:
  push:
    branches: [main]

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Pipedream
        run: |
          curl -X POST ${{ secrets.PIPEDREAM_WEBHOOK_GITHUB }} \
            -H "Content-Type: application/json" \
            -d '{"event": "push", "branch": "${{ github.ref }}"}'
```

### Zapier

#### Required Secrets

**Webhook URLs only** (Zapier doesn't use API keys for webhooks)

```
Name: ZAPIER_WEBHOOK_PAYMENTS
Value: https://hooks.zapier.com/hooks/catch/YOUR_HOOK_ID/

Name: ZAPIER_WEBHOOK_NOTIFICATIONS
Value: https://hooks.zapier.com/hooks/catch/YOUR_HOOK_ID/
```

**Where to get:**
1. Create Zap in Zapier
2. Choose "Webhooks by Zapier" as trigger
3. Select "Catch Hook"
4. Copy the custom webhook URL

#### Using in GitHub Actions

```yaml
- name: Notify Zapier
  run: |
    curl -X POST ${{ secrets.ZAPIER_WEBHOOK_NOTIFICATIONS }} \
      -H "Content-Type: application/json" \
      -d '{"title": "${{ github.event.head_commit.message }}"}'
```

---

## 📢 Communication Platforms

### Discord

**Where to get webhook:**
1. Go to Discord channel
2. Channel Settings → Integrations → Webhooks
3. Create webhook
4. Copy webhook URL

```
Name: DISCORD_WEBHOOK_URL
Value: https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_TOKEN
```

**Usage:**
```yaml
- name: Send Discord notification
  run: |
    curl -X POST ${{ secrets.DISCORD_WEBHOOK_URL }} \
      -H "Content-Type: application/json" \
      -d '{"content": "Deployment successful! 🚀"}'
```

### Slack

**Where to get webhook:**
1. Go to [Slack API](https://api.slack.com/apps)
2. Create new app
3. Add "Incoming Webhooks"
4. Copy webhook URL

```
Name: SLACK_WEBHOOK_URL
Value: https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

---

## 🔐 Accessing Secrets in Workflows

### Basic Usage

```yaml
name: Deploy with Secrets

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup environment
        env:
          STRIPE_SECRET_KEY: ${{ secrets.STRIPE_SECRET_KEY }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          echo "Deploying with configured secrets..."
          # Secrets are available as environment variables
          ./deploy.sh
```

### Multiple Secrets

```yaml
- name: Run automation script
  env:
    # Payment
    STRIPE_SECRET_KEY: ${{ secrets.STRIPE_SECRET_KEY }}
    STRIPE_WEBHOOK_SECRET: ${{ secrets.STRIPE_WEBHOOK_SECRET }}
    
    # AI
    ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
    OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
    
    # Automation
    PIPEDREAM_API_KEY: ${{ secrets.PIPEDREAM_API_KEY }}
    
    # Notifications
    DISCORD_WEBHOOK_URL: ${{ secrets.DISCORD_WEBHOOK_URL }}
  run: |
    python automation/run_all.py
```

### Conditional Secrets

```yaml
- name: Deploy to production
  if: github.ref == 'refs/heads/main'
  env:
    STRIPE_SECRET_KEY: ${{ secrets.STRIPE_SECRET_KEY }}  # Live key
    STRIPE_PUBLISHABLE_KEY: ${{ secrets.STRIPE_PUBLISHABLE_KEY }}
  run: |
    npm run deploy:production
    
- name: Deploy to staging
  if: github.ref == 'refs/heads/develop'
  env:
    STRIPE_SECRET_KEY: ${{ secrets.STRIPE_TEST_SECRET_KEY }}  # Test key
    STRIPE_PUBLISHABLE_KEY: ${{ secrets.STRIPE_TEST_PUBLISHABLE_KEY }}
  run: |
    npm run deploy:staging
```

---

## 🧪 Testing Secret Configuration

### Verify Secrets Are Set

```yaml
name: Test Secrets Configuration

on:
  workflow_dispatch:

jobs:
  test-secrets:
    runs-on: ubuntu-latest
    steps:
      - name: Check Stripe secrets
        env:
          STRIPE_SECRET_KEY: ${{ secrets.STRIPE_SECRET_KEY }}
        run: |
          if [ -z "$STRIPE_SECRET_KEY" ]; then
            echo "❌ STRIPE_SECRET_KEY not set"
            exit 1
          else
            echo "✅ STRIPE_SECRET_KEY is configured"
            echo "Key starts with: ${STRIPE_SECRET_KEY:0:10}..."
          fi
      
      - name: Check AI secrets
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          [ -n "$ANTHROPIC_API_KEY" ] && echo "✅ ANTHROPIC_API_KEY configured" || echo "❌ ANTHROPIC_API_KEY missing"
          [ -n "$OPENAI_API_KEY" ] && echo "✅ OPENAI_API_KEY configured" || echo "❌ OPENAI_API_KEY missing"
```

### Test Stripe Connection

```yaml
- name: Test Stripe API
  env:
    STRIPE_SECRET_KEY: ${{ secrets.STRIPE_SECRET_KEY }}
  run: |
    # Install Stripe CLI
    pip install stripe
    
    # Test API connection
    python - <<EOF
    import stripe
    import os
    
    stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
    
    try:
        # Retrieve account info
        account = stripe.Account.retrieve()
        print(f"✅ Stripe connected: {account.email}")
    except Exception as e:
        print(f"❌ Stripe connection failed: {e}")
        exit(1)
    EOF
```

---

## 🔄 Secret Rotation

### When to Rotate Secrets

- **Immediately:** If exposed in commits, logs, or public
- **Every 90 days:** Regular security practice
- **When team member leaves:** Revoke access
- **After security incident:** Precautionary measure

### Rotation Process

1. **Generate new secret** in service dashboard
2. **Update GitHub Secret** with new value
3. **Test workflows** to ensure they work
4. **Revoke old secret** in service dashboard
5. **Document rotation** in security log

### Example: Rotating Stripe Key

```bash
# 1. Generate new key in Stripe Dashboard
# Dashboard → Developers → API Keys → Roll key

# 2. Update GitHub Secret
# Go to: Settings → Secrets → STRIPE_SECRET_KEY → Update

# 3. Test the new key
# Run a workflow that uses Stripe

# 4. If successful, old key is automatically revoked by Stripe
```

---

## 📊 Monitoring Secret Usage

### GitHub Actions Logs

Secrets are automatically masked in logs:
```
Using secret: sk_live_***...***
```

### Stripe Dashboard

Monitor API key usage:
1. Go to Stripe Dashboard
2. Developers → API Keys
3. Click on key to see usage stats
4. Review "Recent requests"

### Best Practices

- ✅ Set up alerts for unusual activity
- ✅ Review logs weekly
- ✅ Monitor for failed authentication
- ✅ Track which workflows use which secrets
- ❌ Never log full secret values
- ❌ Don't expose secrets in error messages

---

## ⚠️ Security Warnings

### Common Mistakes to Avoid

1. **Don't echo secrets in workflows:**
   ```yaml
   # ❌ WRONG - secret will appear in logs
   - run: echo "API Key is ${{ secrets.STRIPE_SECRET_KEY }}"
   
   # ✅ CORRECT - reference without echoing
   - run: ./deploy.sh
     env:
       STRIPE_SECRET_KEY: ${{ secrets.STRIPE_SECRET_KEY }}
   ```

2. **Don't pass secrets as command arguments:**
   ```yaml
   # ❌ WRONG - visible in process list
   - run: ./script.sh ${{ secrets.API_KEY }}
   
   # ✅ CORRECT - use environment variables
   - run: ./script.sh
     env:
       API_KEY: ${{ secrets.API_KEY }}
   ```

3. **Don't commit secrets to repository:**
   ```yaml
   # ❌ WRONG - hardcoded secret
   STRIPE_KEY: sk_live_12345...
   
   # ✅ CORRECT - use GitHub Secret
   STRIPE_KEY: ${{ secrets.STRIPE_SECRET_KEY }}
   ```

---

## 🆘 Troubleshooting

### Secret Not Found

**Error:** `Context access might be invalid: secrets.STRIPE_SECRET_KEY`

**Solution:**
1. Verify secret name matches exactly (case-sensitive)
2. Check secret is added to correct repository
3. Ensure workflow has access to secrets

### Secret Not Working

**Error:** Authentication failed or invalid API key

**Solution:**
1. Verify secret value is correct (copy-paste errors)
2. Check for extra whitespace in secret value
3. Confirm API key is active in service dashboard
4. Try rotating the key

### Workflows Not Triggering

**Issue:** Pipedream/Zapier webhooks not receiving data

**Solution:**
1. Test webhook URL manually with `curl`
2. Check webhook URL is correct
3. Verify workflow is enabled in Pipedream/Zapier
4. Check network connectivity

---

## 📚 Additional Resources

- [GitHub Secrets Documentation](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Stripe API Keys Best Practices](https://stripe.com/docs/keys)
- [Pipedream Documentation](https://pipedream.com/docs)
- [Zapier Webhook Documentation](https://zapier.com/apps/webhook/help)

---

**Next Steps:**
1. Add all required secrets to GitHub
2. Test workflows with secrets
3. Set up monitoring and alerts
4. Schedule regular secret rotation

**Remember:** Never commit secrets to code. Always use GitHub Secrets for automation.

---

**Last Updated:** December 2024  
**Maintainer:** @issdandavis
