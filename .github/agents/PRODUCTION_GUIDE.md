# Production Implementation Guide

## ⚠️ Important Security Notice

The current SAML implementation includes **placeholder functions** for demonstration and testing purposes. These placeholders **MUST be replaced** with proper implementations before deploying to production.

## Placeholder Functions to Replace

### 1. Signature Verification (`saml-auth.js`)

**Current (Placeholder):**
```javascript
verifySignature(xml) {
  console.warn('WARNING: Using placeholder signature verification');
  return true; // Always returns true - INSECURE!
}
```

**Production Implementation:**
```javascript
verifySignature(xml) {
  const { SignedXml } = require('xml-crypto');
  const { DOMParser } = require('xmldom');
  
  try {
    // Parse XML
    const doc = new DOMParser().parseFromString(xml);
    const signature = doc.getElementsByTagNameNS('http://www.w3.org/2000/09/xmldsig#', 'Signature')[0];
    
    if (!signature) {
      throw new Error('No signature found in SAML response');
    }
    
    // Create SignedXml instance
    const sig = new SignedXml();
    sig.keyInfoProvider = {
      getKey: () => {
        // Return IdP's public key from certificate
        return this.config.identityProvider.x509Certificate;
      }
    };
    
    // Load and verify signature
    sig.loadSignature(signature);
    const isValid = sig.checkSignature(xml);
    
    if (!isValid) {
      console.error('Signature validation errors:', sig.validationErrors);
      throw new Error('Invalid SAML signature');
    }
    
    return true;
  } catch (error) {
    console.error('Signature verification failed:', error);
    throw error;
  }
}
```

### 2. Attribute Extraction (`saml-auth.js`)

**Current (Placeholder):**
```javascript
extractAttributes(xml) {
  console.warn('WARNING: Using placeholder attribute extraction');
  return {
    userId: 'placeholder-user-id',
    email: 'user@example.com',
    displayName: 'Agent User',
    groups: ['curator']
  };
}
```

**Production Implementation:**
```javascript
extractAttributes(xml) {
  const { DOMParser } = require('xmldom');
  const xpath = require('xpath');
  
  try {
    // Parse SAML response XML
    const doc = new DOMParser().parseFromString(xml);
    const select = xpath.useNamespaces({
      'saml': 'urn:oasis:names:tc:SAML:2.0:assertion',
      'samlp': 'urn:oasis:names:tc:SAML:2.0:protocol'
    });
    
    // Extract attributes from AttributeStatement
    const attributes = {};
    const attrNodes = select('//saml:AttributeStatement/saml:Attribute', doc);
    
    for (const attrNode of attrNodes) {
      const name = attrNode.getAttribute('Name');
      const values = select('.//saml:AttributeValue/text()', attrNode);
      
      if (values.length === 1) {
        attributes[name] = values[0].nodeValue;
      } else if (values.length > 1) {
        attributes[name] = values.map(v => v.nodeValue);
      }
    }
    
    // Map to application attributes based on config
    const mapping = this.config.attributes.mapping;
    const mappedAttributes = {};
    
    for (const [appAttr, samlAttr] of Object.entries(mapping)) {
      if (attributes[samlAttr]) {
        mappedAttributes[appAttr] = attributes[samlAttr];
      }
    }
    
    // Validate required attributes
    for (const required of this.config.attributes.required) {
      if (!mappedAttributes[required]) {
        throw new Error(`Required attribute ${required} not found in SAML assertion`);
      }
    }
    
    return mappedAttributes;
  } catch (error) {
    console.error('Attribute extraction failed:', error);
    throw error;
  }
}
```

### 3. Authentication Flow (`explorer.js`)

**Current (Placeholder):**
```javascript
async authenticate() {
  console.log('Initiating SAML authentication...');
  const loginUrl = this.auth.initiateLogin();
  
  // Using simulated IdP response for testing
  console.warn('WARNING: Using simulated IdP response');
  const mockSamlResponse = this.simulateIdPResponse();
  const userAttributes = this.auth.validateAssertion(mockSamlResponse);
  // ...
}
```

**Production Implementation:**

For a web application:
```javascript
// In your web server (Express example)
const express = require('express');
const app = express();

// Login endpoint
app.get('/agent/saml/login', (req, res) => {
  const auth = new SAMLAuthenticator();
  const loginUrl = auth.initiateLogin();
  
  // Redirect user to IdP
  res.redirect(loginUrl);
});

// Assertion Consumer Service (ACS) endpoint
app.post('/agent/saml/acs', express.urlencoded({ extended: true }), (req, res) => {
  const auth = new SAMLAuthenticator();
  
  try {
    // Get SAML response from IdP
    const samlResponse = req.body.SAMLResponse;
    
    // Validate assertion
    const userAttributes = auth.validateAssertion(samlResponse);
    
    // Create session
    const sessionId = auth.createSession(userAttributes);
    
    // Store session in cookie or session storage
    req.session.samlSessionId = sessionId;
    
    // Redirect to application
    res.redirect('/agent/explorer');
  } catch (error) {
    console.error('SAML authentication failed:', error);
    res.status(401).send('Authentication failed');
  }
});
```

For the explorer class:
```javascript
async authenticate() {
  if (!this.auth.config.permissions.requireAuthentication) {
    return true;
  }

  // Check if session exists (from cookie/storage)
  const sessionId = this.getSessionFromStorage();
  
  if (sessionId) {
    try {
      // Verify session is still valid
      this.auth.authorizeOperation(sessionId, 'repository.read');
      this.sessionId = sessionId;
      return true;
    } catch (error) {
      // Session invalid, need to re-authenticate
    }
  }
  
  // No valid session - initiate login
  const loginUrl = this.auth.initiateLogin();
  console.log('Please authenticate at:', loginUrl);
  
  // In a web context, redirect to login
  // In a CLI context, open browser or provide URL
  
  return false; // User needs to complete authentication
}
```

## Required Dependencies

Install these packages for production:

```bash
npm install xml-crypto xmldom xpath
```

### Package Descriptions

- **xml-crypto**: XML signature creation and verification
- **xmldom**: W3C DOM Level 2 compatible XML parser
- **xpath**: XPath query support for XML documents

## Additional Security Enhancements

### 1. Replay Attack Prevention

Track processed assertion IDs:

```javascript
class SAMLAuthenticator {
  constructor(configPath) {
    this.config = JSON.parse(fs.readFileSync(configPath, 'utf8')).saml;
    this.sessions = new Map();
    this.processedAssertions = new Set(); // Track assertion IDs
  }
  
  validateAssertion(samlResponse) {
    const decodedResponse = Buffer.from(samlResponse, 'base64').toString('utf8');
    
    // Extract assertion ID
    const assertionId = this.extractAssertionId(decodedResponse);
    
    // Check for replay
    if (this.processedAssertions.has(assertionId)) {
      throw new Error('Assertion replay detected');
    }
    
    // Verify signature
    if (!this.verifySignature(decodedResponse)) {
      throw new Error('Invalid signature');
    }
    
    // Extract and validate attributes
    const attributes = this.extractAttributes(decodedResponse);
    
    // Mark assertion as processed
    this.processedAssertions.add(assertionId);
    
    return attributes;
  }
  
  extractAssertionId(xml) {
    const doc = new DOMParser().parseFromString(xml);
    const assertion = doc.getElementsByTagNameNS(
      'urn:oasis:names:tc:SAML:2.0:assertion', 
      'Assertion'
    )[0];
    return assertion.getAttribute('ID');
  }
}
```

### 2. Timestamp Validation

Verify NotBefore and NotOnOrAfter:

```javascript
validateTimestamp(xml) {
  const { DOMParser } = require('xmldom');
  const doc = new DOMParser().parseFromString(xml);
  
  const conditions = doc.getElementsByTagNameNS(
    'urn:oasis:names:tc:SAML:2.0:assertion',
    'Conditions'
  )[0];
  
  if (!conditions) {
    throw new Error('No Conditions element in assertion');
  }
  
  const notBefore = new Date(conditions.getAttribute('NotBefore'));
  const notOnOrAfter = new Date(conditions.getAttribute('NotOnOrAfter'));
  const now = new Date();
  
  if (now < notBefore) {
    throw new Error('Assertion not yet valid');
  }
  
  if (now >= notOnOrAfter) {
    throw new Error('Assertion expired');
  }
  
  return true;
}
```

### 3. Certificate Validation

Verify IdP certificate hasn't expired:

```javascript
validateCertificate() {
  const { Certificate } = require('@fidm/x509');
  
  const cert = Certificate.fromPEM(
    '-----BEGIN CERTIFICATE-----\n' +
    this.config.identityProvider.x509Certificate +
    '\n-----END CERTIFICATE-----'
  );
  
  const now = new Date();
  
  if (now < cert.validFrom) {
    throw new Error('Certificate not yet valid');
  }
  
  if (now > cert.validTo) {
    throw new Error('Certificate expired');
  }
  
  console.log('Certificate valid until:', cert.validTo);
  return true;
}
```

## Testing Production Implementation

Create a test file `test-production-saml.js`:

```javascript
const SAMLAuthenticator = require('./.github/agents/saml-auth');
const fs = require('fs');

async function testProduction() {
  console.log('Testing production SAML implementation...\n');
  
  // Load real SAML response from IdP (captured during testing)
  const realSamlResponse = fs.readFileSync('./test-saml-response.xml', 'utf8');
  const base64Response = Buffer.from(realSamlResponse).toString('base64');
  
  const auth = new SAMLAuthenticator();
  
  try {
    // Test signature verification
    console.log('Testing signature verification...');
    const decoded = Buffer.from(base64Response, 'base64').toString('utf8');
    const sigValid = auth.verifySignature(decoded);
    console.log('Signature valid:', sigValid);
    
    // Test attribute extraction
    console.log('\nTesting attribute extraction...');
    const attrs = auth.extractAttributes(decoded);
    console.log('Extracted attributes:', attrs);
    
    // Test full validation
    console.log('\nTesting full assertion validation...');
    const userAttrs = auth.validateAssertion(base64Response);
    console.log('User attributes:', userAttrs);
    
    // Test session creation
    console.log('\nTesting session creation...');
    const sessionId = auth.createSession(userAttrs);
    console.log('Session created:', sessionId);
    
    console.log('\n✅ All production tests passed!');
  } catch (error) {
    console.error('\n❌ Production test failed:', error.message);
    console.error(error.stack);
  }
}

testProduction().catch(console.error);
```

## Deployment Checklist

Before deploying to production:

- [ ] All placeholder functions replaced with production implementations
- [ ] Dependencies installed (`xml-crypto`, `xmldom`, `xpath`)
- [ ] IdP certificate configured and validated
- [ ] SAML endpoints configured in IdP
- [ ] HTTPS enforced for all endpoints
- [ ] Replay attack prevention implemented
- [ ] Timestamp validation implemented
- [ ] Certificate expiration monitoring configured
- [ ] Error handling and logging configured
- [ ] Load testing completed
- [ ] Security audit performed
- [ ] Documentation updated

## Support

If you need help implementing the production SAML flow:

1. Review SAML 2.0 specification
2. Check your IdP's documentation
3. Use SAML debugging tools (SAML-tracer browser extension)
4. Test with SAML test IdPs (samltool.io, etc.)
5. Consult `xml-crypto` and `xmldom` documentation

## Resources

- [xml-crypto Documentation](https://github.com/node-saml/xml-crypto)
- [xmldom Documentation](https://github.com/xmldom/xmldom)
- [SAML 2.0 Specification](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html)
- [OASIS Security Standards](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=security)
