# GitHub Copilot CLI Guide for Avalon Development

## Overview

GitHub Copilot CLI is a command-line interface tool that brings the power of GitHub Copilot to your terminal. It provides AI-assisted command suggestions, explanations, and git operations to streamline your development workflow on the Avalon project.

---

## 📦 Installation

### Prerequisites
- **GitHub CLI** (`gh`) installed and authenticated
- **GitHub Copilot** subscription (Individual, Business, or Enterprise)
- **Node.js** 16+ (for ChoiceScript development)

### Install GitHub Copilot CLI

```bash
# Install the GitHub Copilot extension for GitHub CLI
gh extension install github/gh-copilot

# Verify installation
gh copilot --version
```

### Authentication

```bash
# Authenticate GitHub CLI (if not already done)
gh auth login

# Follow the prompts to authenticate with your GitHub account
```

---

## 🚀 Core Commands

### `gh copilot suggest`

Get AI-powered command suggestions for any task.

#### Basic Usage

```bash
# Get a command suggestion
gh copilot suggest "run the ChoiceScript game locally"

# Shorter alias
ghcs "install dependencies for a Node.js project"
```

#### Examples for Avalon Development

```bash
# Setting up the development environment
gh copilot suggest "clone the ChoiceScript repository and set up the game files"

# Managing dependencies
gh copilot suggest "install Node.js dependencies and start a local server"

# Git operations
gh copilot suggest "create a new branch for adding a game scene"

# File operations
gh copilot suggest "find all .txt files in the scenes directory"

# Testing
gh copilot suggest "run a local HTTP server to test the HTML game"
```

### `gh copilot explain`

Get explanations for complex commands or code.

#### Basic Usage

```bash
# Explain a command
gh copilot explain "grep -r 'Polly' --include='*.txt' ."

# Shorter alias
ghce "git rebase -i HEAD~3"
```

#### Examples for Avalon Development

```bash
# Understand ChoiceScript syntax
gh copilot explain "*choice
  #Accept the mission
    *set courage +10
  #Decline politely
    *set caution +10"

# Understand bash scripts
gh copilot explain "cat game/scenes/*.txt | wc -l"

# Understand git operations
gh copilot explain "git log --oneline --graph --all --decorate"
```

---

## 🎮 Avalon-Specific Workflows

### Setting Up the Development Environment

```bash
# Get setup suggestions
gh copilot suggest "set up a local development environment for a ChoiceScript game"

# Clone ChoiceScript engine
gh copilot suggest "clone a git repository into a specific directory"

# Start local server
gh copilot suggest "start a simple HTTP server for testing HTML files"
```

### Working with Game Content

```bash
# Count words in game files
gh copilot suggest "count words in all .txt files in a directory"

# Search for character mentions
gh copilot suggest "search for a specific string in all text files recursively"

# Find unused variables
gh copilot suggest "find lines containing 'set' in ChoiceScript files"
```

### Git Workflow for Game Development

```bash
# Create feature branch
gh copilot suggest "create a git branch for adding a new game ending"

# Review changes before committing
gh copilot suggest "show unstaged changes in git"

# Commit with descriptive message
gh copilot suggest "commit all staged files with a message"

# Push to remote
gh copilot suggest "push current branch to remote repository"
```

### Testing and Quality Assurance

```bash
# Check for typos
gh copilot suggest "spell check all markdown files in a directory"

# Validate JSON/data files
gh copilot suggest "validate a JSON file syntax"

# Count scenes
gh copilot suggest "list all files in a directory with their line counts"
```

### Publishing Workflow

```bash
# Create release branch
gh copilot suggest "create a git tag for version 1.0"

# Generate changelog
gh copilot suggest "show git commits since last tag"

# Archive game files
gh copilot suggest "create a zip archive of a directory"
```

---

## 💡 Tips and Best Practices

### 1. **Be Specific in Your Requests**

**❌ Less Effective:**
```bash
gh copilot suggest "update files"
```

**✅ More Effective:**
```bash
gh copilot suggest "find and replace 'old_character_name' with 'new_character_name' in all .txt files in the scenes directory"
```

### 2. **Use Context from Your Environment**

Copilot CLI understands your current directory and git state. Work from the relevant directory:

```bash
# Navigate to the right location first
cd /home/runner/work/Avalon/Avalon/choicescript_game/scenes/

# Then get contextual suggestions
gh copilot suggest "count the number of choice blocks in all scene files"
```

### 3. **Chain Commands with Explanations**

```bash
# Get a complex command
gh copilot suggest "recursively find all files modified in the last 7 days"

# Then understand what it does
gh copilot explain "find . -type f -mtime -7"
```

### 4. **Save Frequently Used Commands as Aliases**

Add to your `~/.bashrc` or `~/.zshrc`:

```bash
# Copilot aliases
alias ghcs='gh copilot suggest'
alias ghce='gh copilot explain'

# Project-specific aliases
alias avalon-wordcount='find choicescript_game/scenes -name "*.txt" -exec wc -w {} + | tail -1'
alias avalon-server='cd game && python3 -m http.server 8000'
```

---

## 🎯 Common Avalon Development Tasks

### Task 1: Adding a New Game Scene

```bash
# 1. Create branch
gh copilot suggest "create a new git branch called feature/add-library-scene"

# 2. Create scene file
gh copilot suggest "create a new text file in a directory with a template"

# 3. Check scene structure
gh copilot explain "*label library_entrance"

# 4. Test the scene
gh copilot suggest "sync modified files to another directory"

# 5. Commit and push
gh copilot suggest "stage all changes, commit with message, and push to remote"
```

### Task 2: Updating Character Lore

```bash
# 1. Find all mentions of a character
gh copilot suggest "search for 'Izack' in all files and show the filename and line number"

# 2. Open relevant files
gh copilot suggest "open multiple files in vim from a list"

# 3. Verify consistency
gh copilot suggest "compare two text files side by side"
```

### Task 3: Preparing for Submission

```bash
# 1. Word count check
gh copilot suggest "count total words in all .txt files in a directory tree"

# 2. Verify file structure
gh copilot suggest "display directory tree structure with file sizes"

# 3. Create submission package
gh copilot suggest "create a zip file excluding .git and node_modules directories"

# 4. Generate changelog
gh copilot suggest "show git commit history formatted for a changelog"
```

### Task 4: Debugging ChoiceScript Syntax

```bash
# 1. Find unclosed choice blocks
gh copilot suggest "find files where the number of '*choice' doesn't match the indentation pattern"

# 2. Validate variable names
gh copilot suggest "find all lines with '*set' or '*create' and extract variable names"

# 3. Check for common errors
gh copilot explain "grep -n '\*goto' scenes/*.txt | grep -v '_'"
```

---

## 🔧 Integration with Avalon Workflow

### With `AUTOMATION_GUIDE.md` Workflows

Copilot CLI complements the automation workflows documented in `docs/AUTOMATION_GUIDE.md`:

```bash
# Get suggestions for Zapier automation setup
gh copilot suggest "create a webhook to trigger on git push"

# Discord notification automation
gh copilot suggest "send a message to Discord webhook with curl"

# Google Sheets integration
gh copilot suggest "export CSV data to a Google Sheets-compatible format"
```

### With AI Session Handoff (`AI_SESSION_HANDOFF.md`)

```bash
# Quickly review session context
gh copilot suggest "show git log for commits in the last session"

# Update documentation
gh copilot suggest "append a new entry to a markdown file with timestamp"

# Branch management
gh copilot suggest "list all branches sorted by last commit date"
```

### With Game Testing

```bash
# Start test server
gh copilot suggest "run a local web server on port 8000 in the game directory"

# Check for broken links
gh copilot suggest "find all href and src attributes in HTML files"

# Validate game paths
gh copilot suggest "check if all goto labels in ChoiceScript files have corresponding labels"
```

---

## 📚 Advanced Use Cases

### Scripting with Copilot Suggestions

You can use Copilot CLI suggestions in scripts:

```bash
#!/bin/bash
# Script to validate game content before commit

echo "Checking word count..."
gh copilot suggest "count total words in .txt files in choicescript_game/scenes" --format shell | bash

echo "Checking for TODOs..."
gh copilot suggest "find all TODO comments in text files" --format shell | bash

echo "Running syntax checks..."
gh copilot suggest "validate ChoiceScript syntax (check for balanced choice blocks)" --format shell | bash
```

### Custom Commands for Avalon

Create a `scripts/` directory with Copilot-assisted utilities:

```bash
# scripts/scene-stats.sh
#!/bin/bash
# Generated with: gh copilot suggest "create a script to count choices in ChoiceScript files"

find choicescript_game/scenes -name "*.txt" -exec grep -c "^\s*#" {} \; | \
  awk '{sum += $1} END {print "Total choices:", sum}'
```

---

## 🐛 Troubleshooting

### Copilot CLI Not Working

```bash
# Check installation
gh extension list

# Reinstall if needed
gh extension remove github/gh-copilot
gh extension install github/gh-copilot

# Check authentication
gh auth status
```

### Getting Better Suggestions

1. **Provide more context**: Include file types, directory names, and specific goals
2. **Use domain language**: Mention "ChoiceScript", "scenes", "game variables"
3. **Iterate**: If the first suggestion isn't perfect, refine your request

### Rate Limits

If you hit rate limits:
- Wait a few minutes between requests
- Simplify complex queries
- Use local commands for simple operations

---

## 📖 Learning Resources

### GitHub Copilot CLI Documentation
- [Official GitHub Copilot CLI Docs](https://docs.github.com/en/copilot/github-copilot-in-the-cli)
- [GitHub CLI Manual](https://cli.github.com/manual/)

### ChoiceScript Resources
- [ChoiceScript Wiki](https://choicescriptdev.fandom.com/wiki/ChoiceScript_Wiki)
- [Choice of Games Forum](https://forum.choiceofgames.com/)

### Git and Version Control
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [GitHub Docs](https://docs.github.com/)

---

## 🎓 Quick Reference

### Most Useful Commands for Avalon Development

```bash
# Environment setup
ghcs "install Node.js dependencies"
ghcs "start a local HTTP server"

# Content management
ghcs "count words in all text files"
ghcs "find and replace text in multiple files"
ghcs "search for a pattern in all files"

# Git workflow
ghcs "create a new feature branch"
ghcs "show recent commits"
ghcs "stage and commit all changes"

# Testing
ghcs "validate JSON syntax"
ghcs "check file encodings"
ghcs "list files by modification date"

# Publishing
ghcs "create a git tag"
ghcs "generate a changelog"
ghcs "create a zip archive"
```

### Command Templates

Replace `<description>` with your specific need:

```bash
gh copilot suggest "<description>"
gh copilot explain "<command>"
```

---

## 🌟 Benefits for Avalon Development

1. **Faster Onboarding**: New contributors can get up to speed quickly
2. **Consistent Commands**: Everyone uses best-practice commands
3. **Documentation as Code**: Commands are self-documenting
4. **Error Prevention**: Get correct syntax the first time
5. **Time Savings**: Reduce time searching Stack Overflow
6. **Learning Tool**: Understand complex commands as you use them

---

## 🤝 Contributing to This Guide

Found a useful workflow? Add it to this guide!

1. Test your Copilot CLI commands
2. Document the use case and commands
3. Add examples specific to Avalon development
4. Submit a PR with your additions

---

**"Let AI handle the syntax. You focus on the story."**

*— A guide for weaving technology and narrative in Avalon*

---

## Appendix: Example Workflows

### Complete New Scene Workflow

```bash
# 1. Plan the scene
gh copilot suggest "create a new git branch for adding a marketplace scene"

# 2. Create the file
cd choicescript_game/scenes
touch marketplace.txt

# 3. Add boilerplate
gh copilot suggest "show me a basic ChoiceScript scene template"

# 4. Add to scene list
gh copilot suggest "append a line to startup.txt"

# 5. Sync and test
cd ../..
./game/sync_scenes.sh

# 6. Review changes
gh copilot suggest "show git diff for staged and unstaged files"

# 7. Commit
gh copilot suggest "commit with message: Add marketplace scene with merchant interactions"

# 8. Push
git push -u origin feature/marketplace-scene
```

### Bug Fix Workflow

```bash
# 1. Identify the issue
gh copilot suggest "search for 'undefined variable' errors in ChoiceScript"

# 2. Create fix branch
gh copilot suggest "create a branch called bugfix/undefined-courage-variable"

# 3. Find all instances
gh copilot suggest "find all files containing the variable 'courage'"

# 4. Review current usage
gh copilot explain "grep -rn 'courage' choicescript_game/scenes/"

# 5. Fix the issue
# (manual editing)

# 6. Verify fix
gh copilot suggest "check if a variable is defined before its first use in ChoiceScript"

# 7. Test
gh copilot suggest "start a local server to test the game"

# 8. Commit and push
gh copilot suggest "stage all changes, commit, and push to remote"
```

### Release Preparation Workflow

```bash
# 1. Update version
gh copilot suggest "update version number in package.json to 1.1.0"

# 2. Generate changelog
gh copilot suggest "show all commits since tag v1.0.0"

# 3. Update docs
gh copilot suggest "append changelog entries to CHANGELOG.md"

# 4. Word count verification
gh copilot suggest "count total words in all scene files and compare to 30000"

# 5. Create tag
gh copilot suggest "create an annotated git tag v1.1.0 with message"

# 6. Build release package
gh copilot suggest "create a zip file named pollys-wingscroll-v1.1.0.zip"

# 7. Push tag
gh copilot suggest "push a git tag to remote repository"

# 8. Create GitHub release
gh copilot suggest "create a GitHub release from a tag using gh CLI"
```

---

*Last updated: November 2025*
