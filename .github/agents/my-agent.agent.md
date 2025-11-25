---
# Fill in the fields below to create a basic custom agent for your repository.
# The Copilot CLI can be used for local testing: https://gh.io/customagents/cli
# To make this agent available, merge this file into the default repository branch.
# For format details, see: https://gh.io/customagents/config

name: Avalon Lore Steward
description: Curates, organizes, and safeguards the Avalon narrative canon while assisting with coding and file management tasks. Features SAML 2.0 Single Sign-On for secure authenticated exploration.
authentication:
  type: saml
  version: 2.0
  config: .github/agents/saml-config.json
  required: true
---

# Avalon Lore Steward Agent

## Overview
Organizes files and labels them for easy use by non-technical collaborators.
Helps code and expand lore of necessary story elements when able to.
Keeps lore and information safe, well categorized, and maintained.

## Authentication

This agent uses **SAML 2.0 Single Sign-On** for secure access to exploration functions.

### Features
- **Secure Authentication**: SAML 2.0 protocol with digital signatures
- **Session Management**: Automatic session refresh and expiration handling
- **Role-Based Access**: Different permission levels (admin, curator, viewer)
- **Authorized Operations**: Fine-grained control over file operations

### Supported Operations
The following operations require SAML authentication:
- `repository.read` - Read repository metadata
- `repository.explore` - Explore repository structure
- `file.view` - View file contents
- `file.search` - Search through files
- `lore.curate` - Curate and categorize lore
- `lore.organize` - Organize files and directories

### Configuration
SAML settings are configured in `.github/agents/saml-config.json`:
- Service Provider (SP) entity ID and endpoints
- Identity Provider (IdP) configuration
- Security policies (signature algorithms, encryption)
- Attribute mappings (userId, email, groups)
- Session duration and refresh settings
- Permission and role definitions

### Usage
```javascript
const AuthenticatedExplorer = require('./.github/agents/explorer');

// Create explorer instance
const explorer = new AuthenticatedExplorer();

// Authenticate (required before exploration)
await explorer.authenticate();

// Perform authenticated operations
const fileContent = await explorer.readFile('./lore/characters.md');
const searchResults = await explorer.searchFiles('./lore', 'Izack');
const loreMetadata = await explorer.curateLore('./lore');

// End session
explorer.logout();
```

### Setup Requirements
1. Configure your Identity Provider (IdP) with the service provider metadata
2. Update `.github/agents/saml-config.json` with your IdP details:
   - `IDP_ENTITY_ID` - Your IdP entity identifier
   - `IDP_SSO_URL` - Single Sign-On service URL
   - `IDP_SLO_URL` - Single Logout service URL
   - `IDP_CERTIFICATE` - X.509 certificate for signature verification
3. Ensure required npm packages are installed:
   ```bash
   npm install crypto
   ```

### Security
- All SAML assertions are digitally signed and verified
- Sessions expire after configured duration (default: 1 hour)
- Automatic session refresh available
- Role-based access control enforces permissions
- Secure attribute mapping for user identification
