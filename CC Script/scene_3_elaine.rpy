## Scene 3
label second_club_meeting:
    # $scene2 = True

    play music club_theme fadeout 5.0 fadein 5.0

    scene black
    with fade

    show text "{color=#ffffff}{b}Second Club Meeting{/b}{/color}" at truecenter
    with dissolve

    $renpy.pause(3.0, hard = True)

    scene hallway morning
    with fade

    "Finally, class is done."
    "Time to visit Michelle's Chinese Club"

    scene club room1
    with fade

    "I come back to the club room, and everyone else was there...."
    "Except for Elaine."
    "I look for a seat, when Elaine suddenly walked in."

    show elaine normal at left
    with dissolve
    e "Don't mind me..."
    hide elaine

    show michelle normal
    with dissolve

    m "Hello everyone!"
    m "Thank you for coming to our second meeting!"

    #show michelle happy

    m "I have an important announcement:"
    m "We are having the Culture Fair in a month, and I want to prepare for it as soon as possible."
    m "We will need to work together, and research about Chinese culture."
    m "I'll be working on clothing. Everyone else, split into working on \'music\' and \'food\'."

    show elaine normal at left
    with dissolve

    e "I'll work on music."

    show linda normal at right
    with dissolve

    l "Ummm"
    l "I'll... I'll do food, I guess."

    hide michelle
    hide elaine
    hide linda
    with dissolve

    show chris normal
    with dissolve

    ch "I'll help with decorations!"

    hide chris
    with dissolve

    show michelle normal
    with dissolve


label culture_fair_choice:
    menu:
        m "Hey, [povname], what do you want to work on?"

        "Food":
            $food_choice = True
            hide michelle
            with dissolve

            show linda normal
            with dissolve

            l "Hey, [povname], it's... it's okay."
            l "Ummm... I think I can do this by myself."
            l "Th--Thank you for offering your help, though."

            hide linda
            with dissolve

            show michelle normal
            with dissolve

            jump culture_fair_choice

            # l "I guess you're working with me."
            # pov "Yes, I'd like to research on some foods!"

            hide linda
            with dissolve

        "Clothing":
            $clothing_choice = True
            m "Okay, you'll be working with me!"

        "Music":
            $music_choice = True
            $e_likes += 1
            hide michelle
            with dissolve

            show elaine normal
            with dissolve

            e "Really? Why did you choose music?"
            pov "Well...."

            $renpy.pause(2.0, hard = True)

            hide elaine
            with dissolve


    show michelle normal
    with dissolve

label second_club_meeting_end:
    m "So that settles it."
    m "We'll end the club meeting early today."
    m "Oh, and of course, can't forget about a quick Chinese culture fact:"
    m "Fortune cookies are not traditional Chinese food. They were actually made in San Francisco in 1920."

    $addtodb_gen("Fortune cookies are often served as a dessert in Chinese restaurants in the United States and other Western countries, but are not a tradition in China.")
    $renpy.notify("New Chinese fact added to Journal")

    m "I will see you all next time, have fun with the Culture Fair work!"
    hide michelle
    with dissolve

    if clothing_choice == True:
        jump culture_fair_clothing
    elif music_choice == True:
        jump culture_fair_music
    else:
        jump culture_fair_food

label culture_fair_clothing:
    $renpy.pause(3.0)

    show michelle normal
    with dissolve

    m "Hey, since we're going to research about clothing together, I need a way to contact you."
    m "What's your number?"
    pov "He...Here you go."

    $renpy.pause(2.0)

    pov "When do you want to meet up to work on this Culture Fair stuff?"
    m "We could meet up on Saturday at my house, in the afternoon."
    m "Does that work for you?"
    pov "Sure, I'll see you there."
    m "Goodbye, [povname], I will see you on Saturday!"

    # $add_m_info("Michelle seems very nice.")
    # $renpy.notify("Michelle character updated")

    jump saturday_michelle

# label culture_fair_food:
#     $renpy.pause(3.0)
#
#     show linda normal
#     with dissolve
#
#     l "Hey, [povname], right?"
#     l "It seems like we are going to work together on foods for the Culture Fair!"
#     pov "Yes, I am excited!"
#     l "When do you want to meet?"
#     pov "What day is good for you?"
#     l "Saturday afternoon?"
#     pov "That works. Where should we meet?"
#     l "I guess you could come by my place, I will text you the address."
#     pov "Great, see you then."
#     "She smiled and left the room."
#
#     # $add_l_info("Linda appears to be quite shy.")
#     # $renpy.notify("Linda character updated")
#
#     jump saturday_linda

label culture_fair_music:
    $renpy.pause(3.0)

    show elaine normal
    with dissolve

    e "Here's my number."
    e "So we can work together on this."
    pov "Uhh, okay."
    e "You know I was just messing with you earlier, yeah?"

    $renpy.pause(1.0)

    e "But I actually forgot your name."
    pov "It's [povname]."
    pov "I look forward to working with you, Elaine."
    "She smiled slightly."
    e "Yeah, yeah."
    e "Just text me when you want to meet up."

    # $add_e_info("Elaine seems to like teasing me.")
    # $renpy.notify("Elaine character updated")
    jump saturday_elaine



## Researching on Saturday with Elaine
label saturday_elaine:
    default self_research = False

    play music quirk fadeout 5.0 fadein 15.0

    scene black
    with fade

    show text "{color=#ffffff}{b}Saturday{/b}{/color}" at truecenter
    with dissolve

    $renpy.pause(3.0)

    default text_name = False
    scene main bedroom
    with fade

    pov "I haven't texted Elaine since the last club meeting."
    pov "There's nothing to do all day, so I might as well text her now."
    pov "{i}Hey Elaine, let's work on the Culture Fair together.{/i}"
    pov "Okay, now I wait..."
    "..."
    with hpunch
    "{b}BZZZZ{/b}"
    pov "That was fast!"

    $renpy.pause(2.0)

    pov "Oh, nevermind."
    pov "That was just an email."
    "I got excited for nothing"
    menu:
        "What do I do until she replies to me?"

        "Sleep":
            "I could use a nap."
            scene black
            with fade
            $renpy.pause(3.0, hard = True)

            jump elaine_on_phone

        "Text Elaine again":

            menu:

                "\"{i}Hey, what's up?{/i}\"":
                    pov "{i}Hey, what's up?{/i}"
                    jump elaine_on_phone

                "\"{i}Hello?{/i}\"":
                    pov "{i}Hello?{/i}"
                    jump elaine_on_phone

                "\"{i}It's [povname]{/i}\"":
                    $text_name = True
                    pov "{i}It's [povname]{/i}"
                    jump elaine_on_phone

        "Research":
            $self_research = True
            "I'll start working on this."
            $renpy.pause(2.5)
            "Interesting."
            "It says on the on this website that the term \'Shidaiqu,\' which means \"music of the era\" or \"popular music,\""
            "Is used to describe all contemporary music sung in Mandarin and other Chinese dialects recorded in China, from 1920 to 1952."
            $addtodb_mus("The term \"Shidaiqu\" means \"music of the era,\" or \"popular music\". It is used to describe all contemporary music sung in Mandarin and other Chinese dialects recorded in China from 1920 to 1952.")
            $renpy.notify("New Chinese fact added to Journal")


label elaine_on_phone:
    default meeting_elaine_house = False
    default meeting_elaine_diner = False
    default e_make_music = False

    show main bedroom
    with hpunch
    "{b}BZZZZ{/b}"
    with hpunch
    "{b}BZZZZ{/b}"
    "Oh, is that her?"
    e "{i}WHAT??{/i}"
    e "{i}I'M BUSY!!!{/i}"
    "Yep, definitely her."

    if text_name == False:
        e "{i}Who is this???{/i}"
        pov "{i}It's [povname]{/i}"

    pov"{i}How are you so busy?{i}"
    e "{i}What do you care?{i}"
    e "{i}I have things to take care of.{/i}"
    pov "{i}What about the Culture Fair? It's really soon.{/i}"
    e "{i}Ohhh, darn. You're right!{/i}"

    $renpy.pause(2.0)

    e "{i}I can't meet at my place. Can we meet somewhere else?{/i}"

    menu:
        "Where should we meet?"

        "My house":
            $meeting_elaine_house = True
            pov "{i}You could come over to my place.{/i}"
        "Diner":
            $meeting_elaine_diner = True
            pov "{i}I can meet you at {b}Champ's Diner{/b}"

    e "{i}Okay, I will meet you there in an hour.{/i}"

    scene black
    with fade

    show text "{color=#ffffff}{b}Later that day...{/b}{/color}" at truecenter
    with dissolve

    $renpy.pause(3.0)

    if meeting_elaine_house:
        jump meet_elaine_house
    elif meeting_elaine_diner:
        jump meet_elaine_diner

label meet_elaine_house:
    scene main bedroom
    with fade
    "Elaine is going to get here soon."
    "{b}KNOCK KNOCK{/b}"
    "That's probably her."

    show elaine normal
    with dissolve

    e "Hey [povname], sorry I am late."
    e "I had some stuff going on at home."
    pov "Is everything okay?"
    e "Yes, yes. I just needed to deal with some issues, you don't need to worry about it."
    pov "Let's get to work."
    e "Yeah."

    menu:
        "Pretend to listen (Skip)":
            show black behind elaine
            with dissolve
            "I completely zoned out."
            "I just stared at her."
            "Smiled and nodded here and there..."
            "She mentioned something about \'Pop music\'..."
            "And \'Shanghai\'..."
            "But then..."
            hide black
            with dissolve

            jump music_quiz_bedroom

        "Work on the research":
            e "Here is some stuff that I found about CantoPop:"
            if self_research == False:
                e "The term \"Shidaiqu,\" which means \"music of the era,\" or \"popular music,\""
                e "Is used to describe all contemporary music sung in Mandarin and other Chinese dialects which were recorded in China from 1920 to 1952."
                $addtodb_mus("The term \"Shidaiqu\" means \"music of the era,\" or \"popular music\". It is used to describe all contemporary music sung in Mandarin and other Chinese dialects recorded in China from 1920 to 1952.")

            e "It says on this website that Shanghai was the main hub of the Chinese popular music recording industry."
            pov "Uh huh. Sounds interesting."
            pov "I am not sure I understand exactly what's \"CantoPop\"."
            e "Cantonese Pop music."
            pov "So, why are we talking about \"CantoPop\"?"
            e "Because this is the part of Chinese Culture that is most popular around here."
            pov "Oh, I see now."
            e "There's this guy, Li Jinhui, who is very important in all of this."
            e "He is known as the father of CantoPop."
            e "Around 1927, he composed the song \"The Drizzle.\""
            e "His daughter, Li Minghui, was on the vocals for the song."
            e "Apparently the song is also generally regarded as the first Chinese Pop song."
            pov "That sounds cool."
            e "In 2000, EolAsia.com was founded as the first online CantoPop music portal in Hong Kong."
            e "The company survived the dot-com bubble and offered online legal music downloads in February 2005."
            e "The site primarily targets consumers in Hong Kong and Macau, but some songs require Hong Kong id to purchase."


            $addtodb_mus("Shanghai was the main hub of the Chinese popular music recording industry, and important name of the period is composer {i}Li Jinhui{/i}, also known as the father of C-Pop.")
            $addtodb_mus("\"The Drizzle,\" composed by Li Jingui, was sung by his daughter, Li Minghui. The song is generally regarded as the first Chinese pop song. The tune fuses jazz and Chinese folk music.")
            $addtodb_mus("In 2000, EolAsia.com was founded as the first online C-pop music portal in Hong Kong.")
            $addtodb_mus("The company survived the dot-com bubble and offered online legal music downloads in February 2005.")
            $renpy.notify("New Chinese facts added to Journal")


            e "Perhaps this is too much for the Cultural Fair-- talking about legality stuff..."
            pov "We can work with it."
            pov "That sounds interesting, though. Downloading music has left an impact on the music industry as a whole,"
            pov "So that fact is definitely important."
            e "I guess."
            pov "I think this is good enough for the Culture Fair, no?"
            e "Really? Were you actually listening this whole time?"
            pov "Yes, obviously."
            e "So you understood what I was reading?"
            pov "Surely..."

            jump music_quiz_bedroom

label music_quiz_bedroom:
    $music_quiz_ans = 0
    menu:
        e "Do you remember what song was regarded as the first Chinese Pop song?"

        "Drizzle":
            $music_quiz_ans += 1
            $e_likes +=1

        "Grizzle":
            e "Hahaha."
            e "No."

        "Scribble":
            e "Hmmmm."

    menu:
        e "What was the main hub of Chinese popular music recording industry?"

        "Hong Kong":
            e "Were you really listening?"

        "Beijing":
            e "I really don't think you listened to me."

        "Shanghai":
            $music_quiz_ans += 1
            $e_likes +=1

    menu:
        e "What about the father of CantoPop? Do you remember who he was?"

        "Tommy Lee Jones":
            e "Nah."
            e "He is the American actor, silly."

        "Li Jinhui":
            $music_quiz_ans += 1
            $e_likes +=1

        "I am not good with names":
            e "So am I."

    menu:
        e "Lastly, what website was founded as the first online C-Pop music portal in Hong Kong?"

        "CantoPop.com":
            e "Hmmm."

        "CantoPop-to-mp3.net":
            e "That doesn't sound right."

        "EolAsia.com":
            $music_quiz_ans += 1
            $e_likes +=1

    if music_quiz_ans == 1:
        e "Well, it seems you weren't actually listening, but you got one thing right."
        e "Maybe you made the right guess? Hahaha!"

    elif music_quiz_ans == 2:
        e "You got {i}some{/i} things right. Maybe you were listening after all."

    elif music_quiz_ans == 3:
        e "Wow, you really listened to what I read? That's reassuring. Thanks!"
        e "Although you did get one thing wrong there."

    elif music_quiz_ans == 4:
        e "Oh my God! I am so happy I did not bore you with all this information!"
        e "Thank you for listening to what I read!"

    else:
        e "You did not get anything I asked you correctly."
        pov "Oops."

    e "Now that I think about it..."
    e "We could have probably just looked up CantoPop songs instead of reading all of this..."
    e "...just play different songs at the Fair, and be done with it."
    e "Ugh..."

    e "It was nice working with you, but I need to go now."
    pov "Oh, really? It's still quite early. We can do some more work--"
    e "No, sorry. I really need to get going."
    if e_likes <= 2:
        hide elaine
        with dissolve

        "I wish she had stayed for longer."
        "Maybe she doesn't really like me."

        jump scene4_elaine

    elif e_likes == 3:
        e " I will see you at the club, [povname]."
        pov "Sure, see you there..."
        hide elaine
        with dissolve

        "I wish she had stayed for longer."
        "Maybe she doesn't really like me."

        jump scene4_elaine

    elif e_likes >= 4:
        pov "Hey, relax. There's nothing to rush, right?"
        pov "We are done with the research, so let's chill for a bit."
        e "I guess we could. You're right."
        e "You're pretty nice. I'm starting to like you."
        pov "Just \"starting\"?"
        e "Hahaha."
        e "Yes. You did not seem like someone I would hang out with outside of school."
        "That's reassuring..."
        e "What?"
        pov "Nothing, I didn't say anything."
        menu:
            e "What do you like to do outside of school?"

            "\"I like to play video games\"":
                pov "I like to play video games."
                e "Like what kind of video games? I am not really a gamer. I know Linda plays some games..."
                pov "Yes, she plays League of Legends! I do too."
                pov "It's a very popular top-down strategy, action-packed game where you---"
                e "Uh huh."
                e "Hahaha."
                pov "What's so funny?"
                e "Just looking at your face brightening up as you speak of your game."
                pov "I am just really into video games."

            "\"I play a bit of basketball\"":
                pov "I play some basketball. Not that great at it."
                e "I am not a sports person myself either."
                pov "I need to practice more."

                if e_poker_help:
                    e "I'll bet with you I can still score more shots than you!"
                    pov "Again with the betting? You are actually into that, huh?"
                    e "Well, what are we betting on?"
                    pov "I don't want to bet anything yet."
                    e "Come on! Let's have some fun with this!"

            "\"I make music\"":
                $e_make_music = True
                $e_likes += 1
                pov "In my free time, I make music."
                e "Oh my god! Really?"
                e "What kind of music?"
                pov "It's a mixture of genres. Some type of electronic music."
                e "Can I hear some?"
                pov "I will give you a listen some day. Haha!"
                e "I would love that! I am really into all sorts of genres."
                e "This summer I am actually going to this music festival."
                pov "Oh wow, that sounds awesome. What festival is that?"
                e "Electric Daisy Carnival in Las Vegas! I am so excited!"
                pov "Aren't you too young for this?"
                e "Maybe..."
                e "Who cares, dude? It's a freaking music festival! I just want to have fun!"
                pov "These festivals definitely seem like a ton of fun."

        e "It's getting pretty late now, I better get going."
        e "I had a really good time with you today, [povname]."
        pov "I did too, Elaine."

        if e_likes >= 6:
            $renpy.pause(2.0, hard = True)
            pov "Oh, Elaine?"
            e "Yes?"
            pov "What did you mean earlier when you said you \"had stuff going on at home\"?"
            e "It's nothing, really. I did not mean anything."
            pov "You sounded very concerned when you mentioned it."
            pov "You also sounded preoccupied when you said on the phone that I couldn't come over to your place..."
            e "Let's just say that my stepdad isn't the nicest guy you'd meet."
            pov "Elaine...."
            e "What?"
            pov "Has he done anything to you?"
            e "Has he harmed me? No."
            e "He just likes to talk. He never shuts up."
            e "I did not want you to come over because he would just make a scene."
            e "Just like with my ex-boyfriend."
            pov "Your ex?"
            e "Yeah, this guy. A complete douche. He also goes to our school."
            pov "Oh. I wonder if I had run into him."
            e "Unlikely. He doesn't hang out around our spot."
            e "Don't worry about me."
            e "Don't get me wrong, you're very sweet, and kind. I like you."
            e "But this stepdad and ex stuff is just not something you should be concerened about."
            pov "I understand."
            e "I will be on my way now."

        if e_poker_help:
            e "Maybe I could teach you a couple more things about Chinese Poker sometime?"
            pov "For sure, I would love to learn from a true master!"
            e "Hahaha, I am not {i}that{/i} great."
            pov "You're pretty darn good, you cannot lie."

        e "I will see you soon!"
        pov "Take care, I will talk to you later."

        hide elaine
        with dissolve

    jump scene4_elaine

label meet_elaine_diner:
    scene diner night
    with fade

    "There she is, sitting by the booth."

    show elaine normal
    with dissolve

    e "Hey [povname]."
    pov "Hey Elaine, how are you?"
    e "I'm doing alright, had some stuff going on at home."
    pov "Is everything okay?"
    e "Yes, yes. I just needed to deal with some issues, you don't need to worry about it."
    pov "Let's get to work."
    e "Yeah."

    menu:
        "Pretend to listen (Skip)":
            show black behind elaine
            with dissolve
            "I completely zoned out."
            "I just stared at her."
            "Smiled and nodded here and there..."
            "She mentioned something about \'Pop music\'"
            "And \'Shanghai\'..."
            "But then..."
            hide black
            with dissolve

            jump music_quiz_diner
        "Work on the research":
            e "Here is some stuff that I found about CantoPop:"
            if self_research == False:
                e "The term \"Shidaiqu,\" which means \"music of the era,\" or \"popular music,\""
                e "Is used to describe all contemporary music sung in Mandarin and other Chinese dialects which were recorded in China from 1920 to 1952."
                $addtodb_mus("The term \"Shidaiqu\" means \"music of the era,\" or \"popular music\". It is used to describe all contemporary music sung in Mandarin and other Chinese dialects recorded in China from 1920 to 1952.")

            e "It says on this website that Shanghai was the main hub of the Chinese popular music recording industry."
            pov "Uh huh. Sounds interesting."
            pov "I am not sure I understand exactly what's \"CantoPop\"."
            e "Cantonese Pop music."
            pov "So, why are we talking about \"CantoPop\"?"
            e "Because this is the part of Chinese Culture that is most popular around here."
            pov "Oh, I see now."
            e "There's this guy, Li Jinhui, who is very important in all of this."
            e "He is known as the father of CantoPop."
            e "Around 1927, he composed the song \"The Drizzle.\""
            e "His daughter, Li Minghui, was on the vocals for the song."
            e "Apparently the song is also generally regarded as the first Chinese Pop song."
            pov "That sounds cool."
            e "In 2000, EolAsia.com was founded as the first online CantoPop music portal in Hong Kong."
            e "The company survived the dot-com bubble and offered online legal music downloads in February 2005."
            e "The site primarily targets consumers in Hong Kong and Macau, but some songs require Hong Kong id to purchase."

            $addtodb_mus("Shanghai was the main hub of the Chinese popular music recording industry, and important name of the period is composer {i}Li Jinhui{/i}, also known as the father of C-Pop.")
            $addtodb_mus("\"The Drizzle,\" composed by Li Jingui, was sung by his daughter, Li Minghui. The song is generally regarded as the first Chinese pop song. The tune fuses jazz and Chinese folk music.")
            $addtodb_mus("In 2000, EolAsia.com was founded as the first online C-pop music portal in Hong Kong.")
            $addtodb_mus("The company survived the dot-com bubble and offered online legal music downloads in February 2005.")
            $renpy.notify("New Chinese facts added to Journal")


            e "Perhaps this is too much for the Cultural Fair-- talking about legality stuff..."
            pov "We can work with it."
            pov "That sounds interesting, though. Downloading music has left an impact on the music industry as a whole,"
            pov "So that fact is definitely important."
            e "I guess."
            pov "I think this is good enough for the Culture Fair, no?"
            e "Really? Were you actually listening this whole time?"
            pov "Yes, obviously."
            e "So you understood what I was reading?"
            pov "Surely..."

            jump music_quiz_diner


label music_quiz_diner:
    $music_quiz_ans = 0
    menu:
        e "Do you remember what song was regarded as the first Chinese Pop song?"

        "Drizzle":
            $music_quiz_ans += 1
            $e_likes +=1

        "Grizzle":
            e "Hahaha."
            e "No."

        "Scribble":
            e "Hmmmm."

    menu:
        e "What was the main hub of Chinese popular music recording industry?"

        "Hong Kong":
            e "Were you really listening?"

        "Beijing":
            e "I really don't think you listened to me."

        "Shanghai":
            $music_quiz_ans += 1
            $e_likes +=1

    menu:
        e "What about the father of CantoPop? Do you remember who he was?"

        "Tommy Lee Jones":
            e "Nah."
            e "He is the American actor, silly."

        "Li Jinhui":
            $music_quiz_ans += 1
            $e_likes +=1

        "I am not good with names":
            e "So am I."

    menu:
        e "Lastly, what website was founded as the first online C-Pop music portal in Hong Kong?"

        "CantoPop.com":
            e "Hmmm."

        "CantoPop-to-mp3.net":
            e "That doesn't sound right."

        "EolAsia.com":
            $music_quiz_ans += 1
            $e_likes +=1

    if music_quiz_ans == 1:
        e "Well, it seems you weren't actually listening, but you got one thing right."
        e "Maybe you made the right guess? Hahaha!"

    elif music_quiz_ans == 2:
        e "You got {i}some{/i} things right. Maybe you were listening after all."

    elif music_quiz_ans == 3:
        e "Wow, you really listened to what I read? That's reassuring. Thanks!"
        e "Although you did get one thing wrong there."

    elif music_quiz_ans == 4:
        e "Oh my God! I am so happy I did not bore you with all this information!"
        e "Thank you for listening to what I read!"

    else:
        e "You did not get anything I asked you correctly."
        pov "Oops."

    e "Now that I think about it..."
    e "We could have probably just looked up CantoPop songs instead of reading all of this..."
    e "...just play different songs at the Fair, and be done with it."
    e "Ugh..."

    e "It was nice working with you, but I need to go now."
    pov "Oh, really? It's still quite early. We can do some more work--"
    e "No, sorry. I really need to get going."
    if e_likes <= 2:
        hide elaine
        with dissolve

        "I wish she had stayed for longer."
        "Maybe she doesn't really like me."

        jump scene4_elaine

    elif e_likes == 3:
        e " I will see you at the club, [povname]."
        pov "Sure, see you there..."
        hide elaine
        with dissolve

        "I wish she had stayed for longer."
        "Maybe she doesn't really like me."

        jump scene4_elaine

    elif e_likes >= 4:
        pov "Hey, relax. There's nothing to rush, right?"
        pov "We are done with the research, so let's chill for a little while."
        e "I guess we could. You're right."
        e "You're pretty nice. I'm starting to like you."
        pov "Just \"starting\"?"
        e "Hahaha."
        e "Yes. You did not seem like someone I would hang out with outside of school."
        "That's reassuring..."
        e "What?"
        pov "Nothing, I didn't say anything."
        menu:
            e "What do you like to do outside of school?"

            "\"I like to play video games\"":
                pov "I like to play video games."
                e "Like what kind of video games? I am not really a gamer. I know Linda plays some games..."
                pov "Yes, she plays League of Legends! I do too."
                pov "It's a very popular top-down strategy, action-packed game where you---"
                e "Uh huh."
                e "Hahaha."
                pov "What's so funny?"
                e "Just looking at your face brightening up as you speak of your game."
                pov "I am just really into video games."

            "\"I play a bit of basketball\"":
                pov "I play some basketball. Not that great at it."
                e "I am not a sports person myself either."
                pov "I need to practice more."

                if e_poker_help:
                    e "I'll bet with you I can still score more shots than you!"
                    pov "Again with the betting? You are actually into that, huh?"
                    e "Well, what are we betting on?"
                    pov "I don't want to bet anything yet."
                    e "Come on! Let's have some fun with this!"

            "\"I make music\"":
                $e_make_music = True
                $e_likes += 1
                pov "In my free time, I make music."
                e "Oh my god! Really?"
                e "What kind of music?"
                pov "It's a mixture of genres. Some type of electronic music."
                e "Can I hear some?"
                pov "I will give you a listen some day. Haha!"
                e "I would love that! I am really into all sorts of genres."
                e "This summer I am actually going to this music festival."
                pov "Oh wow, that sounds awesome. What festival is that?"
                e "Electric Daisy Carnival in Las Vegas! I am so excited!"
                pov "Aren't you too young for this?"
                e "Maybe..."
                e "Who cares, dude? It's a freaking music festival! I just want to have fun!"
                pov "These festivals definitely seem like a ton of fun."

        e "Oh wow, I did not notice the time."
        e "I better get going now."
        e "I had a really good time with you today, [povname]."
        pov "I did too, Elaine."

        if e_likes == 6:
            $renpy.pause(2.0, hard = True)
            pov "Oh, Elaine?"
            e "Yes?"
            pov "What did you mean earlier when you said you \"had stuff going on at home\"?"
            e "It's nothing, really. I did not mean anything."
            pov "You sounded very concerned when you mentioned it."
            pov "You also sounded preoccupied when you said on the phone that I couldn't come over to your place..."
            e "Let's just say that my stepdad isn't the nicest guy you'd meet."
            pov "Elaine...."
            e "What?"
            pov "Has he done anything to you?"
            e "Has he harmed me? No."
            e "He just likes to talk. He never shuts up."
            e "I did not want you to come over because he would just make a scene."
            e "Just like with my ex-boyfriend."
            pov "Your ex?"
            e "Yeah, this guy. A complete douche. He also goes to our school."
            pov "Oh. I wonder if I had run into him."
            e "Unlikely. He doesn't hang out around our spot."
            e "Don't worry about me."
            e "Don't get me wrong, you're very sweet, and kind. I like you."
            e "But this stepdad and ex stuff is just not something you should be concerened about."
            pov "I understand."
            e "I will be on my way now."
            pov "Yes, I should get going myslef too."

        if e_poker_help:
            e "Maybe I could teach you a couple more things about Chinese Poker sometime?"
            pov "For sure, I would love to learn from a true master!"
            e "Hahaha, I am not {i}that{/i} great."
            pov "You're pretty darn good, you cannot lie."

        e "I will see you soon!"
        pov "Take care, I will talk to you later."

        hide elaine
        with dissolve

    jump scene4_elaine
