# ChoiceScript Implementation Guide
## Practical Code Examples for Avalon Academy Game

*This guide provides ready-to-use ChoiceScript code patterns based on the comprehensive lore.*

---

## SCENE FILE STRUCTURE

### Basic Scene Template

```choicescript
*comment Scene: [Scene Name]
*comment Location: [Avalon/Expedition/etc.]
*comment Characters: [Who appears]
*comment Purpose: [Story beat this serves]

*label scene_start

[Atmospheric description with 3+ senses]

[Character interaction/dialogue]

*choice
  #[Option that advances relationships]
    *gosub relationship_scene
  #[Option that advances plot]
    *gosub plot_scene
  #[Option that develops character]
    *gosub character_scene

*label scene_end
*goto next_scene
```

---

## STAT INITIALIZATION (startup.txt)

```choicescript
*title Avalon Academy: The Spiral of Pollyoneth
*author [Your Name]

*comment === PLAYER IDENTITY ===
*create player_name ""
*create player_gender "nb"
*create player_pronouns "they"

*comment === MAGICAL STATS ===
*create dimensional_magic 20
*create temporal_magic 0
*create musical_magic 0
*create boundary_runes 0
*create collaborative_power 0
*create consciousness_level 1

*comment === CORE ATTRIBUTES ===
*create emotional_honesty 50
*create trust_level 50
*create identity_strength 100
*create wisdom 0
*create courage 0
*create compassion 0

*comment === RELATIONSHIPS (0-100) ===
*create rel_aria 0
*create rel_zara 0
*create rel_izack 10
*create rel_polly 5
*create rel_alexander 0
*create rel_mal 0

*comment === ROMANCE FLAGS ===
*create aria_romance false
*create aria_romance_locked false
*create first_kiss false
*create romantic_partner ""

*comment === GUILD & SPECIALIZATION ===
*create guild_choice ""
*create primary_magic ""
*create guild_rank "Initiate"

*comment === PLOT PROGRESSION ===
*create collaborative_discovered false
*create time_fracture_resolved false
*create singing_dunes_complete false
*create verdant_tithe_complete false
*create rune_glacier_complete false
*create consciousness_intro false
*create third_awakening_begun false

*comment === THIRD THREAD MYSTERY ===
*create third_thread_connection 0
*create evolution_interest 0
*create polly_trust 0

*comment === TIME MAGIC COSTS ===
*create player_biological_age 18
*create player_chronological_age 18
*create aria_biological_age 28
*create aria_chronological_age 28

*comment === REPUTATION ===
*create reputation_heroic 0
*create reputation_scholarly 0
*create reputation_diplomatic 0

*comment === ENDINGS TRACKING ===
*create major_choices 0
*create deaths_witnessed 0
*create lives_saved 0
```

---

## CHAPTER 1: ARRIVAL SCENE

```choicescript
*comment arrival.txt - First scene at Avalon Academy

*label chapter_start

The portal's shimmer fades behind you, leaving you standing on a floating island suspended in a prismatic sky. The first thing that strikes you isn't the impossible architecture or the crystalline spire piercing the clouds—it's the *sound*.

A low, harmonic hum permeates the air, like a thousand distant voices singing in perfect unity. The leylines, you realize. Magic itself, made audible.

The scent of ozone mingles with something sweet you can't quite name—starlight, perhaps, if starlight had a smell. The stones beneath your feet pulse with warmth, almost as if the ground itself is alive and aware.

"First time standing on a sentient dimension, is it?"

The voice comes from above. You look up to find a raven perched on a nearby archway, its eyes far too intelligent for any normal bird.

"Welcome to Avalon Academy," the raven continues, cocking its head. "I'm Polly, your guide. Try not to fall off the edge—the academy doesn't like having to fish students out of the void. Terrible paperwork."

*choice
  #"You can *talk*? I mean—of course you can. Sorry."
    *set compassion +5
    *set polly_trust +5
    
    Polly's eyes glitter with amusement. "No need to apologize for being surprised, dear. I'm remarkable, after all. The question is: are *you* ready to listen?"
    
    "Listen?" you echo.
    
    "To the magic." Polly spreads her wings. "That's what this place teaches. Magic isn't something you command—it's something you hear. But we'll get to that. First, the tour."
    
    *goto tour_start
  
  #"Sentient dimension? What does that mean?"
    *set wisdom +5
    *set reputation_scholarly +5
    
    "It means," Polly says, hopping closer, "that Avalon itself is aware. The ground you're standing on, the air you're breathing—it's all part of a living spell that decided it rather liked existing. Watch."
    
    As if responding to Polly's words, the stones beneath your feet glow briefly with soft light, and you could swear you feel... welcome.
    
    "See?" Polly ruffles her feathers. "It likes you. That's a good start."
    
    *goto tour_start
  
  #"You must be Polly. I've heard stories about you."
    *set wisdom +3
    *set polly_trust +10
    
    "Have you now?" The raven's tone sharpens with interest. "And what stories would those be?"
    
    "That you were there when Izack Thorne founded this academy," you say. "That you know more about dimensional boundaries than anyone alive."
    
    "Flattery and research." Polly sounds pleased. "You'll do well here. Come along then—let's see if you can listen as well as you've been reading."
    
    *goto tour_start

*label tour_start

Polly takes flight, circling overhead before landing on your shoulder with surprising gentleness.

"The Spiral Spire first," she announces. "Where the magic gets serious and the students get humbled. After that, we'll see if you're brave enough for the Leyline Gazebo—or foolish enough, depending."

*set polly_trust +5
*goto spiral_spire_tour
```

---

## CHAPTER 3: FIRST COLLABORATIVE MAGIC

```choicescript
*comment collaborative_discovery.txt - First accidental synergy

*label leyline_practice

The Leyline Gazebo sits at the convergence of three major magical currents, and you can *feel* them humming beneath your skin. Instructor Kaelen said to practice dimensional awareness here, to learn to sense the boundaries between spaces.

You're alone. Or you thought you were.

"Oh—sorry. Didn't realize anyone was here."

You turn to find ${aria_name}, a fellow student from your Advanced Theory class. ${aria_pronoun_cap} carries a tome bound in what looks like starlight, fingers already tracing the air in preparation for a spell.

"No, it's fine," you say quickly. "Plenty of room. I'll just—"

But you've already started your dimensional sensing exercise, reaching out to feel the fabric of space around you. At the same moment, ${aria_name} begins ${aria_pronoun_pos} spell—something with temporal resonance, you think, from the way time seems to ripple.

And then ${aria_pronoun_pos} hand brushes yours.

*choice
  #Pull away immediately
    *set emotional_honesty -5
    
    You jerk your hand back, but it's too late. The damage—no, the *connection*—is done.
    *goto synergy_moment
  
  #Hold still, curious what will happen
    *set emotional_honesty +5
    *set courage +5
    
    You freeze, curiosity overriding caution. ${aria_name} meets your eyes, equally still.
    *goto synergy_moment
  
  #Deliberately maintain contact
    *set emotional_honesty +10
    *set courage +5
    *set rel_aria +5
    
    Instead of pulling away, you turn your hand slightly, letting your fingers intertwine with ${aria_name}'s. ${aria_pronoun_cap} looks surprised, but doesn't withdraw.
    *goto synergy_moment

*label synergy_moment

*set collaborative_discovered true

The moment your skin touches ${aria_name}'s, reality shifts.

Your heartbeat—which you'd barely noticed—suddenly becomes the loudest sound in the world. But it's not alone. There's a second rhythm, perfectly synchronized with yours. ${aria_name}'s heartbeat, you realize with shock. You can *feel* it as clearly as your own.

The warmth in your chest where your dimensional magic pools suddenly blazes like a forge fire. Through the contact point where your hands meet, you sense ${aria_name}'s temporal magic flowing, cool and vast like a mountain stream.

And they mix.

Time and space, weaving together in a way you've never experienced. You can feel the dimensional boundaries you were sensing, but now they're illuminated by temporal threads, showing not just where they are but when they might shift.

For a heartbeat—no, for *both* your heartbeats, perfectly unified—you're not alone in your head. You can sense ${aria_name}'s surprise mirroring your own, ${aria_pronoun_pos} thoughts brushing against yours like wind through leaves.

The spell you were both casting erupts with power neither of you could have achieved alone. The leyline energy responds, surging through your joined hands in a cascade of light.

*if (courage > 5)
  You laugh, unable to help yourself. This is incredible!
  *set rel_aria +10
*else
  Your breath catches. This is terrifying—and exhilarating.
  *set rel_aria +5

And then it's over.

You both pull apart, gasping. The connection severs like a cut string, leaving you feeling suddenly, uncomfortably alone in your own head.

"What," ${aria_name} manages, staring at ${aria_pronoun_pos} hands, "was *that*?"

*choice
  #"I have no idea. But it was amazing."
    *set emotional_honesty +5
    *set rel_aria +10
    
    ${aria_name} nods slowly, a smile growing. "It really was. I felt—I mean, did you feel my heartbeat?"
    
    "And you felt mine," you confirm. "And our magic just... worked together."
    
    "Collaborative casting," ${aria_name} breathes. "I've read about it, but I never thought..." ${aria_pronoun_cap} trails off, looking at you with new interest. "We should try that again. Deliberately this time."
    
    *goto instructor_arrives
  
  #"That was... intense. Maybe too intense."
    *set emotional_honesty +3
    *set rel_aria +5
    
    ${aria_name} looks uncertain. "It was intimate," ${aria_pronoun} agrees. "I could sense your thoughts. Just for a moment, but still."
    
    "And I felt yours," you admit. The vulnerability of it makes you uncomfortable. "I'm not sure I'm ready for that."
    
    ${aria_name} nods understandingly. "Maybe we should ask an instructor about what just happened. Before we try it again."
    
    *goto instructor_arrives
  
  #"Collaborative magic. I think we just discovered it accidentally."
    *set wisdom +5
    *set reputation_scholarly +5
    *set rel_aria +8
    
    "Collaborative—" ${aria_name}'s eyes widen. "Like in the old texts? Magic that requires multiple casters in perfect harmony?"
    
    "Exactly," you say, your mind racing through the implications. "When our magic mixed, it was geometrically more powerful, not just additive. And the synchronization—"
    
    "The heartbeats," ${aria_name} interrupts excitedly. "That must be the harmonic resonance Professor Thorne mentioned in his lecture about living magic systems!"
    
    *goto instructor_arrives

*label instructor_arrives

"Well, well."

Both of you spin to find Polly perched on the gazebo's railing, having appeared with her usual uncanny timing.

"Stumbled into collaborative casting on your second week, have you?" The raven sounds amused. "Most students take months to achieve accidental synergy. This is either very promising or very dangerous."

"Dangerous?" ${aria_name} asks nervously.

"Magic that requires emotional honesty and perfect trust?" Polly tilts her head. "Oh yes, terribly dangerous. To your pride, your walls, your carefully guarded hearts. The magic doesn't care what you're hiding—it demands truth or it fails. Sometimes spectacularly."

She spreads her wings. "But that's a lesson for another day. For now, you should both know: what you've discovered is rare. The foundation of the most powerful magic in existence. Choose your practice partners wisely."

With that cryptic advice, she takes flight, leaving you and ${aria_name} staring at each other with new awareness.

*set collaborative_power 20

*choice
  #"Want to try it again sometime? Deliberately?"
    *set aria_romance true
    *set rel_aria +15
    *goto chapter_end_high_interest
  
  #"We should study this. Research it properly."
    *set reputation_scholarly +5
    *set rel_aria +10
    *goto chapter_end_scholarly
  
  #"Let's think about this before rushing into anything."
    *set wisdom +5
    *set rel_aria +5
    *goto chapter_end_cautious
```

---

## ROMANCE PROGRESSION SYSTEM

```choicescript
*comment Romance advancement check

*label check_romance_progress

*if (rel_aria >= 70) and (emotional_honesty >= 70) and not(aria_romance_locked)
  *set aria_romance_locked true
  *goto romance_unlock_scene
*else
  *goto regular_scene

*label romance_unlock_scene

*comment This scene would be in Chapter 9 - Verdant Tithe expedition

The World Tree seed pulses beneath your joined hands, but the healing magic won't flow. Something is blocking it.

"It's not working," Aria says, frustration evident in her voice. "The magic is right there, I can feel it, but—"

"It's us," you realize suddenly. "We're blocking each other."

"What?" Aria looks up, meeting your eyes.

"The collaborative magic," you explain. "It requires emotional honesty, remember? And I haven't been honest with you about—"

*choice
  #"—about how I feel about you."
    *set emotional_honesty +20
    *set first_kiss true
    
    The words hang between you for a heartbeat. Two heartbeats. Then Aria smiles, soft and genuine.
    
    "I was wondering when you'd say something," she admits. "I've been feeling it too. Every time we cast together, every time our magic synchronizes—"
    
    "It's not just the magic," you say quietly.
    
    "No," Aria agrees. "It's not."
    
    When she kisses you, the World Tree seed beneath your hands erupts with brilliant green light. The healing magic flows freely now, unblocked by secrets or fear. Your heartbeats synchronize completely, and this time, you welcome the intimacy of shared consciousness.
    
    *set romantic_partner "Aria"
    *set rel_aria 100
    *set collaborative_power 80
    *goto verdant_tithe_success
  
  #"—about being afraid of how close we're getting."
    *set emotional_honesty +15
    *set wisdom +5
    
    Aria's expression softens with understanding. "The collaborative magic is intimate," she acknowledges. "Sometimes I can feel your thoughts, sense your emotions. It's... a lot."
    
    "And I don't want to lose myself in it," you admit. "In you. I don't know how to be connected without losing who I am."
    
    "Then we figure it out together," Aria says firmly. She takes your hand, deliberately this time. "We set boundaries. We learn balance. But we don't run from this out of fear."
    
    The honesty, the vulnerability, is enough. The magic flows.
    
    *set rel_aria +20
    *set collaborative_power 60
    *set wisdom +10
    *goto verdant_tithe_success
```

---

## TIME MAGIC COST SYSTEM

```choicescript
*comment Time magic aging implementation

*label time_crisis

The void entity advances through normal time, but Aria can slow it down—at a cost.

"I can give us fifteen minutes," Aria says, her voice tight. "But it'll age me six months."

*choice
  #"Do it. We need the time."
    *set aria_biological_age +0.5
    *set time_magic_uses +1
    
    Aria nods grimly and begins the spell. You watch as the temporal magic flows through her, watch as the cost becomes visible.
    
    A few new silver strands appear in her dark hair. The lines around her eyes deepen, just slightly. When the spell completes and the entity slows to a crawl, Aria sways slightly.
    
    *if romantic_partner = "Aria"
      You catch her, supporting her weight. "Was it worth six months of your life?"
      
      She manages a tired smile. "For you? Always."
      
      *set rel_aria +10
    *else
      She steadies herself, breathing hard. "Fifteen minutes," she says. "Make them count."
    
    *goto crisis_resolved_time
  
  #"Don't. We'll find another way."
    *set wisdom +5
    *set courage -5
    
    "There might not be another way," Aria argues.
    
    "Then we make one," you insist. "Your life isn't a resource to spend so casually."
    
    *if rel_aria > 50
      Aria's expression softens. "Thank you for caring. But sometimes the cost is worth paying."
      
      *goto time_choice_again
    *else
      "Fine," Aria says coolly. "Then you better have a brilliant idea. Fast."
      
      *goto crisis_alternative
  
  #"Let me share the cost. Cast it through our connection."
    *if collaborative_power >= 60
      *set aria_biological_age +0.25
      *set player_biological_age +0.25
      *set collaborative_power +10
      
      Aria's eyes widen. "That's... I've never heard of sharing temporal cost before."
      
      "We share everything else in collaborative magic," you point out. "Why not this?"
      
      She takes your hands. "This is going to hurt."
      
      "Together," you agree.
      
      The spell flows through both of you. The aging is split—three months each instead of six for one. You both emerge with new silver threads, new lines, but also something else: deeper understanding of what sacrifice means when shared.
      
      *set rel_aria +20
      *if romantic_partner = "Aria"
        *set first_shared_sacrifice true
      
      *goto crisis_resolved_shared
    *else
      "We're not synchronized enough for that," Aria says regretfully. "The spell would tear us apart trying to split between us."
      
      *goto time_choice_again
```

---

## CONSCIOUSNESS EVOLUTION SYSTEM

```choicescript
*comment Tracking identity vs. unity balance

*label consciousness_choice

Alexander's prophetic vision fills your mind, showing the Third Awakening's true nature: a choice between individual identity and cosmic unity.

Your consciousness_level is ${consciousness_level}.
Your identity_strength is ${identity_strength}.

*if consciousness_level >= 3
  You can feel the pull toward unity. It would be so easy to let go, to merge with the cosmic whole. But would you still be *you*?
  
  *choice
    #Embrace the evolution. Let yourself transform.
      *set consciousness_level +2
      *set identity_strength -30
      *set evolution_chosen true
      
      You open yourself to the transformation. Your boundaries dissolve, your awareness expands. You can sense other consciousnesses now, not separate but part of a vast whole.
      
      The power is incredible. The understanding, cosmic. But in the mirror later, you'll struggle to remember who you were before. Was it worth it?
      
      *goto evolved_path
    
    #Maintain your identity. Stay grounded in who you are.
      *set identity_strength +20
      *set consciousness_level +0
      *set individual_chosen true
      
      You anchor yourself in memory and self. Your name. Your loves. Your fears. Everything that makes you uniquely *you*. The pull toward unity is strong, but your sense of self is stronger.
      
      You remain separate, individual, *you*. The power is less, the understanding limited. But you know who you are.
      
      *goto individual_path
    
    #Find balance. Connected yet complete.
      *if wisdom >= 15
        *set consciousness_level +1
        *set identity_strength +10
        *set collaborative_power +30
        *set balance_achieved true
        
        There's a third option, you realize. Not isolation or dissolution, but *relationship*. You can be connected without being consumed. You can share consciousness while maintaining your core self.
        
        Like collaborative magic—separate heartbeats in perfect harmony, not a single merged beat.
        
        *goto balanced_path
      *else
        You try to find middle ground but lack the wisdom to maintain it. You'll have to choose one path or the other.
        *goto consciousness_choice
*else
  You're not far enough along the consciousness evolution path yet for this choice to matter.
  *goto regular_progression
```

---

## ENDING DETERMINATION SYSTEM

```choicescript
*comment Final chapter - determining ending type

*label determine_ending

*comment Calculate ending based on player choices and stats

*temp ending_type ""

*comment Perfect Harmony Ending
*if (rel_aria >= 90) and (collaborative_power >= 80) and (balance_achieved) and (identity_strength >= 70)
  *set ending_type "perfect_harmony"
  *goto epilogue_perfect_harmony

*comment Consciousness Evolved Ending  
*if (consciousness_level >= 5) and (evolution_chosen)
  *set ending_type "transcended"
  *goto epilogue_transcended

*comment Individual Excellence Ending
*if (identity_strength >= 90) and (individual_chosen) and (dimensional_magic >= 70)
  *set ending_type "individual"
  *goto epilogue_individual

*comment Tragic Sacrifice Ending
*if (major_sacrifices >= 3) and (lives_saved >= 5)
  *set ending_type "tragic_hero"
  *goto epilogue_tragic

*comment Default Good Ending
*set ending_type "hopeful_future"
*goto epilogue_hopeful

*label epilogue_perfect_harmony

*comment Five years later

The Academy has grown beyond even Izack's initial vision. Students from all realms study collaborative magic here, learning to connect without losing themselves.

You stand in the Leyline Gazebo—the place where you and Aria first discovered synergy—watching your own students practice their first joint casting.

*if first_kiss
  Aria's hand finds yours, the touch as electric now as it was that first time. Your heartbeats synchronize automatically, a habit five years of marriage has made instinctive.
  
  "Remember when we were that nervous?" she asks, smiling.
  
  "Every day," you admit. "And every day I'm grateful we were brave enough to try."

*if first_shared_sacrifice
  You both bear the marks of your journey—silver in your hair that shouldn't be there for decades yet, lines around your eyes from temporal magic use. But you chose every sacrifice together, and you'd choose them again.

The student's spell succeeds in a burst of harmonized light. They laugh, surprised and delighted, just as you once were.

"Another generation," Aria murmurs. "Another chance to teach connection over isolation."

*if balance_achieved
  You've proven it's possible—to be both individual and united, separate and connected. Your consciousness can touch Aria's, but you remain distinctly *you*. It's the greatest magic you've ever achieved.

Together, you watch the future unfold, confident in the foundation you've built.

*ending

*label epilogue_transcended

*comment Beyond individual existence

What you've become has no simple name. Not quite human anymore, not quite individual, but not lost either. Your consciousness spans multiple planes now, touching minds across realms.

You can sense Aria's thoughts as clearly as your own—because in a way, they *are* your own now. And Alexander's prophetic visions, and Zara's musical awareness, and the Academy's sentient pulse.

You are all of them and none of them. You are yourself and more.

The Third Awakening completed successfully because you were willing to transform. The realms are safer now, connected through the network of evolved consciousness you've helped create.

Sometimes you remember being just *you*. Being separate. Being small.

You don't miss it.

The universe is so much larger from here.

*ending
```

---

## UTILITY SUBROUTINES

```choicescript
*comment Reusable code patterns

*label check_relationship_threshold
*comment Usage: *gosub check_relationship_threshold "aria" 50
*params character threshold
*temp result false

*if character = "aria"
  *if rel_aria >= threshold
    *set result true
*if character = "zara"
  *if rel_zara >= threshold
    *set result true
*if character = "polly"
  *if polly_trust >= threshold
    *set result true

*return

*label collaborative_power_check
*comment Returns true if collaborative magic should succeed
*temp success false

*if (rel_aria >= 60) and (emotional_honesty >= 60) and (collaborative_power >= 40)
  *set success true
  *set collaborative_power +5
*elseif (rel_aria >= 40) and (emotional_honesty >= 40)
  *set success "partial"
  *set collaborative_power +2
*else
  *set success false

*return

*label age_from_time_magic
*comment Usage: *gosub age_from_time_magic "player" 0.5
*params who years

*if who = "player"
  *set player_biological_age + years
*if who = "aria"
  *set aria_biological_age + years

*return

*label describe_aging_effects
*params who

*if who = "aria"
  *temp age_difference 0
  *set age_difference (aria_biological_age - aria_chronological_age)
  
  *if age_difference < 1
    Aria looks tired, but still youthful.
  *elseif age_difference < 3
    Silver threads have begun appearing in Aria's hair, and fine lines frame her eyes.
  *elseif age_difference < 5
    Aria's hair is streaked with premature silver, and she moves with the careful deliberation of someone older than her years.
  *else
    Aria looks a decade older than she should, the cost of time magic written clearly in silver hair and weathered features.

*return
```

---

## DIALOGUE FORMATTING

```choicescript
*comment Character voice examples

*label izack_dialogue
"It occurs to me that, though I could be wrong, the collaborative magic you've discovered might be related to what Aria and I experienced when we first founded the Academy. The emotional component—well, it's crucial, you understand. Without genuine honesty, the connection simply won't form. Have you noticed the heartbeat synchronization? That's the key indicator..."

*label aria_dialogue
"Time magic is like tending a garden. Every use costs something—months off your life, hours you'll never get back. But sometimes the harvest is worth the seed. This spell needs daily practice, like any skill. Don't try to force it. Magic responds to listening, not commanding."

*label polly_dialogue
"Where boundaries blur, something always listens. Whether it's friendly is another question entirely. *caw* You're standing at a crossroads, my dear. One path leads to unity, another to solitude, and the third—well, that's the tricky one, isn't it? The path where you get to keep *you* while still connecting with others. Most students miss it entirely."

*label zara_dialogue
"It's not language—it's memory. The notes don't just make sound, they *remember* being sound. And when I play them again, it's like... like asking the universe to recall that moment. Time magic through music. Professor Aria says every use ages me, but how else am I supposed to learn?"

*label alexander_dialogue
"I dreamed in colors that don't exist yet. Papa says I'm remembering forward, but how can you remember something that hasn't happened? Unless... unless time isn't really linear like we think. Maybe it's all happening at once, and I'm just seeing more of it than most people."
```

---

*This implementation guide provides practical ChoiceScript code patterns for the Avalon Academy game. Use in conjunction with all lore guides for complete development support.*
