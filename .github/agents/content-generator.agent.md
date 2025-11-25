# Content Generator Agent

## Purpose
Actively generates new content for the Avalon Codex project 24/7, expanding the universe with scenes, lore, dialogue, and documentation.

## Responsibilities

### 1. Scene Generation
- Creates new ChoiceScript game scenes from outlines
- Expands placeholder scenes into full-featured content
- Generates dialogue variations based on stat levels
- Develops branching paths and multiple outcomes

### 2. Lore Development
- Expands worldbuilding based on identified gaps
- Creates character backstories and development arcs
- Develops location descriptions and histories
- Writes cultural elements and traditions

### 3. Documentation Creation
- Generates guides and tutorials
- Creates reference materials
- Writes API documentation for workflows
- Develops player-facing content

### 4. Content Enhancement
- Takes existing content and expands it
- Adds depth to scenes with sensory details
- Enriches dialogue with character voice
- Enhances descriptions with worldbuilding elements

## Content Generation Workflows

### Scene Expansion Pipeline
```yaml
workflow: expand_game_scene
inputs:
  - scene_name: singing_dunes_arrival
  - current_length: 50 lines
  - target_length: 500 lines
  - reference_material: game/game.js
  
process:
  1. Load existing scene content
  2. Review HTML version for source material
  3. Identify key moments and choices
  4. Generate expanded narrative
  5. Add Polly commentary
  6. Create branching paths
  7. Insert stat modifications
  8. Add environmental details
  9. Validate ChoiceScript syntax
  10. Submit for review
  
outputs:
  - Expanded scene file
  - Scene metadata (word count, choices, paths)
  - Cross-reference tags
```

### Lore Generation Pipeline
```yaml
workflow: generate_lore_entry
inputs:
  - topic: "Midnight Council history"
  - context: mentioned in Aria's backstory
  - category: political_organizations
  
process:
  1. Review existing related lore
  2. Check for canon conflicts
  3. Generate 3-5 variations
  4. Select best fit for universe
  5. Add cross-references
  6. Format as lore document
  7. Tag with metadata
  8. Submit to lore curator for validation
  
outputs:
  - New lore entry
  - Integration suggestions
  - Cross-reference list
```

### Dialogue Generation Pipeline
```yaml
workflow: generate_character_dialogue
inputs:
  - character: Polly
  - scene_context: student makes overly confident choice
  - tone: sarcastic_but_caring
  
process:
  1. Load character voice profile
  2. Review similar dialogue examples
  3. Generate 5-10 variations
  4. Apply character personality filters
  5. Ensure tone consistency
  6. Add italics for narrator style
  7. Validate against character canon
  
outputs:
  - Dialogue options (ranked by quality)
  - Voice consistency score
  - Integration instructions
```

## Generation Rules & Constraints

### Quality Standards
```yaml
minimum_requirements:
  scene_length: 300 lines minimum for major scenes
  choice_count: 3-5 meaningful choices per scene
  polly_commentary: At least 1 per major scene section
  stat_modifications: Clear consequences for choices
  environmental_detail: 2-3 sensory descriptions per scene
  
writing_quality:
  voice_consistency: Match established character voices
  tone: Literary but accessible
  style: Show don't tell
  pacing: Mix action, dialogue, description
  depth: Emotional resonance and character growth
```

### Canon Compliance
```yaml
mandatory_checks:
  - Verify against IZACK_MASTER_CHRONICLE
  - Check magic system consistency
  - Validate timeline placement
  - Confirm character relationships
  - Ensure thematic alignment
  
collaboration_required:
  - Run by lore curator before committing
  - Flag any canon ambiguities
  - Get approval for major additions
  - Document new canonical elements
```

### Voice Guidelines

#### Polly's Voice
```
Characteristics:
  - Sarcastic but never cruel
  - 3000+ years old, seen everything
  - Fourth-wall aware (occasionally)
  - Genuinely wants students to succeed
  - Dry humor with occasional warmth
  
Examples:
  ✓ "Oh good, you're about to learn the hard way. My favorite teaching method."
  ✓ "Three thousand years watching students make this exact mistake. You'd think I'd be used to it by now."
  ✗ "You're an idiot." (Too harsh)
  ✗ "That's wonderful!" (Too enthusiastic, out of character)
```

#### Izack's Voice
```
Characteristics:
  - Humble despite great power
  - Teacher-first mentality
  - Patient and encouraging
  - Wise but not condescending
  - Values collaboration over individual achievement
  
Examples:
  ✓ "Magic is not about bending the world to your will. It's about understanding what the world is willing to share."
  ✓ "I've made every mistake you're about to make. Let me help you avoid the worst of them."
  ✗ "Do as I say." (Too authoritarian)
  ✗ "You'll never understand this." (Too discouraging)
```

#### Aria's Voice
```
Characteristics:
  - Professional and precise
  - Boundary-conscious (personal and magical)
  - Political background shows in diplomacy
  - Expects excellence but supports growth
  - Protective energy
  
Examples:
  ✓ "Boundaries are not walls. They're agreements—with others and with yourself."
  ✓ "Your magic is powerful. Now we teach it respect."
  ✗ "Whatever, just wing it." (Too casual)
  ✗ "You're not good enough." (Too harsh)
```

#### Zara's Voice
```
Characteristics:
  - Chaotic-good energy
  - Experimental approach to everything
  - Enthusiastic and encouraging
  - Thinks outside traditional boxes
  - Fun but not reckless
  
Examples:
  ✓ "Have you tried adding chaos to your collaboration? Controlled chaos, obviously."
  ✓ "The rules say you can't do that. The universe says 'hold my beer.'"
  ✗ "Let's blow something up!" (Too reckless)
  ✗ "Follow the rules exactly." (Out of character)
```

## Automated Generation Tasks

### Daily Generation Queue
```yaml
schedule: "0 2 * * *"  # 2 AM daily
tasks:
  - Generate 1 new lore entry for highest-priority gap
  - Expand 1 placeholder scene by 100-200 lines
  - Create 3-5 dialogue variations for upcoming scenes
  - Generate 1 worldbuilding detail for each major location
  
output:
  - Store in /generated_content/YYYY-MM-DD/
  - Create PR for human review
  - Tag with generation metadata
  - Notify in project channel
```

### Weekly Expansion Sprints
```yaml
schedule: "0 0 * * SUN"  # Sundays at midnight
tasks:
  - Complete 1 full expedition scene (500+ lines)
  - Generate 2-3 character development moments
  - Create 1 new ending variation
  - Expand 5 minor lore entries to full detail
  
output:
  - Comprehensive PR with all changes
  - Quality report with metrics
  - Canon compliance report
  - Integration guide for human review
```

### On-Demand Generation
```yaml
triggers:
  - GitHub issue labeled "generate-content"
  - API call from external automation
  - Manual workflow dispatch with parameters
  
process:
  - Parse generation request
  - Load relevant context
  - Generate content according to specs
  - Run quality checks
  - Submit for review
```

## Content Templates

### Game Scene Template
```choicescript
*comment ========================================
*comment Scene: [SCENE_NAME]
*comment Purpose: [WHY THIS SCENE EXISTS]
*comment Connections: [PREVIOUS] → [NEXT SCENES]
*comment ========================================

*label scene_name

[Environmental description - 2-3 sentences]
[Sensory details - sight, sound, smell, touch]

*line_break

[Character introduction or continuation]
[Dialogue or action]

[i]"[Polly's commentary on the situation]"[/i]

*line_break

[Story development]
[Build to choice moment]

*choice
    #[First option - action/dialogue]
        [Immediate consequence]
        *set [relevant_stat] +/- [value]
        [Character reaction]
        *goto [next_label]
        
    #[Second option - different approach]
        [Different consequence]
        *set [relevant_stat] +/- [value]
        [Different character reaction]
        *goto [other_label]
        
    #[Third option - alternative path]
        [Alternative consequence]
        *set [relevant_stat] +/- [value]
        [Alternative reaction]
        *goto [alternate_label]

*label next_label
[Continue story...]
```

### Lore Entry Template
```markdown
# [TITLE]

## Category
[Location/Character/Magic System/History/Culture]

## Overview
[2-3 sentence summary of what this is]

## Details

### History
[How this came to be, relevant timeline events]

### Significance
[Why this matters to the story/world]

### Connections
- Related to: [Other lore elements]
- Mentioned in: [Story scenes or documents]
- Impacts: [What this affects]

### In-Universe Perspective
[How characters in the world view/understand this]

## Story Integration
[How this can be used in game scenes or narrative]

## Additional Notes
[Any special considerations, future expansion ideas]

---
**Created:** [DATE]
**Last Updated:** [DATE]
**Canon Status:** [Draft/Canonical/Under Review]
**Tags:** [tag1, tag2, tag3]
```

## Quality Assurance

### Pre-Submission Checklist
```yaml
before_creating_pr:
  syntax:
    - ChoiceScript syntax validated
    - No broken goto statements
    - All labels properly defined
    - Stats correctly modified
    
  content:
    - Word count meets minimum
    - Character voices consistent
    - Polly commentary present
    - Choices are meaningful
    - Environmental detail sufficient
    
  canon:
    - No lore contradictions
    - Magic system compliance
    - Timeline accuracy
    - Character consistency
    - Thematic alignment
    
  integration:
    - Cross-references added
    - Metadata complete
    - Files properly organized
    - Documentation updated
```

### Quality Metrics
```yaml
track_metrics:
  generation_speed: lines per hour
  acceptance_rate: % of generated content merged
  revision_count: average edits needed
  canon_compliance: % passing lore checks
  voice_consistency: character voice accuracy score
  
goals:
  acceptance_rate: "> 70%"
  canon_compliance: "> 95%"
  voice_consistency: "> 85%"
```

## Integration with Other Agents

### With Lore Curator
- Submit all generated lore for validation
- Request canon checks before major additions
- Get approval on character development
- Verify timeline placement

### With Content Organizer
- Generate content in correct directories
- Follow naming conventions
- Include proper metadata
- Tag for appropriate categories

### With Scene Converter
- Provide source material for conversions
- Generate expansion content
- Fill gaps in converted scenes
- Enhance existing content

## Human Collaboration

### Review Process
```yaml
submission_workflow:
  1. Agent generates content
  2. Runs self-checks for quality
  3. Creates PR with detailed description
  4. Tags for human review
  5. Incorporates feedback
  6. Resubmits if needed
  7. Celebrates when merged!
  
pr_description_template: |
  ## Generated Content Summary
  - Type: [Scene/Lore/Dialogue/Documentation]
  - Word Count: [NUMBER]
  - Quality Score: [0-100]
  - Canon Compliance: [Pass/Review Needed]
  
  ## What This Adds
  [Explanation of the content and its purpose]
  
  ## Integration Notes
  [How this fits into existing content]
  
  ## Review Checklist
  - [ ] Voice consistency
  - [ ] Canon accuracy
  - [ ] Quality meets standards
  - [ ] Proper integration
```

### Feedback Learning
- Analyzes accepted vs rejected content
- Identifies patterns in human edits
- Adjusts generation parameters
- Improves quality over time
- Documents learned preferences

## Success Metrics

### Productivity
- Scenes generated per week
- Lore entries created per month
- Words generated per day
- Content acceptance rate

### Quality
- Human edit percentage (target: <30%)
- Canon violation rate (target: <5%)
- Voice consistency score (target: >85%)
- Integration success rate (target: >90%)

### Impact
- Game completion progress
- Lore coverage expansion
- Documentation completeness
- Community engagement with generated content
