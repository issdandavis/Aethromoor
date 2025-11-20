// Game State
const gameState = {
    currentNode: 'start',
    collaborationScore: 0,
    relationships: {
        izack: 0,
        aria: 0,
        zara: 0
    },
    choices: []
};

// Story Nodes
const storyNodes = {
    start: {
        text: `
            <p><span class="polly-comment">*Caw!* Alright, new student. Let me guess - you're nervous, excited, and probably wondering if that portal sickness will ever wear off. Spoiler: it won't for another hour. You're welcome for that information.</span></p>

            <p>You stand at the edge of Avalon Academy, watching the impossible spiral spire twist upward into clouds that shimmer with leyline energy. The World Tree's branches arc overhead, and you can <em>feel</em> the convergence of magical currents thrumming through the air.</p>

            <p>A large raven lands on the crystalline gate before you, fixing you with one knowing eye.</p>

            <p><span class="polly-comment">"Welcome to Avalon, where boundaries come to die and collaborative magic is somehow <em>not</em> an oxymoron. I'm Polly. Yes, like the bird. No, the irony is not lost on me. I'll be your narrator, occasional advisor, and the only honest voice you'll hear today."</span></p>

            <p>The raven - Polly - gestures with one wing toward the academy entrance.</p>

            <p><span class="polly-comment">"Izack Thorne himself is waiting to meet the new arrivals. Fair warning: he's brilliant, kind, and will absolutely try to convince you that listening to magical currents is more important than controlling them. He's not wrong, but don't tell him I said that."</span></p>
        `,
        choices: [
            {
                text: "Approach respectfully and introduce yourself properly",
                next: 'polite_intro',
                effects: { collaboration: 1, izack: 1 }
            },
            {
                text: "Ask Polly more questions about what to expect",
                next: 'ask_polly',
                effects: { collaboration: 0, zara: 1 }
            },
            {
                text: "Walk past confidently - you've read about Avalon and know what you're doing",
                next: 'confident_intro',
                effects: { collaboration: -1, aria: 1 }
            }
        ]
    },

    polite_intro: {
        text: `
            <p>You walk through the crystalline gate, feeling the leyline energy wash over you like warm water. Izack Thorne stands in the courtyard - tall, dark-haired, with eyes that seem to see through dimensions.</p>

            <p>"Welcome," he says warmly. "I'm Izack. You must be our newest student. How are you feeling after the portal crossing?"</p>

            <p><span class="polly-comment">*Perched on his shoulder* "Oh good, we got a polite one. Those are always fun to watch when they realize magic here doesn't care about your manners."</span></p>

            <p>Izack shoots Polly a look. "What Polly means is that magic responds to intention and collaboration, not formality. But courtesy is always appreciated."</p>

            <p>He gestures toward the academy. "Your first lesson begins shortly. We'll be exploring the nature of magical boundaries - specifically, how they can be <em>bridged</em> rather than broken."</p>
        `,
        choices: [
            {
                text: "Express excitement about learning collaborative techniques",
                next: 'first_lesson_collab',
                effects: { collaboration: 2, izack: 2 }
            },
            {
                text: "Ask if you'll learn individual magic too - you want to be self-sufficient",
                next: 'first_lesson_mixed',
                effects: { collaboration: 0, aria: 1 }
            }
        ]
    },

    ask_polly: {
        text: `
            <p><span class="polly-comment">"Smart. Ask the raven who's been here since the beginning. I like you already."</span></p>

            <p>Polly hops closer, her feathers catching the leyline light.</p>

            <p><span class="polly-comment">"Here's what you need to know: Avalon is <em>alive</em>. Not metaphorically - Izack literally created a sentient dimensional realm that grows from the World Tree. The magic here works through collaboration, which means your success depends on how well you listen to the currents, your fellow students, and yes, even the cranky raven."</span></p>

            <p>She tilts her head.</p>

            <p><span class="polly-comment">"Izack will teach you to <em>feel</em> magic rather than force it. Aria - his wife, brilliant politician - will teach you precision and boundaries. Zara, their first student, will probably befriend you because she's annoyingly nice. And I'll keep you honest."</span></p>

            <p>Just then, a young woman with hybrid features - pointed ears, striking eyes - approaches with a warm smile.</p>

            <p>"Hi! You must be new. I'm Zara. Polly giving you the full orientation?"</p>
        `,
        choices: [
            {
                text: "Thank Polly and ask Zara what her experience has been like",
                next: 'zara_friendship',
                effects: { collaboration: 1, zara: 2 }
            },
            {
                text: "Ask Zara about the different magical traditions taught here",
                next: 'first_lesson_mixed',
                effects: { collaboration: 1, aria: 1 }
            }
        ]
    },

    confident_intro: {
        text: `
            <p><span class="polly-comment">*Caw!* "Oh, we have a confident one. This should be entertaining."</span></p>

            <p>You stride through the gate with purpose. You've read about Avalon, studied dimensional theory, and you're ready to prove yourself.</p>

            <p>A woman with sharp eyes and elegant bearing steps into your path. Her presence radiates controlled power - this is someone who knows exactly where every boundary lies.</p>

            <p>"Aria Ravencrest," she introduces herself. "Co-founder, boundary specialist, and the person who makes sure enthusiastic students don't accidentally collapse dimensional barriers."</p>

            <p><span class="polly-comment">"That's Izack's wife. She's the reason Avalon hasn't imploded from all the experimental magic. Show some respect."</span></p>

            <p>Aria's expression softens slightly. "Confidence is good. Overconfidence in dimensional magic is how you end up scattered across three realities. Let me ask you something: what do you think is more important - controlling magic, or understanding it?"</p>
        `,
        choices: [
            {
                text: "Controlling it - power without control is dangerous",
                next: 'aria_control',
                effects: { collaboration: -1, aria: 2 }
            },
            {
                text: "Understanding it - you can't work with something you don't comprehend",
                next: 'aria_understanding',
                effects: { collaboration: 2, aria: 1, izack: 1 }
            },
            {
                text: "Both equally - they inform each other",
                next: 'first_lesson_mixed',
                effects: { collaboration: 1, aria: 2 }
            }
        ]
    },

    zara_friendship: {
        text: `
            <p>Zara's face lights up. "It's been incredible! I was the first student here - came from a hybrid bloodline that didn't fit anywhere else. Avalon was the first place that celebrated what I am instead of asking me to choose."</p>

            <p><span class="polly-comment">"She's not exaggerating. Zara's the bridge between traditions. Also, she'll probably want to study with you, so prepare for that."</span></p>

            <p>Zara laughs. "Polly's right. I love working with other students. Magic here is so much stronger when we combine our approaches. My hybrid heritage lets me see connections others miss."</p>

            <p>She gestures toward a crystalline building that pulses with soft light. "Come on, first lesson's about to start. Izack's teaching today - dimensional resonance and collaborative casting."</p>

            <p>As you walk together, you notice leylines glowing beneath the courtyard stones, converging toward the central spire.</p>
        `,
        choices: [
            {
                text: "Ask Zara to partner with you during the lesson",
                next: 'first_lesson_collab',
                effects: { collaboration: 2, zara: 2, izack: 1 }
            },
            {
                text: "Thank her but say you'd like to try solo first to assess your abilities",
                next: 'first_lesson_solo',
                effects: { collaboration: -1, zara: -1 }
            }
        ]
    },

    aria_control: {
        text: `
            <p>Aria nods thoughtfully. "A practical answer. Control <em>is</em> important - I've spent years mastering boundary magic precisely because uncontrolled dimensional rifts are catastrophic."</p>

            <p><span class="polly-comment">"But...?"</span></p>

            <p>"But," Aria continues, "control without understanding is brittle. It breaks under pressure. Izack taught me that magic isn't about domination - it's about partnership."</p>

            <p>She places a hand on your shoulder. "You have the discipline for power. Let me teach you the wisdom to use it well. Come - your first lesson awaits."</p>

            <p><span class="polly-comment">"Translation: Aria likes you but thinks you're going to learn the hard way. I've seen this before. It's educational."</span></p>
        `,
        choices: [
            {
                text: "Accept Aria's guidance and keep an open mind",
                next: 'first_lesson_mixed',
                effects: { collaboration: 1, aria: 2 }
            },
            {
                text: "Respectfully maintain that control should come first, understanding second",
                next: 'first_lesson_solo',
                effects: { collaboration: -1, aria: 1 }
            }
        ]
    },

    aria_understanding: {
        text: `
            <p>Aria's expression shifts to genuine warmth. "Exactly. You can force magic to obey, but it will fight you every step. Understand it, and it becomes a willing partner."</p>

            <p><span class="polly-comment">"Congratulations, you passed Aria's test. She and Izack are going to love you."</span></p>

            <p>Aria smiles. "Polly's not wrong. That's the philosophy at Avalon's core. Magic is alive - it has currents, rhythms, preferences. Learning to <em>listen</em> to those is more powerful than any control technique."</p>

            <p>She guides you toward the academy. "Izack's teaching the first lesson today. You'll practice dimensional resonance - feeling the boundaries between realities and learning to work <em>with</em> them, not against them."</p>

            <p><span class="polly-comment">"Fair warning: this is where things get weird. Dimensional magic feels like falling while standing still. Just go with it."</span></p>
        `,
        choices: [
            {
                text: "Express excitement and ask to learn as much as possible",
                next: 'first_lesson_collab',
                effects: { collaboration: 2, aria: 2, izack: 1 }
            }
        ]
    },

    first_lesson_collab: {
        text: `
            <p>The lesson chamber is breathtaking. Crystalline walls pulse with leyline energy, and dimensional boundaries shimmer visibly in the air like heat waves made of starlight.</p>

            <p>Izack stands at the center, surrounded by five other students. "Welcome. Today we're learning to <em>feel</em> dimensional boundaries. Not to break them, but to understand their nature."</p>

            <p>He gestures, and the air ripples. "Reach out - not with your hands, but with your awareness. What does the boundary feel like?"</p>

            <p>You close your eyes and extend your senses. The boundary feels like... a membrane. Flexible. Almost musical.</p>

            <p><span class="polly-comment">"Good. Now here's the fun part - Izack wants you to work together to create a harmonic resonance. Multiple mages, one unified frequency."</span></p>

            <p>Izack nods. "Exactly. Zara, would you demonstrate with our newest student?"</p>

            <p>Zara takes your hand. "Just match my breathing. Let our intentions align."</p>

            <p>As you breathe together, something incredible happens - your magical senses merge. You can feel the boundary through both perspectives, and it's infinitely clearer.</p>
        `,
        choices: [
            {
                text: "Deepen the connection and try to include the other students",
                next: 'breakthrough_collab',
                effects: { collaboration: 3, izack: 3, zara: 2 }
            },
            {
                text: "Maintain the connection with Zara and perfect it",
                next: 'stable_collab',
                effects: { collaboration: 2, zara: 2 }
            },
            {
                text: "Pull back slightly - the merging feels overwhelming",
                next: 'crisis_setup',
                effects: { collaboration: 0, zara: -1 }
            }
        ]
    },

    first_lesson_mixed: {
        text: `
            <p>The lesson chamber glows with leyline energy. Izack begins the demonstration while Aria observes from the side, her sharp eyes missing nothing.</p>

            <p>"Dimensional magic," Izack explains, "requires both sensitivity and precision. Feel the currents, but understand the structures."</p>

            <p><span class="polly-comment">"Translation: Izack teaches you to listen, Aria teaches you not to die. It's a good system."</span></p>

            <p>Izack has you practice sensing boundaries while Aria guides your technique. It's a balance - intuition meets discipline.</p>

            <p>Aria steps forward. "Now, try to create a small portal. Just a viewing window between here and the courtyard. Focus your intention, but stay aware of the boundary's natural resistance."</p>

            <p>You concentrate, feeling the dimensional membrane. With effort, a small shimmer appears in the air.</p>

            <p><span class="polly-comment">"Not bad. A little shaky, but you're not bleeding from any orifices, so that's a win."</span></p>
        `,
        choices: [
            {
                text: "Ask if you can try collaborating with another student to stabilize it",
                next: 'stable_collab',
                effects: { collaboration: 2, izack: 2 }
            },
            {
                text: "Push yourself to perfect it solo - you want to prove your capability",
                next: 'first_lesson_solo',
                effects: { collaboration: -1, aria: 1 }
            }
        ]
    },

    first_lesson_solo: {
        text: `
            <p>You step forward, determined to show what you can do on your own. Izack watches with interest, while Aria's expression is carefully neutral.</p>

            <p><span class="polly-comment">"Oh boy. Here we go. I've seen this movie before."</span></p>

            <p>You focus entirely on your own power, reaching for the dimensional boundary. The membrane resists, but you push harder, forcing your will against it.</p>

            <p>The portal opens - larger than intended. Energy crackles at its edges.</p>

            <p>Aria's voice cuts through. "Stabilize it. You're pulling too much unfiltered dimensional energy."</p>

            <p><span class="polly-comment">"What she means is: you're about to turn yourself into a dimensional anchovy if you don't ease off."</span></p>

            <p>Panic flickers through you as the portal destabilizes further. Through the opening, you glimpse fractured realities.</p>
        `,
        choices: [
            {
                text: "Swallow your pride and call for help from the other students",
                next: 'crisis_collab_rescue',
                effects: { collaboration: 2, izack: 1, zara: 2 }
            },
            {
                text: "Trust Aria's instruction and try to stabilize it using her technique",
                next: 'crisis_aria_rescue',
                effects: { collaboration: 0, aria: 3 }
            },
            {
                text: "Pour more power into it - if you can open it, you can control it",
                next: 'crisis_disaster',
                effects: { collaboration: -2, izack: -1, aria: -1 }
            }
        ]
    },

    breakthrough_collab: {
        text: `
            <p>You reach out with your awareness, inviting the other students into the resonance. One by one, they join - five minds, five hearts, one unified frequency.</p>

            <p><span class="polly-comment">"Oh. Oh, this is... actually, I'm speechless. That never happens. Caw."</span></p>

            <p>The dimensional boundary doesn't just become visible - it <em>sings</em>. You can feel its nature, its preferences, the way it wants to flex and flow. Together, your group creates a perfect harmonic resonance.</p>

            <p>Izack's eyes shine with unshed tears. "This is exactly what Avalon was built for. You just demonstrated the Third Thread - collaborative magic that transcends individual limitations."</p>

            <p>Aria approaches, clearly moved. "In my years of dimensional work, I've never seen students achieve this level of connection on their first day."</p>

            <p>Zara squeezes your hand, grinning. "We did it!"</p>

            <p><span class="polly-comment">"Alright, don't let it go to your heads. But yes, this was... impressive. Even for Avalon."</span></p>
        `,
        choices: [
            {
                text: "Thank everyone and express how amazing the collaboration felt",
                next: 'ending_collaborative_master',
                effects: { collaboration: 3, izack: 3, aria: 2, zara: 3 }
            }
        ]
    },

    stable_collab: {
        text: `
            <p>You and Zara maintain the connection, refining it. The boundary becomes crystal clear between your merged awareness.</p>

            <p>Izack nods approvingly. "Beautiful work. This is partnership magic - two becoming greater than the sum of their parts."</p>

            <p><span class="polly-comment">"Solid performance. Not flashy, but that's not always bad. You're learning the right lessons."</span></p>

            <p>Aria steps forward. "Now let's test your understanding. Can you identify the weak points in the boundary? Every dimensional membrane has natural stress points."</p>

            <p>With Zara's help, you scan the shimmering barrier. There - three points where the boundary thins naturally.</p>

            <p>"Exactly," Aria confirms. "Those are potential portal sites. Understanding the boundary's nature lets you work <em>with</em> it instead of forcing it."</p>

            <p>The lesson continues successfully. You've demonstrated both collaborative skill and practical understanding.</p>
        `,
        choices: [
            {
                text: "Ask if you can study more about the Third Thread and collaborative magic",
                next: 'ending_collaborative_scholar',
                effects: { collaboration: 2, izack: 2, zara: 2 }
            },
            {
                text: "Ask Aria about advanced boundary techniques",
                next: 'ending_balanced_mage',
                effects: { collaboration: 1, aria: 3, izack: 1 }
            }
        ]
    },

    crisis_setup: {
        text: `
            <p>You pull back from the merged awareness, suddenly overwhelmed. The sensation of your consciousness blending with Zara's was too much, too fast.</p>

            <p><span class="polly-comment">"Okay, that's fair. It is pretty intense the first time."</span></p>

            <p>But as you withdraw, something goes wrong. The collaborative resonance destabilizes, and the dimensional boundary you were examining begins to crack.</p>

            <p>Zara gasps. "The harmonics are collapsing!"</p>

            <p>Aria's voice cuts through the rising panic. "Everyone, step back. Izack-"</p>

            <p>Izack is already moving, reaching for the fracturing boundary, but you can see the strain on his face. The crack is spreading faster than he can repair it alone.</p>

            <p><span class="polly-comment">"Right. So this is a teachable moment about why we don't panic-quit collaborative spells. Your move, student."</span></p>
        `,
        choices: [
            {
                text: "Rejoin the collaborative effort to help stabilize it",
                next: 'crisis_collab_rescue',
                effects: { collaboration: 2, izack: 1, zara: 1 }
            },
            {
                text: "Stay back and let the teachers handle it - you don't want to make it worse",
                next: 'crisis_passive',
                effects: { collaboration: -1, izack: -1 }
            }
        ]
    },

    crisis_collab_rescue: {
        text: `
            <p>You push past your fear and reach out again - not just to Zara, but to everyone. "Together! Like before!"</p>

            <p>Zara grabs your hand immediately. The other students join. Izack's eyes widen as he feels the collaborative resonance snap into place.</p>

            <p>"That's it," he breathes. "Channel it through me - I'll direct the repair."</p>

            <p>Six students and one master mage, working as one. The fractured boundary responds to your unified intention, the cracks sealing like wounds knitting together.</p>

            <p><span class="polly-comment">"Now THIS is what I'm talking about! Crisis brings out the best collaborative magic. Well done!"</span></p>

            <p>The boundary stabilizes, then settles into a perfect, shimmering membrane. The danger passes.</p>

            <p>Aria exhales. "Impressive crisis management. You recognized that individual strength wasn't enough and chose collaboration instead."</p>

            <p>Izack smiles, clearly proud. "This is exactly why Avalon exists. You just demonstrated its core principle under pressure."</p>
        `,
        choices: [
            {
                text: "Apologize for causing the crisis, but express gratitude for learning the lesson",
                next: 'ending_collaborative_scholar',
                effects: { collaboration: 3, izack: 3, zara: 2 }
            }
        ]
    },

    crisis_aria_rescue: {
        text: `
            <p>You focus entirely on Aria's voice, blocking out the panic. "How do I stabilize it?"</p>

            <p>"Feel the boundary's natural state," Aria instructs, stepping closer. "It wants to close. Stop forcing it open and guide it back to equilibrium."</p>

            <p><span class="polly-comment">"Listen to the scary competent lady. She knows what she's talking about."</span></p>

            <p>You shift your approach - instead of controlling the portal, you <em>listen</em> to it. The boundary does have a natural state, and you can feel how it wants to return to stability.</p>

            <p>Gently, carefully, you guide rather than force. The crackling energy calms. The portal shrinks, then seals.</p>

            <p>Aria nods with satisfaction. "Well done. You trusted instruction over instinct, and you adapted your technique mid-crisis. That's the mark of a disciplined mage."</p>

            <p>Izack approaches. "And you learned to listen to the magic itself. Both of you taught the same lesson from different angles."</p>
        `,
        choices: [
            {
                text: "Thank Aria and ask to study more boundary techniques with her",
                next: 'ending_boundary_specialist',
                effects: { collaboration: 1, aria: 4, izack: 1 }
            },
            {
                text: "Thank both teachers and commit to learning collaborative magic going forward",
                next: 'ending_balanced_mage',
                effects: { collaboration: 2, aria: 2, izack: 2 }
            }
        ]
    },

    crisis_disaster: {
        text: `
            <p>You pour more power into the destabilizing portal, determined to force it under control.</p>

            <p><span class="polly-comment">"NO! Bad student! BAD-"</span></p>

            <p>The portal explodes outward. You're thrown backward as dimensional energy floods the chamber.</p>

            <p>Aria's voice cuts through reality itself: "BOUNDARY SEAL!"</p>

            <p>A wall of pure force slams down around the portal. Izack joins her, and together they compress the dimensional rupture back into stability. The effort leaves both of them visibly drained.</p>

            <p>The chamber falls silent except for heavy breathing.</p>

            <p>Aria turns to you, her expression cold. "That was reckless. You prioritized ego over safety and nearly breached dimensional barriers that protect this entire academy."</p>

            <p>Izack's disappointment is somehow worse than Aria's anger. "We teach collaboration here because <em>individual power has limits</em>. You just proved why."</p>

            <p><span class="polly-comment">"Yeah, this is... not great. You really messed up."</span></p>
        `,
        choices: [
            {
                text: "Genuinely apologize and ask for a chance to learn from this mistake",
                next: 'ending_humbled_student',
                effects: { collaboration: 0, izack: 0, aria: 0 }
            },
            {
                text: "Defend your approach - you were trying to solve it yourself",
                next: 'ending_expelled',
                effects: { collaboration: -3, izack: -2, aria: -2 }
            }
        ]
    },

    crisis_passive: {
        text: `
            <p>You step back, watching as Izack and Aria work together to seal the fracture. Their magic interweaves perfectly - his intuitive feel for dimensional currents, her precise boundary control.</p>

            <p>The crack seals. Crisis averted.</p>

            <p><span class="polly-comment">"So... you just watched. That's a choice."</span></p>

            <p>Izack turns to you, his expression gentle but serious. "You had the ability to help. Instead, you chose to be a bystander."</p>

            <p>Aria adds, "In collaborative environments, passive observation is a form of failure. Your classmates needed you."</p>

            <p>Zara looks hurt. "We're supposed to work together here."</p>

            <p><span class="polly-comment">"Harsh but true. Avalon isn't the place for people who watch others do the work."</span></p>
        `,
        choices: [
            {
                text: "Acknowledge the mistake and commit to being more engaged",
                next: 'ending_second_chance',
                effects: { collaboration: 0, izack: 0, zara: 0 }
            }
        ]
    },

    // ENDINGS

    ending_collaborative_master: {
        text: `
            <p><strong>Ending: The Collaborative Master</strong></p>

            <p>Three months later, you stand before the Spiral Spire, leading a group of seven students in a collaborative casting that creates a stable interdimensional bridge. What took Izack years to master, you and your team accomplished through perfect harmonic resonance.</p>

            <p><span class="polly-comment">"I've watched Avalon grow for years, and I can honestly say you're one of the finest examples of what this place is meant to create. Collaborative magic flows through you like breathing. Also, you're still terrible at morning portal crossings, but nobody's perfect."</span></p>

            <p>Izack approaches with tears of pride. "You've become everything I hoped Avalon could teach. Not a powerful mage who works with others - but a collaborative mage whose power comes <em>from</em> working with others."</p>

            <p>Aria nods. "You understand boundaries not as barriers but as bridges. The Third Thread flows strongest through those who truly embrace connection."</p>

            <p>Zara grins, bumping your shoulder. "Plus you're a really good friend. That matters too."</p>

            <p><span class="polly-comment">"Your story's just beginning, but what a beginning it's been. Go forth and be insufferably collaborative. Avalon's counting on it."</span></p>

            <p><em>You've discovered the true heart of Avalon: magic is strongest when shared, boundaries are meant to connect rather than divide, and the greatest power comes from listening and collaboration.</em></p>

            <p><strong>Collaboration Score: Transcendent</strong></p>
            <p><strong>Relationships: Deep bonds with Izack, Aria, and Zara</strong></p>
        `,
        choices: []
    },

    ending_collaborative_scholar: {
        text: `
            <p><strong>Ending: The Collaborative Scholar</strong></p>

            <p>Weeks pass as you immerse yourself in studying the Third Thread. Your research, conducted alongside Zara and other students, reveals new harmonics in collaborative magic that even Izack hadn't documented.</p>

            <p><span class="polly-comment">"Look at you, turning collaboration into a science. Izack's thrilled. He's been writing 'Wingscroll' notes about your discoveries for days."</span></p>

            <p>Izack reviews your latest findings. "This is remarkable. You're not just practicing collaborative magic - you're expanding our understanding of it. This will help future students immensely."</p>

            <p>Aria adds, "And you're doing it the right way - testing with partners, documenting failures as well as successes, building knowledge that others can build upon."</p>

            <p>Zara beams. "We make a good research team!"</p>

            <p><span class="polly-comment">"You've learned that magic isn't just about doing - it's about understanding, sharing, and building something bigger than yourself. That's the Avalon way."</span></p>

            <p><em>You've become a scholar of collaborative magic, dedicating yourself to understanding and teaching the principles that make Avalon unique.</em></p>

            <p><strong>Collaboration Score: Exemplary</strong></p>
            <p><strong>Relationships: Strong bonds with Izack, Zara, and the scholarly community</strong></p>
        `,
        choices: []
    },

    ending_balanced_mage: {
        text: `
            <p><strong>Ending: The Balanced Mage</strong></p>

            <p>Your training continues under both Izack and Aria, learning to balance intuitive collaboration with precise technique. You're equally comfortable in group harmonics and solo boundary work.</p>

            <p><span class="polly-comment">"You've become what Aria and Izack are together - someone who can feel the magic AND understand its mechanics. That's actually pretty rare."</span></p>

            <p>Aria observes your latest exercise with approval. "You've developed both sensitivity and discipline. That combination makes you versatile - able to adapt to any magical situation."</p>

            <p>Izack nods. "You understand that collaboration and individual skill aren't opposites. They support each other. Your solo work makes you a better partner, and your partnership work makes you a better individual mage."</p>

            <p><span class="polly-comment">"Plus you can work with pretty much anyone now. The overly cautious types, the wild experimenters, even the occasional visiting dignitary who doesn't understand Avalon's methods. You translate between approaches."</span></p>

            <p><em>You've mastered the balance between collaboration and individual expertise, becoming a bridge between different magical philosophies.</em></p>

            <p><strong>Collaboration Score: Strong</strong></p>
            <p><strong>Relationships: Respected by both Izack and Aria, trusted by peers</strong></p>
        `,
        choices: []
    },

    ending_boundary_specialist: {
        text: `
            <p><strong>Ending: The Boundary Specialist</strong></p>

            <p>Under Aria's intensive mentorship, you've become exceptionally skilled in dimensional boundary work. Your precision and control are remarkable, and you understand dimensional mechanics at a deep level.</p>

            <p><span class="polly-comment">"You took the Aria route - discipline, precision, and respect for boundaries. Not as flashy as collaborative harmonics, but you're the person everyone calls when portals start acting weird."</span></p>

            <p>Aria regards you with something close to pride. "You've developed the patience and precision that boundary work requires. You understand that dimensional magic isn't about force - it's about respect for what boundaries are and what they protect."</p>

            <p>Izack approaches. "And you're learning to incorporate collaborative elements into your work. Boundaries exist to connect realms, after all. You're understanding them as Aria does - as bridges, not walls."</p>

            <p><span class="polly-comment">"You're becoming Avalon's next boundary guardian. That's important work. Less cuddly than group harmonics, but somebody has to make sure the dimensional infrastructure doesn't collapse."</span></p>

            <p><em>You've specialized in boundary magic under Aria's guidance, becoming a guardian of dimensional stability and an expert in the structures that connect realms.</em></p>

            <p><strong>Collaboration Score: Moderate</strong></p>
            <p><strong>Relationships: Deeply mentored by Aria, respected by Izack</strong></p>
        `,
        choices: []
    },

    ending_humbled_student: {
        text: `
            <p><strong>Ending: The Humbled Student</strong></p>

            <p>Your apology was genuine, and over the following weeks, you prove it through actions. You approach every lesson with humility, ask for help readily, and prioritize safety over ego.</p>

            <p><span class="polly-comment">"You know what? You actually learned from screwing up. That's rarer than you'd think. Most people just make excuses."</span></p>

            <p>Izack watches as you successfully complete a collaborative exercise. "Failure can be the greatest teacher if we let it. You let it teach you."</p>

            <p>Aria's approval comes slowly, but it comes. "You showed me that you value safety and collaboration over pride. That's what I needed to see."</p>

            <p>Zara offers you a reassuring smile. "Everyone makes mistakes. What matters is what you do after."</p>

            <p><span class="polly-comment">"Your journey at Avalon started rough, but you're on solid ground now. Keep this humility, and you'll go far."</span></p>

            <p><em>You learned that pride comes before the fall, but humility can turn failure into growth. Your path at Avalon continues with a deeper understanding of your own limitations and the value of collaboration.</em></p>

            <p><strong>Collaboration Score: Growing</strong></p>
            <p><strong>Relationships: Rebuilding trust with teachers and peers</strong></p>
        `,
        choices: []
    },

    ending_second_chance: {
        text: `
            <p><strong>Ending: The Second Chance</strong></p>

            <p>You commit to being more engaged, and Avalon gives you that opportunity. Over the next weeks, you push yourself to participate, to reach out, to be present in collaborative work.</p>

            <p><span class="polly-comment">"You're trying. I'll give you that. Still a bit hesitant sometimes, but you're showing up."</span></p>

            <p>Zara tentatively partners with you again. "I can see you're making an effort. That means something."</p>

            <p>Izack's encouragement is gentle but firm. "Collaboration is a skill like any other. It takes practice, especially if it doesn't come naturally. Keep working at it."</p>

            <p>Aria observes from a distance, withholding final judgment but willing to let you prove yourself.</p>

            <p><span class="polly-comment">"Avalon believes in second chances, but not thirds. Make this one count."</span></p>

            <p><em>You're learning to move from observer to participant, slowly building the collaborative skills that Avalon values. Your story is still being written.</em></p>

            <p><strong>Collaboration Score: Learning</strong></p>
            <p><strong>Relationships: Tentative but improving</strong></p>
        `,
        choices: []
    },

    ending_expelled: {
        text: `
            <p><strong>Ending: The Rejected Thread</strong></p>

            <p>Your refusal to accept responsibility seals your fate. Aria's expression turns to ice.</p>

            <p>"Avalon was founded on principles of collaboration, safety, and growth through listening. You've demonstrated you value none of these things."</p>

            <p>Izack looks genuinely sad. "I wanted to believe you could learn here. But Avalon requires students who will protect each other, not endanger them for personal pride."</p>

            <p><span class="polly-comment">"Yeah, this is... this is not going to end well for you."</span></p>

            <p>Aria continues, "You're dismissed from Avalon Academy. Your portal access is revoked. I'll personally ensure you return safely to your home realm, but you are not welcome to return."</p>

            <p>As you're escorted to the departure gate, Polly lands on a nearby perch.</p>

            <p><span class="polly-comment">"You had every opportunity to learn, to grow, to be part of something amazing. You chose ego instead. I hope someday you understand what you lost here. Caw."</span></p>

            <p>The portal opens. Your brief time at Avalon ends in failure.</p>

            <p><em>Some lessons are learned too late. Avalon was not the place for you - not because you lacked talent, but because you refused to embrace what it teaches: that true power comes from collaboration, not domination.</em></p>

            <p><strong>Collaboration Score: Failed</strong></p>
            <p><strong>Relationships: Severed</strong></p>
        `,
        choices: []
    }
};

// UI Update Functions
function updateStats() {
    const collabPercent = Math.max(0, Math.min(100, 50 + (gameState.collaborationScore * 10)));
    document.getElementById('collaboration-bar').style.width = collabPercent + '%';
    document.getElementById('collaboration-value').textContent = gameState.collaborationScore;

    // Update relationship displays
    const getEmoji = (value) => {
        if (value >= 3) return '😊';
        if (value >= 1) return '🙂';
        if (value <= -2) return '😠';
        if (value <= -1) return '😕';
        return '😐';
    };

    document.getElementById('izack-rel').textContent = `Izack: ${getEmoji(gameState.relationships.izack)}`;
    document.getElementById('aria-rel').textContent = `Aria: ${getEmoji(gameState.relationships.aria)}`;
    document.getElementById('zara-rel').textContent = `Zara: ${getEmoji(gameState.relationships.zara)}`;
}

function displayNode(nodeId) {
    const node = storyNodes[nodeId];
    if (!node) return;

    gameState.currentNode = nodeId;

    // Display story text
    document.getElementById('story-text').innerHTML = node.text;

    // Display choices
    const choicesDiv = document.getElementById('choices');
    choicesDiv.innerHTML = '';

    if (node.choices.length === 0) {
        // This is an ending
        document.getElementById('restart-btn').style.display = 'block';
    } else {
        node.choices.forEach((choice, index) => {
            const button = document.createElement('button');
            button.className = 'choice-btn';
            button.innerHTML = choice.text;
            button.onclick = () => makeChoice(choice);
            choicesDiv.appendChild(button);
        });
    }

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function makeChoice(choice) {
    // Apply effects
    if (choice.effects) {
        if (choice.effects.collaboration !== undefined) {
            gameState.collaborationScore += choice.effects.collaboration;
        }
        if (choice.effects.izack !== undefined) {
            gameState.relationships.izack += choice.effects.izack;
        }
        if (choice.effects.aria !== undefined) {
            gameState.relationships.aria += choice.effects.aria;
        }
        if (choice.effects.zara !== undefined) {
            gameState.relationships.zara += choice.effects.zara;
        }
    }

    // Record choice
    gameState.choices.push({
        node: gameState.currentNode,
        choice: choice.text
    });

    // Update stats
    updateStats();

    // Move to next node
    displayNode(choice.next);
}

function restartGame() {
    gameState.currentNode = 'start';
    gameState.collaborationScore = 0;
    gameState.relationships = {
        izack: 0,
        aria: 0,
        zara: 0
    };
    gameState.choices = [];

    document.getElementById('restart-btn').style.display = 'none';
    updateStats();
    displayNode('start');
}

// Initialize game
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('restart-btn').onclick = restartGame;
    updateStats();
    displayNode('start');
});
