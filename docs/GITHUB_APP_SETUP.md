# GitHub App Setup Guide

Complete guide to setting up and configuring GitHub Apps for the Avalon project's AI automation system.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Creating a GitHub App](#creating-a-github-app)
- [Configuration](#configuration)
- [Installation](#installation)
- [Webhook Setup](#webhook-setup)
- [API Integration](#api-integration)
- [Security](#security)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)

## Overview

### What is a GitHub App?

A GitHub App is an integration that extends GitHub's functionality. For Avalon, it enables:

- Automated code reviews
- Documentation validation
- Lore consistency checking
- CI/CD integration
- Custom workflows

### Why Use a GitHub App?

Benefits over personal access tokens:

1. **Fine-grained permissions** - Only access what's needed
2. **Better rate limits** - 5,000 requests/hour vs 60/hour
3. **Installation flexibility** - Install on specific repositories
4. **Audit trail** - Clear logging of all actions
5. **Multiple installations** - Use across organizations

## Prerequisites

Before creating a GitHub App, you need:

### Required

- [ ] GitHub account with repository admin access
- [ ] Repository: `issdandavis/Avalon`
- [ ] OpenAI API key (for AI features)
- [ ] Basic understanding of webhooks and APIs

### Optional

- [ ] Server to host webhook endpoint
- [ ] Domain name for webhook URL
- [ ] SSL certificate for HTTPS
- [ ] Anthropic API key (for Claude integration)

### Technical Requirements

- Node.js 18+ or Python 3.11+
- Git installed
- GitHub CLI (`gh`) installed
- Basic command line knowledge

## Creating a GitHub App

### Step 1: Navigate to GitHub Settings

1. Go to your GitHub account
2. Click Settings → Developer settings
3. Click GitHub Apps → New GitHub App

Or use direct link:
```
https://github.com/settings/apps/new
```

### Step 2: Basic Information

Fill in the app details:

```yaml
GitHub App name: Avalon Development Assistant
Description: AI-powered development assistant for the Avalon game project
Homepage URL: https://github.com/issdandavis/Avalon
```

### Step 3: Callback URL (Optional)

If using OAuth:
```
Callback URL: https://your-domain.com/auth/callback
```

For basic automation, you can skip this.

### Step 4: Webhook Configuration

#### Option A: Active Webhook

If you have a server:

```yaml
Webhook URL: https://your-domain.com/webhook
Webhook secret: <generate a random secret>
SSL verification: Enable
```

Generate secret:
```bash
ruby -rsecurerandom -e 'puts SecureRandom.hex(20)'
```

#### Option B: No Webhook

For GitHub Actions only:

```yaml
Active: Uncheck this box
```

### Step 5: Permissions

Set repository permissions:

```yaml
Repository permissions:
  Contents: Read and write
  Pull requests: Read and write
  Issues: Read and write
  Checks: Read and write
  Workflows: Read and write
  Metadata: Read-only

Organization permissions:
  Members: Read-only (optional)
```

### Step 6: Subscribe to Events

Select events to receive:

```yaml
Repository events:
  ☑ Check run
  ☑ Check suite
  ☑ Issues
  ☑ Issue comment
  ☑ Pull request
  ☑ Pull request review
  ☑ Pull request review comment
  ☑ Push
  ☑ Workflow run
```

### Step 7: Installation

Choose where the app can be installed:

```yaml
Where can this GitHub App be installed?
  ○ Any account
  ● Only on this account
```

For private repositories, select "Only on this account".

### Step 8: Create App

Click "Create GitHub App"

You'll be redirected to the app's settings page.

## Configuration

### Generate Private Key

1. Scroll to "Private keys"
2. Click "Generate a private key"
3. Save the downloaded `.pem` file securely

```bash
# Store securely
mkdir -p ~/.github-apps
mv ~/Downloads/avalon-app.*.private-key.pem ~/.github-apps/
chmod 600 ~/.github-apps/avalon-app.*.private-key.pem
```

### Note App ID

At the top of the settings page, note:
- **App ID**: (e.g., 123456)
- **Client ID**: (e.g., Iv1.abc123...)

### Configure .env File

Create `.env` in your project root:

```bash
# GitHub App Configuration
GITHUB_APP_ID=123456
GITHUB_APP_CLIENT_ID=Iv1.abc123...
GITHUB_APP_PRIVATE_KEY_PATH=~/.github-apps/avalon-app.private-key.pem
GITHUB_WEBHOOK_SECRET=your_webhook_secret_here

# API Keys
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# Optional
GITHUB_INSTALLATION_ID=78910  # Set after installation
```

**Never commit `.env` to git!** It's already in `.gitignore`.

## Installation

### Install on Repository

1. Go to app settings
2. Click "Install App" in left sidebar
3. Select "issdandavis" account
4. Choose repositories:
   - Select: Only select repositories
   - Choose: Avalon
5. Click "Install"

### Get Installation ID

After installation:

```bash
# Using GitHub CLI
gh api /repos/issdandavis/Avalon/installation

# Look for "id" field
{
  "id": 12345678,  # This is your GITHUB_INSTALLATION_ID
  ...
}
```

Add to `.env`:
```bash
GITHUB_INSTALLATION_ID=12345678
```

### Verify Installation

```bash
# Check installed apps
gh api /repos/issdandavis/Avalon/installations

# Should list your app
```

## Webhook Setup

### Option 1: Using Ngrok (Development)

For local development:

```bash
# Install ngrok
brew install ngrok  # macOS
# or download from https://ngrok.com

# Start tunnel
ngrok http 3000

# Update webhook URL in app settings
# URL: https://abc123.ngrok.io/webhook
```

### Option 2: Hosted Server (Production)

#### Deploy Webhook Handler

Example with Node.js:

```javascript
// webhook.js
const express = require('express');
const crypto = require('crypto');

const app = express();
app.use(express.json());

// Verify webhook signature
function verifySignature(payload, signature) {
  const hmac = crypto.createHmac('sha256', process.env.GITHUB_WEBHOOK_SECRET);
  const digest = 'sha256=' + hmac.update(payload).digest('hex');
  return crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(digest));
}

app.post('/webhook', (req, res) => {
  const signature = req.headers['x-hub-signature-256'];
  const payload = JSON.stringify(req.body);
  
  if (!verifySignature(payload, signature)) {
    return res.status(401).send('Invalid signature');
  }
  
  const event = req.headers['x-github-event'];
  
  // Handle events
  switch (event) {
    case 'pull_request':
      handlePullRequest(req.body);
      break;
    case 'issues':
      handleIssue(req.body);
      break;
    // ... other events
  }
  
  res.status(200).send('OK');
});

app.listen(3000, () => {
  console.log('Webhook server running on port 3000');
});
```

#### Deploy to Cloud

Choose a platform:

**Vercel:**
```bash
npm install -g vercel
vercel --prod
```

**Heroku:**
```bash
heroku create avalon-webhook
git push heroku main
```

**AWS Lambda:**
Use Serverless Framework or AWS SAM

### Option 3: GitHub Actions Only

No webhook server needed:

```yaml
# .github/workflows/on-pr.yml
name: PR Automation

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  automate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run automation
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Your automation script
```

## API Integration

### Authentication

#### Get Installation Token

```javascript
const { App } = require('@octokit/app');

const app = new App({
  appId: process.env.GITHUB_APP_ID,
  privateKey: fs.readFileSync(process.env.GITHUB_APP_PRIVATE_KEY_PATH, 'utf8')
});

// Get installation token
const installationId = process.env.GITHUB_INSTALLATION_ID;
const { token } = await app.octokit.auth({
  type: 'installation',
  installationId
});

// Use token for API calls
const octokit = new Octokit({ auth: token });
```

#### Python Example

```python
import jwt
import time
import requests

def generate_jwt(app_id, private_key):
    payload = {
        'iat': int(time.time()),
        'exp': int(time.time()) + 600,
        'iss': app_id
    }
    return jwt.encode(payload, private_key, algorithm='RS256')

def get_installation_token(app_id, installation_id, private_key):
    jwt_token = generate_jwt(app_id, private_key)
    
    response = requests.post(
        f'https://api.github.com/app/installations/{installation_id}/access_tokens',
        headers={
            'Authorization': f'Bearer {jwt_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
    )
    
    return response.json()['token']
```

### Making API Calls

```javascript
const octokit = new Octokit({ auth: installationToken });

// Get PR files
const { data: files } = await octokit.pulls.listFiles({
  owner: 'issdandavis',
  repo: 'Avalon',
  pull_number: 123
});

// Add comment
await octokit.issues.createComment({
  owner: 'issdandavis',
  repo: 'Avalon',
  issue_number: 123,
  body: 'AI review complete! ✅'
});

// Request changes
await octokit.pulls.createReview({
  owner: 'issdandavis',
  repo: 'Avalon',
  pull_number: 123,
  event: 'REQUEST_CHANGES',
  body: 'Found some issues that need addressing.'
});
```

## Security

### Private Key Security

**DO:**
- Store private key securely
- Use environment variables
- Restrict file permissions (chmod 600)
- Rotate keys periodically

**DON'T:**
- Commit private key to git
- Share private key
- Store in public locations
- Use same key across apps

### Webhook Security

**Verify Signatures:**

```javascript
const crypto = require('crypto');

function verifyWebhook(req) {
  const signature = req.headers['x-hub-signature-256'];
  const payload = JSON.stringify(req.body);
  const secret = process.env.GITHUB_WEBHOOK_SECRET;
  
  const hmac = crypto.createHmac('sha256', secret);
  const digest = 'sha256=' + hmac.update(payload).digest('hex');
  
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(digest)
  );
}
```

### Rate Limiting

Monitor rate limits:

```javascript
const response = await octokit.rateLimit.get();
console.log(`Remaining: ${response.data.rate.remaining}`);
console.log(`Resets at: ${new Date(response.data.rate.reset * 1000)}`);
```

### Secrets Management

Use GitHub Secrets:

```bash
# Set repository secret
gh secret set OPENAI_API_KEY

# Use in workflows
env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

## Testing

### Test Webhook Locally

```bash
# Start local server
node webhook.js

# In another terminal, start ngrok
ngrok http 3000

# Update app webhook URL to ngrok URL

# Trigger event (create PR, comment, etc.)
```

### Test API Integration

```javascript
// test-app.js
const { App } = require('@octokit/app');

async function test() {
  const app = new App({ ... });
  
  // Test authentication
  const { data } = await app.octokit.apps.getAuthenticated();
  console.log('Authenticated as:', data.name);
  
  // Test installation
  const { token } = await app.octokit.auth({
    type: 'installation',
    installationId: process.env.GITHUB_INSTALLATION_ID
  });
  console.log('Got installation token:', token.slice(0, 10) + '...');
}

test();
```

### Test Permissions

```bash
# Check app permissions
gh api /repos/issdandavis/Avalon/installation/permissions

# Should show all granted permissions
```

## Troubleshooting

### Common Issues

#### "Bad Credentials" Error

**Cause:** Invalid or expired token

**Solution:**
1. Regenerate private key
2. Check App ID is correct
3. Verify installation ID
4. Ensure clock is synchronized

#### Webhook Not Receiving Events

**Cause:** Various networking/config issues

**Solutions:**
1. Check webhook URL is accessible
2. Verify SSL certificate is valid
3. Check event subscriptions
4. Review webhook deliveries in app settings

#### Permission Denied

**Cause:** Insufficient permissions

**Solution:**
1. Review app permissions
2. Reinstall app if permissions changed
3. Check file/folder access

#### Rate Limit Exceeded

**Cause:** Too many API calls

**Solution:**
1. Implement caching
2. Use conditional requests
3. Add delays between calls
4. Monitor rate limit headers

### Debugging

#### View Webhook Deliveries

1. Go to app settings
2. Click "Advanced" tab
3. Review "Recent Deliveries"
4. Check request/response for errors

#### Check Logs

```bash
# GitHub Actions logs
gh run list
gh run view RUN_ID --log

# Local logs
tail -f /var/log/webhook.log
```

#### Enable Debug Mode

```javascript
const { Octokit } = require('@octokit/rest');

const octokit = new Octokit({
  auth: token,
  log: console  // Enable debug logging
});
```

## Next Steps

After setup:

1. **Configure Workflows** - Set up GitHub Actions
2. **Create Custom Agents** - See [CUSTOM_AGENTS.md](CUSTOM_AGENTS.md)
3. **Enable AI Features** - Configure OpenAI integration
4. **Test Automation** - Create test PR
5. **Monitor Usage** - Track API costs and limits

## Additional Resources

- [GitHub Apps Documentation](https://docs.github.com/apps)
- [Octokit Libraries](https://github.com/octokit)
- [Webhook Events Reference](https://docs.github.com/webhooks/event-payloads)
- [AI Automation Guide](AI_AUTOMATION.md)
- [Custom Agents Guide](CUSTOM_AGENTS.md)

## Support

For help with GitHub App setup:

1. Review this documentation
2. Check GitHub Apps troubleshooting
3. Review webhook delivery logs
4. Open issue with `github-app` label

---

*Proper GitHub App setup enables powerful automation while maintaining security and control.*
