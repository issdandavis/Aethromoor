# GitHub Copilot Setup Guide for Avalon Repository

## About This Guide

This guide helps you access and use GitHub Copilot features, including Copilot Spark, with the Avalon repository.

---

## Understanding GitHub Copilot Spark

**GitHub Copilot Spark** is a conversational AI feature available to GitHub Copilot subscribers. It provides an interactive chat experience for coding assistance.

### How to Access Copilot Spark

Copilot Spark is accessed through your GitHub account settings, NOT through individual repositories.

#### Step 1: Verify Your Subscription
1. Go to [https://github.com/settings/copilot](https://github.com/settings/copilot)
2. Confirm you have an active Copilot subscription
3. Check that your subscription includes Copilot Chat features

#### Step 2: Enable Features
1. Visit [https://github.com/settings/copilot/features](https://github.com/settings/copilot/features)
2. Review available features for your subscription tier
3. Enable any features that are available to you

#### Step 3: Access Copilot Spark

**In VS Code:**
- Install the "GitHub Copilot Chat" extension
- Press `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Shift+I` (Mac) to open Copilot Chat
- Or click the chat icon in the activity bar

**On GitHub.com:**
- Look for the Copilot icon in the top navigation bar
- Click to start a conversation
- Use it to ask questions about repositories, code, and more

**In GitHub Mobile:**
- Open the GitHub app
- Tap the Copilot icon
- Start a conversation

---

## Using Copilot with Avalon Repository

This repository is already configured for optimal Copilot assistance!

### Repository-Specific Instructions

The Avalon repository includes custom Copilot instructions:
- **`.github/COPILOT_INSTRUCTIONS.md`** - Detailed instructions for game development
- **`.github/copilot-instructions.md`** - Repository-wide coding guidelines
- **`.github/agents/my-agent.agent.md`** - Custom "Avalon Lore Steward" agent

### Custom Agent: Avalon Lore Steward

A custom agent is configured to help with:
- Organizing files and labels for easy collaboration
- Expanding lore and story elements
- Keeping narrative canon safe and well-categorized

To use the custom agent (requires Copilot access):
- Mention `@Avalon Lore Steward` in Copilot Chat
- Ask questions about lore, story structure, or file organization

---

## Troubleshooting

### "I can't see Copilot features"

**Possible causes:**
1. **Subscription not active**: Check [billing settings](https://github.com/settings/billing)
2. **Extensions not installed**: Install GitHub Copilot extensions in your IDE
3. **Feature not available in your tier**: Some features require specific subscription levels
4. **Organization restrictions**: Your organization may have disabled certain features

### "I paid but can't access Spark"

**Steps to resolve:**
1. Verify payment processed: [https://github.com/settings/billing](https://github.com/settings/billing)
2. Check subscription tier: Different tiers have different features
3. Restart your IDE after subscribing
4. Clear cache and reload extensions

### "Features page shows nothing"

This might mean:
- Your subscription doesn't include advanced features yet
- Features are rolling out gradually to users
- Your account needs verification

**Contact GitHub Support:**
- [https://support.github.com](https://support.github.com)
- Navigate to: Support → Copilot → Billing/Access Issues

---

## Available Copilot Features (as of November 2024)

### Included in Most Subscriptions:
- ✅ **Code Completions** - Inline suggestions as you type
- ✅ **Copilot Chat** - Conversational AI in your IDE
- ✅ **Code Explanations** - Ask Copilot to explain code
- ✅ **Code Generation** - Generate code from natural language
- ✅ **Test Generation** - Create tests automatically
- ✅ **Bug Fixes** - Get suggestions for fixing errors

### May Require Specific Tiers:
- 🔹 **Copilot Enterprise** features
- 🔹 **Custom Models** (organization feature)
- 🔹 **Advanced Context** (workspace indexing)
- 🔹 **Voice** capabilities (experimental)

---

## IDE Setup Instructions

### Visual Studio Code
1. Install extensions:
   - GitHub Copilot
   - GitHub Copilot Chat
2. Sign in with your GitHub account
3. Verify connection: Look for Copilot icon in status bar
4. Open chat: `Ctrl+Shift+I` / `Cmd+Shift+I`

### JetBrains IDEs (IntelliJ, PyCharm, etc.)
1. Go to Settings → Plugins
2. Search for "GitHub Copilot"
3. Install and restart IDE
4. Sign in when prompted
5. Open Copilot Chat from Tools menu

### Visual Studio
1. Go to Extensions → Manage Extensions
2. Search for "GitHub Copilot"
3. Install both Copilot and Copilot Chat
4. Restart Visual Studio
5. Sign in with GitHub account

### Neovim/Other Editors
- Check GitHub Copilot documentation for your specific editor
- Most modern editors have Copilot plugins available

---

## Getting the Most from Copilot in Avalon

### Best Practices for This Repository

1. **Reference the instructions**: Copilot can read `.github/COPILOT_INSTRUCTIONS.md` automatically
2. **Use specific prompts**: "Convert this HTML game scene to ChoiceScript format"
3. **Ask about lore**: "What are the rules of the Singing Dunes?"
4. **Request consistency checks**: "Does this match Polly's character voice?"
5. **Generate content**: "Expand this scene with more environmental description"

### Example Prompts

```
"Help me convert the singing_dunes HTML scene to ChoiceScript"
"Explain the relationship between Izack and Polly"
"Generate a new ending scene that follows the style guide"
"Check if this stat progression makes sense"
"What's the current development priority according to the roadmap?"
```

---

## Still Having Issues?

### Repository-Specific Questions
- Open an issue in this repository
- Check `docs/` folder for additional guides
- Read `START_HERE.md` for project orientation

### GitHub Copilot Access Issues
- **GitHub Support**: [https://support.github.com](https://support.github.com)
- **Copilot Documentation**: [https://docs.github.com/copilot](https://docs.github.com/copilot)
- **Community Forum**: [https://github.community](https://github.community)

### Billing Questions
- **Manage Subscription**: [https://github.com/settings/billing](https://github.com/settings/billing)
- **Upgrade/Downgrade**: [https://github.com/settings/copilot](https://github.com/settings/copilot)

---

## Important Notes

⚠️ **Copilot Spark vs Repository Features**
- Copilot Spark is a GitHub account-level feature
- This repository's Copilot configuration enhances what Copilot knows about the project
- Both work together but are configured separately

✨ **This Repository is Copilot-Ready**
- Custom instructions are already configured
- No additional repository setup needed
- Just ensure your personal Copilot subscription is active

---

**Last Updated**: November 24, 2024
**For Issues**: Contact GitHub Support for account/billing questions
**For Code Help**: Use the configured Copilot instructions in this repo
