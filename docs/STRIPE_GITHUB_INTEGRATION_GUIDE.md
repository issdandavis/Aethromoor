# 🔧 Stripe + GitHub Integration Technical Guide
## Step-by-Step Implementation for Payment Processing & Content Delivery

**Last Updated:** November 2025  
**Difficulty:** Intermediate  
**Estimated Time:** 4-6 hours

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Stripe Setup](#stripe-setup)
3. [GitHub Setup](#github-setup)
4. [Webhook Server](#webhook-server)
5. [Payment Flow](#payment-flow)
6. [Access Control](#access-control)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Troubleshooting](#troubleshooting)

---

## 🎯 Prerequisites

### Required Accounts

- [x] Stripe account (stripe.com)
- [x] GitHub account with organization (for Teams feature)
- [ ] Domain name (optional but recommended)
- [ ] Hosting service for webhook server (Vercel, Netlify, or Heroku)

### Required Skills

- Basic JavaScript/Node.js knowledge
- Understanding of REST APIs
- Git/GitHub familiarity
- Basic web development (HTML/CSS)

### Tools Needed

- Node.js (v16 or higher)
- Git CLI
- Code editor (VS Code recommended)
- Stripe CLI (for testing webhooks)

---

## 💳 Stripe Setup

### Step 1: Create Stripe Account

```bash
# 1. Go to stripe.com and sign up
# 2. Verify your email
# 3. Complete business profile
# 4. Add bank account for payouts
```

### Step 2: Get API Keys

```bash
# Navigate to: Developers → API Keys
# Copy these keys (NEVER commit to Git):

STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
```

**Store in `.env` file:**
```bash
# Create .env in project root
cat > .env << EOF
STRIPE_PUBLIC_KEY=pk_test_51...
STRIPE_SECRET_KEY=sk_test_51...
STRIPE_WEBHOOK_SECRET=whsec_...
GITHUB_TOKEN=ghp_...
GITHUB_ORG=issdandavis
EOF

# Add to .gitignore
echo ".env" >> .gitignore
```

### Step 3: Create Products

**Via Stripe Dashboard:**

```
Products → Create Product

Product 1: Apprentice Tier
- Name: Apprentice Tier - Monthly Subscription
- Description: Access to full game + monthly exclusive content
- Pricing: $2.99 USD / month
- Recurring: Monthly
- Product ID: prod_apprentice

Product 2: Mage Tier
- Name: Mage Tier - Monthly Subscription
- Description: Early access + exclusive lore + beta testing
- Pricing: $6.99 USD / month
- Recurring: Monthly
- Product ID: prod_mage

Product 3: Master Tier
- Name: Master Tier - Monthly Subscription
- Description: Full access + personal consultation + merchandise
- Pricing: $14.99 USD / month
- Recurring: Monthly
- Product ID: prod_master

Product 4: Full Game (One-Time)
- Name: Polly's Wingscroll - Full Game
- Description: Complete game with all endings
- Pricing: $4.99 USD
- Recurring: One-time
- Product ID: prod_game_full
```

**Or via API:**

```javascript
// create-products.js
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

async function createProducts() {
  // Create Apprentice Tier
  const apprentice = await stripe.products.create({
    name: 'Apprentice Tier - Monthly Subscription',
    description: 'Access to full game + monthly exclusive content',
    metadata: {
      tier: 'apprentice',
      github_team: 'apprentice-tier'
    }
  });

  const apprenticePrice = await stripe.prices.create({
    product: apprentice.id,
    unit_amount: 299, // $2.99 in cents
    currency: 'usd',
    recurring: { interval: 'month' }
  });

  // Create Mage Tier
  const mage = await stripe.products.create({
    name: 'Mage Tier - Monthly Subscription',
    description: 'Early access + exclusive lore + beta testing',
    metadata: {
      tier: 'mage',
      github_team: 'mage-tier'
    }
  });

  const magePrice = await stripe.prices.create({
    product: mage.id,
    unit_amount: 699, // $6.99 in cents
    currency: 'usd',
    recurring: { interval: 'month' }
  });

  // Create Master Tier
  const master = await stripe.products.create({
    name: 'Master Tier - Monthly Subscription',
    description: 'Full access + consultation + merchandise',
    metadata: {
      tier: 'master',
      github_team: 'master-tier'
    }
  });

  const masterPrice = await stripe.prices.create({
    product: master.id,
    unit_amount: 1499, // $14.99 in cents
    currency: 'usd',
    recurring: { interval: 'month' }
  });

  console.log('Products created successfully!');
  console.log('Apprentice Price ID:', apprenticePrice.id);
  console.log('Mage Price ID:', magePrice.id);
  console.log('Master Price ID:', masterPrice.id);
}

createProducts();
```

### Step 4: Configure Webhooks

```bash
# In Stripe Dashboard:
# Developers → Webhooks → Add Endpoint

# Endpoint URL (update with your domain):
https://your-domain.com/api/stripe-webhook

# Events to listen for:
✓ checkout.session.completed
✓ customer.subscription.created
✓ customer.subscription.updated
✓ customer.subscription.deleted
✓ invoice.payment_succeeded
✓ invoice.payment_failed
```

---

## 🐙 GitHub Setup

### Step 1: Create Organization Teams

```bash
# Via GitHub Web UI:
# Organization → Teams → New Team

# Create these teams:
1. apprentice-tier
   - Description: Apprentice tier subscribers
   - Privacy: Secret

2. mage-tier
   - Description: Mage tier subscribers
   - Privacy: Secret

3. master-tier
   - Description: Master tier subscribers
   - Privacy: Secret
```

### Step 2: Create Private Repository

```bash
# Create new repository:
Repository name: Aethromoor-Premium
Description: Premium content for Avalon subscribers
Visibility: Private
Initialize: Yes (with README)

# Add teams with appropriate permissions:
apprentice-tier → Read access
mage-tier → Read access
master-tier → Maintain access
```

### Step 3: Generate GitHub Personal Access Token

```bash
# Settings → Developer Settings → Personal Access Tokens → Tokens (classic)

# Create new token with these scopes:
✓ repo (all)
✓ admin:org (read:org, write:org)
✓ user (read:user, user:email)

# Copy token and store in .env:
GITHUB_TOKEN=ghp_...
```

### Step 4: Set Up Repository Structure

```bash
# Clone premium repository
git clone https://github.com/issdandavis/Aethromoor-Premium.git
cd Aethromoor-Premium

# Create directory structure
mkdir -p {game-full,dlc,beta,assets,docs}

# Create README
cat > README.md << EOF
# Avalon Premium Content

Welcome to the premium content repository!

## Access Levels

- **Apprentice Tier**: Full game + monthly content
- **Mage Tier**: Everything + early access + source code
- **Master Tier**: Everything + exclusive features

## Download Instructions

1. Navigate to the \`game-full\` directory
2. Download \`index.html\`
3. Open in your browser
4. Enjoy!

For support, contact: support@your-domain.com
EOF

git add .
git commit -m "Initial premium repository structure"
git push
```

---

## 🔌 Webhook Server Setup

### Step 1: Create Node.js Server

**Project Structure:**
```
webhook-server/
├── package.json
├── index.js
├── routes/
│   ├── stripe-webhook.js
│   └── health.js
├── services/
│   ├── stripe-service.js
│   └── github-service.js
├── utils/
│   └── logger.js
└── .env
```

**Initialize project:**

```bash
mkdir webhook-server
cd webhook-server
npm init -y

# Install dependencies
npm install express stripe @octokit/rest dotenv body-parser
npm install --save-dev nodemon
```

### Step 2: Create Main Server File

**`index.js`:**

```javascript
require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

// Health check (for monitoring)
app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Stripe webhook (raw body required)
app.post(
  '/api/stripe-webhook',
  bodyParser.raw({ type: 'application/json' }),
  require('./routes/stripe-webhook')
);

// Other routes use JSON parser
app.use(bodyParser.json());

app.listen(PORT, () => {
  console.log(`Webhook server running on port ${PORT}`);
});
```

### Step 3: Create Stripe Webhook Handler

**`routes/stripe-webhook.js`:**

```javascript
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
const { addUserToGitHub, removeUserFromGitHub } = require('../services/github-service');
const { sendWelcomeEmail, sendCancellationEmail } = require('../services/email-service');

module.exports = async (req, res) => {
  const sig = req.headers['stripe-signature'];
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;

  let event;

  try {
    // Verify webhook signature
    event = stripe.webhooks.constructEvent(req.body, sig, webhookSecret);
  } catch (err) {
    console.error('Webhook signature verification failed:', err.message);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Handle the event
  try {
    switch (event.type) {
      case 'checkout.session.completed':
        await handleCheckoutCompleted(event.data.object);
        break;

      case 'customer.subscription.created':
        await handleSubscriptionCreated(event.data.object);
        break;

      case 'customer.subscription.deleted':
        await handleSubscriptionDeleted(event.data.object);
        break;

      case 'invoice.payment_succeeded':
        await handlePaymentSucceeded(event.data.object);
        break;

      case 'invoice.payment_failed':
        await handlePaymentFailed(event.data.object);
        break;

      default:
        console.log(`Unhandled event type: ${event.type}`);
    }

    res.json({ received: true });
  } catch (err) {
    console.error('Error processing webhook:', err);
    res.status(500).send('Webhook processing error');
  }
};

async function handleCheckoutCompleted(session) {
  console.log('Checkout completed:', session.id);

  // Get customer details
  const customer = await stripe.customers.retrieve(session.customer);
  const githubUsername = session.metadata.github_username;
  const tier = session.metadata.tier;

  if (!githubUsername) {
    console.error('No GitHub username in session metadata');
    return;
  }

  // Add user to appropriate GitHub team
  await addUserToGitHub(githubUsername, tier);

  // Send welcome email
  await sendWelcomeEmail(customer.email, githubUsername, tier);

  console.log(`Added ${githubUsername} to ${tier} tier`);
}

async function handleSubscriptionCreated(subscription) {
  console.log('Subscription created:', subscription.id);
  // Additional logic if needed
}

async function handleSubscriptionDeleted(subscription) {
  console.log('Subscription deleted:', subscription.id);

  // Get customer details
  const customer = await stripe.customers.retrieve(subscription.customer);
  const metadata = customer.metadata;

  if (metadata.github_username && metadata.tier) {
    // Remove user from GitHub team
    await removeUserFromGitHub(metadata.github_username, metadata.tier);

    // Send cancellation email
    await sendCancellationEmail(customer.email, metadata.github_username);

    console.log(`Removed ${metadata.github_username} from ${metadata.tier} tier`);
  }
}

async function handlePaymentSucceeded(invoice) {
  console.log('Payment succeeded:', invoice.id);
  // Log successful payment, update analytics, etc.
}

async function handlePaymentFailed(invoice) {
  console.log('Payment failed:', invoice.id);
  // Send dunning email, notify customer, etc.
}
```

### Step 4: Create GitHub Service

**`services/github-service.js`:**

```javascript
const { Octokit } = require('@octokit/rest');

const octokit = new Octokit({
  auth: process.env.GITHUB_TOKEN
});

const ORG = process.env.GITHUB_ORG || 'issdandavis';

// Team slugs for each tier
const TEAM_SLUGS = {
  'apprentice': 'apprentice-tier',
  'mage': 'mage-tier',
  'master': 'master-tier'
};

async function addUserToGitHub(username, tier) {
  const teamSlug = TEAM_SLUGS[tier];

  if (!teamSlug) {
    throw new Error(`Invalid tier: ${tier}`);
  }

  try {
    // Add user to organization team
    await octokit.teams.addOrUpdateMembershipForUserInOrg({
      org: ORG,
      team_slug: teamSlug,
      username: username,
      role: 'member'
    });

    console.log(`Successfully added ${username} to ${teamSlug}`);
    return true;
  } catch (error) {
    console.error(`Error adding ${username} to ${teamSlug}:`, error.message);
    throw error;
  }
}

async function removeUserFromGitHub(username, tier) {
  const teamSlug = TEAM_SLUGS[tier];

  if (!teamSlug) {
    throw new Error(`Invalid tier: ${tier}`);
  }

  try {
    // Remove user from organization team
    await octokit.teams.removeMembershipForUserInOrg({
      org: ORG,
      team_slug: teamSlug,
      username: username
    });

    console.log(`Successfully removed ${username} from ${teamSlug}`);
    return true;
  } catch (error) {
    console.error(`Error removing ${username} from ${teamSlug}:`, error.message);
    throw error;
  }
}

async function verifyUserAccess(username, tier) {
  const teamSlug = TEAM_SLUGS[tier];

  try {
    const { data } = await octokit.teams.getMembershipForUserInOrg({
      org: ORG,
      team_slug: teamSlug,
      username: username
    });

    return data.state === 'active';
  } catch (error) {
    return false;
  }
}

module.exports = {
  addUserToGitHub,
  removeUserFromGitHub,
  verifyUserAccess
};
```

---

## 💰 Payment Flow Implementation

### Step 1: Create Checkout Page

**`checkout.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Avalon Premium - Subscribe</title>
  <script src="https://js.stripe.com/v3/"></script>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: #333;
    }
    .container {
      background: white;
      border-radius: 10px;
      padding: 40px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    .tier-cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin: 30px 0;
    }
    .tier-card {
      border: 2px solid #e0e0e0;
      border-radius: 8px;
      padding: 30px;
      text-align: center;
      transition: transform 0.2s, border-color 0.2s;
    }
    .tier-card:hover {
      transform: translateY(-5px);
      border-color: #667eea;
    }
    .tier-card.featured {
      border-color: #667eea;
      position: relative;
      overflow: hidden;
    }
    .tier-card.featured::before {
      content: 'POPULAR';
      position: absolute;
      top: 10px;
      right: -30px;
      background: #667eea;
      color: white;
      padding: 5px 40px;
      transform: rotate(45deg);
      font-size: 12px;
      font-weight: bold;
    }
    .tier-name {
      font-size: 24px;
      font-weight: bold;
      margin-bottom: 10px;
      color: #667eea;
    }
    .tier-price {
      font-size: 36px;
      font-weight: bold;
      margin: 20px 0;
    }
    .tier-price small {
      font-size: 16px;
      color: #666;
    }
    .tier-features {
      list-style: none;
      padding: 0;
      margin: 20px 0;
      text-align: left;
    }
    .tier-features li {
      padding: 10px 0;
      border-bottom: 1px solid #f0f0f0;
    }
    .tier-features li::before {
      content: '✓ ';
      color: #667eea;
      font-weight: bold;
      margin-right: 10px;
    }
    .subscribe-btn {
      background: #667eea;
      color: white;
      border: none;
      padding: 15px 30px;
      border-radius: 5px;
      font-size: 16px;
      cursor: pointer;
      width: 100%;
      transition: background 0.2s;
    }
    .subscribe-btn:hover {
      background: #5568d3;
    }
    .github-input {
      width: 100%;
      padding: 10px;
      margin: 10px 0;
      border: 1px solid #ddd;
      border-radius: 5px;
      font-size: 14px;
    }
    .input-group {
      margin-bottom: 15px;
      text-align: left;
    }
    .input-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: 500;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1 style="text-align: center; color: #667eea;">Choose Your Tier</h1>
    <p style="text-align: center; color: #666; margin-bottom: 40px;">
      Get access to premium Avalon content and join our community
    </p>

    <div class="tier-cards">
      <!-- Apprentice Tier -->
      <div class="tier-card">
        <div class="tier-name">Apprentice</div>
        <div class="tier-price">$2.99<small>/month</small></div>
        <ul class="tier-features">
          <li>Full game access</li>
          <li>Monthly exclusive stories</li>
          <li>Discord community</li>
          <li>Vote on content</li>
          <li>Name in credits</li>
        </ul>
        <div class="input-group">
          <label for="github-apprentice">GitHub Username:</label>
          <input type="text" id="github-apprentice" class="github-input" 
                 placeholder="your-github-username" required>
        </div>
        <button class="subscribe-btn" onclick="subscribe('apprentice')">
          Subscribe Now
        </button>
      </div>

      <!-- Mage Tier (Featured) -->
      <div class="tier-card featured">
        <div class="tier-name">Mage</div>
        <div class="tier-price">$6.99<small>/month</small></div>
        <ul class="tier-features">
          <li>Everything in Apprentice</li>
          <li>Early access (2 weeks)</li>
          <li>Source code access</li>
          <li>Exclusive lore docs</li>
          <li>Beta testing</li>
          <li>Free DLC</li>
        </ul>
        <div class="input-group">
          <label for="github-mage">GitHub Username:</label>
          <input type="text" id="github-mage" class="github-input" 
                 placeholder="your-github-username" required>
        </div>
        <button class="subscribe-btn" onclick="subscribe('mage')">
          Subscribe Now
        </button>
      </div>

      <!-- Master Tier -->
      <div class="tier-card">
        <div class="tier-name">Master</div>
        <div class="tier-price">$14.99<small>/month</small></div>
        <ul class="tier-features">
          <li>Everything in Mage</li>
          <li>1-on-1 consultation</li>
          <li>Story collaboration</li>
          <li>Full source access</li>
          <li>Commercial license</li>
          <li>Physical merch</li>
          <li>Character naming</li>
        </ul>
        <div class="input-group">
          <label for="github-master">GitHub Username:</label>
          <input type="text" id="github-master" class="github-input" 
                 placeholder="your-github-username" required>
        </div>
        <button class="subscribe-btn" onclick="subscribe('master')">
          Subscribe Now
        </button>
      </div>
    </div>

    <p style="text-align: center; color: #666; margin-top: 40px;">
      Cancel anytime. 14-day money-back guarantee.
    </p>
  </div>

  <script>
    // Initialize Stripe
    const stripe = Stripe('YOUR_STRIPE_PUBLIC_KEY');

    // Price IDs for each tier (get from Stripe Dashboard)
    const PRICE_IDS = {
      'apprentice': 'price_...',
      'mage': 'price_...',
      'master': 'price_...'
    };

    async function subscribe(tier) {
      // Get GitHub username
      const githubUsername = document.getElementById(`github-${tier}`).value.trim();

      if (!githubUsername) {
        alert('Please enter your GitHub username');
        return;
      }

      // Validate GitHub username format
      if (!/^[a-z\d](?:[a-z\d]|-(?=[a-z\d])){0,38}$/i.test(githubUsername)) {
        alert('Please enter a valid GitHub username');
        return;
      }

      try {
        // Create checkout session
        const response = await fetch('/api/create-checkout-session', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            priceId: PRICE_IDS[tier],
            githubUsername: githubUsername,
            tier: tier
          })
        });

        const { sessionId } = await response.json();

        // Redirect to Stripe Checkout
        const { error } = await stripe.redirectToCheckout({ sessionId });

        if (error) {
          console.error('Stripe error:', error);
          alert('An error occurred. Please try again.');
        }
      } catch (err) {
        console.error('Subscription error:', err);
        alert('An error occurred. Please try again.');
      }
    }
  </script>
</body>
</html>
```

### Step 2: Create Checkout Session Endpoint

**`routes/create-checkout-session.js`:**

```javascript
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

module.exports = async (req, res) => {
  const { priceId, githubUsername, tier } = req.body;

  if (!priceId || !githubUsername || !tier) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  try {
    const session = await stripe.checkout.sessions.create({
      mode: 'subscription',
      payment_method_types: ['card'],
      line_items: [
        {
          price: priceId,
          quantity: 1,
        },
      ],
      success_url: `${process.env.DOMAIN}/success?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${process.env.DOMAIN}/checkout`,
      customer_email: req.body.email, // Optional: pre-fill email
      metadata: {
        github_username: githubUsername,
        tier: tier
      },
      // Save GitHub username to customer metadata
      subscription_data: {
        metadata: {
          github_username: githubUsername,
          tier: tier
        }
      }
    });

    res.json({ sessionId: session.id });
  } catch (err) {
    console.error('Error creating checkout session:', err);
    res.status(500).json({ error: 'Failed to create checkout session' });
  }
};
```

---

## ✅ Testing

### Step 1: Test Locally with Stripe CLI

```bash
# Install Stripe CLI
# macOS:
brew install stripe/stripe-cli/stripe

# Windows:
scoop bucket add stripe https://github.com/stripe/scoop-stripe-cli.git
scoop install stripe

# Login to Stripe
stripe login

# Forward webhooks to local server
stripe listen --forward-to localhost:3000/api/stripe-webhook

# This will give you a webhook secret (whsec_...)
# Add it to your .env file as STRIPE_WEBHOOK_SECRET
```

### Step 2: Test Payment Flow

```bash
# Start your webhook server
npm run dev

# In another terminal, trigger a test webhook
stripe trigger checkout.session.completed

# Check your server logs for webhook processing
```

### Step 3: Test GitHub Integration

```javascript
// test-github.js
require('dotenv').config();
const { addUserToGitHub, removeUserFromGitHub } = require('./services/github-service');

async function test() {
  try {
    // Test adding user
    console.log('Adding test user...');
    await addUserToGitHub('test-username', 'apprentice');
    console.log('Success!');

    // Wait a bit
    await new Promise(resolve => setTimeout(resolve, 5000));

    // Test removing user
    console.log('Removing test user...');
    await removeUserFromGitHub('test-username', 'apprentice');
    console.log('Success!');
  } catch (err) {
    console.error('Test failed:', err);
  }
}

test();
```

---

## 🚀 Deployment

### Option 1: Deploy to Vercel (Recommended)

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
vercel

# Set environment variables in Vercel dashboard
# Settings → Environment Variables:
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
GITHUB_TOKEN=ghp_...
GITHUB_ORG=issdandavis

# Update Stripe webhook URL to:
https://your-project.vercel.app/api/stripe-webhook
```

### Option 2: Deploy to Heroku

```bash
# Install Heroku CLI
brew tap heroku/brew && brew install heroku

# Login
heroku login

# Create app
heroku create avalon-webhook-server

# Set environment variables
heroku config:set STRIPE_SECRET_KEY=sk_live_...
heroku config:set STRIPE_WEBHOOK_SECRET=whsec_...
heroku config:set GITHUB_TOKEN=ghp_...
heroku config:set GITHUB_ORG=issdandavis

# Deploy
git push heroku main

# Update Stripe webhook URL to:
https://avalon-webhook-server.herokuapp.com/api/stripe-webhook
```

---

## 🔍 Troubleshooting

### Common Issues

**1. Webhook signature verification fails**
```
Error: No signatures found matching the expected signature
Solution: Ensure STRIPE_WEBHOOK_SECRET matches the value from Stripe Dashboard
```

**2. GitHub user not added to team**
```
Error: User not found or insufficient permissions
Solution: 
- Verify GitHub username is correct
- Ensure user has accepted organization invitation
- Check GitHub token has correct permissions
```

**3. Payment succeeds but webhook not triggered**
```
Solution:
- Check webhook URL is correct in Stripe Dashboard
- Verify endpoint is accessible (not localhost)
- Check server logs for errors
```

**4. CORS errors on checkout page**
```
Solution: Add CORS headers to webhook server:
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Content-Type');
  next();
});
```

---

## 📚 Additional Resources

- [Stripe Documentation](https://stripe.com/docs)
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Stripe Webhook Guide](https://stripe.com/docs/webhooks)
- [GitHub Teams API](https://docs.github.com/en/rest/teams)

---

## 🎯 Next Steps

After completing this integration:

1. **Test thoroughly** with test mode
2. **Switch to live mode** when ready
3. **Monitor webhooks** for issues
4. **Set up alerts** for failed payments
5. **Create customer support** workflows
6. **Build admin dashboard** for managing subscriptions

---

**Questions or issues?** Open an issue in the repository!

---

*Last Updated: November 2025*
