# Troubleshooting Guide

Complete troubleshooting guide for the Avalon project's development environment, AI automation, and game systems.

## Table of Contents

- [Quick Diagnostics](#quick-diagnostics)
- [ChoiceScript Issues](#choicescript-issues)
- [Game Development](#game-development)
- [AI Automation](#ai-automation)
- [GitHub Workflows](#github-workflows)
- [Build and Testing](#build-and-testing)
- [Lore and Content](#lore-and-content)
- [Common Error Messages](#common-error-messages)
- [Getting Help](#getting-help)

## Quick Diagnostics

### System Check

Run this to check your environment:

```bash
# Create diagnostic script
cat > check_system.sh << 'EOF'
#!/bin/bash
echo "=== Avalon Project Diagnostics ==="
echo ""

echo "Git Version:"
git --version

echo ""
echo "Node.js Version:"
node --version 2>&1 || echo "Node.js not installed"

echo ""
echo "Python Version:"
python3 --version 2>&1 || echo "Python not installed"

echo ""
echo "GitHub CLI:"
gh --version 2>&1 || echo "GitHub CLI not installed"

echo ""
echo "Repository Status:"
git status

echo ""
echo "Current Branch:"
git branch --show-current

echo ""
echo "Recent Commits:"
git log --oneline -5

echo ""
echo "Remotes:"
git remote -v

echo ""
echo "File Counts:"
echo "ChoiceScript scenes: $(find choicescript_game/scenes -name '*.txt' 2>/dev/null | wc -l)"
echo "Lore documents: $(find lore -name '*.md' 2>/dev/null | wc -l)"
echo "Documentation files: $(find docs -name '*.md' 2>/dev/null | wc -l)"

echo ""
echo "=== Diagnostics Complete ==="
EOF

chmod +x check_system.sh
./check_system.sh
```

### Health Check Commands

```bash
# Quick checks
git status                          # Check repo state
gh repo view                        # View repo info
gh pr list                          # List PRs
gh run list --limit 5               # Recent workflow runs

# File validation
find . -name "*.txt" -type f -exec grep -l "^\*title" {} \;  # ChoiceScript titles
find . -name "*.md" -type f -exec wc -l {} \;               # Document sizes
```

## ChoiceScript Issues

### Syntax Errors

#### Missing *title Command

**Error:**
```
Scene file must start with *title
```

**Solution:**
```choicescript
*title Your Scene Name

Your scene content here...
```

#### Unbalanced *if Statements

**Error:**
```
*if without matching *else or *endif
```

**Solution:**
```choicescript
*if condition
  Content when true
*else
  Content when false

*comment Always close your *if blocks
```

#### Orphaned Choice

**Error:**
```
*choice without options
```

**Solution:**
```choicescript
*choice
  #Option 1
    Consequence of option 1
  #Option 2
    Consequence of option 2
  #Option 3
    Consequence of option 3
```

### Variable Issues

#### Undefined Variable

**Error:**
```
Variable 'collaboration' not defined
```

**Solution:**

1. Check `startup.txt`:
```choicescript
*create collaboration 50
```

2. Or check `choicescript_stats.txt`:
```choicescript
*stat_chart
  text Name
  text Collaboration
```

#### Variable Name Typo

**Error:**
```
Variable 'colaboration' not found (should be 'collaboration')
```

**Solution:**

Search and replace:
```bash
# Find all instances
grep -r "colaboration" choicescript_game/scenes/

# Fix with sed
sed -i 's/colaboration/collaboration/g' choicescript_game/scenes/*.txt
```

### Scene Flow Issues

#### Goto Target Not Found

**Error:**
```
*goto target_label not found
```

**Solution:**

1. Ensure label exists:
```choicescript
*label target_label
Content here...
```

2. Check spelling matches exactly
3. Labels are case-sensitive

#### Infinite Loop

**Error:**
```
Scene appears to loop infinitely
```

**Solution:**

Add progression:
```choicescript
*label scene_loop
*if loop_counter > 5
  *goto end_scene
*else
  *set loop_counter + 1
  Scene content...
  *goto scene_loop

*label end_scene
```

### Testing ChoiceScript Locally

```bash
# Clone ChoiceScript if not done
cd game
./bootstrap_choicescript.sh

# Sync your scenes
./sync_scenes.sh

# Start server
cd choicescript
./serve.sh  # or serve.command on Mac

# Open browser
open http://localhost:4200
```

If scenes don't appear:

```bash
# Force sync
rm -rf choicescript/web/mygame/scenes/*
./sync_scenes.sh

# Restart server
```

## Game Development

### HTML Version Issues

#### Game Not Loading

**Problem:** index.html shows blank page

**Solutions:**

1. Check browser console (F12)
2. Verify file paths:
```html
<script src="game.js"></script>
<link rel="stylesheet" href="style.css">
```

3. Check for JavaScript errors:
```javascript
// Open browser console and look for:
Uncaught ReferenceError: ...
SyntaxError: ...
```

4. Validate HTML:
```bash
# Check for basic issues
grep -n "<!DOCTYPE" game/index.html
grep -n "</html>" game/index.html
```

#### Save/Load Not Working

**Problem:** Game state not persisting

**Solution:**

Check localStorage:
```javascript
// In browser console
localStorage.getItem('avalonGameState')

// Clear and try again
localStorage.clear()
```

### Stats Not Updating

**Problem:** Collaboration or relationship stats don't change

**Solutions:**

1. Check stat modification:
```javascript
// In game.js, ensure:
stats.collaboration += value;
updateStatsDisplay();
```

2. Verify stat tracking:
```javascript
console.log('Collaboration:', stats.collaboration);
```

3. Check for typos:
```javascript
// Wrong
stats.colaboration += 10;

// Right
stats.collaboration += 10;
```

### Choice Logic Errors

**Problem:** Wrong choices lead to wrong scenes

**Solution:**

Debug choice handling:
```javascript
function makeChoice(choiceId) {
  console.log('Choice selected:', choiceId);
  console.log('Current scene:', currentScene);
  console.log('Stats before:', {...stats});
  
  // Your choice logic
  
  console.log('Stats after:', {...stats});
  console.log('Next scene:', nextScene);
}
```

## AI Automation

### AI Code Review Not Running

**Problem:** No AI review comments on PR

**Diagnostics:**

```bash
# Check if workflow exists
ls .github/workflows/ai-code-review.yml

# Check workflow runs
gh run list --workflow=ai-code-review.yml

# View specific run
gh run view RUN_ID --log
```

**Common Causes:**

1. **Missing API Key**
   ```bash
   # Check if secret exists
   gh secret list
   
   # Set if missing
   gh secret set OPENAI_API_KEY
   ```

2. **Path Filters**
   ```yaml
   # Check paths in workflow file
   paths:
     include:
       - 'choicescript_game/**/*.txt'
   
   # Ensure changed files match
   ```

3. **Workflow Disabled**
   ```bash
   # Check workflow status
   gh workflow list
   
   # Enable if needed
   gh workflow enable ai-code-review.yml
   ```

### High API Costs

**Problem:** Unexpected OpenAI/Anthropic charges

**Solutions:**

1. **Check Usage:**
   ```bash
   # Review recent runs
   gh run list --workflow=ai-code-review.yml --limit 20
   
   # Count API calls
   grep -r "openai.ChatCompletion.create" .github/workflows/
   ```

2. **Reduce Token Usage:**
   ```yaml
   # In agent config
   ai_config:
     max_tokens: 1000  # Reduce from 4000
   ```

3. **Add Rate Limiting:**
   ```yaml
   # In .github/agents/config.yml
   rate_limits:
     per_hour: 50  # Reduce from 100
     per_day: 200  # Reduce from 500
   ```

4. **Use Cheaper Model:**
   ```yaml
   ai_config:
     model: "gpt-3.5-turbo"  # Instead of gpt-4
   ```

### Lore Checker False Positives

**Problem:** AI flags correct lore as inconsistent

**Solutions:**

1. **Update Canonical Names:**
   ```yaml
   # In code_review_agent.yml
   lore_checks:
     character_names:
       canonical:
         - "Izack Thorne"
         - "Professor Thorne"  # Add variant
   ```

2. **Add Exemptions:**
   ```yaml
   exemptions:
     - path: "specific_scene.txt"
       rules: ["consistent_character_names"]
       reason: "Uses informal names"
   ```

3. **Improve AI Prompt:**
   ```yaml
   system_prompt: |
     Character name variants are allowed:
     - "Izack" = "Izack Thorne" = "Professor Thorne"
     Only flag actual misspellings.
   ```

### Agent Timeout

**Problem:** Agent runs too long and times out

**Solutions:**

1. **Reduce File Size:**
   ```yaml
   context:
     max_file_size: 5000  # Reduce from 10000
   ```

2. **Enable Parallel Processing:**
   ```yaml
   performance:
     parallel: true
     max_workers: 4
   ```

3. **Increase Timeout:**
   ```yaml
   performance:
     timeout_per_file: 60  # Increase from 30
   ```

## GitHub Workflows

### Workflow Not Triggering

**Problem:** Workflow doesn't run on push/PR

**Diagnostics:**

```bash
# Check workflow syntax
yamllint .github/workflows/ci.yml

# Validate workflow
gh workflow view ci.yml

# Check workflow runs
gh run list --workflow=ci.yml
```

**Common Causes:**

1. **YAML Syntax Error:**
   ```bash
   # Validate YAML
   python3 -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))"
   ```

2. **Wrong Branch:**
   ```yaml
   on:
     push:
       branches: [ main, master ]  # Check branch name matches
   ```

3. **Path Filters Too Restrictive:**
   ```yaml
   paths:
     - 'choicescript_game/**'  # May be too narrow
   ```

### Permission Denied

**Problem:** Workflow can't access repository

**Solution:**

Add permissions:
```yaml
permissions:
  contents: read
  pull-requests: write
  issues: write
```

### Secrets Not Available

**Problem:** `${{ secrets.API_KEY }}` is empty

**Solutions:**

1. **Set Secret:**
   ```bash
   gh secret set API_KEY
   ```

2. **Check Secret Name:**
   ```yaml
   # Exact match required
   OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
   ```

3. **Check Repository:**
   ```bash
   # Secrets are repository-specific
   gh secret list --repo issdandavis/Avalon
   ```

## Build and Testing

### ChoiceScript Tests Failing

**Problem:** CI reports ChoiceScript validation errors

**Debug:**

```bash
# Run validation locally
node .github/workflows/validate_cs.js

# Check specific file
node --check choicescript_game/scenes/arrival.txt
```

**Common Issues:**

1. **Missing Title:**
   ```bash
   # Find files without *title
   find choicescript_game/scenes -name "*.txt" -type f ! -exec grep -q "^\*title" {} \; -print
   ```

2. **Syntax Errors:**
   ```bash
   # Check for common issues
   grep -n "*cho ice" choicescript_game/scenes/*.txt  # Space typo
   grep -n "* if" choicescript_game/scenes/*.txt      # Space before if
   ```

### Link Checker Failures

**Problem:** Documentation links broken

**Solution:**

```bash
# Find broken links
find . -name "*.md" -exec grep -H "\[.*\](.*)" {} \; | while read line; do
  file=$(echo $line | cut -d: -f1)
  link=$(echo $line | grep -oP '\]\(\K[^)]+')
  
  if [[ ! $link =~ ^http ]]; then
    target="$(dirname $file)/$link"
    if [[ ! -e "$target" ]]; then
      echo "Broken: $file -> $link"
    fi
  fi
done
```

### Linting Errors

**Problem:** Code style violations

**Solutions:**

1. **Auto-fix:**
   ```bash
   # For JavaScript
   npx eslint --fix game/game.js
   
   # For Python
   black examples/
   
   # For YAML
   yamllint -f auto .github/
   ```

2. **Check Configuration:**
   ```bash
   # View linter config
   cat .eslintrc.json
   cat .yamllint
   ```

## Lore and Content

### Character Name Inconsistency

**Problem:** Character referred to with different names

**Find Variants:**

```bash
# Search for character mentions
grep -r "Izack" choicescript_game/scenes/ writing_drafts/ lore/
grep -r "Isaac" choicescript_game/scenes/ writing_drafts/ lore/  # Wrong spelling
```

**Fix:**

```bash
# Replace wrong spelling
find choicescript_game/scenes -name "*.txt" -exec sed -i 's/Isaac Thorne/Izack Thorne/g' {} \;
```

### Timeline Conflicts

**Problem:** Events in wrong chronological order

**Solution:**

Create timeline:
```bash
# Extract dates from lore
grep -r "year \|age \|century " lore/ docs/AETHERMOOR_CHRONICLES.md | sort
```

Reference canonical timeline in `docs/AETHERMOOR_CHRONICLES.md`.

### Magic System Inconsistency

**Problem:** Magic described differently in different scenes

**Solution:**

1. Review canonical magic system in `lore/magic_system.md`
2. Search for conflicting descriptions:
   ```bash
   grep -r "dimensional" choicescript_game/scenes/
   grep -r "collaborative casting" choicescript_game/scenes/
   ```

3. Standardize terminology

## Common Error Messages

### Git Errors

#### "Your branch is behind"

```bash
# Pull latest changes
git pull origin main

# Or if you have local commits
git pull --rebase origin main
```

#### "Merge conflict"

```bash
# View conflicts
git status

# Edit conflicting files
# Look for <<<<<<< and >>>>>>>

# After resolving
git add .
git commit -m "Resolve merge conflict"
```

#### "Permission denied (publickey)"

```bash
# Check SSH key
ssh -T git@github.com

# Or use HTTPS instead
git remote set-url origin https://github.com/issdandavis/Avalon.git
```

### Node.js Errors

#### "Module not found"

```bash
# Install dependencies
npm install

# Or specific module
npm install missing-module
```

#### "Port already in use"

```bash
# Find process using port
lsof -i :4200

# Kill process
kill -9 PID
```

### Python Errors

#### "No module named 'yaml'"

```bash
# Install missing module
pip install pyyaml

# Or from requirements.txt
pip install -r requirements.txt
```

#### "Permission denied"

```bash
# Fix with chmod
chmod +x script.py

# Or run with python
python3 script.py
```

## Getting Help

### Before Asking for Help

1. **Check This Guide** - Search for your error message
2. **Review Documentation:**
   - [README.md](../README.md)
   - [CONTRIBUTING.md](../CONTRIBUTING.md)
   - [AI_AUTOMATION.md](AI_AUTOMATION.md)
   - [CUSTOM_AGENTS.md](CUSTOM_AGENTS.md)

3. **Check Existing Issues:**
   ```bash
   gh issue list --label troubleshooting
   gh issue list --search "your error message"
   ```

4. **Gather Information:**
   - Error message (full text)
   - What you were trying to do
   - What you expected to happen
   - What actually happened
   - Your environment (OS, versions)

### Creating a Bug Report

```bash
# Create detailed issue
gh issue create --label bug --title "Clear description of problem"
```

Include:

```markdown
## Description
Brief description of the problem

## Steps to Reproduce
1. Step one
2. Step two
3. Error occurs

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Error Message
```
Full error message here
```

## Environment
- OS: macOS 13.0
- Node.js: v18.0.0
- Python: 3.11.0
- Git: 2.39.0

## Additional Context
Any other relevant information
```

### Where to Get Help

1. **GitHub Issues** - For bugs and problems
   ```bash
   gh issue create
   ```

2. **Discussions** - For questions and ideas
   ```bash
   gh browse  # Then click Discussions
   ```

3. **Pull Request Comments** - For PR-specific issues
   ```bash
   gh pr view --comments
   ```

4. **Project Maintainers** - @issdandavis

### Self-Service Resources

- [GitHub Docs](https://docs.github.com)
- [ChoiceScript Wiki](https://choiceofgames.com/make-your-own-games/choicescript-intro/)
- [Node.js Docs](https://nodejs.org/docs)
- [Python Docs](https://docs.python.org)
- [Git Documentation](https://git-scm.com/doc)

## Quick Reference

### Useful Commands

```bash
# Repository
git status                    # Check status
git pull                      # Update local
git log --oneline -10         # Recent commits

# GitHub CLI
gh repo view                  # View repo
gh pr list                    # List PRs
gh issue list                 # List issues
gh run list                   # Workflow runs

# Testing
node --check file.js          # Check JS syntax
python3 -m py_compile file.py # Check Python syntax
yamllint file.yml             # Check YAML syntax

# Project Specific
cd game && ./sync_scenes.sh   # Sync ChoiceScript
open game/index.html          # Play HTML version
gh workflow run ci.yml        # Trigger CI
```

### Emergency Fixes

```bash
# Undo last commit (not pushed)
git reset --soft HEAD~1

# Discard all local changes
git checkout -- .

# Start fresh from remote
git fetch origin
git reset --hard origin/main

# Clear all caches
rm -rf node_modules/
npm cache clean --force
pip cache purge
```

---

*When in doubt, check the documentation first, then ask for help with specific details.*
