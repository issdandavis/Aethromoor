# SAML SSO Quick Reference Card

## 🚀 Quick Start

### 1. Configure Identity Provider
Add these to your IdP:
- **Entity ID**: `avalon-agent-explorer`
- **ACS URL**: `https://github.com/issdandavis/Avalon/agent/saml/acs`
- **Attributes**: userId, email, displayName, groups

### 2. Update Configuration
Edit `.github/agents/saml-config.json`:
```json
"identityProvider": {
  "entityId": "your-idp-entity-id",
  "singleSignOnService": { "url": "your-sso-url" },
  "x509Certificate": "your-certificate"
}
```

### 3. Set Environment Variables
Copy `config/.env.example` to `config/.env` and fill:
```bash
IDP_ENTITY_ID=https://your-idp.com/entity-id
IDP_SSO_URL=https://your-idp.com/sso
IDP_SLO_URL=https://your-idp.com/slo
IDP_CERTIFICATE=your-x509-certificate
```

### 4. Test
```bash
node .github/agents/test-saml.js
```

## 📋 Usage

### Basic Authentication
```javascript
const AuthenticatedExplorer = require('./.github/agents/explorer');

const explorer = new AuthenticatedExplorer();
await explorer.authenticate();

// Use exploration functions
const content = await explorer.readFile('./lore/file.txt');
const results = await explorer.searchFiles('./lore', 'Polly');
const metadata = await explorer.curateLore('./lore');

explorer.logout();
```

### Manual SAML Flow
```javascript
const SAMLAuthenticator = require('./.github/agents/saml-auth');

const auth = new SAMLAuthenticator();
const loginUrl = auth.initiateLogin();
// Redirect to loginUrl...

// After IdP callback
const attrs = auth.validateAssertion(samlResponse);
const sessionId = auth.createSession(attrs);
auth.authorizeOperation(sessionId, 'file.view');
```

## 🔐 Protected Operations

| Operation | Admin | Curator | Viewer |
|-----------|-------|---------|--------|
| repository.read | ✅ | ✅ | ✅ |
| repository.explore | ✅ | ✅ | ✅ |
| file.view | ✅ | ✅ | ✅ |
| file.search | ✅ | ✅ | ✅ |
| lore.curate | ✅ | ✅ | ❌ |
| lore.organize | ✅ | ✅ | ❌ |
| All operations | ✅ | ❌ | ❌ |

## 🛠️ Configuration Options

### Session Settings
```json
"session": {
  "duration": 3600,          // 1 hour
  "refreshEnabled": true,
  "refreshThreshold": 300    // Refresh 5 min before expiry
}
```

### Security Settings
```json
"security": {
  "authnRequestsSigned": true,
  "wantAssertionsSigned": true,
  "signatureAlgorithm": "rsa-sha256",
  "digestAlgorithm": "sha256"
}
```

### Role Permissions
```json
"roleBasedAccess": {
  "admin": ["*"],
  "curator": ["repository.read", "file.view", "lore.curate"],
  "viewer": ["repository.read", "file.view"]
}
```

## 🔍 Troubleshooting

### Authentication Fails
1. Verify IdP URL in config
2. Check SP entity ID matches IdP
3. Validate certificate format
4. Test network connectivity

### Session Expired
1. Increase session duration
2. Enable auto-refresh
3. Check system clock sync

### Authorization Denied
1. Verify user groups from IdP
2. Check role definitions
3. Confirm operation permissions
4. Review audit logs

## 📚 Documentation

- **Setup Guide**: `.github/agents/SAML_SETUP.md`
- **Implementation**: `.github/agents/IMPLEMENTATION_SUMMARY.md`
- **Agent Config**: `.github/agents/my-agent.agent.md`

## 🧪 Testing

Run automated tests:
```bash
node .github/agents/test-saml.js
```

Expected output: `8/8 tests passing`

## 🌐 Supported IdPs

✅ Okta | ✅ Azure AD | ✅ Auth0 | ✅ OneLogin
✅ Google Workspace | ✅ ADFS | ✅ Shibboleth

## 📞 Support

Check SAML_SETUP.md for detailed troubleshooting and configuration guides.
