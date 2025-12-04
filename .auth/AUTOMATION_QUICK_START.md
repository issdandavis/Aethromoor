# 🤖 Automation Tools Quick Reference

This guide shows automation tools (Pipedream, Zapier, n8n, etc.) how to access API keys from this repository.

---

## 📍 Key Locations

### Option 1: Local Keys (Development)
**File:** `.auth/keys.json`  
**Status:** ✅ Available when running locally  
**Access:** Read JSON file directly

### Option 2: Environment Variables (Recommended)
**Source:** Loaded from `.env` files or GitHub Secrets  
**Status:** ✅ Available in all environments  
**Access:** `process.env.VARIABLE_NAME`

### Option 3: GitHub Secrets (CI/CD)
**Source:** GitHub Repository Secrets  
**Status:** ✅ Available in GitHub Actions only  
**Access:** Via workflow environment variables

---

## 🔑 Available Keys

| Service | JSON Path | Environment Variable | GitHub Secret |
|---------|-----------|---------------------|---------------|
| **Stripe** | `keys.stripe.secret_key` | `STRIPE_SECRET_KEY` | `STRIPE_SECRET_KEY` |
| **Stripe** | `keys.stripe.publishable_key` | `STRIPE_PUBLISHABLE_KEY` | `STRIPE_PUBLISHABLE_KEY` |
| **Stripe** | `keys.stripe.webhook_secret` | `STRIPE_WEBHOOK_SECRET` | `STRIPE_WEBHOOK_SECRET` |
| **OpenAI** | `keys.openai.api_key` | `OPENAI_API_KEY` | `OPENAI_API_KEY` |
| **Anthropic** | `keys.anthropic.api_key` | `ANTHROPIC_API_KEY` | `ANTHROPIC_API_KEY` |
| **Pipedream** | `keys.pipedream.api_key` | `PIPEDREAM_API_KEY` | `PIPEDREAM_API_KEY` |
| **GitHub** | `keys.github.personal_access_token` | `GITHUB_TOKEN` | `GITHUB_TOKEN` |

---

## 📖 Usage Examples

### Pipedream Workflows

#### Method 1: Read from JSON file (local deployment)
```javascript
// In a Pipedream Node.js code step
import fs from 'fs';
import path from 'path';

export default defineComponent({
  async run({ steps, $ }) {
    // Read keys from JSON file
    const keysPath = path.join(process.env.HOME, 'Aethromoor', '.auth', 'keys.json');
    const keys = JSON.parse(fs.readFileSync(keysPath, 'utf8'));
    
    // Access Stripe key
    const stripeKey = keys.stripe.secret_key;
    
    // Use the key
    const stripe = require('stripe')(stripeKey);
    const customers = await stripe.customers.list({ limit: 10 });
    
    return customers;
  }
});
```

#### Method 2: Use environment variables (recommended)
```javascript
// In a Pipedream Node.js code step
export default defineComponent({
  async run({ steps, $ }) {
    // Access from environment variables
    const stripeKey = process.env.STRIPE_SECRET_KEY;
    
    // Use the key
    const stripe = require('stripe')(stripeKey);
    const customers = await stripe.customers.list({ limit: 10 });
    
    return customers;
  }
});
```

#### Method 3: Use Pipedream connected accounts
```javascript
// In Pipedream, connect your Stripe account
// Then reference it in your workflow
export default defineComponent({
  props: {
    stripe: {
      type: "app",
      app: "stripe",
    }
  },
  async run({ steps, $ }) {
    // Pipedream automatically handles authentication
    const customers = await this.stripe.customers.list({ limit: 10 });
    return customers;
  }
});
```

### Zapier Webhooks

#### Trigger Zapier from Code
```javascript
// Node.js example
const axios = require('axios');

async function triggerZapier(data) {
  const webhookUrl = process.env.ZAPIER_WEBHOOK_URL || 
                     require('./.auth/keys.json').zapier.webhook_urls.catch_hook;
  
  const response = await axios.post(webhookUrl, {
    stripe_customer: data.customer_id,
    amount: data.amount,
    timestamp: new Date().toISOString()
  });
  
  return response.data;
}
```

### n8n Workflows

#### Read credentials from JSON
```javascript
// In an n8n Function node
const fs = require('fs');
const keys = JSON.parse(fs.readFileSync('.auth/keys.json', 'utf8'));

// Use credentials
const stripe = require('stripe')(keys.stripe.secret_key);

// Process items
const results = [];
for (const item of items) {
  const customer = await stripe.customers.create({
    email: item.json.email,
    name: item.json.name
  });
  results.push({ json: customer });
}

return results;
```

### Make.com (formerly Integromat)

#### HTTP Request with authentication
```
URL: https://api.stripe.com/v1/customers
Method: GET
Headers:
  Authorization: Bearer {{env.STRIPE_SECRET_KEY}}
```

---

## 🔐 Security Best Practices for Automation

### 1. Never Log Full Keys
```javascript
// ❌ WRONG - logs full key
console.log(`Using key: ${stripeKey}`);

// ✅ CORRECT - logs partial key only
console.log(`Using key: ${stripeKey.substring(0, 10)}...`);
```

### 2. Validate Keys Before Use
```javascript
function validateStripeKey(key) {
  if (!key) {
    throw new Error('Stripe key not found');
  }
  if (!key.startsWith('sk_')) {
    throw new Error('Invalid Stripe key format');
  }
  if (key.includes('test') && process.env.NODE_ENV === 'production') {
    throw new Error('Test key used in production!');
  }
  return true;
}

const stripeKey = process.env.STRIPE_SECRET_KEY;
validateStripeKey(stripeKey);
```

### 3. Handle Missing Keys Gracefully
```javascript
export default defineComponent({
  async run({ steps, $ }) {
    const stripeKey = process.env.STRIPE_SECRET_KEY;
    
    if (!stripeKey) {
      $.export('error', 'STRIPE_SECRET_KEY not configured');
      $.flow.exit('Please configure Stripe API key');
      return;
    }
    
    // Continue with workflow...
  }
});
```

### 4. Use Environment-Specific Keys
```javascript
// Determine environment
const env = process.env.NODE_ENV || 'development';

// Select appropriate key
const stripeKey = env === 'production' 
  ? process.env.STRIPE_LIVE_SECRET_KEY
  : process.env.STRIPE_TEST_SECRET_KEY;

console.log(`Using ${env} environment`);
```

---

## 🚀 Integration Patterns

### Pattern 1: GitHub → Pipedream → Stripe

**Use case:** Create Stripe customer when issue is labeled "customer"

**Setup:**
1. GitHub webhook → Pipedream HTTP trigger
2. Filter for label "customer"
3. Create Stripe customer
4. Comment on issue with customer ID

**Pipedream code:**
```javascript
export default defineComponent({
  async run({ steps, $ }) {
    // GitHub event data
    const issue = steps.trigger.event.issue;
    
    // Check for customer label
    const hasCustomerLabel = issue.labels.some(l => l.name === 'customer');
    if (!hasCustomerLabel) return;
    
    // Create Stripe customer
    const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
    const customer = await stripe.customers.create({
      email: issue.user.email,
      metadata: {
        github_issue: issue.number,
        github_user: issue.user.login
      }
    });
    
    // Store for next step
    return { customer_id: customer.id };
  }
});
```

### Pattern 2: Stripe → Zapier → Discord

**Use case:** Notify Discord when payment succeeds

**Setup:**
1. Stripe webhook → Zapier webhook trigger
2. Filter for `payment_intent.succeeded`
3. Post to Discord webhook

**Zapier webhook:**
```
Trigger: Webhooks by Zapier - Catch Hook
URL: https://hooks.zapier.com/hooks/catch/YOUR_ID/

Action: Webhooks by Zapier - POST
URL: {{env.DISCORD_WEBHOOK_URL}}
Payload:
{
  "content": "💰 Payment received: ${{amount}} from {{customer_email}}"
}
```

### Pattern 3: Scheduled Task → n8n → Multiple APIs

**Use case:** Daily sync of customer data

**n8n workflow:**
```
1. Schedule Trigger (daily 9am)
2. HTTP Request to Stripe (list customers)
3. For each customer:
   - Update Google Sheet
   - Send to Pipedream webhook
   - Log to Discord
```

---

## 🧪 Testing Automation

### Test Connection to Keys

Create a test workflow that verifies all keys are accessible:

```javascript
// Pipedream test workflow
export default defineComponent({
  async run({ steps, $ }) {
    const tests = {
      stripe: !!process.env.STRIPE_SECRET_KEY,
      openai: !!process.env.OPENAI_API_KEY,
      anthropic: !!process.env.ANTHROPIC_API_KEY,
      pipedream: !!process.env.PIPEDREAM_API_KEY
    };
    
    const allConfigured = Object.values(tests).every(v => v);
    
    $.export('tests', tests);
    $.export('status', allConfigured ? 'OK' : 'MISSING_KEYS');
    
    return tests;
  }
});
```

### Test Stripe Connection

```javascript
// Test Stripe API is working
export default defineComponent({
  async run({ steps, $ }) {
    try {
      const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
      
      // Simple API call to verify connection
      const account = await stripe.balance.retrieve();
      
      $.export('status', 'success');
      $.export('account', account);
      
      return { success: true, available: account.available };
    } catch (error) {
      $.export('status', 'error');
      $.export('error', error.message);
      
      return { success: false, error: error.message };
    }
  }
});
```

---

## 📋 Checklist for New Automation

Before deploying a new automation workflow:

- [ ] **Keys configured** - All required API keys are set
- [ ] **Environment checked** - Using correct keys (test vs. live)
- [ ] **Error handling** - Handles missing or invalid keys gracefully
- [ ] **Logging** - Never logs full key values
- [ ] **Testing** - Tested with test/sandbox keys first
- [ ] **Security review** - No secrets in code or logs
- [ ] **Monitoring** - Alerts set up for failures
- [ ] **Documentation** - Workflow documented for team

---

## 🆘 Troubleshooting

### Common Issues

#### 1. "Cannot read property 'stripe' of undefined"

**Cause:** `.auth/keys.json` file not found

**Solution:**
```bash
# Copy template
cp .auth/keys.example.json .auth/keys.json

# Fill in your keys
nano .auth/keys.json
```

#### 2. "stripe.customers is not a function"

**Cause:** Stripe key not loaded correctly

**Solution:**
```javascript
// Verify key is loaded
console.log('Key exists:', !!process.env.STRIPE_SECRET_KEY);
console.log('Key format:', process.env.STRIPE_SECRET_KEY?.substring(0, 7));

// Should show: sk_test or sk_live
```

#### 3. "Invalid API Key provided"

**Cause:** Using wrong key or expired key

**Solution:**
1. Verify key in Stripe Dashboard
2. Check for extra whitespace
3. Regenerate key if needed
4. Update in all locations

---

## 📚 Additional Resources

### Platform Documentation
- [Pipedream Docs](https://pipedream.com/docs)
- [Zapier Developer Docs](https://zapier.com/developer)
- [n8n Documentation](https://docs.n8n.io/)
- [Make.com Help](https://www.make.com/en/help)

### API References
- [Stripe API](https://stripe.com/docs/api)
- [OpenAI API](https://platform.openai.com/docs/api-reference)
- [GitHub API](https://docs.github.com/en/rest)

### Security Guides
- [Avalon Security Guide](./docs/SECURITY.md)
- [GitHub Secrets Setup](./docs/GITHUB_SECRETS_SETUP.md)
- [.auth Directory README](./.auth/README.md)

---

**Quick Start:**
1. Copy `keys.example.json` to `keys.json`
2. Fill in your API keys
3. Test with provided examples
4. Build your automation!

**Remember:** Always use test keys for development, production keys for live workflows.

---

**Last Updated:** December 2024  
**Maintainer:** @issdandavis
