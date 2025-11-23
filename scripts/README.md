# Scripts Directory

This directory contains automation scripts for the Avalon repository.

## Available Scripts

### 🤖 Auto-Commit Scripts

**`auto-commit.sh`** - Manual auto-commit script
- Commits and pushes changes on demand
- Supports custom messages and options
- Safe with dry-run mode and file size checks

**`watch-and-commit.sh`** - File watcher with auto-commit
- Monitors repository for changes
- Automatically commits at specified intervals
- Great for long work sessions

**`auto-commit-config.example.sh`** - Configuration template
- Copy to `auto-commit-config.sh` to customize behavior
- Set commit message prefix, push behavior, file size limits, etc.

### 🎮 CSIDE Preparation Script

**`prepare-for-cside.sh`** - Prepares game files for CSIDE upload
- Packages all ChoiceScript game files
- Creates organized folder structure
- Generates upload instructions
- Perfect for getting your game into CSIDE quickly!

## Quick Start

```bash
# Simple auto-commit
./scripts/auto-commit.sh

# Auto-commit with custom message
./scripts/auto-commit.sh -m "Updated game scenes"

# Start file watcher (commits every 5 minutes)
./scripts/watch-and-commit.sh

# Watch with custom interval
./scripts/watch-and-commit.sh -i 300

# Prepare game files for CSIDE upload
./scripts/prepare-for-cside.sh
```

## Documentation

See **[docs/AUTO_COMMIT_GUIDE.md](../docs/AUTO_COMMIT_GUIDE.md)** for complete documentation.

## Setup

1. Make scripts executable (already done in this repo):
   ```bash
   chmod +x scripts/*.sh
   ```

2. Optionally create config file:
   ```bash
   cp scripts/auto-commit-config.example.sh scripts/auto-commit-config.sh
   # Edit as needed
   ```

3. Start using!

## Safety Features

- ✅ Dry-run mode to preview changes
- ✅ Large file detection (warns for files > 10MB)
- ✅ Respects .gitignore
- ✅ Shows what will be committed before committing
- ✅ Configurable exclusion patterns
- ✅ Safe error handling

## Additional Tools

Beyond these scripts, you can also use:
- **GitHub Actions** (`.github/workflows/auto-commit.yml`) - Scheduled commits
- **Git Aliases** - Add shortcuts to your git config
- **Git Hooks** - Integrate into your git workflow

See the full guide for details!
