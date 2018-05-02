## Scene 4
label scene4_elaine:
    scene black
    with fade


    show text "{color=#ffffff}{b}A few days later...{/b}{/color}" at truecenter
    with dissolve

    $renpy.pause(3.0, hard = True)

    scene main bedroom
    with fade

    if e_likes < 6:
        "There's nothing to do today."
        "I {i}could{/i} do some homework, but I'd rather binge on Netflix."
        "I'll try to text Elaine again."
        "{i}Hey, what are you up to today? Let's hang out.{/i}"
        "Now I wait..."

        $renpy.pause(3.0)

        with hpunch
        "{b}BZZZZ{/b}"
        "I hope that's her...."
        e "{i}Hi, sorry. Super busy today.{/i}"
        "I... I thought she liked being with me."
        "She might actually be busy."
        "Or maybe she doesn't like me as much as I thought she did."
        "I thought going to the Chinese Club will help me find new people to hang out with."

        jump neutral_ending1

    elif e_likes >=6:
        with hpunch
        "{b}BZZZZ{/b}"
        "What's this?"
        "It's from Elaine...."
        "{i}Seeing that text message made me feel great.{/i}"
        e "{i}Hey, [povname], how are you? Let's hang out today. I've had a good time with you on Saturday.{/i}"
        "My instinct was to immediately reply."
        "I feel great being with her."
        "But I am scared."

        $renpy.pause(2.0)

        "This is something I am not willing to lose."
        "Finally, I have something that feels more than just friendship..."
        "Something more...."

        menu:
            "\"Of course, I'd love that.\"":
                pov "{i}Of course! I would love to see you again.{/i}"
                pov "{i}Where should we meet?{/i}"
                e "{i}Come over to my place. Nobody is here.{/i}"
                pov "{i}Sounds great. What time do you want me to come?{/i}"
                e "{i}Now is good.{/i}"
                pov "{i}I'll be on my way.{/i}"
                jump elaine_date

            "\"I'm sorry, I can't see you today.\"":
                pov "{i}I am sorry, Elaine. I won't be able to see you today.{/i}"
                with hpunch
                "{b}BZZZZ{/b}"
                with hpunch
                "{b}BZZZZ{/b}"
                e "{i}What do you mean??{/i}"
                e "{i}Did something happen?!{/i}"
                pov "{i}No, nothing happened. I am sorry.{/i}"
                "I did not bother looking at the phone after that interaction."

                jump bad_ending2


label elaine_date:
    scene bus_stop
    with fade
    "It was a wonderful day outside."
    "The weather was extremely pleasant."
    "Yet, I was feeling so stressed."
    "I was nervous-- to meet Elaine again."
    "Of course, I like being with her."
    "But I still felt strange."
    "I guess I can only hope for today to go well...."

    scene linda bedroom
    show elaine normal
    with fade


    e "Hey [povname], welcome to my humble place!"

    "The place was surprisingly very cozy."
    "I always imagined Elaine's room to be completely unorganized. I don't know why. Just a thought."
    "While her room was quite small, it felt just right."
    "Maybe it was some \'in-the-moment\' feeling..."
    "Who knows."
    e "What are you day-dreaming about?"
    pov "What?"
    e "You're just staring at my bed over there, not saying anything."
    e "What were you thinking about?"
    pov "Oh, nothing. Your room is..."
    pov "It's..."
    e "What? Trashy?"
    with vpunch
    pov "NO!"
    pov "I meant to say it looks nice. Looks cozy."
    e "Don't lie, [povname], I {i}know{/i} it's {i}not{/i} nice."
    e "I am kidding."
    e "But it's definitely not the best-looking room."
    e "Enough about this..."
    e "How have you been?"
    pov "I've been doing alright. Just doing school work, not much else, honestly."
    e "Yep, I'm on the same boat as you."
    e "Oh, how rude of me; would you like something to eat? Drink? Maybe smoke? I have this new stuff that is {i}{b}Really. Freaking. Good.{/b}{/i} "
    menu:
        "Eat":
            pov "I'll just have something to eat, thanks."
            e "I only have some snacks and leftovers."
            pov "That's fine."

        "Drink":
            pov "I'll just have a drink."
            e "I've got all sorts of drinks. My dad thinks he can hide the booze, but I always find the bottles."
            pov "Uhhh...."
            pov "I meant a drink as in water, or soda."
            e "Awww. That's not fun though."

        "Smoke":
            pov "I never smoked."
            e "I am here with you, you'll be fine."
            "I was thinking about it as I was looking at her."
            "She was smiling at me. Her face was glistening."
            "Although I was willing to bond with Elaine over a smoking session, I felt it was not the right move... for now."
            pov "I'll actually pass."
            pov "Maybe some other time. Heheheh."
            e "Alright, man. Your choice. I won't smoke without you. It's not courteous."

    e "I told you this already..."
    e "By now I really like you."
    pov "So we are past the \"starting to like me\"?"
    e "Hahahah! Yes, we are."
    e "Meeting you at the Chinese Club was great. I happy we met when we did."
    pov "I am too."
    e "What do you think of the Chinese Club?"
    pov "I think Michelle is doing a good job."
    e "She is, yes."
    pov "Are you two close?"
    e "We haven't been speaking a lot these past few months. We were really close friends before, though."
    pov "What happened?"
    e "It doesn't matter..."
    pov "Is it..."
    e "I won't get into it."
    "I understood that tone of voice."
    "I shouldn't try to push her. This may be a sensitive topic for her."

    if e_poker_help:
        pov "Would you like to play some Chinese Poker?"
        e "Sure, but I'll have to let you win some rounds."
        pov "Aw, come on! I've been practicing."
        e "Let's see then."
        "We had a couple of rounds. They were absolutely enjoyable."
        "I won two out of five rounds, although I feel as if Elaine let me win. Like she said she would."


    if e_make_music:
        e "Oh, I remember you told me you make music."
        pov "Yes, let me show you some of my work."

        play music mym fadeout 2.0 fadein 1.0

        e "I would love that."
        "I handed her my phone and a pair of headphones."

        "Just as the music started playing, Elaine was nodding her head."

        e "This is lovely!"

        $renpy.pause(2.0, hard = True)

        e "This is actually really good!"
        "I felt wondeful."
        "This is the very moment I wished to experience..."
        "Just me..."
        "...and Elaine..."
        "...together."

    stop music fadeout 5.0
    with hpunch
    "{i}{size=+10}KNOCK KNOCK KNOCK{/size}{/i}"
    with hpunch
    "{i}{size=+10}KNOCK KNOCK KNOCK{/size}{/i}"
    "Someone was banging on the apartment's door really loudly."
    "I could feel the walls shaking."
    who "{b}ELAINE!{/b}"
    who "{b}ELAINE! OPEN UP!{/b}"
    if e_make_music:
        "Elaine quickly took the headphones off of her head."
    "Her smile quickly faded away."
    e "Oh god."
    e "Oh no no no."
    e "What is he doing here?"
    pov "What's going on?!"
    e "Stay here, don't leave my room. I'll handle it."
    e "Just stay here!"

    hide elaine
    with dissolve

    "I knew something was wrong. I had to help her."
    "There was yelling from the other side of the door."
    e "You can't go in there! STOP!"
    e "{b}TYLER, STOP!{/b}"
    "\"Tyler\"?"
    "I have never heard that name."
    "I headed to the door, when it suddenly swung open."
    "It was Tyler, he entered the room in a rush."

    show tomer normal
    with dissolve

    "While he sounded furious a minute ago, he appeared calm; he looked composed."

    t "We need to talk, pal."

    jump to_be_cont
