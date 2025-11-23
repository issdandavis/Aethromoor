# Auto-Commit Guide for Avalon Repository

This guide explains how to use the automated commit functionality to streamline your workflow when working on the Avalon project.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [Available Methods](#available-methods)
4. [Configuration](#configuration)
5. [Usage Examples](#usage-examples)
6. [Troubleshooting](#troubleshooting)
7. [Best Practices](#best-practices)

---

## Overview

The Avalon repository includes several auto-commit tools to help you save your work automatically:

- **Manual Script** - Run commits on-demand
- **File Watcher** - Continuously monitor and commit changes
- **GitHub Actions** - Scheduled automatic commits (runs on GitHub servers)
- **Git Hooks** - Automatic commits on certain git operations

Choose the method that best fits your workflow!

---

## Quick Start

### Simplest Method: Manual Auto-Commit

```bash
# From the repository root
./scripts/auto-commit.sh
```

That's it! This will:
1. ✅ Stage all your changes
2. ✅ Create a commit with timestamp
3. ✅ Push to your current branch

---

## Available Methods

### 1. Manual Auto-Commit Script

**Best for:** Running commits when you want them

**Usage:**
```bash
./scripts/auto-commit.sh [OPTIONS]
```

**Options:**
- `-m "message"` - Custom commit message
- `-n` - Dry run (see what would happen without committing)
- `-P` - Don't push (commit only)
- `-U` - Don't include untracked files
- `-h` - Show help

**Examples:**
```bash
# Simple auto-commit with default message
./scripts/auto-commit.sh

# Custom message
./scripts/auto-commit.sh -m "Updated lore documents"

# Dry run to preview
./scripts/auto-commit.sh -n

# Commit but don't push
./scripts/auto-commit.sh -P

# Commit tracked files only (no new files)
./scripts/auto-commit.sh -U
```

---

### 2. File Watcher (Continuous Auto-Commit)

**Best for:** Long work sessions where you want automatic saves

**Usage:**
```bash
./scripts/watch-and-commit.sh [OPTIONS]
```

**Options:**
- `-i SECONDS` - Check interval (default: 300 = 5 minutes)
- `-m "prefix"` - Custom commit message prefix
- `-P` - Don't auto-push
- `-h` - Show help

**Examples:**
```bash
# Watch every 5 minutes (default)
./scripts/watch-and-commit.sh

# Watch every minute (for active work sessions)
./scripts/watch-and-commit.sh -i 60

# Watch every 10 minutes without pushing
./scripts/watch-and-commit.sh -i 600 -P

# Custom commit prefix
./scripts/watch-and-commit.sh -m "Writing session:"
```

**To stop watching:** Press `Ctrl+C`

**Run in background:**
```bash
# Start watcher in background
nohup ./scripts/watch-and-commit.sh -i 300 > /tmp/auto-commit.log 2>&1 &

# Stop background watcher
pkill -f watch-and-commit
```

---

### 3. GitHub Actions (Scheduled Auto-Commit)

**Best for:** Automatic commits from external tools or integrations

**How it works:**
- Runs automatically every 6 hours (configurable)
- Can also be triggered manually from GitHub
- Runs on GitHub's servers (no local setup needed)

**Configuration:**
The workflow is in `.github/workflows/auto-commit.yml`

To change the schedule, edit the cron expression:
```yaml
schedule:
  - cron: '0 */6 * * *'  # Every 6 hours
```

**Cron examples:**
- `0 * * * *` - Every hour
- `0 */3 * * *` - Every 3 hours
- `0 0 * * *` - Daily at midnight
- `0 9,17 * * *` - Twice daily (9 AM and 5 PM)

**Manual trigger:**
1. Go to your repository on GitHub
2. Click "Actions" tab
3. Select "Scheduled Auto-Commit"
4. Click "Run workflow"
5. Optionally enter a custom commit message

---

### 4. Create a Git Alias (Optional)

Make auto-commit even easier with a git alias:

```bash
# Add to your ~/.gitconfig or run:
git config --global alias.ac '!bash scripts/auto-commit.sh'

# Now you can use:
git ac
git ac -m "My custom message"
```

---

## Configuration

### Global Configuration File

Create `scripts/auto-commit-config.sh` to set your preferences:

```bash
# Copy the example file
cp scripts/auto-commit-config.example.sh scripts/auto-commit-config.sh

# Edit with your preferences
nano scripts/auto-commit-config.sh
```

**Available settings:**
```bash
# Commit message prefix
COMMIT_MESSAGE_PREFIX="Auto-commit:"

# Auto-push after commit (true/false)
AUTO_PUSH=true

# Include untracked files (true/false)
INCLUDE_UNTRACKED=true

# Max file size warning (MB)
MAX_FILE_SIZE_MB=10

# Exclude patterns (space-separated)
EXCLUDE_PATTERNS="*.log *.tmp node_modules/ .env"

# Dry run mode (true/false)
DRY_RUN=false
```

---

## Usage Examples

### For Writers Working on Lore

```bash
# Start a writing session with auto-commits every 10 minutes
./scripts/watch-and-commit.sh -i 600 -m "Lore writing:"

# When done, press Ctrl+C to stop
```

### For Game Development

```bash
# Commit game changes with descriptive message
./scripts/auto-commit.sh -m "Updated first lesson scene with new dialogue"
```

### For Testing/Experimentation

```bash
# See what would be committed without actually committing
./scripts/auto-commit.sh -n

# Commit locally but don't push yet
./scripts/auto-commit.sh -P
```

### For Collaborative Work

```bash
# Quick save during collaboration
./scripts/auto-commit.sh -m "Session with [collaborator]: added new characters"
```

---

## Troubleshooting

### "Permission denied" error

Make scripts executable:
```bash
chmod +x scripts/auto-commit.sh
chmod +x scripts/watch-and-commit.sh
```

### "Not a git repository" error

Make sure you're in the repository root:
```bash
cd /path/to/Avalon
./scripts/auto-commit.sh
```

### "Push failed" error

Your branch may be behind the remote. Pull first:
```bash
git pull
./scripts/auto-commit.sh
```

### "Large files detected" warning

Files over 10MB (configurable) trigger a warning. Options:
1. Confirm to proceed anyway
2. Add large files to `.gitignore`
3. Increase `MAX_FILE_SIZE_MB` in config file
4. Use Git LFS for large files

### Changes not being committed

Check `.gitignore` to ensure files aren't excluded:
```bash
git status --ignored
```

---

## Best Practices

### ✅ DO:

- **Use descriptive messages** when possible: `-m "Clear description"`
- **Test with dry-run** first: `-n` flag
- **Configure to your needs** with config file
- **Review commits** occasionally: `git log`
- **Keep .gitignore updated** to exclude build artifacts
- **Use scheduled commits** for automated processes
- **Commit frequently** but with logical groupings

### ❌ DON'T:

- **Don't commit secrets** - ensure `.env` and `keys.txt` are in `.gitignore`
- **Don't use very short intervals** (< 30 seconds) for file watcher
- **Don't commit build artifacts** - configure `.gitignore` properly
- **Don't auto-commit during merge conflicts** - resolve manually
- **Don't rely solely on auto-commits** - make meaningful manual commits too

---

## Integration with Existing Workflow

### With AUTOMATION_GUIDE.md Workflows

The auto-commit scripts complement the Zapier workflows described in `docs/AUTOMATION_GUIDE.md`:

1. **Google Docs → GitHub** - Use scheduled auto-commits to pull changes
2. **Local edits → GitHub** - Use manual or watch scripts
3. **Automated processes → GitHub** - Use GitHub Actions workflow

### With Git Hooks (Advanced)

You can integrate auto-commit into git hooks:

**Example: Pre-push hook that shows what will be committed**
```bash
#!/bin/bash
# .git/hooks/pre-push

echo "Running auto-commit check..."
./scripts/auto-commit.sh -n
```

---

## Safety Features

All auto-commit scripts include safety features:

1. **Large file detection** - Warns before committing files > 10MB
2. **Dry-run mode** - Preview commits without making them
3. **Status display** - Shows what will be committed
4. **Configurable exclusions** - Respects .gitignore and custom patterns
5. **Confirmation prompts** - For potentially problematic operations
6. **Error handling** - Fails safely without corrupting repository

---

## Advanced Usage

### Running Multiple Watchers

You can run multiple watchers for different purposes:

```bash
# Terminal 1: Watch lore files every 5 minutes
./scripts/watch-and-commit.sh -i 300 -m "Lore:"

# Terminal 2: Watch game files every 2 minutes
./scripts/watch-and-commit.sh -i 120 -m "Game:"
```

### Custom Commit Message Templates

Modify the script or config to use templates:

```bash
# In your config file
COMMIT_MESSAGE_PREFIX="📝 Auto-save:"

# Result: "📝 Auto-save: Updated 3 file(s) at 2025-01-15 14:30:00"
```

### Integration with Build Systems

Combine with build/test scripts:

```bash
#!/bin/bash
# build-and-commit.sh

npm run build
npm test

if [ $? -eq 0 ]; then
    ./scripts/auto-commit.sh -m "Build passed: auto-commit"
else
    echo "Build failed, not committing"
fi
```

---

## Support

For issues or questions:
1. Check this guide
2. Review `CONTRIBUTING.md`
3. Check git status: `git status`
4. Review recent commits: `git log --oneline -10`
5. Open an issue on GitHub

---

## Files Reference

- **`scripts/auto-commit.sh`** - Main auto-commit script
- **`scripts/watch-and-commit.sh`** - File watcher script
- **`scripts/auto-commit-config.example.sh`** - Example configuration
- **`.github/workflows/auto-commit.yml`** - GitHub Actions workflow
- **`docs/AUTO_COMMIT_GUIDE.md`** - This file

---

*Happy auto-committing! May your work always be saved.* 🎮✨
