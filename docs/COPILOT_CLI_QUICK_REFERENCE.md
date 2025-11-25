# GitHub Copilot CLI Quick Reference

## Installation

```bash
gh extension install github/gh-copilot
```

## Core Commands

| Command | Description | Alias |
|---------|-------------|-------|
| `gh copilot suggest "<task>"` | Get command suggestion | `ghcs` |
| `gh copilot explain "<command>"` | Explain a command | `ghce` |

## Common Avalon Development Tasks

### Setup & Environment

```bash
# Install dependencies
ghcs "install Node.js dependencies"

# Start local server
ghcs "start a local HTTP server for testing HTML files"

# Clone ChoiceScript engine
ghcs "clone a git repository into a specific directory"
```

### Content Management

```bash
# Count words in game files
ghcs "count words in all .txt files in choicescript_game/scenes"

# Search for character mentions
ghcs "search for 'Polly' in all text files recursively"

# Find all choice blocks
ghcs "count occurrences of '*choice' in all scene files"
```

### Git Workflow

```bash
# Create feature branch
ghcs "create a git branch for adding a new game scene"

# Show changes
ghcs "show unstaged changes in git"

# Commit changes
ghcs "stage all files and commit with a descriptive message"

# Push branch
ghcs "push current branch to remote repository"
```

### Testing & Validation

```bash
# Validate ChoiceScript syntax
ghcs "check for balanced choice blocks in text files"

# List scenes
ghcs "list all .txt files in a directory with line counts"

# Find TODOs
ghcs "search for TODO comments in all files"
```

### Publishing

```bash
# Create version tag
ghcs "create an annotated git tag v1.0.0"

# Generate changelog
ghcs "show git commits since last tag formatted as changelog"

# Create release archive
ghcs "create a zip file excluding .git and node_modules"
```

## Tips for Better Suggestions

1. **Be specific**: Include file types, directories, and goals
2. **Use context**: Run commands from the relevant directory
3. **Chain commands**: Get a suggestion, then explain it
4. **Iterate**: Refine requests if the first answer isn't perfect

## Example Workflow: Adding a New Scene

```bash
# 1. Create branch
ghcs "create a git branch called feature/add-library-scene"

# 2. Create scene file
cd choicescript_game/scenes
touch library.txt

# 3. Get template
ghcs "show me a basic ChoiceScript scene template"

# 4. Add to scene list
ghcs "append a line to startup.txt"

# 5. Test locally
ghcs "start a local HTTP server in the game directory"

# 6. Commit and push
ghcs "stage all changes, commit with message, and push to remote"
```

## Useful Aliases

Add to `~/.bashrc` or `~/.zshrc`:

```bash
# Copilot shortcuts
alias ghcs='gh copilot suggest'
alias ghce='gh copilot explain'

# Avalon-specific
alias avalon-wc='find choicescript_game/scenes -name "*.txt" -exec wc -w {} + | tail -1'
alias avalon-serve='cd game && python3 -m http.server 8000'
alias avalon-scenes='ls -lh choicescript_game/scenes/*.txt'
```

## Troubleshooting

```bash
# Check installation
gh extension list

# Reinstall
gh extension remove github/gh-copilot
gh extension install github/gh-copilot

# Verify authentication
gh auth status
```

## Learn More

📖 Full guide: `docs/GITHUB_COPILOT_CLI_GUIDE.md`

---

*Quick reference for GitHub Copilot CLI in Avalon development*
