# Multi-AI Coordination System Documentation

This document outlines the multi-AI coordination system utilized in the Avalon project, detailing the handoff stages between different AI assistants and custom GitHub Copilot agents.

## Overview
The Avalon project employs a multi-AI coordination system to enhance efficiency and leverage the strengths of different AI models. This includes both manual AI coordination (using different AI tools) and GitHub Copilot custom agents for specialized tasks.

## GitHub Copilot Custom Agents

### Available Custom Agents
This repository includes specialized GitHub Copilot custom agents:

1. **Avalon Lore Steward** (`.github/agents/my-agent.agent.md`)
   - Curates and validates narrative content
   - Ensures lore consistency
   - Manages file organization
   - Usage: `@avalon-lore-steward [your request]`

2. **ChoiceScript Converter** (`.github/agents/choicescript-converter.agent.md`)
   - Converts HTML scenes to ChoiceScript
   - Implements stat tracking
   - Maintains scene parity
   - Usage: `@choicescript-converter [your request]`

### Setup and Usage
If custom agents are not available, see:
- **Quick Fix**: [docs/QUICK_START_CUSTOM_AGENTS.md](../docs/QUICK_START_CUSTOM_AGENTS.md)
- **Full Guide**: [docs/CUSTOM_AGENTS_SETUP.md](../docs/CUSTOM_AGENTS_SETUP.md)
- **Overview**: [docs/CUSTOM_AGENTS_OVERVIEW.md](../docs/CUSTOM_AGENTS_OVERVIEW.md)

## Manual Multi-AI Handoff Stages

For coordinating multiple AI assistants (Copilot, Claude, etc.) manually:

## Handoff Stages

### 1. Task Assignment
- **Description**: Initial task assignment takes place where the main task is defined.
- **Responsible AI**: @Copilot is responsible for the task setup and initial input generation.

### 2. Processing
- **Description**: The task is actively processed. @Copilot creates the initial drafts or solutions based on the defined requirements.
- **Output**: An output is generated, which is then evaluated for quality and completeness.

### 3. Handoff to @Claude
- **Description**: Upon completion of the initial processing, @Copilot hands off the task to @Claude for further refinement.
- **Criteria for Handoff**: The output from @Copilot must meet predetermined quality thresholds.

### 4. Refinement by @Claude
- **Description**: @Claude reviews and enhances the output, addressing any limitations and improving coherence and usability.
- **Output**: The refined output is finalized and prepared for delivery or implementation.

### 5. Feedback Loop
- **Description**: Post-delivery feedback is collected to assess performance.
- **Purpose**: This feedback is crucial for refining task definitions and improving future handoffs.

## Conclusion
Understanding the multi-AI coordination system is essential for ensuring the efficient collaboration between AI models. By following the outlined stages, we can leverage the unique capabilities of each AI and maximize our productivity.