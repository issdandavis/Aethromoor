# 🤖 Auto-Commit Quick Reference

Need to save your work fast? Here's the TL;DR:

## One-Command Auto-Commit

```bash
./scripts/auto-commit.sh
```

That's it! This will commit and push all your changes.

## Common Uses

```bash
# Custom commit message
./scripts/auto-commit.sh -m "Updated game lore"

# Preview what would be committed (safe to run)
./scripts/auto-commit.sh -n

# Commit but don't push yet
./scripts/auto-commit.sh -P

# Start auto-save every 5 minutes
./scripts/watch-and-commit.sh
```

## Full Documentation

See **[docs/AUTO_COMMIT_GUIDE.md](docs/AUTO_COMMIT_GUIDE.md)** for complete guide.

## What It Does

1. ✅ Adds all your changed files (respects .gitignore)
2. ✅ Creates a commit with timestamp
3. ✅ Pushes to your current branch
4. ✅ Shows you what it's doing
5. ✅ Warns about large files
6. ✅ Safe - won't commit secrets or build artifacts

## Safety First

- Always respects `.gitignore`
- Warns about files > 10MB
- Shows what will be committed before committing
- Dry-run mode available (`-n` flag)
- Won't commit `.env`, `*.log`, or other sensitive files

## Integration

Works great with:
- Writing sessions (use file watcher)
- Game development (use manual script)
- Automated workflows (use GitHub Actions)
- Zapier integrations (see AUTOMATION_GUIDE.md)

## Need Help?

- Run `./scripts/auto-commit.sh -h` for all options
- Check **[docs/AUTO_COMMIT_GUIDE.md](docs/AUTO_COMMIT_GUIDE.md)** for detailed guide
- See **[scripts/README.md](scripts/README.md)** for script info

---

*Part of the Avalon automation toolkit* 🎮✨
