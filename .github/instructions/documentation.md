---
applyTo:
  - "*.md"
  - "docs/**/*.md"
  - "lore/**/*.md"
  - "writing_drafts/**/*.md"
---

# Documentation Instructions

## Documentation Style Guide

### General Principles
- **Clarity first**: Write for someone discovering the project for the first time
- **Conversational tone**: Be friendly and approachable, especially in player-facing docs
- **Scannable**: Use headings, bullet points, and formatting to make docs easy to skim
- **Accurate**: Keep documentation synchronized with actual code and content

### Document Types

#### Player-Facing Documentation
Files: `README.md`, `START_HERE.md`, `PLAY_THE_GAME.md`, `QUICK_START.md`, `SUBMISSION_GUIDE.md`

Style:
- Enthusiastic and welcoming tone
- Step-by-step instructions
- Emoji usage is encouraged for visual appeal (🎮, ✨, 📚, etc.)
- Focus on "what" and "how" rather than "why"
- Include troubleshooting sections

Example:
```markdown
## 🎮 Quick Start - PLAY NOW!

### Option 1: Instant Play (HTML Version)
**👉 Just open `game/index.html` in your browser - that's it!**
```

#### Developer Documentation
Files: `docs/AUTOMATION_GUIDE.md`, `docs/PROJECT_ROADMAP.md`

Style:
- Professional and concise
- Technical accuracy is critical
- Include code examples where helpful
- Link to relevant resources
- Keep actionable and practical

#### Worldbuilding Documentation
Files: `lore/*.md`, `lore/*.txt`

Style:
- Immersive and descriptive
- Maintain in-universe perspective where appropriate
- Be consistent with established canon
- Include references to related lore documents

### Markdown Formatting

#### Headings
Use ATX-style headings with proper hierarchy:
```markdown
# Top Level (Document Title)
## Major Sections
### Subsections
#### Minor Points
```

#### Links
- Use descriptive link text: `[how to play](PLAY_THE_GAME.md)` not `[click here](PLAY_THE_GAME.md)`
- Verify all internal links work
- Use relative paths for internal links

#### Code Blocks
Use fenced code blocks with language specification:
```markdown
    ```javascript
    const example = "code";
    ```
```

#### Emphasis
- **Bold** for strong emphasis and UI elements: "Click the **Play** button"
- *Italic* for subtle emphasis and terms: "The *collaboration score* affects..."
- Use sparingly for maximum impact

### File Structure References

When referencing the repository structure, use consistent formatting:

```markdown
Avalon/
├── game/              # Description
│   ├── index.html
│   └── game.js
├── lore/
└── docs/
```

### Common Documentation Tasks

#### Updating README.md
- Keep the project overview current
- Update statistics (word count, scene count, etc.)
- Ensure all links work
- Maintain the folder structure diagram

#### Updating START_HERE.md / PLAY_THE_GAME.md
- Keep instructions simple and direct
- Test instructions to ensure they work
- Update for any structural changes
- Keep troubleshooting sections current

#### Adding to docs/
- Follow existing document structure
- Include table of contents for long docs
- Date-stamp documents if relevant
- Cross-reference related documents

#### Updating lore/
- Maintain consistency with existing worldbuilding
- Reference canonical sources
- Use consistent naming for places, characters, magic systems
- Consider impact on game narrative

## Documentation Standards

### Player-Facing Docs
✅ **Do:**
- Start with the quickest path to success
- Provide multiple options when available
- Include visual indicators (emoji, formatting)
- Anticipate common questions
- End with encouragement or next steps

❌ **Don't:**
- Assume technical knowledge
- Use jargon without explanation
- Write walls of text without breaks
- Forget to test instructions
- Leave broken links or outdated information

### Technical Docs
✅ **Do:**
- Be precise and specific
- Include prerequisites
- Provide command examples
- Link to relevant resources
- Keep updated with code changes

❌ **Don't:**
- Be vague or ambiguous
- Assume context
- Skip error handling
- Leave outdated information
- Over-complicate simple concepts

### Worldbuilding Docs
✅ **Do:**
- Maintain canonical consistency
- Cross-reference related lore
- Use evocative, immersive language
- Organize by topic or theme
- Preserve established voice

❌ **Don't:**
- Contradict existing lore
- Add content that conflicts with game narrative
- Use anachronistic or out-of-world language
- Leave orphaned or disconnected content

## File Organization

### Top-Level Documentation
- `README.md` - Project overview and primary entry point
- `START_HERE.md` - Simplest possible instructions
- `PLAY_THE_GAME.md` - Detailed play instructions
- `QUICK_START.md` - Concise playing guide
- `SUBMISSION_GUIDE.md` - Publishing information
- `ORGANIZATION_SUMMARY.md` - Repository structure explanation

### Directory Documentation
Each major directory should have a `README.md` explaining its contents:
- `docs/README.md` - Overview of development documentation
- `lore/README.md` - Overview of worldbuilding content
- `writing_drafts/README.md` - Overview of manuscripts

## Maintenance

### When to Update Documentation
- After adding new features or content
- When file structure changes
- After fixing bugs that affect user experience
- When testing reveals unclear instructions
- Before any release or milestone

### Version Information
- Update version badges in README.md
- Update statistics (word count, scene count, etc.)
- Keep changelogs current if applicable
- Note major changes in relevant docs

## Cross-References

When referencing game content in documentation:
- Link to specific files when helpful
- Use consistent terminology from the game
- Reference character names, locations, and mechanics accurately
- Keep game spoilers minimal in player-facing docs

## Accessibility

- Use descriptive heading structure
- Provide alt text for images (if any are added)
- Use clear, simple language
- Ensure code examples are readable
- Test with screen readers when possible
