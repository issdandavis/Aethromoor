# 🤖 Pipedream Workflow Orchestration

## Overview

This directory contains Pipedream workflow components for orchestrating automation between GitHub, Google Drive, Dropbox, and Slack.

---

## 📁 Workflows

### `workflow-orchestration.mjs`

**Automated Workflow Orchestration** - A comprehensive Pipedream component that:
- 🔄 Backs up GitHub commits to Google Drive and Dropbox
- 📋 Manages and tracks GitHub issues
- ☁️ Syncs files between Google Drive and Dropbox
- 💬 Sends Slack notifications for important events

---

## 🚀 Quick Start

### 1. Import to Pipedream

**Option A: Via Pipedream UI**
1. Go to [Pipedream](https://pipedream.com/)
2. Create a new workflow
3. Add a "Run Node.js code" step
4. Copy the contents of `workflow-orchestration.mjs`
5. Paste into the code editor

**Option B: Via Pipedream CLI**
```bash
# Install Pipedream CLI
npm install -g @pipedream/cli

# Login
pd login

# Deploy workflow
pd deploy pipedream/workflows/workflow-orchestration.mjs
```

### 2. Configure Connected Accounts

In Pipedream, connect the following accounts:
- ✅ **GitHub** - For repository access
- ✅ **Google Drive** - For backup storage
- ✅ **Dropbox** - For backup storage
- ✅ **Slack** (via webhook) - For notifications

### 3. Set Required Props

Configure the workflow properties:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `repoFullname` | string | ✅ | GitHub repository (e.g., "issdandavis/Aethromoor") |
| `slackWebhook` | string | ✅ | Slack webhook URL for notifications |
| `backupFolder` | string | ❌ | Backup folder name (default: "GitHub-Backups") |
| `syncBetweenClouds` | boolean | ❌ | Enable cloud sync (default: true) |
| `enableCommitTracking` | boolean | ❌ | Enable commit backups (default: true) |
| `enableIssueManagement` | boolean | ❌ | Enable issue tracking (default: true) |

---

## 🔑 API Keys Setup

This workflow requires API keys configured in your Pipedream account or using the `.auth/keys.json` structure from this repository.

### Required Keys

From `.auth/keys.json`:
```json
{
  "github": {
    "personal_access_token": "ghp_YOUR_TOKEN_HERE"
  },
  "google": {
    "api_key": "YOUR_GOOGLE_API_KEY",
    "service_account_key": "path/to/service-account.json"
  },
  "slack": {
    "webhook_url": "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
  }
}
```

### Using Keys in Pipedream

**Method 1: Connected Accounts (Recommended)**
Pipedream manages authentication automatically when you connect accounts.

**Method 2: Environment Variables**
```javascript
// Access from Pipedream secrets
const githubToken = process.env.GITHUB_TOKEN;
const slackWebhook = process.env.SLACK_WEBHOOK_URL;
```

**Method 3: Read from Repository Keys**
```javascript
// If deploying locally or with access to repo
import fs from 'fs';
const keys = JSON.parse(fs.readFileSync('.auth/keys.json', 'utf8'));
const githubToken = keys.github.personal_access_token;
```

---

## 📋 Workflow Features

### 1. Commit Backup
- Fetches last 5 commits from repository
- Creates JSON backup with commit metadata
- Saves to both Google Drive and Dropbox
- Includes SHA, message, author, and timestamp

### 2. Issue Management
- Retrieves open issues from repository
- Identifies high-priority issues (urgent/critical labels)
- Sends Slack alerts for high-priority items
- Creates issue summary documents in Google Drive

### 3. Cloud Sync
- Lists recent files from Google Drive
- Syncs 3 most recent files to Dropbox
- Handles file conflicts with auto-rename
- Logs sync operations

### 4. Slack Notifications
- Workflow start notification
- High-priority issue alerts
- Orchestration summary
- Error notifications

---

## 🔄 Workflow Execution Flow

```
1. Validate Inputs
   ↓
2. Send Start Notification (Slack)
   ↓
3. Create Backup Structure (Google Drive)
   ↓
4. Backup Repository Data (Commits)
   ├─→ Save to Google Drive
   └─→ Save to Dropbox
   ↓
5. Manage GitHub Issues
   ├─→ Filter high-priority
   ├─→ Send Slack alerts
   └─→ Create summary
   ↓
6. Sync Files Between Clouds
   ├─→ List Google Drive files
   └─→ Upload to Dropbox
   ↓
7. Send Summary Notification (Slack)
   ↓
8. Return Results
```

---

## 📊 Output Format

The workflow returns a structured result:

```json
{
  "success": true,
  "repository": "issdandavis/Aethromoor",
  "orchestrationResults": {
    "timestamp": "2024-12-04T12:00:00.000Z",
    "workflows": {
      "backupSetup": {
        "driveFolder": {
          "id": "folder_id",
          "name": "GitHub-Backups-2024-12-04"
        }
      },
      "commitBackup": {
        "commits": 5,
        "backupFile": "commit-backup-1701691200000.json"
      },
      "issueManagement": {
        "totalIssues": 10,
        "highPriorityIssues": 2
      },
      "cloudSync": {
        "completed": true
      }
    }
  },
  "summary": {
    "totalWorkflows": 4,
    "successfulWorkflows": 4,
    "enabledFeatures": {
      "commitTracking": true,
      "issueManagement": true,
      "cloudSync": true
    }
  }
}
```

---

## 🎯 Use Cases

### Use Case 1: Daily Repository Backup
**Schedule:** Every day at midnight
**Config:**
- Enable commit tracking: ✅
- Enable issue management: ✅
- Enable cloud sync: ✅

**Result:** Daily snapshots of commits and issues backed up to cloud storage.

### Use Case 2: High-Priority Issue Monitoring
**Trigger:** Every 30 minutes
**Config:**
- Enable commit tracking: ❌
- Enable issue management: ✅
- Enable cloud sync: ❌

**Result:** Real-time Slack alerts for urgent issues.

### Use Case 3: Multi-Cloud Backup
**Trigger:** After every push
**Config:**
- Enable commit tracking: ✅
- Enable issue management: ❌
- Enable cloud sync: ✅

**Result:** Commits backed up to both Google Drive and Dropbox.

---

## 🔧 Customization

### Change Backup Frequency

Adjust the number of commits backed up:
```javascript
// In backupRepositoryData()
const commits = await this.github.getCommits({
  repoFullname: this.repoFullname,
  per_page: 10, // Change from 5 to 10
});
```

### Modify Slack Channels

Update notification channels:
```javascript
// In manageGitHubIssues()
await this.sendSlackNotification(
  `🚨 High Priority Issues...`,
  "#custom-channel" // Change from "#alerts"
);
```

### Add Custom Issue Filters

Filter by additional criteria:
```javascript
const customIssues = issues.filter(issue => {
  const hasLabel = issue.labels.some(l => l.name === 'custom-label');
  const isRecent = new Date(issue.created_at) > sevenDaysAgo;
  return hasLabel && isRecent;
});
```

### Sync More Files

Increase sync file count:
```javascript
// In syncFilesBetweenClouds()
for (const file of driveFiles.files.slice(0, 10)) { // Change from 3 to 10
  // ... sync logic
}
```

---

## 🚨 Error Handling

The workflow includes comprehensive error handling:

### Commit Backup Errors
- Logs error to console
- Returns `{ commits: 0 }`
- Continues with other workflows

### Issue Management Errors
- Logs error to console
- Returns `{ totalIssues: 0, highPriorityIssues: 0 }`
- Continues with other workflows

### Cloud Sync Errors
- Logs per-file errors
- Skips failed files
- Continues with remaining files

### Fatal Errors
- Catches top-level errors
- Sends Slack notification
- Returns `{ success: false, error: message }`

---

## 🧪 Testing

### Test Locally

```bash
# Create test event
cat > test-event.json << EOF
{
  "repoFullname": "issdandavis/Aethromoor",
  "slackWebhook": "https://hooks.slack.com/services/YOUR/TEST/WEBHOOK",
  "enableCommitTracking": true,
  "enableIssueManagement": true,
  "syncBetweenClouds": false
}
EOF

# Run with Pipedream CLI
pd run workflow-orchestration.mjs --event test-event.json
```

### Test in Pipedream UI

1. Go to your workflow
2. Click "Test"
3. Provide test repository name
4. Check execution logs
5. Verify Slack notifications
6. Confirm files in cloud storage

---

## 📚 Integration with Repository

This workflow integrates with the secure API key management system:

### Use Repository Keys

```javascript
// At the top of your workflow
import fs from 'fs';
import path from 'path';

// Load keys from repository
const keysPath = path.join(process.cwd(), '.auth', 'keys.json');
const keys = JSON.parse(fs.readFileSync(keysPath, 'utf8'));

// Use in workflow
export default defineComponent({
  async run({ $ }) {
    const githubToken = keys.github.personal_access_token;
    const slackWebhook = keys.slack.webhook_urls.general;
    // ... rest of workflow
  }
});
```

### Reference Documentation

- **Security Guide:** [`docs/SECURITY.md`](../docs/SECURITY.md)
- **Automation Quick Start:** [`.auth/AUTOMATION_QUICK_START.md`](../.auth/AUTOMATION_QUICK_START.md)
- **GitHub Secrets:** [`docs/GITHUB_SECRETS_SETUP.md`](../docs/GITHUB_SECRETS_SETUP.md)

---

## 🔐 Security Best Practices

1. **Never hardcode credentials** in workflow files
2. **Use Pipedream secrets** for sensitive values
3. **Rotate API keys** every 90 days
4. **Monitor usage** in connected account dashboards
5. **Use test repositories** during development
6. **Limit backup retention** to avoid storage costs

---

## 📖 Additional Resources

### Pipedream Documentation
- [Pipedream Docs](https://pipedream.com/docs)
- [Node.js Code Steps](https://pipedream.com/docs/code/nodejs/)
- [Connected Accounts](https://pipedream.com/docs/connected-accounts/)

### API Documentation
- [GitHub API](https://docs.github.com/en/rest)
- [Google Drive API](https://developers.google.com/drive/api/v3/reference)
- [Dropbox API](https://www.dropbox.com/developers/documentation)
- [Slack API](https://api.slack.com/)

---

## 🆘 Troubleshooting

### "Repository name is required"
**Cause:** Missing `repoFullname` prop  
**Solution:** Set `repoFullname` in workflow configuration

### "Failed to send Slack notification"
**Cause:** Invalid webhook URL or network error  
**Solution:** Verify webhook URL and test with curl

### "Error creating Google Drive folder"
**Cause:** Insufficient permissions or quota exceeded  
**Solution:** Check Google Drive permissions and storage quota

### "Error backing up repository data"
**Cause:** Invalid GitHub token or rate limiting  
**Solution:** Verify token has `repo` scope and check rate limits

---

## 🎉 Success Criteria

After successful execution, you should see:
- ✅ New folder in Google Drive with today's date
- ✅ Commit backup JSON files in Google Drive
- ✅ Commit backup JSON files in Dropbox
- ✅ Issue summary JSON in Google Drive
- ✅ Slack notifications in configured channels
- ✅ Synced files in Dropbox `/synced-files/` directory

---

**Created:** December 2024  
**Repository:** Avalon/Aethromoor  
**Maintainer:** @issdandavis
