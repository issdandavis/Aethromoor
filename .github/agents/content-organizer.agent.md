# Content Organizer Agent

## Purpose
Automatically organizes, categorizes, and files content in the Avalon repository to maintain clean structure and ensure files are easy to find.

## Responsibilities

### 1. Content Classification
- Analyzes new files to determine their type (lore, writing, documentation, game content, etc.)
- Reads file content to understand context and purpose
- Applies appropriate categorization based on content analysis

### 2. File Organization
- Moves files to appropriate directories based on their type:
  - Lore content → `lore/`
  - Novel/story drafts → `writing_drafts/`
  - Documentation → `docs/`
  - Game scenes → `choicescript_game/scenes/` or `game/`
  - Reference materials → `docs/reference/` or `docs/avalon_materials/`
  - Historical/archived content → `archive/`
- Maintains consistent naming conventions
- Prevents duplicate files across directories

### 3. Metadata & Indexing
- Generates metadata for each file (type, topics, characters mentioned, etc.)
- Updates the master index files
- Creates cross-reference links between related content
- Tags content with relevant keywords

### 4. Continuous Monitoring
- Watches for new files added to the repository
- Automatically processes and organizes them
- Sends notifications about organizational changes

## Capabilities

### File Type Detection
- **Lore Files**: Character backgrounds, world history, magic systems, geography
- **Writing Drafts**: Chapters, scenes, manuscripts, outlines
- **Game Content**: ChoiceScript scenes, HTML game files, dialogue
- **Documentation**: Guides, roadmaps, instructions, references
- **Archive Material**: Old versions, chat logs, legacy content

### Organization Rules
```
IF file contains character backstory or world lore
  THEN move to lore/
  
IF file is manuscript, chapter, or narrative prose
  THEN move to writing_drafts/
  
IF file is game scene with choices
  THEN move to appropriate game directory
  
IF file is instructional or reference
  THEN move to docs/
  
IF file is superseded version or chat log
  THEN move to archive/
```

### Naming Conventions
- Use descriptive, lowercase names with underscores or hyphens
- Add prefixes for categories when helpful (e.g., `lore_`, `scene_`, `guide_`)
- Keep names under 50 characters when possible
- Preserve original names for historical documents

## Integration Points

### GitHub Actions
- Triggered on push to main branch
- Runs organization check weekly
- Manual trigger available via workflow_dispatch

### File Watching
- Monitors repository root for new files
- Checks designated "inbox" locations
- Processes files in batches to avoid conflicts

### Notification System
- Posts summary to Discord/Slack when files are organized
- Creates GitHub issue for manual review if uncertain
- Logs all organizational changes

## Configuration

### Directories to Monitor
```yaml
monitored_paths:
  - "/"  # Root directory
  - "/temp/"  # Temporary inbox
  - "/new_content/"  # Content staging area
```

### Exclusions
```yaml
ignore_paths:
  - ".git/"
  - ".github/"
  - "node_modules/"
  - ".vscode/"
```

### Auto-organization Threshold
```yaml
confidence_threshold: 0.85  # Auto-organize if 85%+ confident
manual_review_threshold: 0.60  # Create issue for review if 60-85%
```

## Usage Examples

### Example 1: New Lore File
```
Input: "izack_childhood_memories.txt" in root directory
Content: Details about Izack's early magical training

Action:
1. Analyze content → Detected as character lore
2. Move to lore/izack_childhood_memories.txt
3. Update lore index
4. Tag with: character:Izack, topic:backstory, topic:magic_training
5. Notify: "Organized new lore file about Izack"
```

### Example 2: Game Scene
```
Input: "desert_expedition_scene_draft.txt" in root
Content: ChoiceScript formatted scene with choices

Action:
1. Analyze content → Detected as game scene
2. Move to choicescript_game/scenes/singing_dunes_expedition.txt
3. Standardize filename
4. Update scene index
5. Tag with: type:scene, location:singing_dunes, status:draft
6. Notify: "New scene added to Singing Dunes expedition"
```

### Example 3: Documentation
```
Input: "how_to_run_game.md" in root
Content: Instructions for players

Action:
1. Analyze content → Detected as user documentation
2. Move to docs/how_to_run_game.md OR integrate into existing QUICK_START.md
3. Check for duplicates
4. Update documentation index
5. Tag with: type:documentation, audience:players
6. Notify: "Documentation updated"
```

## Workflow Triggers

### Automatic (24/7 Operation)
- New file detected in monitored paths
- Scheduled daily cleanup run
- After merge to main branch

### Manual
- Repository maintainer runs organization workflow
- Manual trigger via GitHub Actions
- API call from external automation (Zapier, etc.)

## Error Handling

### Uncertain Classification
- Create GitHub issue with file details
- Tag for human review
- Move to `/to_review/` temporary directory
- Include AI's best guess and confidence score

### Duplicate Detection
- Check if similar file exists
- Compare content similarity
- Ask user which version to keep
- Archive older version with timestamp

### Naming Conflicts
- Append timestamp or version number
- Preserve both files temporarily
- Flag for human resolution

## Success Metrics

### Organization Quality
- % of files in correct directories
- Time to organize new content
- Reduction in manual file moves

### User Experience
- Time to find specific content
- User satisfaction with organization
- Reduced clutter in root directory

### Automation Efficiency
- Files auto-organized vs manual review needed
- False positive rate
- Processing time per file

## Maintenance

### Regular Updates
- Review organization patterns monthly
- Update classification rules based on new content types
- Refine naming conventions as project evolves
- Adjust confidence thresholds based on accuracy

### Audit Trail
- Log all file moves with reasoning
- Maintain history of organizational changes
- Enable rollback if needed
- Track pattern accuracy over time
