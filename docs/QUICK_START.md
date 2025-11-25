# Quick Start Guide

Get up and running with the Avalon project in minutes, whether you're playing the game, contributing to development, or using AI automation features.

## Table of Contents

- [For Players](#for-players)
- [For Contributors](#for-contributors)
- [For AI Assistants](#for-ai-assistants)
- [For Developers](#for-developers)
- [Common Tasks](#common-tasks)

## For Players

### Playing the HTML Version (Easiest)

**1-Click Play:**

```bash
# Just open the file!
open game/index.html
# Or double-click in file browser
```

That's it! The game runs entirely in your browser.

### Playing the ChoiceScript Version

**Prerequisites:**
- Node.js 18+ installed
- Git installed

**Steps:**

```bash
# 1. Clone repository
git clone https://github.com/issdandavis/Avalon.git
cd Avalon

# 2. Bootstrap ChoiceScript
cd game
./bootstrap_choicescript.sh

# 3. Sync scenes
./sync_scenes.sh

# 4. Start server
cd choicescript
./serve.sh  # Linux/WSL
# OR
./serve.command  # macOS
# OR
run-server.bat  # Windows

# 5. Play!
# Opens automatically at http://localhost:4200
```

### Game Controls

- **Click** to make choices
- **Stats** button shows your progress
- **Restart** to play again
- **Achievements** tracks your accomplishments

### Tips for First Playthrough

1. **Read Polly's Commentary** - It's witty and helpful
2. **Choices Matter** - They affect your Collaboration stat
3. **Explore Relationships** - Get to know Izack, Aria, Zara, and Magnus
4. **Pick an Expedition** - Each reveals different lore
5. **Try Different Paths** - 14 unique endings await!

## For Contributors

### First-Time Setup

```bash
# 1. Fork the repository (on GitHub website)

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/Avalon.git
cd Avalon

# 3. Add upstream remote
git remote add upstream https://github.com/issdandavis/Avalon.git

# 4. Create a branch
git checkout -b feature/your-feature-name

# 5. Make changes
# Edit files...

# 6. Commit
git add .
git commit -m "Descriptive commit message"

# 7. Push
git push origin feature/your-feature-name

# 8. Create Pull Request (on GitHub)
```

### Contribution Workflow

```bash
# Update your fork
git fetch upstream
git checkout main
git merge upstream/main

# Create feature branch
git checkout -b feature/new-scene

# Make changes
# ...

# Test changes
cd game
./sync_scenes.sh
# Test in browser or ChoiceScript

# Commit and push
git add .
git commit -m "Add new exploration scene"
git push origin feature/new-scene

# Open PR on GitHub
```

### What to Contribute

**Writing & Narrative:**
- New scenes or dialogue
- Character development
- Lore expansion
- Polly's commentary

**Code:**
- Bug fixes
- New features
- Performance improvements
- Code quality

**Documentation:**
- Improve README files
- Add tutorials
- Fix typos
- Clarify instructions

**Testing:**
- Play through scenes
- Report bugs
- Test different paths
- Validate lore consistency

### Before Submitting PR

```bash
# Check for issues
git status

# Run tests (if applicable)
npm test  # or
python -m pytest

# Review your changes
git diff

# Make sure lore is consistent
grep -r "character names" choicescript_game/scenes/
```

## For AI Assistants

### Starting a Session

**Essential Reading:**

1. **Repository Context:**
   ```bash
   cat START_HERE.md
   cat docs/AI_SESSION_HANDOFF.md
   ```

2. **Current Status:**
   ```bash
   cat docs/PROJECT_ROADMAP.md
   cat docs/NEXT_TASKS.md
   ```

3. **Recent Changes:**
   ```bash
   git log --oneline -10
   git status
   ```

### Session Workflow

```markdown
1. **Understand Task**
   - Read issue/request carefully
   - Check related documentation
   - Review relevant code

2. **Plan Approach**
   - Identify affected files
   - Consider lore implications
   - Plan minimal changes

3. **Make Changes**
   - Edit files
   - Follow project conventions
   - Maintain lore consistency

4. **Test Changes**
   - Validate ChoiceScript syntax
   - Check game logic
   - Verify lore accuracy

5. **Document Work**
   - Update relevant docs
   - Add comments if needed
   - Update changelog

6. **Commit and Handoff**
   - Descriptive commit messages
   - Update AI_SESSION_HANDOFF.md
   - Create/update PR
```

### Key Principles

**DO:**
- ✅ Respect established lore
- ✅ Follow ChoiceScript conventions
- ✅ Keep Polly's voice consistent
- ✅ Test before committing
- ✅ Update documentation

**DON'T:**
- ❌ Contradict canon
- ❌ Skip testing
- ❌ Make massive changes
- ❌ Ignore style guide
- ❌ Forget to update docs

### Useful Commands

```bash
# Repository navigation
cat FILE_LOCATIONS.txt           # Find files
grep -r "search term" lore/      # Search lore
find . -name "*.txt"             # Find scenes

# Testing
node --check game/game.js        # Check JS
yamllint .github/workflows/      # Check YAML
./game/sync_scenes.sh            # Sync scenes

# Git operations
git log --oneline -20            # Recent history
git diff                         # See changes
git status                       # Current state
```

### Session Handoff Template

```markdown
## Session [ID] - [Date]

**Task:** Brief description

**Changes Made:**
- File 1: What changed
- File 2: What changed

**Testing:**
- [ ] ChoiceScript syntax validated
- [ ] Game logic tested
- [ ] Lore consistency checked

**Next Steps:**
- What remains to be done
- Any blockers or questions

**Branch:** feature/branch-name
**PR:** #123 (if created)
```

## For Developers

### Development Environment Setup

#### macOS

```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install node python git gh

# Clone repository
git clone https://github.com/issdandavis/Avalon.git
cd Avalon

# Install project dependencies (if any)
npm install  # if package.json exists
pip install -r requirements.txt  # if requirements.txt exists
```

#### Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install dependencies
sudo apt install nodejs npm python3 python3-pip git

# Install GitHub CLI
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh

# Clone repository
git clone https://github.com/issdandavis/Avalon.git
cd Avalon
```

#### Windows

```powershell
# Install Chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install dependencies
choco install nodejs python git gh

# Clone repository
git clone https://github.com/issdandavis/Avalon.git
cd Avalon
```

### IDE Setup

#### VS Code (Recommended)

```bash
# Install VS Code
# Download from https://code.visualstudio.com

# Open project
code .

# Recommended extensions (install from Extensions panel):
# - ChoiceScript Language
# - Markdown All in One
# - GitLens
# - ESLint
# - Python
```

#### GitHub Codespaces

```bash
# Create codespace (on GitHub website)
# Click "Code" → "Codespaces" → "New codespace"

# Everything pre-configured!
# Just start coding
```

### Testing Setup

```bash
# ChoiceScript validation
cd game
./bootstrap_choicescript.sh
./sync_scenes.sh
cd choicescript
./serve.sh

# JavaScript linting (if configured)
npm run lint

# Python testing (if configured)
pytest
```

### AI Automation Setup

See [GITHUB_APP_SETUP.md](GITHUB_APP_SETUP.md) for detailed instructions.

Quick version:

```bash
# 1. Set secrets
gh secret set OPENAI_API_KEY
gh secret set ANTHROPIC_API_KEY

# 2. Enable workflows
gh workflow enable ai-code-review.yml
gh workflow enable ci.yml

# 3. Test
gh workflow run ci.yml --ref your-branch
```

## Common Tasks

### Adding a New Scene

```bash
# 1. Create scene file
cd choicescript_game/scenes
touch new_scene.txt

# 2. Add title and content
cat > new_scene.txt << 'EOF'
*title New Scene

Your scene content here...

*choice
  #Option 1
    Consequence 1
  #Option 2
    Consequence 2

*goto next_scene
EOF

# 3. Link from another scene
# Edit the previous scene to *goto new_scene

# 4. Test
cd ../../game
./sync_scenes.sh
# Test in browser
```

### Updating Lore

```bash
# 1. Edit lore file
vim lore/characters/new_character.md

# 2. Verify consistency
grep -r "New Character" choicescript_game/scenes/

# 3. Update master chronicle
vim lore/IZACK_MASTER_CHRONICLE_UPDATED.txt

# 4. Commit
git add lore/
git commit -m "Add new character lore"
```

### Running CI Locally

```bash
# Validate ChoiceScript
node .github/workflows/validate_cs.js

# Check markdown
find . -name "*.md" -exec markdown-lint {} \;

# Validate YAML
yamllint .github/

# Check lore consistency
python .github/workflows/check_lore.py
```

### Creating a Release

```bash
# 1. Update version
# Edit relevant files with new version number

# 2. Update CHANGELOG
vim CHANGELOG.md

# 3. Commit
git add .
git commit -m "Release v1.1.0"

# 4. Tag
git tag -a v1.1.0 -m "Version 1.1.0"

# 5. Push
git push origin main --tags

# 6. Create GitHub release
gh release create v1.1.0 \
  --title "Version 1.1.0" \
  --notes "Release notes here"
```

### Debugging Issues

```bash
# Check logs
gh run list
gh run view RUN_ID --log

# Validate configuration
yamllint .github/agents/
node --check game/game.js

# Check for common issues
grep -r "TODO\|FIXME\|XXX" .

# Test locally
./game/sync_scenes.sh
open game/index.html
```

## Getting Help

### Documentation

- [README.md](../README.md) - Project overview
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Contribution guidelines
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Problem solving
- [AI_AUTOMATION.md](AI_AUTOMATION.md) - AI features
- [CUSTOM_AGENTS.md](CUSTOM_AGENTS.md) - Agent development

### Support Channels

```bash
# Create issue
gh issue create

# Start discussion
gh browse  # Then click Discussions

# View existing help
gh issue list --label help
```

### Quick Links

- 🎮 [Play the Game](../PLAY_THE_GAME.md)
- 📚 [Full Documentation](README.md)
- 🐛 [Report Bug](https://github.com/issdandavis/Avalon/issues/new?labels=bug)
- 💡 [Request Feature](https://github.com/issdandavis/Avalon/issues/new?labels=enhancement)
- ❓ [Ask Question](https://github.com/issdandavis/Avalon/discussions)

---

*Welcome to Avalon! Whether playing, contributing, or developing, we're glad you're here. Every choice matters. Every contribution counts.*
