# 📚 Git Basics & Workflows

**Level:** Intermediate  
**Prerequisites:** Basic GitHub knowledge ([GITHUB_TUTORIAL.md](GITHUB_TUTORIAL.md))  
**Goal:** Master Git workflows for effective collaboration

---

## Table of Contents

1. [Git vs GitHub](#git-vs-github)
2. [Essential Git Concepts](#essential-git-concepts)
3. [Common Workflows](#common-workflows)
4. [Branching Strategies](#branching-strategies)
5. [Advanced Commands](#advanced-commands)
6. [Collaboration Patterns](#collaboration-patterns)
7. [Troubleshooting](#troubleshooting)
8. [Best Practices](#best-practices)

---

## Git vs GitHub

### Git (The Tool)

**What it is:** Version control software that runs on your computer

**What it does:**
- Tracks changes to files
- Creates snapshots (commits)
- Manages branches
- Works offline

**Example:**
```bash
git init           # Create new repository
git add .          # Stage changes
git commit -m ""   # Save snapshot
git log            # View history
```

### GitHub (The Service)

**What it is:** A website that hosts Git repositories

**What it does:**
- Stores your code online
- Enables collaboration
- Provides Pull Request workflow
- Offers issue tracking, wikis, actions

**Example:**
```bash
git push origin main    # Upload to GitHub
git pull origin main    # Download from GitHub
```

### The Relationship

```
Your Computer (Git)  ←→  GitHub (Remote)
     ↓                      ↓
  Local repo           Online copy
  Private edits        Team access
  Work offline         Backup & share
```

---

## Essential Git Concepts

### The Three States

Files in Git exist in three states:

**1. Working Directory**
- Files you're currently editing
- Changes not yet staged

**2. Staging Area (Index)**
- Changes marked for commit
- Preview of next commit

**3. Repository**
- Committed snapshots
- Project history

**Workflow:**
```
Edit files → Stage changes → Commit snapshot
    ↓             ↓               ↓
Working Dir   Staging Area    Repository
```

**Commands:**
```bash
# Edit file
echo "Hello" > file.txt

# Stage it
git add file.txt

# Commit it
git commit -m "Add greeting"
```

### HEAD, Branches, and Commits

**HEAD:**
- Pointer to current commit
- Usually points to branch tip
- Moving HEAD = changing what you see

**Branch:**
- Named pointer to a commit
- Moves forward with new commits
- Lightweight (just a 41-byte file!)

**Commit:**
- Snapshot of all files
- Contains metadata (author, date, message)
- Has unique SHA hash
- Points to parent commit(s)

**Visualization:**
```
main → C3 ← HEAD
       ↓
       C2
       ↓
       C1
```

After new commit:
```
main → C4 ← HEAD
       ↓
       C3
       ↓
       C2
       ↓
       C1
```

---

## Common Workflows

### Workflow 1: Feature Branch

**Best for:** Adding new features without breaking main

**Steps:**

```bash
# 1. Update main
git checkout main
git pull origin main

# 2. Create feature branch
git checkout -b feature/add-singing-dunes

# 3. Work on feature
# ... edit files ...
git add scenes/singing_dunes.txt
git commit -m "Add Singing Dunes expedition scene"

# 4. Push branch
git push origin feature/add-singing-dunes

# 5. Create PR on GitHub
# 6. After PR merged, delete branch
git checkout main
git pull origin main
git branch -d feature/add-singing-dunes
```

**Why this works:**
- Main branch stays stable
- Easy to review before merging
- Can work on multiple features simultaneously
- Easy to abandon if feature doesn't work out

### Workflow 2: Fork and Pull Request

**Best for:** Contributing to others' projects

**Steps:**

```bash
# 1. Fork on GitHub (one time)
# Click "Fork" button

# 2. Clone your fork
git clone https://github.com/yourusername/Aethromoor.git
cd Aethromoor

# 3. Add upstream remote
git remote add upstream https://github.com/issdandavis/Aethromoor.git

# 4. Create feature branch
git checkout -b fix-typo-readme

# 5. Make changes
# ... edit README.md ...
git add README.md
git commit -m "Fix typo in installation instructions"

# 6. Push to YOUR fork
git push origin fix-typo-readme

# 7. Create PR on GitHub
# Go to your fork → "Compare & pull request"

# 8. Keep fork updated
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

**Why this works:**
- You don't need write access to original repo
- Original repo stays clean
- Your fork = your playground
- Easy for maintainers to review

### Workflow 3: Hotfix

**Best for:** Urgent fixes to production code

**Steps:**

```bash
# 1. Create hotfix branch from main
git checkout main
git pull origin main
git checkout -b hotfix/fix-critical-bug

# 2. Fix the bug
# ... edit file ...
git add fixed_file.js
git commit -m "Fix critical stat tracking bug"

# 3. Push and create PR
git push origin hotfix/fix-critical-bug
# Create PR targeting main

# 4. After merge, update all other branches
git checkout feature/my-feature
git merge main  # Get the fix
```

**Why this works:**
- Fast response to critical issues
- Clear labeling of urgent fixes
- Easy to track in history

### Workflow 4: Rebase for Clean History

**Best for:** Keeping feature branch up to date

**Steps:**

```bash
# You're on feature branch
git checkout feature/new-scene

# Main has new commits
git fetch origin

# Rebase instead of merge
git rebase origin/main

# If conflicts, resolve them
# ... fix conflicts ...
git add conflicted_file.txt
git rebase --continue

# Force push (only to YOUR branches!)
git push origin feature/new-scene --force-with-lease
```

**Why use rebase:**
- Creates linear history
- Avoids messy merge commits
- Easier to understand git log

**⚠️ Warning:**
- Never rebase public branches (main, develop)
- Only rebase YOUR feature branches
- Requires force push

---

## Branching Strategies

### Git Flow

**Branches:**
- `main` - Production code
- `develop` - Integration branch
- `feature/*` - New features
- `release/*` - Release preparation
- `hotfix/*` - Emergency fixes

**Example:**
```
main ──────M──────────M────
            ↑           ↑
develop ──F─┴─F─F─R────┘
          ↓   ↓   ↓
feature  F1  F2  F3
```

**When to use:**
- Large projects
- Scheduled releases
- Multiple versions in production

### GitHub Flow

**Branches:**
- `main` - Always deployable
- `feature/*` - Everything else

**Process:**
1. Create branch from main
2. Add commits
3. Open PR
4. Discuss and review
5. Deploy for testing
6. Merge to main

**When to use:**
- Continuous deployment
- Smaller teams
- Web applications

### Trunk-Based Development

**Branches:**
- `main` - Everyone works here
- Short-lived feature branches (< 1 day)

**Process:**
1. Small changes
2. Frequent integration
3. Feature flags for incomplete work

**When to use:**
- High-maturity teams
- Excellent test coverage
- Automated deployment

### This Repository's Strategy

We use **Modified GitHub Flow:**

**Branches:**
- `main` - Stable game version
- `feature/*` - New content/features
- `ai-*` - AI worker branches (automated)
- `claude/*` - AI assistant sessions

**Rules:**
- All changes via PR
- Main must always be playable
- AI branches auto-merge if tests pass
- Human branches need review

---

## Advanced Commands

### Stashing Changes

**Problem:** Need to switch branches but have uncommitted work

**Solution:** Stash it!

```bash
# Save current work
git stash save "WIP: working on dialogue"

# Do other work
git checkout main
# ... do stuff ...

# Return to original branch
git checkout feature/dialogue

# Restore stashed work
git stash pop

# See all stashes
git stash list

# Apply specific stash
git stash apply stash@{1}

# Delete stash
git stash drop stash@{0}

# Clear all stashes
git stash clear
```

### Cherry-Picking Commits

**Problem:** Want specific commit from another branch

**Solution:** Cherry-pick it!

```bash
# On target branch
git checkout main

# Pick commit from other branch
git cherry-pick a1b2c3d

# Cherry-pick multiple commits
git cherry-pick a1b2c3d e4f5g6h

# Cherry-pick without committing
git cherry-pick --no-commit a1b2c3d
```

### Interactive Rebase

**Problem:** Want to clean up commit history

**Solution:** Interactive rebase!

```bash
# Rebase last 5 commits
git rebase -i HEAD~5

# Editor opens with:
# pick a1b2c3d Add scene
# pick e4f5g6h Fix typo
# pick i7j8k9l Fix another typo
# pick m1n2o3p Add dialogue
# pick q4r5s6t Fix spacing

# Change to:
# pick a1b2c3d Add scene
# squash e4f5g6h Fix typo
# squash i7j8k9l Fix another typo
# pick m1n2o3p Add dialogue
# fixup q4r5s6t Fix spacing

# Commands:
# pick = use commit
# squash = merge with previous, edit message
# fixup = merge with previous, discard message
# reword = change commit message
# edit = pause to amend commit
# drop = remove commit
```

### Bisect for Bug Hunting

**Problem:** Bug appeared but don't know which commit caused it

**Solution:** Binary search!

```bash
# Start bisect
git bisect start

# Mark current as bad
git bisect bad

# Mark known good commit
git bisect good abc123

# Git checks out middle commit
# Test if bug exists

# If bug present
git bisect bad

# If bug absent
git bisect good

# Repeat until Git finds the culprit commit
# When done
git bisect reset
```

### Reflog for Recovery

**Problem:** Accidentally deleted commits

**Solution:** Reflog to the rescue!

```bash
# See all HEAD movements
git reflog

# Output:
# a1b2c3d HEAD@{0}: reset: moving to HEAD~3
# e4f5g6h HEAD@{1}: commit: Add feature
# i7j8k9l HEAD@{2}: commit: Fix bug

# Recover lost commit
git checkout e4f5g6h

# Or create branch at that point
git branch recovery-branch e4f5g6h
```

### Submodules

**Problem:** Need to include another repository

**Solution:** Submodules!

```bash
# Add submodule
git submodule add https://github.com/user/repo.git path/to/submodule

# Clone repo with submodules
git clone --recursive https://github.com/user/repo.git

# Update submodules
git submodule update --remote

# Remove submodule
git submodule deinit path/to/submodule
git rm path/to/submodule
```

---

## Collaboration Patterns

### Code Review Best Practices

**Creating a PR:**

✅ **Do:**
```markdown
## Changes
- Added Singing Dunes expedition scene
- Implemented truth-testing mechanic
- Added 3 possible outcomes

## Testing
- Tested all choice paths
- Verified stat changes
- Checked dialogue consistency

## Screenshots
[Include if UI changes]

## Related Issues
Closes #42
```

❌ **Don't:**
```
Made some changes
```

**Reviewing a PR:**

```bash
# Checkout PR locally
git fetch origin pull/123/head:pr-123
git checkout pr-123

# Test it
# ... run game, check changes ...

# Leave review on GitHub
```

**Review comments:**

✅ **Constructive:**
> "This dialogue is great! Consider adding Polly's reaction here for consistency with her character in other scenes."

❌ **Not helpful:**
> "This is bad."

### Pair Programming with Git

**Pattern 1: Shared Branch**

```bash
# Person A creates branch
git checkout -b feature/shared-work
git push origin feature/shared-work

# Person B fetches
git fetch origin
git checkout feature/shared-work

# Both work on it
# Person A
git add .
git commit -m "Add part 1"
git push origin feature/shared-work

# Person B pulls then adds
git pull origin feature/shared-work
# ... edit ...
git add .
git commit -m "Add part 2"
git push origin feature/shared-work
```

**Pattern 2: Co-authored Commits**

```bash
git commit -m "Implement feature

Co-authored-by: Name <email@example.com>"
```

Shows both authors in GitHub!

### Release Management

**Semantic Versioning:**
```
v1.2.3
│ │ │
│ │ └─ Patch (bug fixes)
│ └─── Minor (new features, backwards compatible)
└───── Major (breaking changes)
```

**Creating a release:**

```bash
# Tag the release
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push tag
git push origin v1.0.0

# Create release on GitHub
# Go to Releases → Draft new release
```

---

## Troubleshooting

### Problem: Merge Conflict

**Scenario:**
```bash
git merge feature-branch
# CONFLICT (content): Merge conflict in game.js
```

**Solution:**

```bash
# 1. Open conflicted file
# Look for:
<<<<<<< HEAD
Your version
=======
Their version
>>>>>>> feature-branch

# 2. Choose resolution
# Either keep yours, theirs, or combine

# 3. Remove markers
# Final version should have no <<<, ===, >>>

# 4. Stage resolution
git add game.js

# 5. Complete merge
git commit -m "Resolve merge conflict in game.js"
```

**Tools:**
```bash
# Use merge tool
git mergetool

# Accept all theirs
git checkout --theirs game.js
git add game.js

# Accept all yours
git checkout --ours game.js
git add game.js

# Abort merge
git merge --abort
```

### Problem: Detached HEAD

**Scenario:**
```bash
git checkout a1b2c3d
# You are in 'detached HEAD' state
```

**What happened:** You checked out a commit instead of a branch

**Solution:**

```bash
# If you made changes you want to keep
git branch new-branch-name
git checkout new-branch-name

# If you want to discard changes
git checkout main
```

### Problem: Pushed Wrong Commit

**Scenario:** Pushed sensitive data or wrong code to remote

**Solution depends on situation:**

**If you're the only one using the branch:**
```bash
# Reset to previous commit
git reset --hard HEAD~1

# Force push
git push origin branch-name --force
```

**If others are using it:**
```bash
# Revert the commit (creates new commit that undoes it)
git revert HEAD

# Push normally
git push origin branch-name
```

**If sensitive data:**
1. Revert/reset as above
2. **Rotate all exposed credentials immediately**
3. Use tools like BFG Repo-Cleaner for thorough cleanup
4. Contact GitHub support if needed

### Problem: Lost Commits

**Scenario:** Accidentally reset and lost work

**Solution:**

```bash
# Find lost commit
git reflog

# Look for your lost commit
# e4f5g6h HEAD@{4}: commit: My lost work

# Recover it
git cherry-pick e4f5g6h

# Or reset to it
git reset --hard e4f5g6h
```

### Problem: Can't Pull

**Scenario:**
```bash
git pull
# error: Your local changes would be overwritten
```

**Solutions:**

**Option 1: Stash**
```bash
git stash
git pull
git stash pop
```

**Option 2: Commit**
```bash
git add .
git commit -m "WIP"
git pull
```

**Option 3: Discard**
```bash
git reset --hard
git pull
```

---

## Best Practices

### Commit Messages

**Format:**
```
Short summary (50 chars or less)

More detailed explanation if needed. Wrap at 72 chars.
Explain what and why, not how.

- Bullet points are okay
- Use present tense: "Add feature" not "Added feature"

Closes #123
```

**Examples:**

✅ **Good:**
```
Add truth-testing mechanic to Singing Dunes

Implements the three-stage truth revelation system where
players must demonstrate understanding of desert wisdom.
Adds stat checks and three possible outcomes based on
collaboration score.

Closes #42
```

✅ **Good (simple):**
```
Fix typo in README.md
```

❌ **Bad:**
```
stuff
```

❌ **Bad:**
```
Fixed the thing that was broken in the file
```

### Branch Naming

**Convention:**
```
type/description-in-kebab-case
```

**Types:**
- `feature/` - New functionality
- `fix/` - Bug fix
- `hotfix/` - Urgent production fix
- `docs/` - Documentation
- `refactor/` - Code restructuring
- `test/` - Adding tests
- `chore/` - Maintenance

**Examples:**
- `feature/add-glacier-expedition`
- `fix/stat-tracking-bug`
- `docs/improve-installation-guide`
- `refactor/simplify-choice-logic`

### File Organization

```bash
# .gitignore - Files Git should ignore
node_modules/
.env
*.log
.DS_Store
dist/

# Keep it updated
# Commit .gitignore
git add .gitignore
git commit -m "Update .gitignore"
```

### Commit Frequency

**Guidelines:**
- Commit when a unit of work is complete
- Commit before switching tasks
- Commit at end of day
- Don't commit broken code to shared branches

**Anti-patterns:**
- ❌ One commit for entire feature
- ❌ Committing every keystroke
- ❌ Huge commits mixing multiple changes

**Good pattern:**
```
✅ "Add Singing Dunes scene structure"
✅ "Implement truth-testing logic"
✅ "Add dialogue for desert wisdom"
✅ "Add outcomes and stat changes"
✅ "Test and refine Singing Dunes scene"
```

### Security

**Never commit:**
- Passwords
- API keys
- Private keys
- Personal data
- Compiled binaries (usually)

**Use:**
- `.env` files (gitignored)
- GitHub Secrets
- Environment variables
- Config templates (.env.example)

**If you accidentally commit secrets:**
1. Remove from code
2. Commit removal
3. **Immediately rotate the credentials**
4. Consider using BFG Repo-Cleaner
5. Force push (if safe)

---

## Git Aliases

**Make life easier:**

```bash
# Add to ~/.gitconfig
[alias]
    co = checkout
    br = branch
    ci = commit
    st = status
    unstage = reset HEAD --
    last = log -1 HEAD
    visual = log --graph --oneline --all
    amend = commit --amend --no-edit
```

**Usage:**
```bash
git co main        # instead of git checkout main
git br             # instead of git branch
git visual         # pretty branch visualization
```

---

## Useful Git Configurations

```bash
# Your identity
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Default editor
git config --global core.editor "vim"
git config --global core.editor "code --wait"  # VS Code

# Default branch name
git config --global init.defaultBranch main

# Color output
git config --global color.ui auto

# Credential caching (15 min)
git config --global credential.helper cache

# Credential caching (1 hour)
git config --global credential.helper 'cache --timeout=3600'

# Line ending handling
git config --global core.autocrlf true    # Windows
git config --global core.autocrlf input   # Mac/Linux

# See all config
git config --list
```

---

## Quick Reference

### Daily Commands

```bash
# Status and diffs
git status
git diff
git diff --staged
git log --oneline

# Branching
git checkout -b new-branch
git checkout existing-branch
git branch -d merged-branch

# Staging and committing
git add file.txt
git add .
git commit -m "message"
git commit -am "message"  # add and commit

# Syncing
git fetch
git pull
git push
git push origin branch-name

# Undoing
git checkout -- file.txt  # discard working changes
git reset HEAD file.txt   # unstage
git reset --soft HEAD~1   # undo commit, keep changes
git reset --hard HEAD~1   # undo commit, discard changes
```

### Emergency Commands

```bash
# Made mistake, need to undo
git reflog              # find what to recover
git reset --hard abc123 # go back to commit

# Need to switch branches but have changes
git stash
git checkout other-branch
git checkout original-branch
git stash pop

# Conflict resolution
git merge --abort
git rebase --abort

# Remove untracked files
git clean -n   # preview
git clean -fd  # actually remove
```

---

## Next Steps

### Now You Can:

- ✅ Use Git efficiently
- ✅ Understand branching strategies
- ✅ Resolve conflicts
- ✅ Collaborate effectively
- ✅ Recover from mistakes

### Continue Learning:

1. **Practice:** Work on real projects
2. **Explore:** Try advanced features (rebase, bisect)
3. **Read:** Pro Git book (free online)
4. **Contribute:** Join open source projects
5. **Teach:** Help others learn Git

### Recommended Resources:

- [Pro Git Book](https://git-scm.com/book) - Comprehensive guide
- [Git Flight Rules](https://github.com/k88hudson/git-flight-rules) - Problem-solution guide
- [Oh Shit, Git!](https://ohshitgit.com/) - How to undo mistakes
- [Learn Git Branching](https://learngitbranching.js.org/) - Interactive tutorial

---

## For This Repository

**Workflow Summary:**

```bash
# 1. Fork and clone (first time)
git clone https://github.com/yourusername/Aethromoor.git
cd Aethromoor
git remote add upstream https://github.com/issdandavis/Aethromoor.git

# 2. Start new feature
git checkout main
git pull upstream main
git checkout -b feature/my-contribution

# 3. Work and commit
# ... edit files ...
git add .
git commit -m "Descriptive message"

# 4. Keep updated
git fetch upstream
git rebase upstream/main

# 5. Push and PR
git push origin feature/my-contribution
# Create PR on GitHub

# 6. After merge
git checkout main
git pull upstream main
git branch -d feature/my-contribution
```

---

**Questions?** Open an issue with "question" label!

**Ready to contribute?** See [CONTRIBUTING.md](../CONTRIBUTING.md)

**Need GitHub basics?** Start with [GITHUB_TUTORIAL.md](GITHUB_TUTORIAL.md)

---

*"Git gets easier once you understand the concepts. Keep practicing!"* 🚀
