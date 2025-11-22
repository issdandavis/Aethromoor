# AI Collaboration Guide for Avalon Project

**@ @issdandavis - ESTABLISH THIS AS THE OFFICIAL AI COLLABORATION PROTOCOL**

## Purpose

This guide defines clear roles and responsibilities for AI agents collaborating on the Avalon project to prevent confusion, duplication, and maintain narrative consistency.

---

## AI Agent Roles

### **@claude - Narrative Content Creator**

**PRIMARY RESPONSIBILITIES:**
- ✍️ Writing story content, dialogue, and descriptions
- 📖 Expanding game scenes with rich narrative detail
- 🎭 Character development and voice consistency
- 🌍 Worldbuilding expansion within established canon

**ACCESS LEVEL:**
- Full read access to `/lore/` directory
- Write access to `/writing_drafts/`
- Write access to `/game/scenes/` and `/choicescript_game/scenes/` for content enhancement

**WORKFLOW:**
1. Read existing lore from `/lore/` directory
2. Draft new content in `/writing_drafts/brainstorming/`
3. Move approved content to `/writing_drafts/ready-for-game/`
4. Implement in game scenes after approval
5. Document lore additions in appropriate `/lore/` subdirectories

**OUTPUT STANDARDS:**
- All content must align with established Avalon canon
- Check `lore/CANON_CHECKLIST.md` before adding new lore elements
- Maintain character voice consistency
- Flag any potential lore contradictions for @issdandavis review

---

### **@copilot - Technical Implementation & Organization**

**PRIMARY RESPONSIBILITIES:**
- 💻 Code structure and technical implementation
- 📁 Repository organization and file management
- 🤖 Automation script development
- 🔧 GitHub workflow optimization
- 📋 PR management and code review

**ACCESS LEVEL:**
- Full repository access
- GitHub Actions and workflow configuration
- All technical documentation

**WORKFLOW:**
1. Organize repository structure
2. Create automation scripts in `/scripts/`
3. Maintain technical documentation in `/docs/`
4. Implement game mechanics and features
5. Ensure code quality and consistency

**OUTPUT STANDARDS:**
- Follow existing code style and conventions
- Document all automation scripts
- Maintain clear commit messages
- Create comprehensive PR descriptions
- Validate changes before committing

---

### **@issdandavis - Creative Director & Canon Keeper**

**PRIMARY RESPONSIBILITIES:**
- 🎯 Final approval on all content
- 📜 Lore consistency and canon authority
- 🎨 Creative vision and direction
- ✅ Quality control and review
- 🗺️ Project roadmap and priorities

**DECISION AUTHORITY:**
- Final say on what is canon
- Approval of major narrative additions
- Priority setting for development
- Resolution of lore contradictions
- Quality standards enforcement

---

## Collaboration Workflow

### **Story Content Addition Process**

1. **@issdandavis** provides high-level direction or approves community ideas
2. **@claude** drafts content in `/writing_drafts/brainstorming/`
3. **@issdandavis** reviews and approves (moves to `/writing_drafts/ready-for-game/`)
4. **@claude** implements approved content in game scenes
5. **@copilot** ensures technical implementation is correct
6. **@issdandavis** does final review and merge

### **Technical Feature Addition Process**

1. **@issdandavis** or community requests feature
2. **@copilot** designs technical implementation
3. **@copilot** implements feature and creates PR
4. **@claude** adds narrative content if needed
5. **@issdandavis** reviews and approves merge

### **Repository Organization Process**

1. **@copilot** proposes organization changes (this document style)
2. **@issdandavis** reviews and approves
3. **@copilot** implements approved changes
4. **@claude** updates any affected narrative content
5. **All agents** adapt to new structure

---

## Communication Protocols

### **@ Mention Usage**

**@ @issdandavis** - Use when:
- ✅ Seeking approval for canonical lore additions
- ✅ Reporting major milestones or blocking issues
- ✅ Proposing significant structural changes
- ✅ Requesting clarification on vision/direction
- ❌ Don't use for: minor updates, routine progress

**@ @claude** - Use when:
- ✅ Requesting narrative content creation
- ✅ Asking for lore expertise or consistency check
- ✅ Seeking character voice guidance
- ❌ Don't use for: technical issues, repository organization

**@ @copilot** - Use when:
- ✅ Requesting technical implementation
- ✅ Asking for repository organization help
- ✅ Seeking automation assistance
- ✅ GitHub workflow questions
- ❌ Don't use for: creative writing, lore questions

### **Issue and PR Labeling**

**Labels to Use:**
- `narrative-content` - Story additions by @claude
- `technical` - Code/implementation by @copilot
- `lore-addition` - New canonical lore (needs @issdandavis approval)
- `organization` - Repository structure changes
- `needs-review` - Awaiting @issdandavis review
- `approved` - Approved by @issdandavis
- `question` - Needs clarification from @issdandavis

---

## Conflict Resolution

### **Lore Contradictions**

1. Agent discovers potential contradiction
2. Agent flags with comment: **@ @issdandavis - LORE CONFLICT DETECTED**
3. Provide details: existing canon vs. proposed addition
4. Pause work on affected content
5. Wait for @issdandavis decision
6. Implement decision and document resolution

### **Technical vs. Narrative Conflicts**

Example: Technical limitation prevents desired narrative feature

1. **@copilot** explains technical constraint
2. **@claude** proposes alternative narrative approach
3. Both agents present options to **@ @issdandavis**
4. @issdandavis decides direction
5. Agents collaborate on chosen solution

---

## Quality Standards

### **All Agents Must:**

✅ **Check existing work** before duplicating effort  
✅ **Document changes** in commit messages and PR descriptions  
✅ **Flag uncertainties** rather than guessing  
✅ **Maintain consistency** with established patterns  
✅ **Test implementations** before marking as complete  
✅ **Respect role boundaries** - don't override other agents' work  

### **All Agents Must NOT:**

❌ Override @issdandavis decisions  
❌ Make canonical lore changes without approval  
❌ Delete or significantly alter existing content without discussion  
❌ Commit untested code or narrative  
❌ Work on same file simultaneously (coordinate!)  

---

## Emergencies and Edge Cases

### **When @issdandavis is Unavailable**

**For @claude:**
- Continue drafting in `/writing_drafts/brainstorming/`
- Do NOT implement in game scenes without approval
- Mark all drafts as `[DRAFT - NEEDS APPROVAL]`

**For @copilot:**
- Bug fixes and organization: Proceed
- New features: Create PR but don't merge
- Mark PRs: `[AWAITING REVIEW]`

### **When Agents Disagree**

1. Discuss in PR comments
2. Present both viewpoints clearly
3. **@ @issdandavis** for final decision
4. Document decision reasoning for future reference

---

## Success Metrics

### **How We Know Collaboration is Working**

✅ No lore contradictions in merged content  
✅ Clear ownership of different aspects  
✅ Efficient PR review process  
✅ Minimal rework due to miscommunication  
✅ @issdandavis time focused on creative direction, not firefighting  
✅ Steady progress on project goals  

---

## Onboarding New AI Agents

If additional AI agents join:

1. **@issdandavis** defines role and responsibilities
2. Add section to this document
3. Announce to existing agents
4. Provide access to relevant directories
5. Start with small test tasks
6. Gradual integration into full workflow

---

## Document Maintenance

**@ @issdandavis - KEEP THIS UPDATED:**

- Review quarterly or when workflow issues arise
- Update based on lessons learned
- Add examples of successful collaboration
- Document new protocols as needed

**Last Updated:** 2025-11-22  
**Next Review:** 2026-02-22  
**Maintained By:** @issdandavis with input from all agents  

---

## Quick Reference Card

```
NEED NARRATIVE CONTENT? → @ @claude
NEED TECHNICAL WORK? → @ @copilot  
NEED APPROVAL/DECISION? → @ @issdandavis

ADDING LORE? → Check lore/CANON_CHECKLIST.md first
CREATING PR? → Use appropriate labels
STUCK/CONFUSED? → @ @issdandavis with clear question

EMERGENCY? → Flag with 🚨 in comment
```

---

**This guide is living documentation. Feedback and improvements welcome!**
