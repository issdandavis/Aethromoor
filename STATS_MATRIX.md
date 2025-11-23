# STATS_MATRIX.md
## Comprehensive Stat Tracking for Polly's Wingscroll

**Purpose:** Track all choice impacts on stats to ensure balanced progression  
**Last Updated:** November 23, 2025  
**Version:** 1.0 (Stage1 Initialization)

---

## 📊 Stat System Overview

### Core Stats
| Stat Name | Range | Purpose | Ending Impact |
|-----------|-------|---------|---------------|
| `collaboration` | 0-100 | Measures collaborative vs solo magic approach | Primary ending determinant |
| `izack_relationship` | 0-100 | Bond with mentor Izack | Affects available scenes & dialogue |
| `aria_relationship` | 0-100 | Bond with Aria Ravencrest | Glacier expedition depth |
| `zara_relationship` | 0-100 | Bond with chaos mage Zara | Optional content access |
| `polly_relationship` | 0-100 | Bond with Polly (narrator) | Commentary variations |

### Temporary Expedition Stats
| Stat Name | Type | Scene | Purpose |
|-----------|------|-------|---------|
| `truth_level` | temp | Singing Dunes | Tracks honesty choices |
| `kael_trust` | temp | Singing Dunes | Desert guide approval |
| `forest_attunement` | temp | Verdant Tithe | Connection to sentient forest |
| `ice_harmony` | temp | Rune Glacier | Partnership vs control approach |

### Artifact Flags
| Flag Name | Type | Acquisition | Ending Path |
|-----------|------|-------------|-------------|
| `artifact_earned` | string | Expedition completion | Determines ending eligibility |
| `sand_blessing` | boolean | Singing Dunes success | Truthbound Mage path |
| `oath_learned` | boolean | Dunes oath spirits | Truth magic knowledge |
| `glacier_partner` | boolean | Glacier harmony | Partnership ending |
| `heartwood_bound` | boolean | Forest deep path | Heartwood Guardian ending |

---

## 🎮 STAT CHANGES BY SCENE

### Startup & Character Creation

**File:** `startup.txt`

| Choice | Collaboration Δ | Relationships Δ | Notes |
|--------|-----------------|-----------------|-------|
| Approach: Collaborative | +10 | - | Sets initial tendency |
| Approach: Individual | -5 | - | Solo magic preference |
| Approach: Balanced | 0 | - | Neutral start |
| First meeting: Friendly | - | Izack +5 | Warm introduction |
| First meeting: Cautious | - | - | Neutral |
| First meeting: Skeptical | - | Izack -3 | Reserved |

---

### Arrival Scenes

**File:** `arrival.txt` (231 lines)

| Choice | Collaboration Δ | Relationships Δ | Notes |
|--------|-----------------|-----------------|-------|
| Arrival method: Portal (Izack) | - | Izack +5 | Chose his method |
| Arrival method: Carriage (Aria) | - | Aria +5 | Chose her method |
| Arrival method: Flight (Zara) | - | Zara +5 | Chose her method |
| First reaction: Wonder | +3 | - | Open to magic |
| First reaction: Analysis | -2 | - | Cautious approach |
| Accept Polly's help | - | Polly +5 | Trust narrator |
| Question Polly | - | Polly -2 | Skeptical |

---

### First Lesson (Dimensional Magic)

**File:** `first_lesson.txt` (289 lines)

| Choice | Collaboration Δ | Relationships Δ | Notes |
|--------|-----------------|-----------------|-------|
| Listen to Izack's guidance | +5 | Izack +3 | Collaborative learning |
| Try alone first | -3 | Izack -2 | Independent |
| Ask questions | +3 | Izack +5 | Engagement |
| Portal creation: Team approach | +10 | - | Core collaboration choice |
| Portal creation: Solo attempt | -5 | - | Self-reliance |
| Portal creation: Balanced | +3 | - | Measured approach |
| Share discovery with class | +5 | - | Generous |
| Keep insight private | -3 | - | Competitive |
| Magic feels: Natural connection | +5 | - | Attuned to collaboration |
| Magic feels: Force of will | -5 | - | Domination tendency |

**Scene Total Range:** -16 to +33 collaboration  
**Balance Assessment:** ✅ Multiple paths to success

---

### Singing Dunes Expedition

**File:** `singing_dunes.txt` (931 lines)

#### Initial Arrival & Kael Introduction

| Choice | Collaboration Δ | Relationships Δ | Temp Stats Δ | Notes |
|--------|-----------------|-----------------|--------------|-------|
| "I'm ready, nothing to hide" | +5 | - | kael_trust +1 | Bold honesty |
| "What if sand turns red?" | 0 | - | - | Cautious inquiry |
| "Can we observe first?" | -3 | - | kael_trust -1 | Avoidance |

#### First Truth Test

| Choice | Collaboration Δ | Relationships Δ | Temp Stats Δ | Notes |
|--------|-----------------|-----------------|--------------|-------|
| Share vulnerable truth | +8 | Polly +3 | truth_level +3 | Genuine vulnerability |
| Share safe truth | +3 | - | truth_level +1 | Cautious honesty |
| Avoid deep truth | -5 | - | truth_level -1 | Evasion |
| Lie to test | -10 | Polly -5 | truth_level -3 | Desert punishes |

#### Oath Spirit Encounter

| Choice | Collaboration Δ | Relationships Δ | Temp Stats Δ | Notes |
|--------|-----------------|-----------------|--------------|-------|
| Make collaborative oath | +10 | - | oath_learned = true | Learn oath magic |
| Make personal oath | +3 | - | - | Individual commitment |
| Observe spirits | 0 | - | - | Study without engaging |
| Refuse oath | -5 | - | kael_trust -2 | Miss learning opportunity |

#### Desert Final Truth

| Choice | Collaboration Δ | Relationships Δ | Temp Stats Δ | Artifact Impact |
|--------|-----------------|-----------------|--------------|-----------------|
| Embrace full truth | +15 | Kael +10 | truth_level +5 | Truth-Sworn Sand (if truth_level ≥ 5) |
| Partial honesty | +5 | - | truth_level +2 | Minor blessing |
| Withhold truth | -10 | Kael -5 | truth_level -2 | Desert rejection |

**Expedition Total Range:** -33 to +51 collaboration  
**Artifact Thresholds:**
- Truth-Sworn Sand: truth_level ≥ 5 AND collaboration ≥ 40
- Oath Knowledge: oath_learned = true
- Desert Blessing: truth_level ≥ 7

**Balance Assessment:** ✅ High variance rewards truth, penalties manageable

---

### Verdant Tithe Expedition

**File:** `verdant_tithe.txt` (183 lines) - ⚠️ NEEDS EXPANSION

#### Currently Implemented

| Choice | Collaboration Δ | Relationships Δ | Temp Stats Δ | Notes |
|--------|-----------------|-----------------|--------------|-------|
| Enter forest openly | +5 | - | forest_attunement +2 | Welcoming approach |
| Enter cautiously | 0 | - | - | Neutral |
| Thoughtvine: Share thoughts | +8 | - | forest_attunement +3 | Vulnerability |
| Thoughtvine: Guard thoughts | -3 | - | - | Resistance |
| Dreamwillow: Accept vision | +5 | - | - | Openness to future |
| Dreamwillow: Question vision | 0 | - | - | Analytical |

#### Missing Content (To Be Implemented)

| Expected Choice | Est. Collaboration Δ | Temp Stats Δ | Artifact Path |
|-----------------|---------------------|--------------|---------------|
| Thoughtvine deep merge | +15 | forest_attunement +5 | Thoughtvine Bond |
| Heartwood communion | +20 | forest_attunement +8 | Ancient Wisdom |
| Forest tithe payment | +10 | - | Forestbound status |
| Vision interpretation | Variable | - | Affects ending dialogue |

**Current Total Range:** -3 to +18 (INCOMPLETE)  
**Target Range:** -5 to +48 (after expansion)  
**Priority:** HIGH - Needs implementation for Heartwood Guardian ending

---

### Rune Glacier Expedition

**File:** `rune_glacier.txt` (1,266 lines)

#### Ice Awakening & Aria's Lesson

| Choice | Collaboration Δ | Relationships Δ | Temp Stats Δ | Notes |
|--------|-----------------|-----------------|--------------|-------|
| Listen to ice | +5 | Aria +3 | ice_harmony +2 | Partnership beginning |
| Command ice | -5 | Aria -2 | ice_harmony -2 | Domination approach |
| Study ice patterns | +2 | Aria +5 | - | Analytical learning |

#### Control vs Harmony Path (Major Branch)

| Choice | Collaboration Δ | Relationships Δ | Temp Stats Δ | Artifact Path |
|--------|-----------------|-----------------|--------------|---------------|
| CONTROL: Dominate ice | -10 | Aria -5 | ice_harmony -5 | Runeweaver's Mark |
| CONTROL: Master runes | -5 | - | ice_harmony -3 | Control success |
| HARMONY: Partner with ice | +15 | Aria +10 | ice_harmony +5 | Glacier Partnership |
| HARMONY: Co-create magic | +20 | Aria +8 | ice_harmony +8 | Deep partnership |

#### Spell Library Discovery

| Choice | Collaboration Δ | Relationships Δ | Temp Stats Δ | Notes |
|--------|-----------------|-----------------|--------------|-------|
| Study collaboratively | +8 | - | - | Team learning |
| Focus on personal power | -5 | - | - | Individual gain |
| Share knowledge | +10 | Aria +5 | - | Generosity |

#### Boundary Test

| Choice | Collaboration Δ | Relationships Δ | Temp Stats Δ | Notes |
|--------|-----------------|-----------------|--------------|-------|
| Respect ice's limits | +12 | Aria +8 | ice_harmony +4 | Partnership respect |
| Push boundaries safely | +5 | Aria +3 | - | Balanced exploration |
| Force beyond limits | -15 | Aria -10 | ice_harmony -6 | Dangerous domination |

**Expedition Total Range:** -50 to +70 collaboration  
**Artifact Thresholds:**
- Glacier Partnership: ice_harmony ≥ 10 AND collaboration ≥ 60
- Runeweaver's Mark: ice_harmony ≤ -5 AND successful control
- Harmony Bracelet: ice_harmony between -2 and +2 (balanced)

**Balance Assessment:** ✅ Strongest divergence, reflects major philosophical choice

---

## 🏆 ENDING REQUIREMENTS

### High Collaboration Endings

| Ending | Collaboration Min | Artifact Required | Relationship Reqs | Notes |
|--------|------------------|-------------------|------------------|-------|
| Collaborative Master | 80 | Glacier Partnership | - | Ultimate collaboration |
| Collaborative Scholar | 75 | - | - | Teaching path |
| Truthbound Mage | 70 | Truth-Sworn Sand | - | Honesty + collaboration |
| Glacier Partner | 60 | Glacier Partnership | - | Ice harmony |
| Forestbound Guardian | 60 | Dreamwillow/Thoughtvine | - | Forest connection |
| Heartwood Guardian | 65 | Ancient Wisdom | - | Deepest forest bond |

### Balanced Endings

| Ending | Collaboration Range | Artifact | Notes |
|--------|---------------------|----------|-------|
| Boundary Specialist | 50-74 | - | Middle path |
| Balanced Mage | 45-70 | Harmony Bracelet | True balance |
| Humble Seeker | 40-65 | Rune of Mystery | Wisdom through humility |

### Low Collaboration Endings

| Ending | Collaboration Max | Special Conditions | Notes |
|--------|------------------|-------------------|-------|
| Runeweaver | 55 | Runeweaver's Mark | Control mastery |
| Second Chance | 30-45 | Showed growth | Redemption arc |
| Humbled Student | 25-40 | Learned from failure | Character growth |
| Standard Path | 30-60 | No special artifacts | Default completion |
| Expelled | < 20 | Multiple failures | Failure ending |

---

## ⚖️ BALANCE ANALYSIS

### Collaboration Score Distribution

**Theoretical Ranges (all scenes):**
- Maximum possible: ~154 (taking all collaborative choices)
- Minimum possible: ~-89 (taking all solo/domination choices)
- Starting value: 50 (neutral)

**Practical Ranges:**
- Most collaborative playthrough: ~120-140
- Balanced playthrough: 45-75
- Most solo playthrough: 10-35

### Accessibility Assessment

| Ending Tier | Difficulty | Accessibility |
|-------------|-----------|---------------|
| Collaborative Master | Very Hard | Requires near-perfect collaborative choices |
| Heartwood Guardian | Hard | Needs Verdant expansion + high collab |
| Glacier Partner | Medium-Hard | Major harmony commitment |
| Truthbound Mage | Medium | Desert honesty focus |
| Forestbound Guardian | Medium | Forest path completion |
| Balanced Mage | Easy-Medium | Natural middle ground |
| Boundary Specialist | Easy | Default mid-range |
| Standard Path | Very Easy | Hard to miss |

### Balance Issues

✅ **Well-Balanced:**
- Multiple viable paths to endings
- Failure has narrative purpose
- Balanced choices are viable
- No "trap" choices

⚠️ **Needs Attention:**
- Verdant Tithe expansion needed for Heartwood Guardian accessibility
- Consider adding more mid-range artifact options
- Ensure Collaboration 40-60 range has compelling endings

---

## 🔄 Stat Balancing Guidelines

### When Adding New Choices

1. **Collaborative choices:** +3 to +15 (average +8)
2. **Solo/control choices:** -2 to -10 (average -5)
3. **Neutral/inquiry choices:** -2 to +3 (average 0)
4. **Major branch points:** ±10 to ±20
5. **Minor variations:** ±2 to ±5

### Relationship Stat Guidelines

- **Positive interactions:** +2 to +10
- **Following character's advice:** +3 to +5
- **Impressing character:** +5 to +10
- **Neutral interactions:** 0 to +2
- **Disappointing character:** -2 to -5
- **Opposing character's values:** -5 to -10

### Temporary Stat Thresholds

- **High achievement:** ≥ 8
- **Success:** ≥ 5
- **Adequate:** ≥ 3
- **Minimal:** ≥ 1
- **Failure:** < 0

---

## 📝 Update Protocol

### When Adding/Modifying Choices

1. **Document the choice** in this matrix
2. **List all stat changes** (permanent and temporary)
3. **Note artifact impacts** if any
4. **Calculate scene total range**
5. **Update ending accessibility** if thresholds change
6. **Cross-reference** with SCENE_PARITY_CHECKLIST.md
7. **Test** that ending logic still works

### Quality Checks

- [ ] No single choice swings > 25 collaboration points
- [ ] Scene has both positive and negative options
- [ ] Neutral paths exist for major choices
- [ ] Endings remain accessible through different paths
- [ ] Artifact acquisition feels earned
- [ ] Relationship changes feel realistic

---

## 🎯 Priority Updates Needed

### Immediate
1. **Complete Verdant Tithe stat mapping** after expansion
2. **Verify Heartwood Guardian** accessibility calculations
3. **Test edge cases** for ending triggers

### Short-term
1. Add more granular tracking for minor choices
2. Create stat flow diagram for visual reference
3. Document "optimal path" for each ending type

---

**Maintained by:** Quality Balancer role (Multi-AI Collaboration)  
**Update Frequency:** After any stat-affecting changes  
**Version:** 1.0 (Stage1 Initialization)  
**Next Review:** After Verdant Tithe expansion
