# 🚀 Git & GitHub Quick Reference

**One-page cheat sheet for daily use**

---

## Essential Git Commands

### Getting Started
```bash
git init                          # Create new repo
git clone <url>                   # Download repo
git config --global user.name ""  # Set name
git config --global user.email "" # Set email
```

### Daily Workflow
```bash
git status                        # Check current state
git add .                         # Stage all changes
git add <file>                    # Stage specific file
git commit -m "message"           # Save changes
git push origin <branch>          # Upload to GitHub
git pull origin <branch>          # Download from GitHub
```

### Branching
```bash
git branch                        # List branches
git branch <name>                 # Create branch
git checkout <branch>             # Switch branch
git checkout -b <name>            # Create and switch
git merge <branch>                # Merge branch
git branch -d <name>              # Delete branch
```

### Viewing History
```bash
git log                           # Full history
git log --oneline                 # Compact view
git log --graph --all             # Visual tree
git diff                          # Show changes
git show <commit>                 # Show commit details
```

### Undoing Changes
```bash
git checkout -- <file>            # Discard working changes
git reset HEAD <file>             # Unstage file
git reset --soft HEAD~1           # Undo commit, keep changes
git reset --hard HEAD~1           # Undo commit, discard all
git revert <commit>               # Undo with new commit
```

### Stashing
```bash
git stash                         # Save current work
git stash list                    # List all stashes
git stash pop                     # Restore latest stash
git stash drop                    # Delete latest stash
git stash clear                   # Delete all stashes
```

---

## GitHub Workflow

### Fork & Clone Pattern
```bash
# 1. Fork on GitHub (click Fork button)

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
cd REPO-NAME

# 3. Add upstream
git remote add upstream https://github.com/ORIGINAL-OWNER/REPO-NAME.git

# 4. Keep updated
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### Feature Branch Pattern
```bash
# 1. Update main
git checkout main
git pull origin main

# 2. Create feature branch
git checkout -b feature/my-feature

# 3. Work
# ... edit files ...

# 4. Commit
git add .
git commit -m "Add my feature"

# 5. Push
git push origin feature/my-feature

# 6. Create PR on GitHub

# 7. After merge
git checkout main
git pull origin main
git branch -d feature/my-feature
```

---

## Common Scenarios

### Starting New Work
```bash
git checkout main
git pull origin main
git checkout -b feature/new-work
# ... make changes ...
git add .
git commit -m "Implement new work"
git push origin feature/new-work
```

### Switching Tasks (with uncommitted work)
```bash
git stash
git checkout other-branch
# ... do work ...
git checkout original-branch
git stash pop
```

### Updating Your Branch
```bash
git fetch origin
git checkout your-branch
git merge origin/main
# or
git rebase origin/main
```

### Fixing Last Commit
```bash
# Change message
git commit --amend -m "New message"

# Add forgotten files
git add forgotten-file.txt
git commit --amend --no-edit
```

### Resolving Conflicts
```bash
# 1. Try to merge/pull
git merge branch-name
# CONFLICT appears

# 2. Open conflicted files
# Look for <<<<<<< ======= >>>>>>>

# 3. Edit to resolve
# Remove markers, choose correct version

# 4. Mark as resolved
git add conflicted-file.txt

# 5. Complete merge
git commit -m "Resolve merge conflict"
```

---

## Repository Setup (First Time)

### For Contributing to Existing Project
```bash
# 1. Fork on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/PROJECT.git
cd PROJECT

# 3. Add upstream
git remote add upstream https://github.com/ORIGINAL-OWNER/PROJECT.git

# 4. Verify remotes
git remote -v
```

### For New Project
```bash
# 1. Create locally
mkdir my-project
cd my-project
git init

# 2. Create on GitHub

# 3. Connect
git remote add origin https://github.com/YOUR-USERNAME/my-project.git

# 4. First push
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

---

## Git Aliases (Optional but Useful)

Add to `~/.gitconfig`:

```ini
[alias]
    co = checkout
    br = branch
    ci = commit
    st = status
    unstage = reset HEAD --
    last = log -1 HEAD
    visual = log --graph --oneline --all --decorate
    amend = commit --amend --no-edit
```

Usage:
```bash
git co main      # instead of git checkout main
git br           # instead of git branch
git visual       # pretty visualization
```

---

## GitHub Web Shortcuts

Press `?` on GitHub.com to see all shortcuts!

**Most Useful:**
- `s` or `/` - Search
- `t` - File finder
- `g` + `c` - Go to Code
- `g` + `i` - Go to Issues
- `g` + `p` - Go to Pull Requests
- `.` - Open web editor

---

## Markdown for Issues/PRs

```markdown
# Heading 1
## Heading 2
### Heading 3

**bold** *italic* ~~strikethrough~~

- Bullet list
1. Numbered list

[Link text](https://url.com)

`inline code`

```code block```

> Quote

@username
#123 (issue/PR number)

![Image](url)
```

---

## Emergency Commands

### "I committed to wrong branch!"
```bash
git log -1              # Get commit hash
git checkout correct-branch
git cherry-pick <hash>
git checkout wrong-branch
git reset --hard HEAD~1
```

### "I need to discard everything!"
```bash
git reset --hard HEAD
git clean -fd
```

### "I lost my commits!"
```bash
git reflog              # Find lost commit
git cherry-pick <hash>  # Recover it
```

### "I pushed sensitive data!"
```bash
# 1. Remove from code
git rm sensitive-file
git commit -m "Remove sensitive data"

# 2. Force push (if safe)
git push --force

# 3. ROTATE CREDENTIALS IMMEDIATELY
# 4. Consider using BFG Repo-Cleaner
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Permission denied" | Set up SSH keys or use HTTPS |
| "Merge conflict" | Edit files, remove markers, `git add`, `git commit` |
| "Detached HEAD" | `git checkout branch-name` |
| "Can't pull" | `git stash`, `git pull`, `git stash pop` |
| "Can't push" | `git pull` first, then `git push` |

---

## Best Practices

✅ **Do:**
- Commit often, push regularly
- Write clear commit messages
- Use branches for features
- Pull before starting work
- Review changes before committing
- Keep commits focused and small

❌ **Don't:**
- Commit directly to main (use branches)
- Commit broken code
- Force push to shared branches
- Commit sensitive data
- Use vague commit messages
- Create giant commits with unrelated changes

---

## Commit Message Template

```
Brief summary (50 chars or less)

More detailed explanation if needed (wrap at 72 chars).
Explain what and why, not how.

- Bullet points okay
- Use present tense

Closes #123
```

---

## Branch Naming Convention

```
type/description-in-kebab-case
```

**Types:**
- `feature/` - New feature
- `fix/` - Bug fix
- `hotfix/` - Urgent fix
- `docs/` - Documentation
- `refactor/` - Code cleanup
- `test/` - Tests

**Examples:**
- `feature/add-user-login`
- `fix/button-alignment`
- `docs/update-readme`

---

## .gitignore Common Patterns

```gitignore
# Dependencies
node_modules/
vendor/

# Environment
.env
.env.local

# OS files
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp

# Build output
dist/
build/
*.log

# Secrets
*.key
*.pem
config/secrets.yml
```

---

## Useful Git Configs

```bash
# Colors
git config --global color.ui auto

# Editor
git config --global core.editor "code --wait"

# Default branch
git config --global init.defaultBranch main

# Credential caching (15 min)
git config --global credential.helper cache

# Line endings (Windows)
git config --global core.autocrlf true

# Line endings (Mac/Linux)
git config --global core.autocrlf input

# View all config
git config --list
```

---

## For This Repository (Aethromoor)

### Quick Start
```bash
# Fork on GitHub first!

git clone https://github.com/YOUR-USERNAME/Aethromoor.git
cd Aethromoor
git remote add upstream https://github.com/issdandavis/Aethromoor.git

git checkout -b feature/my-contribution
# ... make changes ...
git add .
git commit -m "Description of changes"
git push origin feature/my-contribution
# Create PR on GitHub
```

### Keep Updated
```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

---

## Resources

**Full Guides:**
- [GitHub Tutorial](GITHUB_TUTORIAL.md) - Complete beginner's guide
- [Git Basics](GIT_BASICS.md) - Advanced workflows
- [Contributing](../CONTRIBUTING.md) - Project contribution guide

**External:**
- [GitHub Docs](https://docs.github.com)
- [Pro Git Book](https://git-scm.com/book)
- [Git Flight Rules](https://github.com/k88hudson/git-flight-rules)

---

**Print this page for quick reference!**

*Last updated: 2025-12-02*
