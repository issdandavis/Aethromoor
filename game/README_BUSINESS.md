# Polly's Wingscroll: HTML Game Version - Business Documentation

## 📋 Overview

**Polly's Wingscroll: The First Thread** is a professional, choice-based interactive narrative game designed for commercial publication through Hosted Games (Choice of Games LLC).

### Quick Facts
- **Version:** 1.0.0
- **Word Count:** 40,000+ words
- **Playtime:** 45-90 minutes
- **Unique Endings:** 14
- **Platform:** Web Browser (HTML5/JavaScript)
- **License:** Commercial - All Rights Reserved

## 🎮 Playing the Game

Simply open `index.html` in any modern web browser. No installation or build process required.

**Supported Browsers:**
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📁 Project Structure

```
game/
├── index.html          - Main game file (open this to play)
├── game.js             - Game logic and story content
├── style.css           - Visual styling
├── tracing.js          - Analytics and event tracking
├── config.json         - Business configuration
├── LICENSE.txt         - Commercial license terms
└── README_BUSINESS.md  - This file
```

## ⚙️ Configuration

### Business Settings

Edit `config.json` to configure:

**Game Settings:**
- Version number
- Author information
- Publisher details
- Word count and metadata

**Feature Flags:**
- Auto-save (currently enabled)
- Analytics (currently disabled for privacy)
- Debug mode (disabled in production)

**Analytics:**
```json
"analytics": {
  "enabled": false,
  "provider": "none",
  "trackingId": ""
}
```

To enable analytics:
1. Set `"enabled": true`
2. Choose provider ("google-analytics", "mixpanel", etc.)
3. Add your tracking ID
4. Update `tracing.js` with integration code

### Code Configuration

Edit constants in `game.js`:
```javascript
const GAME_CONFIG = {
    version: '1.0.0',
    enableAnalytics: false,
    enableAutoSave: true
};
```

## 🔒 Security & Privacy

### Data Storage
- **Local Only:** All save data stored in browser localStorage
- **No External Calls:** No data transmitted to external servers by default
- **Player Privacy:** Session data only tracked locally unless analytics enabled

### License Protection
- All rights reserved for commercial publication
- See `LICENSE.txt` for complete terms
- Beta testing requires authorization

## 📊 Analytics & Tracking

### Built-in Event Tracking

The game tracks these events (locally only):
- `init` - Game initialization
- `choice_made` - Player makes a choice
- `ending_reached` - Player reaches an ending
- `game_restarted` - Player starts new game
- `game_saved` - Auto-save triggered
- `error` - Any errors encountered

### Exporting Analytics Data

For beta testing or debugging, players can export their session data:
```javascript
// In browser console:
console.log(exportTrace());
// or
downloadTrace(); // Downloads JSON file
```

### Adding Analytics Service

To integrate Google Analytics, Mixpanel, or custom analytics:

1. Enable in `config.json`:
```json
"analytics": {
  "enabled": true,
  "provider": "google-analytics",
  "trackingId": "G-XXXXXXXXXX"
}
```

2. Add tracking script to `index.html`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
```

3. Update `sendToAnalytics()` in `tracing.js` with actual implementation

## 🚀 Deployment

### Production Checklist

Before deploying to production:

- [ ] Update version number in all files
- [ ] Set `debugMode: false` in config.json
- [ ] Configure analytics if desired
- [ ] Test auto-save functionality
- [ ] Test on all target browsers
- [ ] Verify all 14 endings are reachable
- [ ] Check mobile responsiveness
- [ ] Review error handling
- [ ] Update copyright year if needed

### Hosting Options

**Static Hosting (Recommended):**
- GitHub Pages
- Netlify
- Vercel
- AWS S3 + CloudFront
- Any static file host

**Requirements:**
- No server-side code needed
- Simple file upload
- HTTPS recommended
- CDN for performance (optional)

### SEO Optimization

The HTML file includes:
- Meta description
- Keywords
- Open Graph tags for social sharing
- Proper semantic HTML
- Mobile viewport settings

Update these in `index.html` before deployment.

## 🧪 Testing

### Manual Testing Checklist

- [ ] All 14 endings reachable
- [ ] Stats update correctly
- [ ] Choices persist correctly
- [ ] Auto-save works
- [ ] Restart function works
- [ ] UI responsive on mobile
- [ ] No console errors
- [ ] Browser compatibility

### Beta Testing

For Hosted Games submission, conduct public beta:
1. Deploy to public URL
2. Post on Choice of Games forum
3. Collect feedback for 2-4 weeks
4. Address bugs and issues
5. Update version number

## 📈 Business Metrics

### Target Metrics
- **Completion Rate:** Target >60% of players reaching an ending
- **Average Playtime:** 45-90 minutes
- **Replay Rate:** Target >30% restart rate (indicates engagement)
- **Error Rate:** Target <1% sessions with errors

### Tracking KPIs

With analytics enabled, track:
- Total plays
- Most/least popular choices
- Drop-off points
- Ending distribution
- Average session duration
- Device breakdown (mobile vs desktop)

## 🛠️ Maintenance

### Version Updates

When releasing updates:

1. Update version in:
   - `config.json`
   - `game.js` (GAME_CONFIG.version)
   - `index.html` (meta tag and display)

2. Document changes in changelog

3. Test save compatibility

4. Consider migration for saved games if needed

### Bug Fixes

Error tracking is built-in:
- Check browser console for errors
- Review trace data from beta testers
- Use `handleError()` function for graceful degradation

## 💼 Commercial Information

### Publication Path
1. Complete beta testing (2-4 weeks)
2. Submit to Hosted Games via email
3. Review process (2-6 weeks)
4. Publication (if approved)
5. Revenue share per Hosted Games terms

### Market Positioning
- **Genre:** Interactive Fiction, Fantasy
- **Target Audience:** IF fans, fantasy readers, choice game players
- **Comparable Titles:** Other Hosted Games, Choice of Games titles
- **Unique Selling Points:** Collaborative magic system, deep relationships, 14 endings

### Contact & Support
- **Project Owner:** [Configure in config.json]
- **Support Email:** [Configure in config.json]
- **Website:** [Configure in config.json]

## 📄 License

**Copyright © 2024 Polly's Wingscroll Project**  
All Rights Reserved

This is commercial software intended for publication through Hosted Games. See `LICENSE.txt` for complete terms.

---

## 🔗 Additional Resources

- **Main Repository README:** ../README.md
- **Submission Guide:** ../SUBMISSION_GUIDE.md
- **ChoiceScript Version:** ../choicescript_game/
- **Lore & Worldbuilding:** ../lore/
- **Choice of Games Forum:** https://forum.choiceofgames.com/

---

**Last Updated:** December 2024  
**Maintained by:** Polly's Wingscroll Project Team
