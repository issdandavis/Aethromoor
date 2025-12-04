# 🤖 Pipedream Workflow Quick Reference

## What's This?

Pre-built Pipedream workflow for orchestrating automation between:
- GitHub (commits & issues)
- Google Drive (backup storage)
- Dropbox (backup storage)
- Slack (notifications)

---

## ⚡ Quick Start (5 minutes)

### 1. Import to Pipedream

Copy the workflow:
```bash
pipedream/workflows/workflow-orchestration.mjs
```

Paste into [Pipedream](https://pipedream.com/) → New Workflow → Node.js Code

### 2. Connect Accounts

In Pipedream, connect:
- ✅ GitHub
- ✅ Google Drive
- ✅ Dropbox
- ✅ Slack (webhook)

### 3. Configure

Set these properties:
- `repoFullname`: Your repository (e.g., "issdandavis/Aethromoor")
- `slackWebhook`: Your Slack webhook URL

### 4. Run!

Click "Test" to run immediately, or schedule it.

---

## 🎯 What It Does

**Every time it runs:**
1. 📦 Backs up last 5 commits to Google Drive & Dropbox
2. 🚨 Checks for high-priority GitHub issues
3. 💬 Sends Slack alerts for urgent issues
4. ☁️ Syncs recent files between clouds
5. 📊 Sends summary to Slack

---

## 📁 File Structure

```
pipedream/
├── README.md                      ← Full documentation
└── workflows/
    └── workflow-orchestration.mjs ← The workflow component
```

---

## 🔑 API Keys

All keys are managed through:
- **Pipedream Connected Accounts** (recommended)
- **OR** `.auth/keys.json` (for local testing)

See [.auth/README.md](.auth/README.md) for key management details.

---

## 📚 Full Documentation

**Complete Guide:** [pipedream/README.md](pipedream/README.md)

Covers:
- Detailed setup instructions
- Configuration options
- Customization examples
- Error handling
- Testing procedures
- Integration with repository keys

---

## 🔧 Common Customizations

**Change backup frequency:**
```javascript
// In backupRepositoryData()
per_page: 10  // Change from 5 to 10 commits
```

**Add more Slack channels:**
```javascript
await this.sendSlackNotification(message, "#your-channel");
```

**Sync more files:**
```javascript
// In syncFilesBetweenClouds()
driveFiles.files.slice(0, 10)  // Change from 3 to 10 files
```

---

## 🚀 Scheduling Options

**In Pipedream:**
- Every hour
- Every day at midnight
- After every GitHub push
- Manual trigger only

**Or use with Auto Sync Agent:**
The Auto Sync Agent can trigger this workflow automatically!

---

## 🆘 Need Help?

**Documentation:**
- Full guide: [pipedream/README.md](pipedream/README.md)
- Automation: [.auth/AUTOMATION_QUICK_START.md](.auth/AUTOMATION_QUICK_START.md)
- Security: [docs/SECURITY.md](docs/SECURITY.md)

**Troubleshooting:**
See [pipedream/README.md#troubleshooting](pipedream/README.md#-troubleshooting)

---

**Ready to automate? Start here: [pipedream/README.md](pipedream/README.md)** 🎉
