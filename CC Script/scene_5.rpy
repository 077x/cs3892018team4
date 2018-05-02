## Scene 5
label m_date:
    play music dim_sum fadeout 3.0 fadein 2.0
    scene black
    with fade

    show text "{color=#ffffff}{b}The next day{/b}{/color}" at truecenter
    with dissolve

    $renpy.pause(3.0, hard = True)

    scene main bedroom
    with fade

    "My first date. I can't believe it."
    "She didn't say it was a date, but it feels like it is."
    "The way she asked me..."
    "It sounded she meant it to be more than just a friendly stroll at the park."
    "I have to look casual. Good thing I watch a lof of shows on Netflix, or I would've overdressed."
    "PHEWWW!"
    "I don't want her to think badly of me."
    "{i}Don't be awkward...{/i}"
    "{i}...don't be boring...{/i}"
    "{i}...don't be yourself...{/i}"
    "{i}...be a better version of yourself...{/i}"
    "...I was thinking to myself as I was getting ready."
    "Okay, time to head for the park."

    scene black
    with fade

    show text "{color=#ffffff}{b}Later that day...{/b}{/color}" at truecenter
    with dissolve

    $renpy.pause(3.0, hard = True)

    scene park
    with fade

    show michelle normal
    with dissolve

    pov "Hey Michelle, long time no see."
    "Why did I say that? I saw her yesterday."
    m "Hahahaha. It's definitely been a while, no?"
    m "I was thinking of heading to Cop Cot."
    pov "Yeah, I'm down. I have not been to Central Park often, so I'll trust your judgement."
    "We took a little walk around."
    "We did not talk a lot."
    "We just looked at each other and smiled from time to time."
    m "I have an app called \'Questions\', we can play it while we walk there."
    pov "Wow, you planned everything so well."
    m "I am only looking for things to do to fill in the silence."

    with vpunch
    "Suddenly, Michelle grabbed my hand and pulled me closer."
    "Her hand felt warm..."
    "My heart was about to burst out my chest."
    "I didn't want to ruin the moment, so I didn't say anything. I tried to contain myself."

    menu:
        m "Before making a telephone call, do you ever rehearse what you are going to say? Why?"

        "\"No\"":
            pov "No, I am pretty good with improvising."
            m "Wow, I can't do that."
            m "It's kinda hard for me. I like to be prepared for everything."

        "\"Yes\"":
            pov "Yes, I tend to forget what I am supposed to say."
            pov "I start to go off topic and forget why I called in the first place."
            m "Hahaha! That is totally me!"
            m "Sometimes I write down what I have to say to be extra prepared."

    m "Okay now you ask."

    pov "Okay. Let me think..."
    pov "Given the choice of anyone in the world, whom would you want as a dinner guest?"
    m "Easy."
    m "Stephen Hawking."
    pov "Really? Why?"
    m "Because I fell in love with the movie \'The Theory of Everything\'."
    m "Even though he was suffering from an illness, he still tried to make a difference in the world."
    m "It's really inspiring."
    m "I just want to hear how he fought through life like that."
    pov "Wow, that's really cool. Maybe I should watch the movie some time."
    m "Yeah, we should watch the movie together. I'd love to see it again."
    m "For the third time."
    m "My turn again."

    menu:
        m "Would you like to be famous? In what way?"

        "\"Video game streamer\"":
            pov "I would love to be a famous streamer. Kind of like that guy on Twitch, Ninja."
            m "Oh yeah! I heard about him making like 500k a month. That's pretty fun playing video games and getting paid."

        "\"Basketball player\"":
            pov "I'd like to be a famous basketball player, like Paul George. That would be the dream!"
            m "Oh, I don't know who that is. I know Lebron James."
            m "Hehehe."
            m "That would be nice being to able to play a sport and get paid for it."

    pov "For what in your life do you feel most grateful?"
    m "I am grateful for my family. They have always been there for me when I needed them."

    # menu:
    #     m "So what do you value most in a friendship?(Damn I don't have friends I'll make something up.)"
    #
    #     "Trust. I would want a friend that I can count on whenver I need them":
    #         m "Yeah I feel the same way."
    #
    #     "Fun to be around. I think its good to have friends that make you have a good time.":
    #         m "Oh okay that's cool."
    #
    # pov "If a crystal ball could tell you the truth about yourself, your life, the future, or anything else, what would you want to know?"
    # m "I would like to know my future."
    # m " This way I can prepare to spend my time on things that would help my future than wasting my time on other things that will not accomplish anything."
    # pov "Always preparing for stuff. I wish I could be as organized as you."
    # m "I'm not that organized. My room is a mess sometimes."
    # m "But my turn to ask."
    #
    # menu:
    #     m "What is the greatest accomplishment of your life?"
    #
    #     "Meeting you":
    #         m "Awww. Thanks your so cute."
    #
    #
    #     "Being Born":
    #         m "Ha ha ha. Your so funny"
    #         pov "I'm not too proud of anything."
    #
    # pov "Let's get on to the next question. If you could wake up tomorrow having gained anyone quality or ability, what would it be?"
    # m "I would like to be able to control time. This way everything I do can go as planned."
    # m "If something messes up I can fix the mistake right away."
    # m "Freezing and slowing down time would be pretty cool too."
    # pov "Yeah that would definetly be usefule to have."
    # pov "I could achieve my dreams with that ability."
    # m "Mhmm now my turn."
    #
    # menu:
    #
    #     m "When did you last sing to yourself? To someone else?"
    #
    #     "I have nevered singed in my whole entire life.":
    #         m "Why not?"
    #         pov "Because the thought of hearing my voice trying to sing scares me."
    #         m "Now I want to hear you sing."
    #         pov "Um maybe in like 20 years but we'll see"
    #
    #     "I sang in the shower but only in the shower.":
    #         m "Wow really can I hear?"
    #         pov "I can only sing in the shower."
    #         m "Okay I see. I know how to hear you sing now."
    #         pov "Really how?"
    #         m "Don't worry about it."
    #
    # pov "Okay I'm moving on to the next question."
    # pov "How close and warm is your family? Do you feel your childhood was happier than most other people's??"
    # m "I have'nt told this to anyone, but sometimes I wish I had different parents."
    # m "They always compare me to my cousins and say how much better they are than I am."
    # m "All they want me is to study and be something they want, but they never ask what I want."
    # m "They want me to get a perfect grades, so they can brag about it to their family and friends."
    # m "Sometimes I think all they care about is their money, their status, their property, but not their own daughter."
    # m "But at the same time I don't want to disappoint them."
    # m "I'm sorry for rambling."
    # pov "It's okay I'm here for you."
    # m "Thanks [povname]"

    "We reach Cop Cot and decide to take a seat."
    m "Now that we're done with the questions, the app says to stare into eachother's eyes for 4 minutes."
    "That sounds weird."
    m "Do you want to do this?"
    "This may be an opportunity."
    pov "Yeah, haha, sure."
    "As I stared into her eyes, I could feel this stream of energy."
    "She was giving off this exhilarating sensation."
    "At that moment, she looked beautiful."

    menu:
        "Do nothing":
            jump to_be_cont

        "Go for the kiss":
            jump to_be_cont
