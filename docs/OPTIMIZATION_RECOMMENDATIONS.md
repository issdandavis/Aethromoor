# Repository Optimization Recommendations

This document outlines additional optimizations to consider for the Avalon project repository.

## 🔴 High Priority (Do Soon)

### 1. Large Archive Files - Use Git LFS
**Issue:** Archive directory is 16MB+ with large binary files  
**Impact:** Slow clones, large repo size  
**Solution:**
```bash
# Install Git LFS
git lfs install

# Track large file types
git lfs track "*.pdf"
git lfs track "*.html" "*.zip"

# Migrate existing large files
git lfs migrate import --include="*.pdf,*.html" --everything
```

**Files to migrate:**
- `archive/ChatGPT Data Export.html` (13MB)
- `docs/avalon_materials/ChatGPT Data Export.html` (16MB)
- All PDFs > 1MB

**Benefit:** Faster clones, smaller repository

---

### 2. Modularize game.js
**Issue:** Single 1382-line file is hard to maintain  
**Impact:** Merge conflicts, hard to navigate  
**Recommendation:**

Split into modules:
```
game/
├── index.html
├── js/
│   ├── config.js        (game state, constants)
│   ├── story-nodes.js   (story content)
│   ├── ui.js            (UI updates)
│   ├── navigation.js    (node display logic)
│   └── main.js          (initialization)
├── data/
│   ├── prologue.json    (story data)
│   ├── expeditions.json
│   └── endings.json
└── game.js              (loads modules)
```

**Benefits:**
- Easier collaboration (less merge conflicts)
- Better code organization
- Faster development

---

### 3. Add Pre-commit Hooks
**Issue:** Errors can slip through to commits  
**Impact:** Broken builds in version history  
**Solution:**

Create `.git/hooks/pre-commit`:
```bash
#!/bin/bash
# Run validation before commit
./scripts/validate-game.sh

if [ $? -ne 0 ]; then
    echo "❌ Validation failed. Fix errors before committing."
    exit 1
fi

echo "✅ Validation passed. Proceeding with commit."
```

**Or use Husky (npm package):**
```bash
npm install --save-dev husky
npx husky init
npx husky add .husky/pre-commit "npm test"
```

---

## 🟡 Medium Priority (Nice to Have)

### 4. Documentation Consolidation
**Issue:** Similar documentation scattered across files  
**Current state:**
- `START_HERE.md`
- `QUICK_START.md`
- `PLAY_THE_GAME.md`
- `README.md`

**Recommendation:** Merge into single comprehensive README with sections

### 5. Automated Deployment
**Issue:** Manual deployment to GitHub Pages  
**Solution:** GitHub Actions workflow

Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
    paths:
      - 'game/**'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./game
```

### 6. Stat Balancing Tool
**Issue:** Hard to balance collaboration scores manually  
**Solution:** Script to analyze stat distribution

```bash
#!/bin/bash
# scripts/analyze-stats.sh
# Analyzes stat changes across all story paths
```

---

## 🟢 Low Priority (Future Enhancement)

### 7. Compress Archive Files
**Current:** Uncompressed text and HTML files  
**Recommendation:** 
```bash
# Compress old conversation logs
tar -czf archive/conversations.tar.gz archive/*.txt
# Remove originals after verification
```

### 8. Code Coverage for Story Paths
**Issue:** Unknown which story paths are tested  
**Solution:** Track which nodes players reach

Add to game.js:
```javascript
const pathAnalytics = {
    visited: new Set(),
    recordVisit: (nodeId) => pathAnalytics.visited.add(nodeId)
};
```

### 9. Performance Monitoring
**Track:**
- Game load time
- Average choice time
- Completion rates
- Popular endings

### 10. Asset Optimization
**When adding assets:**
- Compress images (use WebP or optimized PNG/JPEG)
- Minify CSS/JavaScript
- Use CDN for common libraries

---

## 📊 Impact vs. Effort Matrix

```
High Impact, Low Effort:
✅ Pre-commit hooks
✅ Validation scripts (DONE)

High Impact, Medium Effort:
📌 Git LFS migration
📌 Modularize game.js

Medium Impact, Low Effort:
📝 Documentation consolidation
📝 Automated deployment

Low Impact, High Effort:
⏳ Comprehensive analytics
⏳ Full test coverage
```

---

## 🎯 Recommended Implementation Order

### Week 1
1. ✅ Validation scripts (DONE)
2. Set up pre-commit hooks
3. Document Git LFS migration plan

### Week 2
4. Migrate to Git LFS
5. Test and verify
6. Update documentation

### Week 3
7. Plan game.js modularization
8. Create module structure
9. Migrate incrementally

### Week 4
10. Set up automated deployment
11. Consolidate documentation
12. Create stat balancing tool

---

## 💡 Quick Wins

These can be done in < 30 minutes each:

1. **Add .editorconfig**
   ```ini
   root = true
   
   [*]
   indent_style = space
   indent_size = 4
   end_of_line = lf
   charset = utf-8
   trim_trailing_whitespace = true
   insert_final_newline = true
   ```

2. **Add CODEOWNERS**
   ```
   # Auto-request reviews
   * @issdandavis
   /docs/ @issdandavis
   ```

3. **GitHub Issue Templates**
   - Bug report template
   - Feature request template
   - Story content template

4. **Pull Request Template**
   - Checklist for validation
   - Testing notes
   - Related issues

---

## 🔧 Tools to Consider

### Development Tools
- **ESLint** - JavaScript linting
- **Prettier** - Code formatting
- **Husky** - Git hooks
- **lint-staged** - Run linters on staged files

### CI/CD
- **GitHub Actions** - Already using
- **Dependabot** - Dependency updates
- **CodeQL** - Security scanning

### Documentation
- **Docusaurus** - Documentation site
- **GitBook** - Interactive docs
- **MkDocs** - Markdown docs

---

## 📈 Expected Outcomes

### After All Optimizations:

**Repository:**
- Size: ~5-10MB (down from 45MB)
- Clone time: < 10 seconds
- Organization: Excellent

**Development:**
- Validation: Automated
- Testing: Pre-commit
- Deployment: Automated

**Code Quality:**
- Modular: Easy to maintain
- Validated: Every commit
- Documented: Comprehensive

---

## ⚠️ Important Notes

1. **Backup before migrating:** Always backup before major changes
2. **Test Git LFS:** Verify on fresh clone before committing
3. **Incremental changes:** Don't do everything at once
4. **Team communication:** Coordinate with collaborators

---

## 📞 Need Help?

- **Git LFS:** https://git-lfs.github.com/
- **Husky:** https://typicode.github.io/husky/
- **GitHub Actions:** https://docs.github.com/actions
- **Modularization:** See `docs/` for architecture guidance

---

**Last Updated:** November 23, 2025  
**Status:** Recommendations pending implementation  
**Priority:** See impact matrix above
