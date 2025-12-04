# GitHub App Setup Instructions

## Quick Start

Follow these steps to get your AI Organizer Bot running:

### Step 1: Create the GitHub App

1. Go to: https://github.com/settings/apps/new
   - Or for organization: https://github.com/organizations/issdandavis/settings/apps/new

2. Fill in the basic information:
   ```
   GitHub App name: AI Organizer Bot
   Homepage URL: https://github.com/issdandavis
   Description: An AI-powered assistant that organizes issues, repositories, and workflows across the ISDanDavis enterprise.
   ```

3. **Webhook Configuration:**
   ```
   Webhook URL: https://your-webhook-endpoint.com/github
   Webhook Secret: Generate a strong secret and save it!
   ```
   
   > **Note**: If you don't have a webhook endpoint yet, you can use GitHub Actions only mode (see below)

4. **Permissions**: Select ALL of these:

   **Repository Permissions:**
   - Actions: Read & Write
   - Administration: Read & Write
   - Checks: Read & Write
   - Contents: Read & Write
   - Deployments: Read & Write
   - Discussions: Read & Write
   - Environments: Read & Write
   - Issues: Read & Write
   - Metadata: Read (Mandatory)
   - Pages: Read & Write
   - Projects: Read & Write
   - Pull requests: Read & Write
   - Secrets: Read & Write
   - Security events: Read & Write
   - Webhooks: Read & Write
   - Workflows: Read & Write

   **Organization Permissions:**
   - Administration: Read & Write
   - Members: Read & Write
   - Organization events: Read
   - Organization projects: Read & Write
   - Plan: Read

5. **Subscribe to Events**: Select ALL events listed in the manifest

6. **Installation**: 
   - Select "Only on this account" for personal use
   - Or "Any account" to share with others

7. Click **Create GitHub App**

### Step 2: Generate Private Key

1. After creating the app, scroll down to "Private keys"
2. Click "Generate a private key"
3. Save the downloaded `.pem` file securely
4. You'll need this for authentication

### Step 3: Install the App

1. In your app settings, click "Install App"
2. Select your account/organization
3. Choose:
   - "All repositories" for full automation
   - Or select specific repositories
4. Click "Install"

### Step 4: Configure Repository Secrets

Add these secrets to your repository:

1. Go to: `Settings > Secrets and variables > Actions > New repository secret`

2. Add each secret:

   ```
   Name: GITHUB_APP_ID
   Value: [Your App ID from the app settings page]
   ```

   ```
   Name: GITHUB_APP_INSTALLATION_ID
   Value: [Find this in the app installation URL]
   ```

   ```
   Name: GITHUB_APP_PRIVATE_KEY
   Value: [Paste the entire contents of the .pem file]
   ```

   ```
   Name: WEBHOOK_SECRET
   Value: [The webhook secret you created]
   ```

   Optional (for AI features):
   ```
   Name: OPENAI_API_KEY
   Value: [Your OpenAI API key]
   ```

   ```
   Name: ANTHROPIC_API_KEY
   Value: [Your Anthropic API key]
   ```

### Step 5: Enable Workflows

1. Go to the Actions tab in your repository
2. Enable GitHub Actions if not already enabled
3. The AI Organizer Bot workflow should now be active

### Step 6: Test the Bot

Create a test issue to verify everything works:

```markdown
Title: Test issue for AI Bot
Body: This is a test bug report to see if the bot works correctly.
Labels: None (bot should add them)
```

The bot should:
1. Automatically add appropriate labels
2. Post a comment acknowledging the issue
3. Assign it to the right project/milestone

## Alternative Setup: GitHub Actions Only

If you don't want to set up a webhook endpoint, you can use GitHub Actions only mode:

### What You Lose
- Real-time webhook processing
- Some advanced automation features

### What You Keep
- Issue triaging
- Code reviews on PRs
- Command execution via comments
- Scheduled tasks

### Setup
1. Skip the webhook URL during app creation
2. Or use a placeholder: `https://example.com/webhook`
3. Everything else remains the same
4. The GitHub Actions workflow handles all events

## Webhook Endpoint Setup (Advanced)

If you want full functionality, you need a webhook endpoint:

### Option 1: Use a Serverless Function

**Vercel:**
```javascript
// api/github-webhook.js
module.exports = async (req, res) => {
  const payload = req.body;
  const signature = req.headers['x-hub-signature-256'];
  
  // Verify signature
  // Process webhook
  // Trigger appropriate actions
  
  res.status(200).json({ received: true });
};
```

**AWS Lambda:**
```javascript
exports.handler = async (event) => {
  const payload = JSON.parse(event.body);
  // Process webhook
  return {
    statusCode: 200,
    body: JSON.stringify({ received: true })
  };
};
```

### Option 2: Use GitHub Actions as Webhook Handler

The provided workflow already handles most webhook events automatically!

### Option 3: Self-Hosted Server

```javascript
// server.js
const express = require('express');
const crypto = require('crypto');

const app = express();
app.use(express.json());

app.post('/github', (req, res) => {
  const signature = req.headers['x-hub-signature-256'];
  const payload = JSON.stringify(req.body);
  
  // Verify signature
  const hmac = crypto.createHmac('sha256', process.env.WEBHOOK_SECRET);
  const digest = 'sha256=' + hmac.update(payload).digest('hex');
  
  if (signature !== digest) {
    return res.status(401).send('Invalid signature');
  }
  
  // Process webhook
  console.log('Webhook received:', req.body);
  
  res.status(200).send('OK');
});

app.listen(3000, () => {
  console.log('Webhook server running on port 3000');
});
```

## Troubleshooting

### Bot Not Responding

1. **Check Workflow Runs**
   - Go to Actions tab
   - Look for failed runs
   - Check error messages

2. **Verify Secrets**
   - Settings > Secrets
   - Ensure all required secrets are set
   - Private key should include BEGIN/END markers

3. **Check Permissions**
   - App settings > Permissions
   - Ensure all necessary permissions granted
   - Reinstall the app if needed

4. **Webhook Deliveries**
   - App settings > Advanced > Recent Deliveries
   - Check delivery status
   - Look for error responses

### Common Errors

**"Resource not accessible by integration"**
- Missing permissions
- Reinstall the app with correct permissions

**"Bad credentials"**
- Invalid private key
- Expired JWT token
- Check APP_ID and INSTALLATION_ID

**"Not Found"**
- Wrong repository
- App not installed on repo
- Check installation settings

**Rate Limiting**
- Too many API calls
- Implement caching
- Add delays between requests

## Next Steps

Once everything is working:

1. ✅ Create your first AI agent via issue
2. ✅ Try the command system (`/ai-task`, `/ai-review`, etc.)
3. ✅ Customize agent behaviors in `.github/agents/`
4. ✅ Add custom workflows for your specific needs
5. ✅ Set up scheduled automation tasks
6. ✅ Monitor bot performance and iterate

## Support

If you run into issues:

1. Check the troubleshooting section above
2. Review GitHub Actions logs
3. Check webhook delivery logs
4. Create an issue in the repository
5. Review GitHub Apps documentation: https://docs.github.com/apps

## Security Notes

⚠️ **Important Security Practices:**

1. **Never commit secrets** to the repository
2. **Rotate keys regularly** (every 90 days)
3. **Use least privilege** - only grant needed permissions
4. **Monitor audit logs** - review app activity
5. **Validate webhooks** - always verify signatures
6. **Review permissions** - audit periodically

## Cost Considerations

- GitHub Actions minutes: Free tier has 2,000 min/month
- Additional minutes: $0.008/minute
- Consider GitHub Actions usage limits
- Optimize workflows to reduce runtime

## Updating the App

To update app configuration:

1. Go to app settings
2. Modify permissions/events
3. Users will need to accept new permissions
4. Update workflows accordingly
5. Test thoroughly before deploying

---

**You're all set!** Your AI Organizer Bot is now ready to automate your entire GitHub workflow. 🚀
