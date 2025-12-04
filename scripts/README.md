# Automation Scripts for Avalon Project

This directory contains helper scripts to streamline development, testing, and deployment of Polly's Wingscroll.

## Available Scripts

### 🎮 play-game.sh
Opens the HTML game in your default browser.

**Usage:**
```bash
./scripts/play-game.sh
```

**What it does:**
- Detects your operating system
- Opens `game/index.html` in your default browser
- Works on macOS, Linux, and Windows

---

### ✅ validate-game.sh
Validates both HTML and ChoiceScript versions of the game.

**Usage:**
```bash
./scripts/validate-game.sh
```

**What it checks:**
- HTML file structure and content
- JavaScript syntax validity
- Required story nodes exist
- ChoiceScript scene files
- File organization and duplicates
- Large file warnings

**Exit codes:**
- `0` = All validations passed
- `1` = Critical errors found

**Best practice:** Run this before committing game changes!

---

### 📊 analyze-repo.sh
Analyzes repository health and suggests improvements.

**Usage:**
```bash
./scripts/analyze-repo.sh
```

**What it reports:**
- Repository size breakdown
- File type distribution
- Large files (>1MB)
- Code complexity metrics
- Optimization recommendations

---

## Making Scripts Executable

If you need to make the scripts executable:

```bash
chmod +x scripts/*.sh
```

## Running on Windows

On Windows, you can:
1. Use Git Bash (recommended)
2. Use WSL (Windows Subsystem for Linux)
3. Manually run commands from the script

## Integration with Development Workflow

### Before Committing:
```bash
./scripts/validate-game.sh
```

### Quick Testing:
```bash
./scripts/play-game.sh
```

### Repository Health Check:
```bash
./scripts/analyze-repo.sh
```

## Adding New Scripts

When adding new scripts:
1. Use descriptive names (verb-noun format)
2. Include help text in the script
3. Make them executable (`chmod +x`)
4. Document them in this README
5. Follow the existing error handling patterns

## Error Handling

All scripts use consistent color coding:
- 🟢 Green = Success
- 🟡 Yellow = Warning
- 🔴 Red = Error

## Future Enhancements

Potential scripts to add:
- `deploy-game.sh` - Deploy to GitHub Pages
- `backup-lore.sh` - Create lore backups
- `stats-balance.sh` - Check stat distribution
- `find-broken-links.sh` - Validate internal links
- `generate-changelog.sh` - Auto-generate changelog

## Automation Integration

These scripts are designed to work with:
- GitHub Actions (`.github/workflows/`)
- Local pre-commit hooks
- Zapier workflows (see `docs/AUTOMATION_GUIDE.md`)

---

**Questions or issues?** Check the main `README.md` or `CONTRIBUTING.md`
