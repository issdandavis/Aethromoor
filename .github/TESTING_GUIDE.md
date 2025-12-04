# 🧪 Quick Testing Guide for AI Organizer Bot

## ✅ Implementation Status: COMPLETE

The AI Organizer Bot system is fully implemented and ready for testing!

## 📦 What's Ready to Test

### 1. Issue Triaging (Auto-categorization)
**Test:** Create a new issue with bug-related content

**Example:**
```markdown
Title: The game crashes when I select the Singing Dunes expedition
Body: Steps to reproduce:
1. Complete the first lesson
2. Choose the Singing Dunes expedition
3. Game crashes with error message

Expected: Should load the expedition scene
Actual: Game freezes
```

**Expected Bot Behavior:**
- Automatically adds `bug` label
- Adds `needs-investigation` label
- May add `game-choicescript` label
- Posts acknowledgment comment
- Response time: < 30 seconds

### 2. Feature Request Triaging
**Test:** Create a feature request issue

**Example:**
```markdown
Title: Add save game functionality
Body: It would be great to be able to save the game progress and continue later.
```

**Expected Bot Behavior:**
- Adds `enhancement` label
- Posts acknowledgment comment with checklist

### 3. Command System
**Test:** Use commands in issue comments

**Try these commands:**
```markdown
/ai-help
```
```markdown
/ai-organize triage-all
```

**Expected Bot Behavior:**
- Responds with available commands list
- Executes requested action
- Posts status updates

### 4. Pull Request Review (When you create a PR)
**Test:** Create a test PR with code changes

**Expected Bot Behavior:**
- Analyzes changed files
- Posts review comments
- Checks for:
  - Large files (>500 lines)
  - Missing tests
  - console.log statements
  - ChoiceScript syntax issues
- Approves or comments based on findings

## 🚀 Setup Required First

Before testing, you need to:

### Step 1: Register GitHub App (5 minutes)

1. Go to: https://github.com/settings/apps/new

2. Fill in these fields:
   - **GitHub App name:** `AI Organizer Bot`
   - **Homepage URL:** `https://github.com/issdandavis`
   - **Webhook URL:** Leave blank OR use: `https://example.com/webhook`
     (The workflow uses GitHub Actions, so webhook is optional)
   - **Webhook secret:** Generate a random string (save it!)

3. **Permissions:** Click "Read & Write" for:
   - Actions
   - Contents
   - Deployments
   - Issues
   - Pull requests
   - Workflows

4. **Subscribe to events:** Check ALL:
   - Issues
   - Issue comments
   - Pull requests
   - Pull request reviews
   - Push
   - (and others as listed in the manifest)

5. Click "Create GitHub App"

6. **Download Private Key:**
   - Scroll to "Private keys"
   - Click "Generate a private key"
   - Save the `.pem` file

### Step 2: Install the App (2 minutes)

1. In your app settings, click "Install App"
2. Select your account
3. Choose "All repositories" or select "Avalon"
4. Click "Install"
5. Note the Installation ID from the URL (e.g., `installations/12345678`)

### Step 3: Add Repository Secrets (2 minutes)

1. Go to: https://github.com/issdandavis/Avalon/settings/secrets/actions

2. Click "New repository secret" for each:

   **Secret 1:**
   - Name: `GITHUB_APP_ID`
   - Value: Your app ID (found in app settings)

   **Secret 2:**
   - Name: `GITHUB_APP_INSTALLATION_ID`
   - Value: Installation ID from step 2

   **Secret 3:**
   - Name: `GITHUB_APP_PRIVATE_KEY`
   - Value: Paste entire contents of `.pem` file (including BEGIN/END lines)

   **Secret 4:**
   - Name: `WEBHOOK_SECRET`
   - Value: The secret you created in Step 1

### Step 4: Verify Workflow is Enabled

1. Go to: https://github.com/issdandavis/Avalon/actions
2. Look for "AI Organizer Bot - Main Workflow"
3. If it shows "disabled", click to enable it

## 🧪 Testing Checklist

Once setup is complete, test in this order:

- [ ] **Step 1:** Create a test issue with "bug" in title/body
  - Wait 30 seconds
  - Check if labels were added
  - Check for bot comment

- [ ] **Step 2:** Comment `/ai-help` on the test issue
  - Wait 30 seconds
  - Check for bot response with command list

- [ ] **Step 3:** Create a feature request issue
  - Check if it gets `enhancement` label
  - Check for bot acknowledgment

- [ ] **Step 4:** Try command `/ai-organize triage-all` on any issue
  - Check bot response

- [ ] **Step 5:** (Optional) Create a test PR
  - Check for automated review comment

## 🔍 Troubleshooting

### Bot Not Responding?

**Check Actions Tab:**
1. Go to: https://github.com/issdandavis/Avalon/actions
2. Look for recent workflow runs
3. Click on the latest run
4. Check for error messages

**Common Issues:**

1. **Secrets not configured**
   - Verify all 4 secrets are added
   - Check spelling of secret names
   - Ensure private key includes BEGIN/END markers

2. **Workflow not enabled**
   - Check Actions tab
   - Enable the workflow if disabled

3. **App not installed**
   - Verify app is installed on repository
   - Check installation permissions

4. **Permissions missing**
   - Review app permissions
   - Reinstall app if needed

### Where to Check Logs

1. **Workflow Execution:**
   - Actions tab → Recent workflow runs
   - Click run → Click job → View logs

2. **Webhook Deliveries:**
   - App settings → Advanced → Recent Deliveries
   - Check delivery status and responses

## 📊 Expected Results

### Issue Triaging Test
```
✅ Issue created
   ↓ (< 30 seconds)
✅ Bot adds labels: bug, needs-investigation
   ↓
✅ Bot posts comment:
   "🤖 AI Organizer Bot has triaged this issue.
    Type: Bug Report 🐛
    Applied labels: bug, needs-investigation"
```

### Command Test
```
✅ Comment: /ai-help
   ↓ (< 30 seconds)
✅ Bot replies:
   "🤖 AI Task Executor
    Available commands:
    - /ai-organize triage-all
    - /ai-review pr <number>
    - /ai-task <description>
    ..."
```

## 📚 Next Steps After Testing

Once basic functionality works:

1. **Customize Behaviors:**
   - Edit `.github/config/ai-bot-config.yml`
   - Adjust label taxonomy
   - Configure auto-assignments

2. **Create Custom Agents:**
   - Use `ai-agent-request` issue template
   - Bot will generate agent config automatically

3. **Explore Advanced Features:**
   - Read `.github/IMPLEMENTATION_GUIDE.md`
   - Set up deployment automation
   - Configure security scanning

## 🆘 Need Help?

- **Setup Issues:** See `.github/SETUP_INSTRUCTIONS.md`
- **Command Reference:** See `.github/COMMAND_REFERENCE.md`
- **Architecture:** See `.github/IMPLEMENTATION_GUIDE.md`
- **All Features:** See `.github/AI_BOT_README.md`

## 📝 Notes

- The bot works entirely through GitHub Actions
- No external servers required (webhook URL is optional)
- All processing happens within GitHub
- First response may be slower (~30s) as Actions cold-starts
- Subsequent responses are faster

---

**Ready to test!** Start with Step 1 above and work through the checklist. 🚀

If you encounter any issues, check the troubleshooting section or review the Actions logs.
