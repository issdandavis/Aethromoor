# Enabling External Integrations

This guide shows how to enable optional external integrations for the inbox automation system.

## 🔔 Discord Notifications

Get real-time notifications in Discord when code is pushed, releases are published, or issues/PRs are created.

### Setup Steps:

1. **Create Discord Webhook:**
   - Go to your Discord server
   - Right-click the channel where you want notifications
   - Select "Edit Channel" → "Integrations" → "Webhooks"
   - Click "New Webhook"
   - Customize name and avatar (optional)
   - Click "Copy Webhook URL"

2. **Add Webhook to GitHub:**
   - Go to your repository on GitHub
   - Click "Settings" → "Secrets and variables" → "Actions"
   - Click "New repository secret"
   - Name: `DISCORD_WEBHOOK`
   - Value: Paste the webhook URL
   - Click "Add secret"

3. **Enable Notification Code:**
   - Edit `.github/workflows/notifications.yml`
   - Find the commented section (around line 100):
   ```yaml
   # - name: Send Discord notification
   #   env:
   #     DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK }}
   ```
   - Uncomment the entire section (remove the `#`)
   - Customize the message if desired
   - Commit and push

4. **Test:**
   - Push a commit to main branch
   - Check your Discord channel for notification
   - Adjust message format as needed

### Example Discord Message:

```json
{
  "content": "🎮 New update pushed to Polly's Wingscroll!",
  "embeds": [{
    "title": "Commit to main",
    "description": "Your commit message here",
    "color": 5814783,
    "fields": [
      {"name": "Author", "value": "Your Name", "inline": true},
      {"name": "Files Changed", "value": "3", "inline": true}
    ]
  }]
}
```

### Customization:

**For release notifications:**
```yaml
- name: Discord Release Notification
  if: github.event_name == 'release'
  run: |
    curl -H "Content-Type: application/json" \
      -d '{
        "content": "🚀 **New Release Published!**",
        "embeds": [{
          "title": "${{ github.event.release.tag_name }}",
          "description": "${{ github.event.release.name }}",
          "url": "${{ github.event.release.html_url }}",
          "color": 3066993
        }]
      }' \
      ${{ secrets.DISCORD_WEBHOOK }}
```

**For issue notifications:**
```yaml
- name: Discord Issue Notification
  if: github.event_name == 'issues' && github.event.action == 'opened'
  run: |
    curl -H "Content-Type: application/json" \
      -d '{
        "content": "📋 New issue opened",
        "embeds": [{
          "title": "${{ github.event.issue.title }}",
          "url": "${{ github.event.issue.html_url }}",
          "author": {
            "name": "${{ github.event.issue.user.login }}"
          }
        }]
      }' \
      ${{ secrets.DISCORD_WEBHOOK }}
```

---

## 📧 Email Notifications

Send email notifications for important events.

### Option 1: GitHub Built-in Notifications

1. Go to GitHub Settings → Notifications
2. Configure email preferences
3. Enable "Participating", "Watching", or "Custom" for the repository
4. Choose email frequency

### Option 2: GitHub Actions Email

1. **Add Action to Workflow:**

```yaml
- name: Send Email Notification
  uses: dawidd6/action-send-mail@v3
  with:
    server_address: smtp.gmail.com
    server_port: 465
    username: ${{ secrets.MAIL_USERNAME }}
    password: ${{ secrets.MAIL_PASSWORD }}
    subject: "Avalon: New Release ${{ github.event.release.tag_name }}"
    body: |
      A new version of Polly's Wingscroll has been released!
      
      Version: ${{ github.event.release.tag_name }}
      Name: ${{ github.event.release.name }}
      
      View release: ${{ github.event.release.html_url }}
    to: subscribers@example.com
    from: Avalon Project <noreply@github.com>
```

2. **Add Secrets:**
   - `MAIL_USERNAME` - Your email username
   - `MAIL_PASSWORD` - App-specific password (not your regular password!)

3. **Gmail Setup:**
   - Enable 2-factor authentication
   - Generate app-specific password
   - Use that password in the secret

---

## 🐦 Social Media Posts

Automatically post to Twitter, Reddit, or other platforms on releases.

### Twitter (Using GitHub Actions):

```yaml
- name: Post to Twitter
  env:
    TWITTER_CONSUMER_KEY: ${{ secrets.TWITTER_CONSUMER_KEY }}
    TWITTER_CONSUMER_SECRET: ${{ secrets.TWITTER_CONSUMER_SECRET }}
    TWITTER_ACCESS_TOKEN: ${{ secrets.TWITTER_ACCESS_TOKEN }}
    TWITTER_ACCESS_SECRET: ${{ secrets.TWITTER_ACCESS_SECRET }}
  run: |
    pip install tweepy
    python - <<EOF
    import tweepy
    import os
    
    auth = tweepy.OAuthHandler(
        os.environ['TWITTER_CONSUMER_KEY'],
        os.environ['TWITTER_CONSUMER_SECRET']
    )
    auth.set_access_token(
        os.environ['TWITTER_ACCESS_TOKEN'],
        os.environ['TWITTER_ACCESS_SECRET']
    )
    api = tweepy.API(auth)
    
    message = """🎮 New release of Polly's Wingscroll!
    
    Version: ${{ github.event.release.tag_name }}
    Download: ${{ github.event.release.html_url }}
    
    #InteractiveFiction #ChoiceScript #IndieGame"""
    
    api.update_status(message)
    EOF
```

### Reddit (Using PRAW):

```yaml
- name: Post to Reddit
  env:
    REDDIT_CLIENT_ID: ${{ secrets.REDDIT_CLIENT_ID }}
    REDDIT_SECRET: ${{ secrets.REDDIT_SECRET }}
    REDDIT_USERNAME: ${{ secrets.REDDIT_USERNAME }}
    REDDIT_PASSWORD: ${{ secrets.REDDIT_PASSWORD }}
  run: |
    pip install praw
    python - <<EOF
    import praw
    import os
    
    reddit = praw.Reddit(
        client_id=os.environ['REDDIT_CLIENT_ID'],
        client_secret=os.environ['REDDIT_SECRET'],
        username=os.environ['REDDIT_USERNAME'],
        password=os.environ['REDDIT_PASSWORD'],
        user_agent='Avalon Release Bot'
    )
    
    subreddit = reddit.subreddit('interactivefiction')
    title = "New Release: Polly's Wingscroll ${{ github.event.release.tag_name }}"
    text = """
    I'm excited to announce a new release of Polly's Wingscroll: The First Thread!
    
    **About the Game:**
    A choice-based narrative game set in Avalon Academy with 40,000+ words and 14 unique endings.
    
    **What's New:**
    ${{ github.event.release.body }}
    
    [Download Here](${{ github.event.release.html_url }})
    """
    
    subreddit.submit(title, selftext=text)
    EOF
```

---

## 🔗 Zapier Integration

Connect GitHub to hundreds of services using Zapier.

### Example Zaps:

#### 1. New Issue → Google Sheets

**Trigger:** GitHub - New Issue  
**Action:** Google Sheets - Create Spreadsheet Row

**Setup:**
1. Create Zap in Zapier
2. Connect GitHub account
3. Select repository: `issdandavis/Avalon`
4. Choose trigger: "New Issue"
5. Connect Google Sheets
6. Map fields:
   - Column A: Issue number
   - Column B: Title
   - Column C: Creator
   - Column D: Labels
   - Column E: Created date
   - Column F: URL

#### 2. New PR Merged → Discord

**Trigger:** GitHub - New Pull Request Merged  
**Action:** Discord - Send Channel Message

**Setup:**
1. Trigger: "Pull Request Merged"
2. Filter: Base branch is "main"
3. Action: Send to Discord channel
4. Message: "🎉 PR #{pr_number} merged: {title}"

#### 3. New Release → Email Subscribers

**Trigger:** GitHub - New Release  
**Action:** MailChimp - Send Campaign

**Setup:**
1. Trigger: "New Release Published"
2. Action: Create and send campaign
3. Subject: "New Avalon Release: {tag_name}"
4. Body: Release notes from GitHub

#### 4. Issue Labeled "bug" → Trello Card

**Trigger:** GitHub - Issue Labeled  
**Filter:** Label is "bug"  
**Action:** Trello - Create Card

**Setup:**
1. Trigger: "New Label on Issue"
2. Filter: Label name equals "bug"
3. Action: Create card in "Bugs" list
4. Card title: Issue title
5. Card description: Issue body
6. Link back to GitHub issue

---

## 📊 Analytics Integration

Track project metrics and community engagement.

### Google Analytics for Game (HTML Version):

Add to `game/index.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-GA-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR-GA-ID');
</script>
```

### Custom Event Tracking:

```javascript
// Track when player makes a choice
function trackChoice(sceneName, choiceText) {
  gtag('event', 'game_choice', {
    'event_category': 'gameplay',
    'event_label': sceneName,
    'value': choiceText
  });
}

// Track ending reached
function trackEnding(endingName) {
  gtag('event', 'game_ending', {
    'event_category': 'completion',
    'event_label': endingName
  });
}
```

### GitHub Insights:

Already built-in! View at:
- Repository → Insights → Community
- Repository → Insights → Traffic
- Repository → Insights → Contributors

---

## 🔐 Security Best Practices

### When Adding Secrets:

1. **Never commit secrets to code**
   - Use repository secrets
   - Use environment variables
   - Add to .gitignore

2. **Use minimal permissions**
   - Only grant what's needed
   - Use read-only when possible
   - Regularly audit access

3. **Rotate credentials**
   - Change secrets periodically
   - Revoke old tokens
   - Use expiring tokens when available

4. **Monitor usage**
   - Check Actions logs
   - Review API usage
   - Watch for unauthorized access

### Secret Management:

**GitHub Secrets:**
- Repository Settings → Secrets and variables → Actions
- Organization secrets available to all repos
- Environment secrets for specific deployment environments

**Environment Variables:**
```yaml
env:
  MY_SECRET: ${{ secrets.MY_SECRET }}
```

**Masked Values:**
GitHub automatically masks secret values in logs.

---

## 📝 Testing Integrations

### Test Workflows Manually:

1. Go to Actions tab
2. Select a workflow
3. Click "Run workflow"
4. Choose branch
5. Click "Run workflow"

### Test Discord Webhook:

```bash
curl -H "Content-Type: application/json" \
  -d '{"content": "Test message from Avalon!"}' \
  YOUR_WEBHOOK_URL
```

### Test Email:

Use workflow_dispatch trigger:

```yaml
on:
  workflow_dispatch:
    inputs:
      test_email:
        description: 'Email to send test to'
        required: true
```

### Monitor Workflow Runs:

- Actions tab → Recent runs
- Click run to see details
- Review logs for errors
- Check annotations

---

## 🆘 Troubleshooting

### Discord Webhook Not Working:

- Verify webhook URL is correct
- Check secret is named exactly `DISCORD_WEBHOOK`
- Ensure webhook is uncommented in workflow
- Check Discord channel permissions
- Review workflow run logs

### Email Not Sending:

- Verify SMTP settings
- Use app-specific password (not regular password)
- Check port (465 for SSL, 587 for TLS)
- Review email provider's security settings
- Check spam folder

### Zapier Not Triggering:

- Verify GitHub connection is active
- Check trigger filters
- Review Zap history for errors
- Test trigger manually
- Check API rate limits

### Rate Limits:

- GitHub Actions: 1,000 API requests per hour per repository
- Discord webhooks: 30 per minute per channel
- Email: Depends on provider
- Twitter: 300 tweets per 3 hours

---

## 📚 Additional Resources

**GitHub Actions:**
- [Workflow syntax](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [Contexts and expressions](https://docs.github.com/en/actions/reference/context-and-expression-syntax-for-github-actions)
- [Encrypted secrets](https://docs.github.com/en/actions/reference/encrypted-secrets)

**Discord:**
- [Webhook documentation](https://discord.com/developers/docs/resources/webhook)
- [Embed formatting](https://discord.com/developers/docs/resources/channel#embed-object)

**Zapier:**
- [GitHub integration](https://zapier.com/apps/github/integrations)
- [Webhook by Zapier](https://zapier.com/apps/webhook/integrations)

**Email:**
- [GitHub send-mail action](https://github.com/dawidd6/action-send-mail)
- [Gmail app passwords](https://support.google.com/accounts/answer/185833)

---

**Questions?**  
Open an issue using the [Automation template](../../issues/new?template=automation.yml)

**Last Updated:** November 2025
