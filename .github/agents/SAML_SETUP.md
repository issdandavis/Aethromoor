# SAML Single Sign-On Setup Guide

This guide explains how to configure and use SAML 2.0 Single Sign-On authentication for the Avalon Lore Steward agent's exploration functions.

## Overview

The Avalon agent now supports SAML 2.0 SSO for secure authentication when performing exploration operations such as:
- Reading repository files
- Searching through content
- Curating and organizing lore
- Managing file structures

## Architecture

### Components

1. **Service Provider (SP)**: The Avalon agent acts as the SAML service provider
2. **Identity Provider (IdP)**: Your organization's SSO system (Okta, Azure AD, Auth0, etc.)
3. **SAML Authenticator**: Handles SAML protocol operations (`saml-auth.js`)
4. **Authenticated Explorer**: Wraps exploration functions with authentication (`explorer.js`)
5. **Configuration**: SAML settings and permissions (`saml-config.json`)

### Authentication Flow

```
1. Agent initiates exploration operation
   ↓
2. Checks for active session
   ↓
3. If no session, redirects to IdP login
   ↓
4. User authenticates with IdP
   ↓
5. IdP sends SAML assertion back to SP
   ↓
6. SP validates assertion and creates session
   ↓
7. Agent performs authorized operation
   ↓
8. Session automatically refreshes if needed
```

## Configuration

### Step 1: Identity Provider Setup

Configure your IdP to recognize the Avalon agent as a service provider:

**Entity ID**: `avalon-agent-explorer`

**Assertion Consumer Service (ACS) URL**: 
```
https://github.com/issdandavis/Avalon/agent/saml/acs
```

**Single Logout Service (SLO) URL**:
```
https://github.com/issdandavis/Avalon/agent/saml/slo
```

**Attribute Mappings**:
- `userId` → User's unique identifier
- `email` → User's email address
- `displayName` → User's full name
- `groups` → User's role/group memberships

### Step 2: Update Configuration File

Edit `.github/agents/saml-config.json` and replace the placeholder values:

```json
{
  "saml": {
    "identityProvider": {
      "entityId": "https://your-idp.com/entity-id",
      "singleSignOnService": {
        "url": "https://your-idp.com/sso"
      },
      "singleLogoutService": {
        "url": "https://your-idp.com/slo"
      },
      "x509Certificate": "YOUR_IDP_CERTIFICATE_HERE"
    }
  }
}
```

### Step 3: Configure Permissions

Customize role-based access in `saml-config.json`:

```json
{
  "saml": {
    "permissions": {
      "roleBasedAccess": {
        "admin": ["*"],
        "curator": [
          "repository.read",
          "file.view",
          "file.search",
          "lore.curate",
          "lore.organize"
        ],
        "viewer": [
          "repository.read",
          "file.view",
          "file.search"
        ]
      }
    }
  }
}
```

## Usage

### Basic Usage

```javascript
const AuthenticatedExplorer = require('./.github/agents/explorer');

async function main() {
  const explorer = new AuthenticatedExplorer();
  
  try {
    // Authenticate
    await explorer.authenticate();
    
    // Perform operations
    const loreFile = await explorer.readFile('./lore/IZACK_MASTER_CHRONICLE_UPDATED.txt');
    console.log('Successfully read lore file');
    
    // Search for content
    const results = await explorer.searchFiles('./lore', 'Polly');
    console.log(`Found ${results.length} files mentioning Polly`);
    
    // Curate lore
    const metadata = await explorer.curateLore('./lore');
    console.log('Lore curation complete:', metadata);
    
  } finally {
    // Always logout when done
    explorer.logout();
  }
}

main().catch(console.error);
```

### Advanced: Manual Session Management

```javascript
const SAMLAuthenticator = require('./.github/agents/saml-auth');

const auth = new SAMLAuthenticator('./saml-config.json');

// Get login URL
const loginUrl = auth.initiateLogin();
console.log('Redirect user to:', loginUrl);

// After IdP callback with SAML response
const samlResponse = req.body.SAMLResponse; // From IdP callback
const userAttributes = auth.validateAssertion(samlResponse);

// Create session
const sessionId = auth.createSession(userAttributes);

// Check permissions for specific operation
try {
  auth.authorizeOperation(sessionId, 'lore.curate');
  // Operation authorized, proceed
} catch (error) {
  // Operation not authorized
  console.error(error.message);
}

// Logout
auth.logout(sessionId);
```

## Security Considerations

### Required Security Features

1. **Signed Assertions**: All SAML assertions must be digitally signed
2. **Encrypted Attributes**: Sensitive attributes should be encrypted
3. **Certificate Validation**: IdP certificates must be validated
4. **Session Timeout**: Sessions expire after configured duration
5. **HTTPS Only**: All SAML endpoints must use HTTPS

### Best Practices

- **Rotate Certificates**: Update IdP certificates before expiration
- **Monitor Sessions**: Track active sessions and unusual activity
- **Audit Logs**: Log all authentication and authorization events
- **Principle of Least Privilege**: Grant minimum required permissions
- **Regular Reviews**: Periodically review user roles and access

## Supported Identity Providers

This implementation follows SAML 2.0 standards and works with:

- **Okta**: Enterprise identity management
- **Azure AD**: Microsoft Azure Active Directory
- **Auth0**: Developer-friendly authentication platform
- **OneLogin**: Cloud-based identity provider
- **Google Workspace**: G Suite SAML integration
- **ADFS**: Active Directory Federation Services
- **Shibboleth**: Open-source IdP solution

## Troubleshooting

### Authentication Fails

**Symptom**: Cannot authenticate with IdP

**Solutions**:
1. Verify IdP URL is correct in config
2. Check that SP entity ID matches IdP configuration
3. Ensure IdP certificate is valid and not expired
4. Verify network connectivity to IdP

### Session Expired

**Symptom**: Session expires too quickly

**Solutions**:
1. Increase session duration in config:
   ```json
   "session": {
     "duration": 7200  // 2 hours
   }
   ```
2. Enable automatic refresh:
   ```json
   "session": {
     "refreshEnabled": true,
     "refreshThreshold": 600  // Refresh 10 min before expiry
   }
   ```

### Authorization Denied

**Symptom**: User authenticated but cannot perform operations

**Solutions**:
1. Verify user groups are correctly mapped from IdP
2. Check that user's role is defined in `roleBasedAccess`
3. Ensure required operation is listed in role's permissions
4. Confirm IdP sends group attributes in assertion

### Certificate Errors

**Symptom**: Signature verification fails

**Solutions**:
1. Obtain current certificate from IdP metadata
2. Remove line breaks and headers from certificate
3. Update certificate in config as single line
4. Verify certificate format (PEM without headers)

## Testing

### Test Authentication Flow

```bash
# Install dependencies
npm install

# Run test authentication
node test-saml-auth.js
```

### Test Script

Create `test-saml-auth.js`:

```javascript
const AuthenticatedExplorer = require('./.github/agents/explorer');

async function test() {
  console.log('Testing SAML authentication...');
  
  const explorer = new AuthenticatedExplorer();
  
  // Test authentication
  const authenticated = await explorer.authenticate();
  console.log('Authentication:', authenticated ? 'SUCCESS' : 'FAILED');
  
  if (authenticated) {
    // Test file operations
    try {
      const results = await explorer.searchFiles('./lore', 'test');
      console.log('Search test: SUCCESS');
    } catch (error) {
      console.log('Search test: FAILED -', error.message);
    }
    
    explorer.logout();
  }
}

test().catch(console.error);
```

## Support

For issues with SAML configuration:

1. Check IdP documentation for SAML setup
2. Verify all configuration values are correct
3. Review authentication logs for error details
4. Test with SAML debugging tools (SAML-tracer, etc.)

## References

- [SAML 2.0 Specification](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html)
- [OASIS SAML Standards](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=security)
- [GitHub Custom Agents](https://gh.io/customagents)
