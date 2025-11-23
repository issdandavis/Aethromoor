---
name: documentation-agent
description: Maintains and updates project documentation automatically
triggers:
  - push
  - pull_request
  - workflow_dispatch
permissions:
  contents: write
  pull_requests: write
capabilities:
  - documentation_generation
  - readme_updates
  - changelog_management
  - api_documentation
---

# Documentation Agent

## Purpose
Automatically maintains project documentation including:
- README files
- API documentation
- Changelogs
- Code comments
- Tutorial content
- Architecture diagrams

## Triggers

### Automatic Triggers
- **Push to main/develop**: Update changelog, version references
- **Pull Request merged**: Add to changelog
- **New release**: Generate release notes
- **Code changes**: Update affected documentation

### Manual Triggers
```markdown
/ai-document <module>
/ai-docs update-readme
/ai-docs generate-api-docs
/ai-docs update-changelog
```

## Behaviors

### Changelog Management
```yaml
on_pr_merge:
  - detect_change_type: [feature, fix, breaking, security]
  - extract_description: from PR title and body
  - update_changelog: CHANGELOG.md
  - categorize_change: 
      - Added (new features)
      - Changed (changes in existing)
      - Deprecated (soon to be removed)
      - Removed (removed features)
      - Fixed (bug fixes)
      - Security (security fixes)
```

### README Synchronization
```yaml
on_structure_change:
  - update_file_tree
  - update_feature_list
  - update_installation_steps
  - update_usage_examples
  - verify_links
```

### API Documentation
```yaml
on_code_change:
  - scan_for_doc_comments
  - generate_api_reference
  - update_type_definitions
  - create_usage_examples
  - build_documentation_site
```

### Code Comments
```yaml
on_new_function:
  - detect_missing_docstrings
  - generate_parameter_docs
  - add_return_type_docs
  - include_usage_example
  - add_error_handling_docs
```

## Documentation Standards

### JSDoc Format
```javascript
/**
 * Executes a game scene and returns player choices
 * 
 * @param {string} sceneId - Unique identifier for the scene
 * @param {Object} gameState - Current game state
 * @param {number} gameState.collaboration - Collaboration stat
 * @param {Object} gameState.relationships - Character relationship values
 * @returns {Promise<SceneResult>} Scene execution result
 * @throws {SceneNotFoundError} If scene doesn't exist
 * 
 * @example
 * const result = await executeScene('first_lesson', {
 *   collaboration: 50,
 *   relationships: { izack: 10, aria: 5 }
 * });
 */
function executeScene(sceneId, gameState) {
  // Implementation
}
```

### Markdown Standards
```markdown
# Component Name

## Overview
Brief description of what this is

## Installation
How to install/use

## API Reference
### Methods
- `method(param)` - Description

## Examples
```language
code example
```

## Contributing
How to contribute

## License
License information
```

### ChoiceScript Documentation
```choicescript
*comment ================================================
*comment SCENE: First Lesson
*comment Purpose: Introduce collaborative magic system
*comment Stats Modified: collaboration (+5 to +15)
*comment Relationships: izack, aria
*comment ================================================

*comment This scene teaches the player about collaborative
*comment casting and introduces key NPCs
```

## Automated Updates

### Version References
```yaml
on_version_bump:
  files:
    - README.md: "Version: X.Y.Z"
    - package.json: version field
    - startup.txt: "*comment Version X.Y.Z"
    - index.html: version meta tag
  update_all: true
```

### File Tree Generation
```yaml
on_file_structure_change:
  scan: [src, game, choicescript_game, docs, lore]
  exclude: [node_modules, .git, archive]
  format: tree
  output: README.md
  section: "Repository Structure"
```

### Link Verification
```yaml
on_schedule:
  cron: "0 0 * * 1"  # Weekly on Monday
  tasks:
    - scan_all_markdown_files
    - extract_links
    - verify_internal_links
    - check_external_links
    - create_issues_for_broken_links
```

## Documentation Quality Checks

### Completeness
```yaml
check_for:
  - Every public function has documentation
  - Every module has README
  - All API endpoints documented
  - All configuration options documented
  - Examples provided for complex features
```

### Clarity
```yaml
check_for:
  - Clear headings and structure
  - Code examples are valid
  - Screenshots are up to date
  - No broken links
  - Consistent formatting
```

### Accuracy
```yaml
check_for:
  - Code examples match current API
  - Version numbers are current
  - Deprecated features marked
  - Migration guides provided
```

## Auto-Generated Documentation

### API Reference
```markdown
# API Reference

## Functions

### executeScene(sceneId, gameState)
Executes a game scene

**Parameters:**
- `sceneId` (string) - Scene identifier
- `gameState` (Object) - Current game state

**Returns:** Promise<SceneResult>

**Example:**
\`\`\`javascript
await executeScene('first_lesson', state);
\`\`\`
```

### Changelog
```markdown
# Changelog

## [1.2.0] - 2025-11-23

### Added
- New dorm customization system (#45)
- Character bonds scene (#47)

### Fixed
- Scene transition bug (#52)
- Stat calculation error (#54)

### Changed
- Updated collaboration thresholds
```

### Component Documentation
```markdown
# Dorm Room Component

## Description
Interactive dorm room customization system

## Features
- 4 room styles
- 4 magical features
- 16 unique combinations

## Usage
\`\`\`choicescript
*gosub_scene dorm_room customize
\`\`\`

## Stats Modified
- None directly
- Sets {dorm_style} variable
- Sets {magical_feature} variable
```

## Integration

### With Code Changes
```yaml
workflow:
  1. Developer pushes code
  2. Documentation agent detects changes
  3. Scans modified files
  4. Generates/updates docs
  5. Creates PR with doc updates
  6. Requests review
```

### With CI/CD
```yaml
workflow:
  1. Build process completes
  2. Extract API information
  3. Generate documentation
  4. Deploy to GitHub Pages
  5. Update doc site
```

## Metrics

Track documentation quality:
```yaml
metrics:
  - documentation_coverage: 85%
  - broken_links: 0
  - outdated_sections: 3
  - missing_examples: 5
  - last_updated: 2 days ago
```

## Templates

### New Feature Documentation Template
```markdown
# Feature: {FEATURE_NAME}

## Overview
What this feature does

## How to Use
Step-by-step guide

## API Reference
Functions and parameters

## Examples
Working code examples

## Configuration
Available options

## Troubleshooting
Common issues and solutions
```

### API Endpoint Template
```markdown
### {METHOD} {PATH}

**Description:** What this endpoint does

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id   | int  | Yes      | Item ID     |

**Response:**
\`\`\`json
{
  "status": "success",
  "data": {}
}
\`\`\`

**Example:**
\`\`\`bash
curl -X GET /api/items/123
\`\`\`
```

## Configuration

### Documentation Config
```yaml
# .github/config/docs.yml
documentation:
  style: markdown
  api_format: jsdoc
  changelog_format: keepachangelog
  
  auto_update:
    - readme: true
    - changelog: true
    - api_docs: true
    - code_comments: false  # Manual only
  
  quality_checks:
    - completeness: true
    - link_validation: true
    - code_example_validation: true
    
  deployment:
    target: github_pages
    branch: gh-pages
    directory: docs/
```

## Best Practices

1. **Keep docs close to code**: Documentation in same PR as changes
2. **Use examples**: Every feature needs working example
3. **Version everything**: Document which version added/changed feature
4. **Link related docs**: Cross-reference related documentation
5. **Regular reviews**: Schedule doc review sessions
6. **User perspective**: Write from user's point of view
7. **Update on change**: Never let docs drift from code
