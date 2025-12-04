# 🚀 Quick Command Reference - Avalon Project

This file provides instant access to common commands and workflows for developing Polly's Wingscroll.

## 🎮 Playing the Game

### HTML Version (Local)
```bash
# Option 1: Use the helper script
./scripts/play-game.sh

# Option 2: Open directly
open game/index.html              # macOS
xdg-open game/index.html          # Linux
start game/index.html             # Windows

# Option 3: Local server
npm run serve
# Then visit: http://localhost:8000
```

### ChoiceScript Version
See `choicescript_game/README.md` for ChoiceScript IDE setup

---

## ✅ Testing & Validation

### Run All Validations
```bash
./scripts/validate-game.sh
# or
npm test
```

### Check JavaScript Syntax
```bash
node -c game/game.js
```

### Analyze Repository Health
```bash
./scripts/analyze-repo.sh
# or
npm run analyze
```

---

## 📝 Common Git Workflows

### Before Making Changes
```bash
git pull origin main
git checkout -b feature/your-feature-name
```

### Committing Changes
```bash
# Validate first!
./scripts/validate-game.sh

# Then commit
git add .
git status
git commit -m "Your descriptive message"
git push origin your-branch-name
```

### Checking Status
```bash
git status
git diff
git log --oneline -5
```

---

## 📂 File Navigation

### Key Directories
```bash
# HTML game
cd game/

# ChoiceScript game
cd choicescript_game/

# Lore and worldbuilding
cd lore/

# Writing drafts
cd writing_drafts/

# Documentation
cd docs/

# Archive (old materials)
cd archive/
```

### Finding Files
```bash
# Find all JavaScript files
find . -name "*.js" -not -path "./.git/*"

# Find all story content
find game/scenes -name "*.txt"
find choicescript_game/scenes -name "*.txt"

# Search for text in files
grep -r "Izack" lore/
grep -r "Polly" game/
```

---

## 🛠️ Development Tasks

### Modifying Game Content

**HTML Version:**
1. Edit `game/game.js` - Add/modify story nodes
2. Edit `game/index.html` - Change UI
3. Edit `game/style.css` - Update styling
4. Test: `./scripts/play-game.sh`
5. Validate: `./scripts/validate-game.sh`

**ChoiceScript Version:**
1. Edit `choicescript_game/scenes/*.txt`
2. Edit `choicescript_game/startup.txt` for stats
3. Test in ChoiceScript IDE
4. Validate scene files

### Adding New Story Content

**Required steps:**
1. Plan the story node structure
2. Add nodes to `storyNodes` object in `game/game.js`
3. Link choices using `next:` property
4. Add stat effects using `effects:` property
5. Test all paths
6. Convert to ChoiceScript if needed

---

## 📊 Repository Maintenance

### Cleanup Commands
```bash
# Remove untracked files
git clean -n  # Preview what will be deleted
git clean -f  # Actually delete

# Check repository size
du -sh .
du -sh */ | sort -h

# Find large files
find . -type f -size +1M -not -path "./.git/*"

# Find duplicate files
fdupes -r . 2>/dev/null || echo "Install fdupes for duplicate detection"
```

### Update .gitignore
```bash
# Edit .gitignore
nano .gitignore

# Check what's ignored
git status --ignored
```

---

## 🔧 Troubleshooting

### Game Won't Load
```bash
# Check for JavaScript errors
node -c game/game.js

# Check browser console (F12 in most browsers)
# Look for error messages
```

### Git Issues
```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Discard all local changes
git checkout .

# View commit history
git log --graph --oneline --all
```

### Script Won't Run
```bash
# Make executable
chmod +x scripts/*.sh

# Check script syntax
bash -n scripts/validate-game.sh
```

---

## 📖 Documentation

### Main Documents
- `README.md` - Project overview
- `START_HERE.md` - Quickest start guide
- `QUICK_START.md` - Detailed getting started
- `CONTRIBUTING.md` - How to contribute
- `docs/PROJECT_ROADMAP.md` - Development plan
- `docs/AUTOMATION_GUIDE.md` - Automation setup
- `docs/NEXT_TASKS.md` - Task queue

### Quick Reads
```bash
# View README
cat README.md | less

# View roadmap
cat docs/PROJECT_ROADMAP.md | less

# View next tasks
cat docs/NEXT_TASKS.md
```

---

## 🤝 Collaboration

### Sharing Your Work
```bash
# Create a feature branch
git checkout -b feature/my-feature

# Make changes and commit
git add .
git commit -m "Description of changes"

# Push to GitHub
git push origin feature/my-feature

# Create Pull Request on GitHub.com
```

### Getting Latest Updates
```bash
git fetch origin
git pull origin main
```

---

## 🎯 Common Tasks - Quick Reference

| Task | Command |
|------|---------|
| Play game | `./scripts/play-game.sh` |
| Validate | `./scripts/validate-game.sh` |
| Analyze | `./scripts/analyze-repo.sh` |
| Start server | `npm run serve` |
| Check syntax | `node -c game/game.js` |
| View changes | `git diff` |
| Commit | `git commit -m "message"` |
| Push | `git push` |

---

## 💡 Pro Tips

1. **Always validate before committing:**
   ```bash
   ./scripts/validate-game.sh && git commit
   ```

2. **Use descriptive commit messages:**
   ```bash
   git commit -m "Add truth-testing scene to Singing Dunes expedition"
   ```

3. **Test in browser regularly:**
   Open `game/index.html` and play through your changes

4. **Keep backups:**
   ```bash
   cp game/game.js game/game.js.backup
   ```

5. **Use branches for experiments:**
   ```bash
   git checkout -b experiment/new-feature
   ```

---

## 🔗 External Resources

- [ChoiceScript Wiki](https://choicescriptdev.fandom.com/wiki/ChoiceScript_Wiki)
- [Git Documentation](https://git-scm.com/doc)
- [Hosted Games Forums](https://forum.choiceofgames.com/)
- [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)

---

**Need help?** Check the full documentation or ask in the project Discord/forum.

**Last Updated:** Auto-generated on script run
