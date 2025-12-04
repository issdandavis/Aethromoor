# 🎓 GitHub Tutorial for Complete Beginners

**Time:** 20-30 minutes  
**Prerequisites:** None - start from zero!  
**Goal:** Learn GitHub basics and contribute to this project

---

## Table of Contents

1. [What is GitHub?](#what-is-github)
2. [Setting Up](#setting-up)
3. [Understanding Key Concepts](#understanding-key-concepts)
4. [Your First Actions](#your-first-actions)
5. [Working with This Repository](#working-with-this-repository)
6. [Common Tasks](#common-tasks)
7. [Troubleshooting](#troubleshooting)
8. [Next Steps](#next-steps)

---

## What is GitHub?

### Simple Explanation

Think of GitHub as **Google Docs for code**:
- Multiple people can work on the same project
- You can see who changed what and when
- You can undo changes if needed
- You can suggest changes without breaking the main version

### Real-World Analogy

Imagine you're writing a book with friends:
- **Repository** = The book folder with all chapters
- **Commit** = Saving your changes with a note about what you wrote
- **Branch** = A copy where you can try new ideas without messing up the main book
- **Pull Request** = "Hey team, I finished my chapter, ready to add it to the book?"
- **Merge** = Adding approved changes to the main book

---

## Setting Up

### Step 1: Create a GitHub Account

1. Go to [github.com](https://github.com)
2. Click "Sign Up"
3. Choose a username (make it professional - people will see it!)
4. Verify your email
5. Choose the free plan

**Done!** ✅

### Step 2: Install Git (Optional but Recommended)

**Windows:**
1. Download from [git-scm.com](https://git-scm.com)
2. Run installer (keep default settings)
3. Open "Git Bash" to test

**Mac:**
1. Open Terminal (Cmd+Space, type "terminal")
2. Type: `git --version`
3. If not installed, follow prompts to install

**Linux:**
```bash
sudo apt-get install git  # Ubuntu/Debian
sudo yum install git      # Fedora/RedHat
```

**Verify installation:**
```bash
git --version
# Should show: git version 2.x.x
```

### Step 3: Configure Git

Tell Git who you are:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Check it worked:**
```bash
git config --list
```

---

## Understanding Key Concepts

### Repositories (Repos)

A **repository** is a project folder that Git tracks.

**Example:** This Avalon game is a repository containing:
- Game code
- Documentation
- Lore files
- Configuration

### Commits

A **commit** is a saved snapshot of your changes.

**Example:**
```
Commit: "Add singing dunes scene"
- Added new file: singing_dunes.txt
- Changed: 347 lines
- When: Nov 25, 2025 3:42 PM
- Who: YourUsername
```

### Branches

A **branch** is a parallel version of your project.

**Analogy:** Like having multiple drafts of an essay:
- `main` = The official published version
- `draft-ideas` = Your experimental version
- `proofreading` = Version being reviewed

**Why use branches?**
- Work on features without breaking the main version
- Multiple people can work simultaneously
- Easy to discard failed experiments

### Pull Requests (PRs)

A **Pull Request** is a proposal to merge your changes.

**The Process:**
1. You work on a branch
2. You create a PR: "Hey, I finished this feature!"
3. Team reviews your code
4. If approved → Merge into main
5. If needs work → You make changes

### Issues

**Issues** are like to-do items or bug reports.

**Examples:**
- "Bug: Stats not tracking correctly"
- "Feature request: Add save game function"
- "Question: How do I run the game?"

---

## Your First Actions

### Action 1: Star This Repository

**Why?** It bookmarks the project and shows appreciation.

**How:**
1. Go to this repository on GitHub
2. Click the ⭐ Star button (top-right)

**Done!** ✅

### Action 2: Watch the Repository

**Why?** Get notified about changes and discussions.

**How:**
1. Click the 👁️ Watch button
2. Choose "All Activity" or "Participating and @mentions"

### Action 3: Read Existing Issues

**Why?** Learn what people are working on.

**How:**
1. Click the "Issues" tab
2. Read a few open issues
3. Notice the labels (bug, enhancement, help wanted)

### Action 4: Create Your First Issue

**Why?** Practice participating in the project.

**What to create:** A simple question or introduction

**How:**
1. Click "Issues" → "New Issue"
2. Title: "New contributor introduction"
3. Body:
```markdown
Hi! I'm learning GitHub and would like to contribute.

**Background:** [Your background]
**Interests:** [What interests you about this project]
**Skills:** [What you're good at or want to learn]

Looking forward to helping out!
```
4. Click "Submit new issue"

**Congratulations!** You just made your first GitHub contribution! 🎉

---

## Working with This Repository

### Option A: Using GitHub.com (No Git Required)

**Best for:** Small text changes, documentation

**Steps:**
1. Navigate to the file you want to edit
2. Click the pencil ✏️ icon
3. Make your changes
4. Scroll down to "Propose changes"
5. Write a description
6. Click "Propose changes"
7. Click "Create pull request"

**Example Task:** Fix a typo in README.md

### Option B: Using Git Locally (Recommended for Larger Work)

**Best for:** Adding features, multiple file changes

#### First Time Setup

**1. Fork the repository** (Your own copy)
- Click "Fork" button (top-right)
- This creates: `yourusername/Aethromoor`

**2. Clone to your computer**
```bash
cd ~/Documents  # or wherever you want the folder
git clone https://github.com/yourusername/Aethromoor.git
cd Aethromoor
```

**3. Set up the connection to the original repo**
```bash
git remote add upstream https://github.com/issdandavis/Aethromoor.git
git remote -v  # Verify it worked
```

You should see:
```
origin    https://github.com/yourusername/Aethromoor.git (fetch)
origin    https://github.com/yourusername/Aethromoor.git (push)
upstream  https://github.com/issdandavis/Aethromoor.git (fetch)
upstream  https://github.com/issdandavis/Aethromoor.git (push)
```

#### Making Changes

**1. Create a branch**
```bash
git checkout -b my-feature-name
```

**2. Make your changes**
- Edit files in your favorite editor
- Add new files
- Test your changes

**3. Check what you changed**
```bash
git status          # See changed files
git diff            # See exact changes
```

**4. Stage your changes**
```bash
git add .                    # Add all changes
# OR
git add specific_file.txt    # Add specific file
```

**5. Commit your changes**
```bash
git commit -m "Add description of what you did"
```

**Good commit messages:**
- ✅ "Add GitHub tutorial for beginners"
- ✅ "Fix typo in README.md"
- ✅ "Update Polly's dialogue in dunes scene"

**Bad commit messages:**
- ❌ "stuff"
- ❌ "changes"
- ❌ "asdf"

**6. Push to YOUR fork**
```bash
git push origin my-feature-name
```

**7. Create a Pull Request**
- Go to your fork on GitHub
- Click "Compare & pull request"
- Add description of your changes
- Click "Create pull request"

**8. Wait for review**
- Project maintainer will review
- They might request changes
- Once approved, they'll merge it!

---

## Common Tasks

### Keeping Your Fork Up to Date

The original repo gets updated. Stay in sync:

```bash
# Get latest changes from original repo
git fetch upstream

# Switch to your main branch
git checkout main

# Merge in the updates
git merge upstream/main

# Push updates to YOUR fork
git push origin main
```

**Do this:** Weekly or before starting new work

### Fixing Mistakes

**Mistake:** Committed to the wrong branch

```bash
git log --oneline -1       # Copy the commit hash
git checkout correct-branch
git cherry-pick <hash>     # Apply commit to correct branch
```

**Mistake:** Need to undo last commit

```bash
git reset --soft HEAD~1    # Undo commit, keep changes
# OR
git reset --hard HEAD~1    # Undo commit, discard changes
```

**Mistake:** Want to discard all local changes

```bash
git checkout .             # Discard unstaged changes
git clean -fd              # Remove new files
```

### Viewing History

```bash
git log                    # Full history
git log --oneline          # Compact history
git log --graph --all      # Visual branch history
git show <commit-hash>     # See specific commit details
```

### Working with Branches

```bash
# List all branches
git branch -a

# Switch to existing branch
git checkout branch-name

# Create and switch to new branch
git checkout -b new-branch

# Delete a branch
git branch -d branch-name

# See current branch
git branch
```

---

## Troubleshooting

### "I'm lost! What branch am I on?"

```bash
git status
```

Look at the first line: `On branch branch-name`

### "Help! I have merge conflicts!"

**What happened:** Two people changed the same lines

**Fix:**
1. Open the conflicted file
2. Look for markers:
```
<<<<<<< HEAD
Your version
=======
Their version
>>>>>>> branch-name
```
3. Choose which version to keep (or combine them)
4. Remove the markers
5. Save the file
6. `git add <file>`
7. `git commit -m "Resolve merge conflict"`

### "I can't push my changes"

**Error:** `! [rejected] main -> main (fetch first)`

**Fix:** Pull latest changes first:
```bash
git pull origin main
# Resolve any conflicts
git push origin main
```

### "I accidentally committed sensitive data"

**Fix:**
1. Remove the sensitive data from files
2. Commit the removal
3. Contact repository owner to purge history
4. **ROTATE ANY EXPOSED CREDENTIALS IMMEDIATELY**

### "Git says 'Permission denied'"

**Fix:** Set up SSH keys or use HTTPS with credentials

**SSH Setup:**
```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
cat ~/.ssh/id_ed25519.pub  # Copy this
# Add to GitHub: Settings → SSH Keys → New SSH Key
```

---

## Repository-Specific Tips

### This Avalon Repository

**Structure:**
```
Aethromoor/
├── game/              # HTML game (edit these!)
├── choicescript_game/ # ChoiceScript version
├── docs/              # Documentation (start here!)
├── lore/              # Story content
└── writing_drafts/    # Novel manuscripts
```

**Good first contributions:**
- Fix typos in documentation
- Test the game and report bugs
- Improve tutorial clarity
- Add examples to guides

**Before making changes:**
1. Read `CONTRIBUTING.md`
2. Check `docs/PROJECT_ROADMAP.md`
3. Look at existing issues
4. Ask if unsure!

### Working with AI Workflows

This repository has **AI workers** that:
- Write scenes automatically
- Polish content
- Balance game stats
- Find bugs

**Important:**
- Don't edit files in `ai-*` branches directly
- Review AI-created PRs carefully
- Report AI mistakes as issues

See `AGENT_TUTORIAL.md` for details.

---

## Practice Exercises

### Exercise 1: Make a Fork (5 min)

1. Fork this repository
2. Clone it to your computer
3. Create a new branch called `practice-branch`
4. Create a file: `my-first-contribution.txt`
5. Add your name to the file
6. Commit and push
7. Create a PR (then close it - it's just practice!)

### Exercise 2: Explore History (5 min)

```bash
git log --oneline -10          # See last 10 commits
git show HEAD                  # See latest commit details
git log --author="username"    # See someone's commits
git blame README.md            # See who wrote each line
```

### Exercise 3: Branch Practice (5 min)

```bash
git checkout -b test-branch-1
# Make a change
git add .
git commit -m "Test commit 1"

git checkout -b test-branch-2
# Make another change
git add .
git commit -m "Test commit 2"

git checkout main
git branch -D test-branch-1
git branch -D test-branch-2
```

---

## GitHub Web Features

### Keyboard Shortcuts

Press `?` on GitHub.com to see all shortcuts!

**Useful ones:**
- `s` or `/` - Focus search bar
- `g` + `c` - Go to Code tab
- `g` + `i` - Go to Issues
- `g` + `p` - Go to Pull Requests
- `t` - File finder
- `.` - Open GitHub.dev editor

### Markdown in Comments

GitHub supports rich formatting:

```markdown
# Heading
## Subheading

**bold** *italic* ~~strikethrough~~

- Bullet list
1. Numbered list

[Link text](https://url.com)

`code inline`

```code block```

> Quote

@username mention
#123 link to issue/PR
```

### Using Labels

**Issues and PRs can have labels:**
- `bug` - Something's broken
- `enhancement` - New feature request
- `documentation` - Docs improvements
- `good first issue` - Good for beginners
- `help wanted` - Looking for contributors

**Filter by label:** Click label names in Issues tab

### Using Projects

**GitHub Projects** = Kanban board for tasks

**Columns typically:**
- To Do
- In Progress
- Review
- Done

**Usage:** Drag issues between columns

---

## GitHub Best Practices

### Communication

✅ **Do:**
- Be respectful and constructive
- Ask questions if unclear
- Provide context in issues
- Thank reviewers
- Use emoji moderately 😊

❌ **Don't:**
- Be rude or dismissive
- Demand immediate responses
- Post low-effort "bump" comments
- Spam mentions

### Code Reviews

**When reviewing:**
- Focus on code, not person
- Suggest improvements, don't demand
- Explain *why* something should change
- Approve when ready

**When being reviewed:**
- Don't take it personally
- Ask for clarification
- Make requested changes
- Thank the reviewer

### Commit Hygiene

**Good practices:**
- Commit related changes together
- Write descriptive messages
- Commit often (small chunks)
- Don't commit secrets or credentials
- Test before committing

---

## Resources

### Official Documentation

- [GitHub Docs](https://docs.github.com)
- [Git Book](https://git-scm.com/book)
- [GitHub Skills](https://skills.github.com) - Interactive tutorials

### This Repository

- `CONTRIBUTING.md` - How to contribute
- `docs/PROJECT_ROADMAP.md` - Project status
- `AGENT_TUTORIAL.md` - AI system guide
- `START_HERE.md` - Quick start

### Cheat Sheets

**Git Commands:**
```bash
# Status and info
git status              # Current status
git log                 # Commit history
git diff                # Changes made

# Branching
git branch              # List branches
git checkout -b name    # Create and switch
git merge branch        # Merge branch

# Staging and committing
git add file            # Stage file
git commit -m "msg"     # Commit
git push origin branch  # Push to GitHub

# Updating
git fetch               # Get updates
git pull                # Fetch and merge
git pull --rebase       # Fetch and rebase

# Undoing
git reset --soft HEAD~1 # Undo commit, keep changes
git checkout -- file    # Discard changes
git clean -fd           # Remove new files
```

---

## Next Steps

### Now You Can:

- ✅ Understand what GitHub is
- ✅ Navigate repositories
- ✅ Create issues
- ✅ Fork and clone
- ✅ Make commits
- ✅ Create pull requests
- ✅ Collaborate with others

### Continue Learning:

1. **Practice:** Make small contributions to this project
2. **Explore:** Look at other open-source projects
3. **Read:** `docs/GIT_BASICS.md` for advanced Git workflows
4. **Join:** GitHub community discussions
5. **Build:** Start your own repository!

### Suggested Path for This Project:

**Week 1:**
- Star and watch the repository
- Read all documentation
- Play the game
- Create introduction issue

**Week 2:**
- Fork and clone
- Find a typo or small bug
- Create your first PR
- Engage in discussions

**Week 3:**
- Take on a "good first issue"
- Review others' PRs
- Ask for code review feedback

**Week 4:**
- Contribute a feature
- Help other newcomers
- Become a regular contributor!

---

## FAQ

**Q: Do I need to know how to code?**  
A: No! You can contribute to documentation, testing, and issue discussions.

**Q: What if I break something?**  
A: Git tracks everything. Nothing is permanent. We can always undo.

**Q: How long until my PR is reviewed?**  
A: Varies by project. Days to weeks is normal. Be patient!

**Q: Can I contribute to multiple things at once?**  
A: Yes! Use different branches for different features.

**Q: What if my PR is rejected?**  
A: It happens! Learn from feedback and try again.

**Q: Is it okay to ask "dumb questions"?**  
A: Absolutely! Everyone was a beginner once.

**Q: How do I find issues to work on?**  
A: Look for "good first issue" or "help wanted" labels.

---

## Conclusion

**Congratulations!** You now know GitHub basics! 🎉

Remember:
- **Start small** - Simple contributions build confidence
- **Ask questions** - The community wants to help
- **Learn by doing** - Make mistakes and learn from them
- **Be patient** - Skills develop over time

**Your First Task:**
Create an issue introducing yourself to the project!

---

**Ready for more advanced Git?**  
→ Next: [GIT_BASICS.md](GIT_BASICS.md)

**Want to understand the AI system?**  
→ See: [AGENT_TUTORIAL.md](../AGENT_TUTORIAL.md)

**Ready to contribute?**  
→ Read: [CONTRIBUTING.md](../CONTRIBUTING.md)

---

*"Every expert was once a beginner. Start your journey today!"* 🚀

**Questions?** Open an issue with the label "question"!
