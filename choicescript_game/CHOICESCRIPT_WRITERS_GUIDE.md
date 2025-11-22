# 🎮 CHOICESCRIPT WRITER'S GUIDE FOR AVALON
## Integrating Lore with ChoiceScript Game Development

> **📖 USER GUIDE:** This guide bridges the lore documentation with ChoiceScript game writing
> - How to use the CHARACTER_COMPENDIUM and FACTION_GUIDE in your ChoiceScript scenes
> - ChoiceScript syntax examples for common Avalon scenarios
> - Best practices for maintaining canonical accuracy while writing interactive fiction

---

## 📑 TABLE OF CONTENTS

1. [**Quick Start for Writers**](#-quick-start-for-writers)
2. [**Using Lore Documents in ChoiceScript**](#-using-lore-documents-in-choicescript)
3. [**Character Implementation Guide**](#-character-implementation-guide)
4. [**Faction System in ChoiceScript**](#-faction-system-in-choicescript)
5. [**Code Examples**](#-code-examples)
6. [**Testing Your Scenes**](#-testing-your-scenes)

---

## 🚀 QUICK START FOR WRITERS

### **Your Workflow**

```
1. Read CHARACTER_COMPENDIUM.md → Understand canonical character traits
   ↓
2. Read FACTION_GUIDE.md → Know faction motivations and conflicts
   ↓
3. Write ChoiceScript scenes → Use this guide for syntax
   ↓
4. Test in ChoiceScript IDE → Validate your implementation
```

### **Essential Files for Reference**

Keep these open while writing:

| File | Use For |
|------|---------|
| **lore/CHARACTER_COMPENDIUM.md** | Character dialogue patterns, voice, relationships |
| **lore/FACTION_QUICK_REFERENCE.md** | Quick faction facts, combat styles, alliances |
| **lore/FACTION_GUIDE.md** | Deep faction lore, strategic doctrines |
| **This Guide** | ChoiceScript syntax for implementing lore |

---

## 📚 USING LORE DOCUMENTS IN CHOICESCRIPT

### **The Core Truth About Clay in ChoiceScript**

From CHARACTER_COMPENDIUM.md, we know: **"Clay was CREATED, not summoned."**

**How to Implement in ChoiceScript:**

```
*comment The Core Truth About Clay - magic responds to genuine need

*choice
    #I summon Clay to my side!
        *comment This is WRONG - violates canon
        *set collaboration -10
        *goto wrong_approach
        
    #Please... I don't want to be alone. [Create Clay]
        *comment This is CORRECT - matches canon
        *set collaboration +10
        *set clay_bond +5
        *goto clay_creation
```

### **Izack's Voice Pattern in ChoiceScript**

From CHARACTER_COMPENDIUM.md: Izack compounds words when nervous.

**Correct Implementation:**

```
*label izack_nervous
"That is—I mean—theoretically speaking—oh, bleeding stars!" Izack's words 
tumble over each other. "What I'm trying to say is: magic isn't about forcing 
reality to obey. It's about asking nicely and hoping reality says yes."

*choice
    #"Take your time, Professor."
        *set izack_relationship +5
        *goto patient_response
        
    #"Can you just get to the point?"
        *set izack_relationship -3
        *goto impatient_response
```

### **Aria's Diplomatic Approach**

From CHARACTER_COMPENDIUM.md: Aria handles social/political aspects.

**Implementation:**

```
*label aria_negotiation
*if (collaboration >= 60)
    Aria smiles warmly. "You understand that true power comes from partnership, 
    not domination. That's precisely what Avalon teaches."
    *set aria_relationship +10
*else
    Aria regards you carefully. "Collaborative magic isn't just a technique—it's 
    a philosophy. Are you willing to learn?"
    *set aria_relationship +3
```

---

## 👥 CHARACTER IMPLEMENTATION GUIDE

### **Izack Elion Thorne**

**Stats to Track:**

```
*create izack_relationship 0
*create learned_from_izack false
*create dimensional_understanding 0
```

**Dialogue Patterns:**

```
*comment NERVOUS IZACK - compounds words
"The thing is—well, not the thing exactly, but rather—oh, bleeding stars."

*comment TEACHING MODE - questions not lectures
"What if we approached this differently? What if magic isn't about power, but connection?"

*comment WITH ARIA - acknowledges her skill
"You always know what I mean to say, even when I don't say it right."

*comment GIFT-GIVING - impulsive and meaningful
*if (crisis_moment)
    Without thinking, Izack presses a crystalline token into your hand. 
    "Now you'll always have a piece of Avalon with you. This is real."
    *set received_izack_gift true
```

### **Clay Implementation**

**Remember: Clay was CREATED from genuine need**

```
*create clay_exists false
*create clay_bond 0

*label clay_creation_moment
*comment This is a pivotal canonical moment

You kneel by the sand, loneliness overwhelming you. Without conscious thought, 
your hands move. "Please," you whisper. "I don't want to be alone."

The sand shifts. A form takes shape—not summoned, not commanded, but *answered*.

"I am because someone needed me to be," the creature says softly.

*set clay_exists true
*set clay_bond 10
*set magic_philosophy "creation"
*achievement clay_friend unlocked "Created a friend from genuine need"
```

### **Polly's Sarcasm**

```
*label polly_commentary
*if (player_arrogant)
    *italic "Oh yes, because charging in blindly has worked *so* well for every 
    other student who thought they knew better than centuries of accumulated wisdom," 
    *italic Polly mutters.
*else
    *italic "Finally, someone who asks questions before making catastrophic mistakes," 
    *italic Polly says approvingly.
    *set polly_relationship +5
```

---

## ⚔️ FACTION SYSTEM IN CHOICESCRIPT

### **Tracking Faction Affinity**

```
*comment Based on FACTION_GUIDE.md

*create arcane_dominion_rep 0
*create mortal_confederations_rep 0
*create primordial_collective_rep 0

*comment Sub-faction tracking
*create sun_crown_affinity 0
*create twilight_scholars_affinity 0
*create human_kingdoms_affinity 0
*create demon_court_affinity 0
```

### **Faction Philosophy Choices**

**Sun-Crown Order (Traditionalist):**

```
*choice
    #"Magic should be perfected through centuries of study."
        *set sun_crown_affinity +10
        *set arcane_dominion_rep +5
        *goto traditionalist_path
        
    #"Magic should adapt to serve current needs."
        *set human_kingdoms_affinity +10
        *set mortal_confederations_rep +5
        *goto adaptive_path
```

### **Mal's Ethical Contract Scene**

From FACTION_GUIDE.md: Mal is learning ethical contracting.

```
*label mal_contract_lesson
"Most demons," Mal begins carefully, his young voice struggling with old concepts, 
"they make contracts that exploit. But what if... what if both parties genuinely benefited?"

*choice
    #"That's naive. Power is about leverage."
        Mal's face falls. "I suppose you're right..."
        *set demon_court_traditional true
        *set mal_relationship -5
        
    #"That's revolutionary. Let's explore it."
        Mal brightens. "Really? You think it could work?"
        *set mal_relationship +10
        *set demon_court_reform true
        *achievement ethical_demon unlocked "Encouraged Mal's reforms"
```

### **Zara's Paradox Magic**

From FACTION_GUIDE.md: Zara does the impossible.

```
*label zara_paradox
*if (rigid_thinking)
    "You're trying to force it into categories," Zara observes. "Magic has no limits, 
    only artificial boundaries."
    *goto struggle_with_paradox
*else
    "Yes! You're getting it!" Zara's eyes light up. "Incompatible magic systems can 
    combine if you stop believing they can't!"
    *set third_thread_understanding +10
    *goto paradox_breakthrough
```

---

## 💻 CODE EXAMPLES

### **Avalon Academy Arrival Scene**

```
*comment Based on FACTION_GUIDE.md - Avalon Academy section

*label academy_arrival
*page_break

You step through the dimensional gate onto Avalon Academy grounds. The Spiral 
Spire rises before you—nine levels of living architecture that hums with 
accumulated magic.

*italic "Welcome to Avalon," *italic Polly's voice echoes in your mind. 
*italic "Try not to destroy anything on your first day."

*choice
    #Approach the entrance respectfully
        *set collaboration +5
        *goto respectful_entry
        
    #Rush forward eagerly
        *set enthusiasm +5
        *goto eager_entry
        
    #Pause to observe the World Tree connection
        *set dimensional_awareness +10
        *goto observant_entry
```

### **Guild Selection System**

```
*comment Based on FACTION_GUIDE.md - Guild System

*create guild ""
*temp guild_choice ""

*label guild_selection
*page_break

The Academy's guild system lets you specialize while collaborating across disciplines.

*choice
    #Elementalists - Master fire, water, air, earth
        *set guild "Elementalist"
        *set elemental_affinity +20
        *goto elementalist_path
        
    #Timeweavers - Study chronothurgy and temporal magic
        *set guild "Timeweaver"
        *set temporal_understanding +20
        *goto timeweaver_path
        
    #Runecasters - Learn magical programming and symbolic arts
        *set guild "Runecaster"
        *set runic_knowledge +20
        *goto runecaster_path
        
    #Diplomancers - Master communication and negotiation
        *set guild "Diplomancer"
        *set diplomatic_skill +20
        *goto diplomancer_path
```

### **Faction Encounter Template**

```
*comment Encountering different factions

*label faction_encounter
*temp faction "none"
*temp faction_attitude "neutral"

*if (location = "Sun-Crown Territory")
    *set faction "Sun-Crown Order"
    *if (sun_crown_affinity >= 50)
        *set faction_attitude "friendly"
    *else
        *set faction_attitude "suspicious"

*if (faction_attitude = "friendly")
    The Sun-Crown mage nods approvingly. "Your dedication to perfected techniques 
    honors the old ways."
    *goto friendly_interaction
*else
    "Innovation without foundation is chaos," the mage states coldly. "Prove your 
    worth through traditional means."
    *goto suspicious_interaction
```

### **The Nine Levels of Spiral Spire**

```
*comment Based on FACTION_GUIDE.md - Avalon Academy architecture

*label explore_spire
Which level do you visit?

*choice
    #Level 1 - Foundation Hall
        *goto foundation_hall
    #Level 2 - Elemental Chambers
        *goto elemental_chambers
    #Level 3 - Temporal Studies (heavily warded)
        *if (temporal_clearance)
            *goto temporal_studies
        *else
            "Access restricted. Chronothurgy requires special clearance."
            *goto explore_spire
    #Level 4 - Symbolic Arts
        *goto symbolic_arts
    #Level 5 - Diplomatic Quarters
        *goto diplomatic_quarters
    #Level 6 - Protective Studies
        *goto protective_studies
    #Level 7 - Research Archives
        *goto research_archives
    #Level 8 - Collaborative Workshops
        *goto collaborative_workshops
    #Level 9 - Observatory
        *goto observatory
```

---

## 🧪 TESTING YOUR SCENES

### **ChoiceScript IDE Testing Checklist**

✅ **Character Voice Consistency**
```
*comment Test: Does Izack compound words when nervous?
*comment Test: Does Polly provide sarcastic commentary?
*comment Test: Does Aria handle diplomacy smoothly?
```

✅ **Canon Compliance**
```
*comment Test: Is Clay created (not summoned)?
*comment Test: Does magic respond to genuine need?
*comment Test: Is Avalon built on invitation?
```

✅ **Stat Tracking**
```
*comment Test: Does collaboration increase with teamwork?
*comment Test: Do relationships track properly?
*comment Test: Do faction affinities make sense?
```

✅ **Player Agency**
```
*comment Test: Can players make meaningful choices?
*comment Test: Do different paths feel distinct?
*comment Test: Are there no dead ends without warning?
```

### **Testing in ChoiceScript IDE**

1. **Save Your Scene File**
   - Save as `.txt` in `scenes/` folder
   - Use lowercase, underscores: `faction_encounter.txt`

2. **Update startup.txt**
   ```
   *scene_list
       startup
       your_new_scene
       other_scenes
   ```

3. **Test the Scene**
   - Open `index.html` in ChoiceScript
   - Click through all choice paths
   - Check stat screen for correct updates

4. **Use Quicktest**
   - Run Quicktest in ChoiceScript IDE
   - Fixes common errors automatically

### **Common ChoiceScript Errors to Avoid**

❌ **Wrong:**
```
*goto scene_name
*comment This won't work - use goto_scene for different files
```

✅ **Correct:**
```
*goto_scene scene_name
*comment Use goto_scene to jump between scene files
```

❌ **Wrong:**
```
*set izack-relationship +5
*comment Hyphens not allowed in variable names
```

✅ **Correct:**
```
*set izack_relationship +5
*comment Use underscores for variable names
```

---

## 🎨 ADVANCED TECHNIQUES

### **Callback to Player Choices**

```
*comment Reference earlier choices to make story feel cohesive

*if (created_clay)
    "Remember when you created Clay?" Izack asks. "That moment of genuine need—
    that's the foundation of all our teaching here."
    *set understands_philosophy true
```

### **Branching Based on Faction Affinity**

```
*if (arcane_dominion_rep >= mortal_confederations_rep) and (arcane_dominion_rep >= primordial_collective_rep)
    *comment Player leans toward Arcane Dominion
    *goto arcane_ending_path
*elseif (mortal_confederations_rep >= primordial_collective_rep)
    *comment Player leans toward Mortal Confederations
    *goto mortal_ending_path
*else
    *comment Player leans toward Primordial Collective
    *goto primordial_ending_path
```

### **Multiple Character Interactions**

```
*label group_scene
Izack, Aria, and Zara are all present. Who do you address first?

*choice
    #Izack - Ask about dimensional theory
        *gosub izack_conversation
        *goto continue_group_scene
        
    #Aria - Discuss diplomatic matters
        *gosub aria_conversation
        *goto continue_group_scene
        
    #Zara - Explore paradox magic
        *gosub zara_conversation
        *goto continue_group_scene
```

---

## 📝 QUICK REFERENCE: LORE TO CODE

### **Character Dialogue Quick Reference**

| Character | Key Trait | ChoiceScript Pattern |
|-----------|-----------|---------------------|
| **Izack** | Nervous compounding | "That is—I mean—oh, bleeding stars!" |
| **Aria** | Diplomatic smoothness | "Collaborative magic isn't just technique—it's philosophy." |
| **Clay** | Created nature | "I am because someone needed me to be." |
| **Polly** | Sarcasm in italics | *italic "Oh yes, *brilliant* plan," *italic Polly mutters. |
| **Mal** | Learning ethics | "What if both parties genuinely benefited?" |
| **Zara** | Breaking rules | "Magic has no limits, only artificial boundaries." |

### **Faction Philosophy Quick Reference**

| Faction | Core Belief | Choice Pattern |
|---------|-------------|----------------|
| **Sun-Crown** | Perfection through tradition | "The old ways are proven and pure." |
| **Twilight Scholars** | Understanding boundaries | "Boundaries exist to be understood, not feared." |
| **Starforged** | Restore the past | "The First Realm had it right." |
| **Human Kingdoms** | Unity and adaptation | "Together we're stronger than apart." |
| **Avalon Academy** | Collaborative learning | "Knowledge shared is power multiplied." |
| **Demon Court (Mal)** | Ethical contracts | "What if we both benefit?" |

---

## 🎯 INTEGRATION CHECKLIST

Before finalizing your ChoiceScript scene:

- [ ] Checked CHARACTER_COMPENDIUM.md for dialogue accuracy
- [ ] Verified faction motivations in FACTION_GUIDE.md
- [ ] Used correct character voice patterns
- [ ] Maintained "Clay was created" canon
- [ ] Tracked collaboration vs individual power
- [ ] Updated relationship variables appropriately
- [ ] Tested all choice branches in ChoiceScript IDE
- [ ] Ran Quicktest to catch errors
- [ ] Verified stat screen displays correctly
- [ ] Ensured no dead ends without player warning

---

## 🔗 RELATED RESOURCES

**Lore Documentation:**
- [CHARACTER_COMPENDIUM.md](../lore/CHARACTER_COMPENDIUM.md) - Canonical character traits
- [FACTION_GUIDE.md](../lore/FACTION_GUIDE.md) - Complete faction encyclopedia
- [FACTION_QUICK_REFERENCE.md](../lore/FACTION_QUICK_REFERENCE.md) - Quick faction facts

**ChoiceScript Resources:**
- [Official Documentation](https://www.choiceofgames.com/make-your-own-games/choicescript-intro/)
- [Community Forum](https://forum.choiceofgames.com/)
- [ChoiceScript Wiki](https://choicescriptdev.fandom.com/wiki/)

**Game Files:**
- [choicescript_game/README.md](README.md) - How to play and test
- [choicescript_game/scenes/](scenes/) - Existing scene files

---

## 💡 TIPS FOR SUCCESS

### **Do:**
✅ Keep CHARACTER_COMPENDIUM.md open while writing dialogue
✅ Reference FACTION_GUIDE.md for faction encounters
✅ Test every choice path in ChoiceScript IDE
✅ Use meaningful variable names (`izack_relationship` not `var1`)
✅ Add comments explaining canonical connections
✅ Build on existing scenes, don't contradict them

### **Don't:**
❌ Make Clay summoned instead of created
❌ Have Izack speak smoothly when nervous
❌ Ignore existing relationship tracking
❌ Create faction conflicts that contradict FACTION_GUIDE.md
❌ Forget to update the scene_list in startup.txt
❌ Skip testing - it will break later!

---

*May your scenes honor the lore and delight your players!*

**—ChoiceScript Writer's Guide for The Spiral of Pollyoneth**
**Last Updated: November 2025**

---

**🎉 READY TO WRITE!**

You now have everything you need to create ChoiceScript scenes that are:
- ✨ Canonically accurate to the lore
- 🎮 Properly formatted for ChoiceScript IDE
- 📚 Integrated with the documentation system
- 🎯 Ready for testing and publication

Happy writing! And remember: "Magic responds to genuine need, not commands!"
