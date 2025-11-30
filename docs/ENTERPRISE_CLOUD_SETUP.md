# Enterprise Cloud Setup Guide

## 🏢 Overview

The Enterprise Cloud setup provides a complete cloud infrastructure for the Avalon project, including cloud hosting, automated backups, artifact storage, and enterprise-grade monitoring.

**Last Updated:** 2025-11-30  
**Status:** ✅ Operational  
**Cloud Provider:** GitHub (Free Tier)

---

## ☁️ What is Enterprise Cloud?

Enterprise Cloud refers to the cloud-based infrastructure and services that host, protect, and distribute the Avalon project:

### Core Components

1. **Cloud Hosting (GitHub Pages)**
   - Public web hosting for the HTML game
   - Global CDN distribution
   - Automatic HTTPS encryption
   - Zero cost, enterprise-grade reliability

2. **Cloud Storage (GitHub Artifacts)**
   - Automated storage of enterprise reports
   - Build artifacts and test results
   - 90-day retention for critical data
   - Compressed, secure storage

3. **Cloud Backup System**
   - Weekly automated backups
   - Versioned backup archives
   - Disaster recovery ready
   - Multiple backup locations

4. **Cloud Monitoring**
   - Real-time infrastructure monitoring
   - Automated health checks every 4 hours
   - AI-powered validation and reporting
   - Proactive alerting

---

## 🚀 Quick Start

### Prerequisites
- GitHub repository (✅ Already have)
- GitHub Actions enabled (✅ Already enabled)
- No additional accounts or costs required

### Activation Steps

The enterprise cloud is **already set up and operational**! Here's what's active:

1. **✅ Cloud Deployment Workflow**
   - File: `.github/workflows/deploy-pages.yml`
   - Automatically deploys game to GitHub Pages on push to main
   - Manual deployment available via Actions tab

2. **✅ Cloud Backup System**
   - File: `.github/workflows/enterprise-cloud-backup.yml`
   - Runs weekly (Sundays at 2 AM UTC)
   - Manual backup available anytime

3. **✅ Cloud Monitoring**
   - Integrated into `.github/workflows/enterprise-monitoring.yml`
   - Validates cloud infrastructure every 4 hours
   - Generates health reports

4. **✅ Cloud Configuration**
   - File: `config/enterprise-cloud-config.json`
   - Defines all cloud settings and policies
   - Customizable for your needs

---

## 📋 Cloud Features

### 1. GitHub Pages Deployment

**What it does:**
- Hosts your entire project on the cloud
- Makes all files accessible worldwide
- Provides a public URL for sharing
- Deploys game, documentation, lore, and all project content

**How to use:**

```bash
# Automatic deployment
# Just push any changes to main branch
git add .
git commit -m "Update project content"
git push

# Manual deployment
# Go to Actions tab → Deploy to GitHub Pages → Run workflow
```

**Access your deployed content:**
- URL format: `https://<username>.github.io/<repository>/`
- For this repo: Check Actions tab for deployment URL

**Configuration:**
- Edit `config/enterprise-cloud-config.json`
- Section: `cloud_platforms.github_pages`
- Customize deployment triggers, caching, and more

### 2. Cloud Artifact Storage

**What it does:**
- Stores enterprise monitoring reports
- Keeps build artifacts and test results
- Provides downloadable archives

**How to access:**

1. Go to Actions tab
2. Click on any workflow run
3. Scroll to "Artifacts" section
4. Download available artifacts

**Retention:**
- Enterprise reports: 90 days
- Build artifacts: 30 days
- Test results: 30 days

**Storage used:**
- Free tier: 500 MB
- Current usage: Check Settings → Actions → Storage

### 3. Cloud Backup System

**What it does:**
- Creates comprehensive backups weekly
- Stores all critical project files
- Enables disaster recovery

**Backup includes:**
- ✅ Lore and worldbuilding (`lore/`)
- ✅ Writing drafts (`writing_drafts/`)
- ✅ HTML game files (`game/`)
- ✅ ChoiceScript game (`choicescript_game/`)
- ✅ Configuration files (`config/`)

**Backup schedule:**
- Automatic: Every Sunday at 2 AM UTC
- Manual: Actions → Enterprise Cloud Backup → Run workflow

**Restore from backup:**

1. Go to Actions → Enterprise Cloud Backup
2. Select a completed workflow run
3. Download backup artifacts
4. Extract archives to appropriate directories

**Backup options:**
- Full backup (default)
- Incremental backup
- Critical files only

### 4. Cloud Monitoring

**What it does:**
- Validates cloud infrastructure health
- Checks deployment status
- Monitors storage usage
- Generates detailed reports

**Monitoring schedule:**
- Every 4 hours automatically
- Manual trigger available

**View monitoring results:**

1. Actions → Enterprise Functions Monitoring
2. Check "AI Confirmation Summary" job
3. Download health report artifact
4. Review detailed findings

**What's monitored:**
- ✅ Cloud deployment workflows
- ✅ Artifact storage availability
- ✅ Backup system integrity
- ✅ CDN performance
- ✅ Configuration validity

---

## 🔧 Configuration

### Enterprise Cloud Config File

**Location:** `config/enterprise-cloud-config.json`

**Key sections:**

```json
{
  "cloud_platforms": {
    "github_pages": {
      "enabled": true,
      "deployment_type": "automatic"
    },
    "artifact_storage": {
      "enabled": true,
      "retention_days": {
        "enterprise_reports": 90
      }
    },
    "cloud_backup": {
      "enabled": true,
      "backup_frequency": "weekly"
    }
  }
}
```

**Customization options:**

1. **Deployment triggers:**
   - Edit `deployment_triggers` array
   - Options: `push_to_main`, `manual_dispatch`, `release_tag`

2. **Retention periods:**
   - Adjust `retention_days` for different artifact types
   - Max: 90 days (GitHub limit)

3. **Backup frequency:**
   - Change `backup_frequency`
   - Options: `daily`, `weekly`, `monthly`

4. **CDN caching:**
   - Modify `cdn.cache_control`
   - Optimize for your needs

### Workflow Customization

**Deploy workflow:** `.github/workflows/deploy-pages.yml`
- Customize deployment paths
- Add build steps if needed
- Configure deployment notifications

**Backup workflow:** `.github/workflows/enterprise-cloud-backup.yml`
- Adjust backup schedule (cron expression)
- Add/remove backed-up directories
- Customize backup retention

**Monitoring workflow:** `.github/workflows/enterprise-monitoring.yml`
- Already includes cloud validation
- Adjust monitoring frequency if needed
- Customize alert thresholds

---

## 📊 Cloud Dashboard

### View Cloud Status

**Quick check:**
```bash
# Latest enterprise monitoring run
# Shows cloud infrastructure status
```

Go to: Actions → Enterprise Functions Monitoring → Latest run

**Detailed view:**

1. Download latest health report artifact
2. Open `enterprise-health-report.md`
3. Check "Enterprise Cloud Infrastructure" section

### Key Metrics

**Deployment status:**
- Last deployment time
- Deployment success rate
- Current live version

**Storage usage:**
- Total artifacts stored
- Storage space used
- Retention policy compliance

**Backup status:**
- Last backup date
- Backup size
- Backup integrity

**Monitoring health:**
- Validation frequency
- Success rate
- Alert status

---

## 🔐 Security

### Cloud Security Features

1. **HTTPS Only**
   - All cloud hosting uses HTTPS
   - Automatic SSL/TLS encryption
   - GitHub-managed certificates

2. **Access Control**
   - Public game hosting (by design)
   - Private artifact storage (repo members only)
   - Protected backups (authorized access only)

3. **DDoS Protection**
   - GitHub's enterprise-grade protection
   - Automatic rate limiting
   - Traffic filtering

4. **Data Protection**
   - Encrypted at rest (GitHub-managed)
   - Encrypted in transit (HTTPS)
   - Regular security updates

### Security Best Practices

✅ **Do:**
- Keep workflows up to date
- Review security alerts
- Monitor access logs
- Rotate tokens quarterly

❌ **Don't:**
- Commit secrets to repository
- Disable HTTPS
- Store sensitive data in public artifacts
- Share deployment credentials

---

## 🛠️ Troubleshooting

### Common Issues

**1. Deployment fails**

**Symptoms:** Deploy workflow fails, site not updated

**Solutions:**
```bash
# Check workflow permissions
# Go to: Settings → Actions → General → Workflow permissions
# Ensure "Read and write permissions" is enabled

# Check Pages settings
# Go to: Settings → Pages
# Ensure Source is set to "GitHub Actions"

# Manually trigger deployment
# Go to: Actions → Deploy to GitHub Pages → Run workflow
```

**2. Backup fails**

**Symptoms:** Backup workflow fails, no artifacts created

**Solutions:**
```bash
# Check storage quota
# Go to: Settings → Actions → Storage
# Ensure not over quota (500 MB free tier)

# Check workflow permissions
# Needs "contents: write" permission

# Verify backup paths exist
# Ensure lore/, game/, etc. directories exist
```

**3. Monitoring shows warnings**

**Symptoms:** Health report shows warning status

**Solutions:**
```bash
# Download health report
# Check "Detailed Findings" section
# Address specific issues mentioned

# Validate configurations
python3 -c "import json; json.load(open('config/enterprise-cloud-config.json'))"

# Re-run monitoring
# Go to: Actions → Enterprise Functions Monitoring → Run workflow
```

**4. Can't access deployed site**

**Symptoms:** 404 error, site not loading

**Solutions:**
```bash
# Check Pages status
# Go to: Settings → Pages
# Verify custom domain (if set)

# Check deployment workflow
# Ensure latest run succeeded
# Check "Deploy to Enterprise Cloud" job logs

# Verify files deployed correctly
# Check deployment artifacts
# Ensure index.html exists
```

---

## 📈 Advanced Features

### Custom Domain (Optional)

**Setup:**

1. Purchase a domain (e.g., GoDaddy, Namecheap)
2. Configure DNS:
   ```
   Type: CNAME
   Host: www
   Value: <username>.github.io
   ```
3. Update `config/enterprise-cloud-config.json`:
   ```json
   "custom_domain": {
     "enabled": true,
     "domain": "www.yourdomain.com"
   }
   ```
4. Go to: Settings → Pages → Custom domain
5. Enter domain and verify

### Cloud Analytics (Optional)

**Options:**
- Google Analytics (privacy considerations)
- Plausible Analytics (privacy-focused)
- Simple Analytics (paid)

**Setup:**

1. Choose analytics provider
2. Get tracking code
3. Add to `game/index.html`
4. Update `enterprise-cloud-config.json`

### CDN Optimization

**Default:** GitHub CDN (global)

**Enhanced options:**
- Cloudflare (free tier available)
- Fastly (enterprise)
- AWS CloudFront (pay-as-you-go)

**Benefits:**
- Faster global loading
- Advanced caching
- DDoS protection
- Analytics

---

## 🎯 Best Practices

### 1. Regular Monitoring

✅ **Review health reports weekly**
- Check cloud infrastructure status
- Verify all validations passing
- Address any warnings promptly

✅ **Monitor storage usage**
- Keep under quota
- Clean up old artifacts
- Optimize backup sizes

✅ **Test deployments**
- Verify game loads correctly
- Check all features work
- Test on different devices

### 2. Backup Management

✅ **Verify backups work**
- Download and test restore quarterly
- Ensure all critical files included
- Validate backup integrity

✅ **Maintain backup schedule**
- Don't skip scheduled backups
- Run manual backups before major changes
- Keep multiple backup versions

### 3. Security Hygiene

✅ **Keep dependencies updated**
- Update GitHub Actions regularly
- Review security advisories
- Apply security patches promptly

✅ **Review access permissions**
- Audit who has repository access
- Use least-privilege principle
- Remove inactive collaborators

✅ **Protect sensitive data**
- Use GitHub Secrets for credentials
- Never commit API keys
- Rotate secrets regularly

### 4. Performance Optimization

✅ **Optimize assets**
- Compress images
- Minify CSS/JS (if needed)
- Enable caching

✅ **Monitor page load times**
- Test from different locations
- Use browser dev tools
- Optimize bottlenecks

---

## 📞 Support

### Getting Help

**Documentation:**
- This file (Enterprise Cloud Setup)
- `docs/ENTERPRISE_MONITORING.md`
- `docs/AUTOMATION_GUIDE.md`

**Workflow logs:**
- Check failed workflow runs
- Review error messages
- Download run artifacts

**GitHub Docs:**
- [GitHub Pages](https://docs.github.com/pages)
- [GitHub Actions](https://docs.github.com/actions)
- [Workflow Artifacts](https://docs.github.com/actions/using-workflows/storing-workflow-data-as-artifacts)

**Community:**
- GitHub Community Forum
- Stack Overflow (github-actions tag)
- GitHub Support (for account issues)

---

## ✅ Success Checklist

Verify your enterprise cloud is fully operational:

- [ ] Cloud deployment workflow exists and runs successfully
- [ ] GitHub Pages hosting is enabled
- [ ] Game is accessible via public URL
- [ ] Cloud backup workflow runs weekly
- [ ] Backup artifacts are created and downloadable
- [ ] Cloud monitoring validates infrastructure every 4 hours
- [ ] Health reports show cloud status as operational
- [ ] Configuration files are valid JSON
- [ ] Storage quota is not exceeded
- [ ] All workflows have required permissions

---

## 🎉 You're All Set!

Your enterprise cloud infrastructure is now operational. The system provides:

✅ **Cloud Hosting** - Game deployed globally via GitHub Pages  
✅ **Cloud Storage** - Artifacts stored securely for 90 days  
✅ **Cloud Backup** - Weekly automated backups with disaster recovery  
✅ **Cloud Monitoring** - 24/7 automated validation and reporting

**Everything runs automatically. No ongoing costs. Enterprise-grade reliability.**

---

*Last Updated: 2025-11-30*  
*System Version: 1.0*  
*Cloud Provider: GitHub*
