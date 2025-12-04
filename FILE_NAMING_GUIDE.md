# File Naming Guidelines for Avalon Repository

## Overview
This guide ensures consistent, accessible file naming for all collaborators, especially non-technical users.

## Core Principles

### ✅ DO:
- **Use snake_case** (lowercase with underscores): `my_file_name.txt`
- **Be descriptive**: `izacks_magical_universe_complete.txt` not `universe.txt`
- **Use version numbers**: `v1`, `v2`, `v20` instead of `(1)`, `(2)`, `(20)`
- **Keep it simple**: Avoid special characters and excessive punctuation
- **Be consistent**: Follow the patterns already established in the repository

### ❌ DON'T:
- **No spaces**: Use `spiral_of_avalon.txt` not `spiral of avalon.txt`
- **No special characters**: Avoid `#`, `__`, `()`, `–`, `'`, quotes
- **No ambiguous abbreviations**: `complete` not `comple`, `version` not `v.`
- **No duplicate names**: Each file should have a unique, clear name

## Naming Patterns by Category

### Lore Files
```
izacks_magical_universe_complete.txt
geography_and_natural_lore_spiral_pollyoneth.pdf
unified_worldbuilding_master_framework.txt
```
Pattern: `[topic]_[descriptor]_[context].extension`

### Writing Drafts
```
spiral_of_avalon_draft.txt
spiral_pollyoneth_book1_masterplan.pdf
spiral_pollyoneth_book1_masterplan_v20.pdf
```
Pattern: `[title]_[book/part]_[type]_[version].extension`

### Chapter Files
```
chapter_01_cave_and_the_contract.txt
chapter_02_world_tree_opens.txt
chapter_05_place_called_avalon.txt
```
Pattern: `chapter_[number]_[title_summary].extension`
- Use two-digit numbers: `01`, `02`, `10`, not `1`, `2`, `10`
- Keep title summary brief but clear

### Documentation Files
```
GAME_DEVELOPMENT_MASTER_REFERENCE.md
PROJECT_ROADMAP.md
AUTOMATION_GUIDE.md
```
Pattern: `[TOPIC]_[PURPOSE].md`
- Documentation in root/docs can use UPPERCASE for visibility
- Still no spaces, use underscores

### Archive Files
```
entire_chat_log.txt
chronological_quotes_updated.txt
fantasy_world_history_expansion_claude.html
```
Pattern: `[content]_[descriptor]_[source].extension`
- Archives can be more flexible but still follow core rules
- Include source when relevant (e.g., `_claude`, `_chatgpt`)

### Version Numbering
```
unified_narrative_outline_synthesis.pdf        (original)
unified_narrative_outline_synthesis_v1.pdf     (version 1)
unified_narrative_outline_synthesis_v2.pdf     (version 2)
spiral_of_eternity_v2_4.docx                  (version 2.4)
```
Pattern: `[filename]_v[number].extension`
- Use `v1`, `v2`, `v20` for major versions
- Use `v2_4` for minor versions (underscores, not dots)

## Examples: Before & After

### Before (Problematic):
```
# IZACK'S MAGICAL UNIVERSE - COMPLE.txt
__Geography and Natural Lore of the Spiral of Pollyoneth__.pdf
# The Spiral of Avalon.txt
The Spiral of Avalon.VERY GOOD.1st draft.txt
Unified Narrative Outline and Synthesis (2).pdf
```

### After (Clean):
```
izacks_magical_universe_complete.txt
geography_and_natural_lore_spiral_pollyoneth.pdf
spiral_of_avalon_draft.txt
spiral_of_avalon_first_draft_good.txt
unified_narrative_outline_synthesis_v2.pdf
```

## Special Cases

### README Files
- Keep as `README.md` in each directory
- Explains what's in that directory

### Config Files
- Follow ecosystem conventions: `.gitignore`, `.env.example`
- System files can have dots and specific naming

### Game Assets
- HTML/CSS/JS files can use existing web conventions
- Scene files use descriptive names: `first_lesson.txt`, `singing_dunes.txt`

## Quick Reference Table

| File Type | Pattern | Example |
|-----------|---------|---------|
| Lore | `[topic]_[context].ext` | `tower_layout_reference.txt` |
| Chapters | `chapter_[##]_[title].ext` | `chapter_03_gardens_and_gateways.txt` |
| Drafts | `[title]_[type]_[version].ext` | `spiral_avalon_draft_v2.txt` |
| Documentation | `[TOPIC]_[TYPE].md` | `PROJECT_ROADMAP.md` |
| Reference | `[name]_[descriptor].ext` | `izack_campaign_chronicle.pdf` |
| Archive | `[content]_[source].ext` | `chat_log_claude.txt` |

## When Adding New Files

1. **Choose a clear, descriptive name**
2. **Use snake_case (lowercase_with_underscores)**
3. **Check for similar files to maintain consistency**
4. **Include version if it's not the first/only version**
5. **Avoid special characters, spaces, and ambiguous abbreviations**

## Migration Status

✅ All lore files renamed (November 2024)
✅ All writing_drafts files renamed (November 2024)
✅ All docs/avalon_materials files renamed (November 2024)
✅ All docs/reference files renamed (November 2024)
✅ All archive files renamed (November 2024)
✅ FILE_LOCATIONS.txt updated
✅ ORGANIZATION_SUMMARY.md updated

## Need Help?

If you're unsure about a filename:
1. Check existing files in the same directory
2. Follow the patterns in this guide
3. Ask: "Would a non-technical person understand what this file contains?"
4. When in doubt, be more descriptive rather than less

---

**Remember: Clear file names make collaboration easier for everyone!**
