# Quick Reference: Git Push vs Pull

## 🔄 The Simple Rule

```
PULL = Download ⬇️  (Get changes FROM GitHub)
PUSH = Upload   ⬆️  (Send changes TO GitHub)
```

---

## 📥 Git Pull - Downloading Changes

### What It Does
Gets the latest changes from GitHub and puts them on your computer

### When to Use
- ✅ Before you start working each day
- ✅ When someone (or AI) made changes on GitHub
- ✅ When you see "branch is behind" message
- ✅ To sync your local copy with GitHub

### How to Use
```bash
# Pull from main branch
git pull origin main

# Pull from current branch
git pull

# Pull and see what changed
git pull -v
```

### Visual Example
```
        GitHub (Remote)          Your Computer (Local)
        ┌──────────┐                ┌──────────┐
        │ File A   │                │ File A   │
        │ File B   │     PULL       │ (old)    │
        │ File C   │  ◄────────     │          │
        │ (new)    │                │          │
        └──────────┘                └──────────┘

                    After Pull ⬇️
        ┌──────────┐                ┌──────────┐
        │ File A   │                │ File A   │
        │ File B   │                │ File B   │
        │ File C   │                │ File C   │
        └──────────┘                └──────────┘
                                    (Now synced!)
```

---

## 📤 Git Push - Uploading Changes

### What It Does
Sends your local changes TO GitHub so others can see them

### When to Use
- ✅ After you commit changes
- ✅ To create/update a pull request
- ✅ To backup your work to GitHub
- ✅ When you want to share your work

### How to Use
```bash
# Push to specific branch
git push origin branch-name

# Push to current branch
git push

# Push and create new branch on GitHub
git push -u origin new-branch-name
```

### Visual Example
```
        Your Computer (Local)        GitHub (Remote)
        ┌──────────┐                ┌──────────┐
        │ File A   │                │ File A   │
        │ File B   │     PUSH       │ File B   │
        │ File C   │  ──────────►   │ (old)    │
        │ (new!)   │                │          │
        └──────────┘                └──────────┘

                    After Push ⬆️
        ┌──────────┐                ┌──────────┐
        │ File A   │                │ File A   │
        │ File B   │                │ File B   │
        │ File C   │                │ File C   │
        └──────────┘                └──────────┘
                                    (Now synced!)
```

---

## 🔁 Complete Workflow

Here's the typical sequence you'll use daily:

```bash
# 1️⃣ PULL first (get latest changes)
git pull origin main

# 2️⃣ Make changes to your files
# (edit files in VS Code, editor, etc.)

# 3️⃣ Check what you changed
git status

# 4️⃣ Stage your changes
git add .
# or add specific files:
git add filename.txt

# 5️⃣ Commit your changes
git commit -m "Describe what you changed"

# 6️⃣ PUSH to GitHub
git push origin your-branch-name
```

---

## 🎯 Common Scenarios

### Scenario 1: Starting Your Workday
```bash
cd /home/runner/work/Aethromoor/Aethromoor
git pull origin main  # Get latest changes
# Now you're ready to work!
```

### Scenario 2: Saving Your Work
```bash
git add .
git commit -m "Added new expedition scene"
git push origin your-branch  # Upload to GitHub
```

### Scenario 3: You See "Branch is Behind"
```bash
git pull  # Download newer changes
# If there are conflicts, resolve them
git push  # Upload after resolving
```

### Scenario 4: Creating a Pull Request
```bash
# 1. Make sure you're on your branch
git checkout -b feature/my-new-feature

# 2. Make changes and commit
git add .
git commit -m "Add my feature"

# 3. Push to create PR
git push -u origin feature/my-new-feature

# 4. Go to GitHub.com and create PR
```

---

## ⚠️ Common Mistakes & Fixes

### Mistake 1: Forgot to Pull First
**Problem:** You made changes without pulling latest

**Fix:**
```bash
git stash              # Save your changes temporarily
git pull               # Get latest from GitHub
git stash pop          # Restore your changes
# Resolve any conflicts
git add .
git commit -m "Your message"
git push
```

### Mistake 2: Pushed to Wrong Branch
**Problem:** Accidentally pushed to main instead of feature branch

**Fix:**
```bash
# Can't easily undo, but you can:
# 1. Create new branch from your changes
git checkout -b correct-branch
git push origin correct-branch

# 2. Create PR from correct-branch to main
```

### Mistake 3: Pull/Push Conflict
**Problem:** Someone else changed the same file

**Fix:**
```bash
git pull  # Will show conflict
# Edit files to resolve conflicts (look for <<<<<<< markers)
git add .
git commit -m "Resolved conflicts"
git push
```

---

## 🎮 Practice Exercise

Try this safe practice sequence:

```bash
# 1. Check current status
git status

# 2. Pull (safe - downloads changes)
git pull origin main

# 3. Create a test file
echo "Test file" > test.txt

# 4. Check status again (see new file)
git status

# 5. Add file
git add test.txt

# 6. Commit
git commit -m "Test commit"

# 7. Push
git push origin your-branch

# 8. Check on GitHub.com - your file is there!

# 9. Delete test file
rm test.txt
git add test.txt
git commit -m "Remove test file"
git push
```

---

## 📊 Decision Tree

```
          Need to get latest changes?
                    ↓
              Use: git pull
                    ↓
            Made some changes?
                    ↓
              Use: git add .
                    ↓
         Want to save changes?
                    ↓
         Use: git commit -m "..."
                    ↓
     Want to upload to GitHub?
                    ↓
         Use: git push origin branch
```

---

## 🔍 How to Check Your Status

### Check What Branch You're On
```bash
git branch
# Current branch has * next to it
```

### Check What Changed
```bash
git status
# Shows files you've modified
```

### Check If You're Behind/Ahead
```bash
git fetch
git status
# Shows "Your branch is behind/ahead by X commits"
```

### See Commit History
```bash
git log --oneline -10
# Shows last 10 commits
```

---

## 🆘 Emergency Commands

### Undo All Local Changes (DANGER!)
```bash
git reset --hard  # ⚠️ Deletes all uncommitted changes!
git pull          # Get fresh copy from GitHub
```

### Undo Last Commit (Keep Changes)
```bash
git reset --soft HEAD~1  # Undoes commit, keeps changes
```

### Undo Last Push (Advanced)
```bash
# NOT recommended - better to create new commit fixing the issue
git revert HEAD  # Creates new commit that undoes last one
git push
```

---

## 📝 Cheat Sheet

| What You Want | Command |
|---------------|---------|
| Get latest from GitHub | `git pull origin main` |
| See what changed | `git status` |
| Save changes locally | `git add . && git commit -m "msg"` |
| Send to GitHub | `git push origin branch` |
| Create new branch | `git checkout -b new-branch` |
| Switch branch | `git checkout branch-name` |
| See branches | `git branch -a` |
| Undo changes | `git checkout -- filename` |

---

## 🎓 Remember

1. **PULL before you start working** (⬇️ download)
2. **Make your changes**
3. **Commit your changes** (save locally)
4. **PUSH when done** (⬆️ upload)

### The Golden Rule
```
Pull → Edit → Add → Commit → Push
  ⬇️    ✏️    ➕     💾      ⬆️
```

---

## 🔗 Additional Resources

- **Visual Git Guide:** https://marklodato.github.io/visual-git-guide/index-en.html
- **Git Official Docs:** https://git-scm.com/doc
- **GitHub Guides:** https://guides.github.com/
- **Interactive Tutorial:** https://learngitbranching.js.org/

---

**Pro Tip:** When in doubt, run `git status` to see where you are!
