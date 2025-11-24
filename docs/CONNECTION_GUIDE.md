# Game Connection & Analytics Guide

This guide explains how to connect the Avalon game to external analytics services, webhooks, and automation platforms.

## Overview

The game now includes a lightweight tracing system that captures all player choices, stat changes, and endings. This data can be exported and connected to various services for analytics and automation.

## Current Connection Status

✅ **Implemented:**
- Client-side trace collection (`game/tracing.js`)
- Manual export via UI button
- Clipboard copy functionality
- JSON export format
- Session tracking

⏳ **Planned:**
- Webhook integration for automatic data submission
- Zapier connection workflows
- Real-time analytics dashboard
- A/B testing infrastructure

## Export Functionality

### How It Works

1. **Automatic Tracking**: The game automatically tracks:
   - Game initialization
   - Each scene/node displayed
   - Player choices and their effects
   - Stat changes (Collaboration, Relationships)
   - Endings reached
   - Game restarts

2. **Manual Export**: Players can click the "📊 Export Trace Data" button to:
   - Copy trace data to clipboard (primary method)
   - Download as JSON file (fallback)
   - Receive visual feedback on success

3. **Data Format**: Exported as JSON with structure:
   ```json
   {
     "sessionId": "unique-session-id",
     "startedAt": "2025-11-22T21:25:00.000Z",
     "events": [
       {
         "t": "2025-11-22T21:25:05.123Z",
         "type": "choice_made",
         "fromNode": "start",
         "choiceText": "Approach respectfully...",
         "effects": { "collaboration": 1, "izack": 1 },
         "updatedCollaboration": 1,
         "relationships": { "izack": 1, "aria": 0, "zara": 0 }
       }
     ]
   }
   ```

## Connecting to External Services

### Option 1: Zapier Integration (Recommended)

**Setup Steps:**
1. Create a Zapier webhook trigger
2. Modify `game/game.js` to send trace data to webhook URL
3. Configure Zapier actions (Google Sheets, Discord, Email, etc.)

**Example Code Addition:**
```javascript
// In game/game.js, add to export button onclick:
async function sendToZapier(traceData) {
    const webhookURL = 'YOUR_ZAPIER_WEBHOOK_URL';
    try {
        await fetch(webhookURL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: traceData
        });
        console.log('Data sent to Zapier');
    } catch (error) {
        console.error('Zapier send failed:', error);
    }
}
```

### Option 2: Google Analytics

**Setup Steps:**
1. Add Google Analytics tracking code to `game/index.html`
2. Use custom events for game actions
3. Track key metrics (choices, endings, playtime)

**Example Code:**
```javascript
// Track choice made
gtag('event', 'choice_made', {
    'event_category': 'gameplay',
    'event_label': choiceText,
    'value': collaborationDelta
});
```

### Option 3: Custom Webhook

**Setup Steps:**
1. Create a backend endpoint to receive trace data
2. Add webhook URL to game configuration
3. Implement automatic or manual submission

**Example Implementation:**
```javascript
// Add to game/game.js
async function submitTraceData(webhookURL, sessionData) {
    try {
        const response = await fetch(webhookURL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Session-ID': sessionData.sessionId
            },
            body: JSON.stringify(sessionData)
        });
        return response.ok;
    } catch (error) {
        console.error('Webhook submission failed:', error);
        return false;
    }
}
```

### Option 4: Local Storage Aggregation

For offline-first approach:
```javascript
// Save to localStorage
function saveTraceLocally() {
    const traces = JSON.parse(localStorage.getItem('avalon_traces') || '[]');
    traces.push(window.gameTrace);
    localStorage.setItem('avalon_traces', JSON.stringify(traces));
}

// Later, sync to server
function syncAllTraces(serverURL) {
    const traces = JSON.parse(localStorage.getItem('avalon_traces') || '[]');
    // Send to server...
    localStorage.removeItem('avalon_traces'); // Clear after sync
}
```

## Security Considerations

### API Keys & Secrets

**DO:**
- ✅ Store API keys in `config/.env` (gitignored)
- ✅ Use environment variables for sensitive data
- ✅ Rotate keys immediately if exposed
- ✅ Use server-side endpoints for authenticated requests

**DON'T:**
- ❌ Commit API keys to repository
- ❌ Store secrets in client-side JavaScript
- ❌ Share webhook URLs publicly
- ❌ Include PII in trace data without consent

### Data Privacy

**Trace Data Contains:**
- Session ID (anonymous)
- Timestamps
- In-game choices
- Stat values
- Ending reached

**Does NOT Contain:**
- Player names
- Email addresses
- IP addresses (unless added by webhook)
- Personal information

## Analytics Use Cases

### 1. Choice Popularity Analysis
Track which choices are most/least popular:
```javascript
// Aggregate choice_made events by choiceText
const choiceFrequency = events
    .filter(e => e.type === 'choice_made')
    .reduce((acc, e) => {
        acc[e.choiceText] = (acc[e.choiceText] || 0) + 1;
        return acc;
    }, {});
```

### 2. Ending Distribution
See which endings players reach most often:
```javascript
const endingStats = events
    .filter(e => e.type === 'ending_reached')
    .reduce((acc, e) => {
        acc[e.ending] = (acc[e.ending] || 0) + 1;
        return acc;
    }, {});
```

### 3. Collaboration Score Progression
Analyze how collaboration scores change over time:
```javascript
const collabProgression = events
    .filter(e => e.type === 'choice_made')
    .map(e => ({
        time: e.t,
        score: e.updatedCollaboration
    }));
```

### 4. Session Duration
Calculate average playtime:
```javascript
function getSessionDuration(trace) {
    const start = new Date(trace.startedAt);
    const lastEvent = new Date(trace.events[trace.events.length - 1].t);
    return (lastEvent - start) / 1000 / 60; // minutes
}
```

## Future Enhancements

### Planned Features
- [ ] Real-time dashboard for live player statistics
- [ ] A/B testing framework for choice variations
- [ ] Heatmap visualization of popular paths
- [ ] Automatic anomaly detection (stuck players)
- [ ] Integration with ChoiceScript analytics
- [ ] Discord bot for community stats
- [ ] Achievement tracking across sessions

### Integration Ideas
- **Discord**: Post weekly stats to community channel
- **Google Sheets**: Automatic data aggregation
- **Email**: Send completion certificates
- **Twitter**: Auto-post milestone achievements
- **Notion**: Track playtester feedback
- **Airtable**: Bug reporting integration

## Troubleshooting

### Export Button Not Appearing
- Check browser console for JavaScript errors
- Verify `tracing.js` is loaded before `game.js`
- Wait 5 seconds after page load

### Clipboard Copy Fails
- Fallback download should trigger automatically
- Check browser permissions for clipboard access
- Try HTTPS instead of HTTP for clipboard API

### Invalid JSON Export
- Verify `window.exportTrace()` exists
- Check for circular references in game state
- Test in browser console: `JSON.parse(exportTrace())`

### Webhook Failures
- Check CORS headers on server
- Verify webhook URL is correct
- Test with curl or Postman first
- Check network tab in browser DevTools

## Resources

- [Zapier Webhook Documentation](https://zapier.com/page/webhooks/)
- [Google Analytics Events](https://developers.google.com/analytics/devguides/collection/gtagjs/events)
- [Choice of Games Analytics](https://www.choiceofgames.com/forum/)
- [Tracing.js Implementation](../game/tracing.js)

## Contact & Support

For integration questions:
1. Check [AUTOMATION_GUIDE.md](./AUTOMATION_GUIDE.md)
2. Review [TRACING.md](./TRACING.md)
3. Open a GitHub issue

---

*Last updated: November 2025*
*Version: 1.1 - Export button implementation*
