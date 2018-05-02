## Scene 3 Michelle
label saturday_michelle:
    play music take_give fadeout 5.0 fadein 15.0

    scene black
    with fade

    show text "{color=#ffffff}{b}Saturday{/b}{/color}" at truecenter

    $renpy.pause(3.0)

    scene main bedroom
    with fade

    "It's Saturday..."
    "I am feeling this sense of fear and excitement."
    "Today Michelle and I will be meeting to work on the Culture Fair."
    "I'm emabrrassed that I haven't gone to anyone's house before--"
    "Let alone a girl's house."
    "I only got about 4 hours of sleep last night. Ugh, I am so tired."
    "Thinking about what would happen when I come over to Michelle's house made me feel..."
    "{i}Sigh{/i}"
    "What would she think of me?"
    "What if she likes me and tries to kiss me?"
    "I'd probably just let it happen."
    "Okay..."
    "I'm getting my hopes up. We're just going to do research on clothes."

    with hpunch
    "{b}RING RING{/b}"

    "Michelle is calling!"

    m "Hey, [povname], good morning!"
    pov "Hey Michelle, good morning to you too."
    m "Remember, be at my house at around 2pm."
    m "We've got a lot of research to do."
    pov "Yeah, sure I'll definetly be there."

    scene black
    with fade

    "I come to Michelle's house super excited and tense."
    "I ring the doorbell with sweat on my hands."

    scene linda bedroom
    show michelle normal
    with fade

    m "Hi [povname]!"
    m "Nice to see you here."
    m "Come in, come in."
    m "Oh wait!"
    m "Remember to take your shoes off first!"
    pov "Oh, I am sorry."
    m "Let's start working right away."


    m "Hey, I got a a lot of fun facts on Chinese clothes, listen..."

    menu:
        "Work on the research":
            m "The basic features of traditional clothing are cross-collar--"
            m "Wrapping the right lapel over the left, tying with sash and a form of blouse and a skirt or long gown."
            m "Traditional Chinese attires have many other features, like appearance, cutting, decoration, color and design, and so on..."
            m "All of which changed over the various dynasties."
            m "For example, black is the most dignified color in the Xia Dynasty,"
            m "White in the Shang Dynasty,"
            m "And red in the Zhou Dynasty."
            m "They also vary based on one’s political position, social status, occupation and gender."
            m "For instance, dragon embroideries and bright yellow can only be used by emperors most of the time."

            $addtodb_cloth("As a vital part of Chinese civilization, traditional clothing plays an important role in the country's history and culture. Their basic features are cross-collar, wrapping the right lapel over the left, tying with sash and a form of blouse plus skirt or long gown.")
            $addtodb_cloth("In addition to the basic features and patterns, traditional Chinese attires have many other features like appearance, cutting, decoration, color and design, etc, all of which changed over the various dynasties. For example, black is the most dignified color in the Xia Dynasty (21st - 17th century BC), white in the Shang Dynasty and red in the Zhou Dynasty.")
            $addtodb_cloth("They also vary based on one’s political position, social status, occupation and gender, etc. For instance, dragon embroideries and bright yellow can only be used by emperors most of the time; in the Tang Dynasty (618 - 907 AD), purple official costumes are for the fifth or higher rank officials; in the Qing Dynasty (1644 - 1911 AD), the higher a person’s social rank or the richer one was, the more embroideries and borders there were on his attires.")
            $renpy.notify("New Chinese facts added to Journal")


            m "This is great. Lots of info we can use!"
            m "I am so excited for the Culture Fair!"
            m "Thanks for helping out, [povname]."
            pov "Yeah, of course."

            jump clothes_quiz

        "Pretend to listen (Skip)":
            show black behind michelle
            with dissolve
            "I couldn't bring myself to listen to her."
            "All I did was stare at her face..."
            "...her mesmerizing face."
            "She mentioned some stuff about \'collars\'..."
            "I also heard something about \'dragons\'..."
            "But then..."
            hide black
            with dissolve
            jump clothes_quiz

label clothes_quiz:
    $clothes_quiz_ans = 0
    m "Were you actually listening to me?"
    pov "Ummm, yeah. I was listening."

    menu:
        m "Do you remember what's the basic feature of the traditional clothing?"

        "Cross collar":
            $clothes_quiz_ans += 1
            $m_likes += 1
            m"Yeah you got it."

        "Button down":
            m" Nice try, but nope."

        "Square collar":
            m" Aww. Close.
            "
    menu:
        m "How about this- What is the most dignified color in the Shang Dynasty?"

        "Black":
            m "No, black is the Xia Dynasty's color."

        "Red":
            m "No, that's the Zhou Dynasty's color."

        "White":
            $clothes_quiz_ans += 1
            $m_likes += 1
            m "Good job, you're right."

    m "Okay, one more queston."
    menu:
        m "Emperors would wear clothes with dragon embroderies and bright____?"

        "Flower":
            m "Nope that's not it."

        "Yellow":
            m "Mhmm. Yellow it {i}is{/i}!"
            $clothes_quiz_ans += 1
            $m_likes += 1

        "Red":
            m "Nope. You must be thinking about another clothing."


    m "So what have you found for research?"
    pov "I found a Chinese suit for a man and a Chinese dress for a woman."
    pov "They seem pretty modern."
    "I showed her what I found."
    m "Yeah that looks really good it's the suit is called Tang Zuang and the dress is Qi Pao."
    m "Wow that was quick. Thanks, [povname], you're the best."

    $addtodb_cloth("Chinese Suit (Tang Zhuang): It is a combination of the Manchu male jacket of the Qing Dynasty and the western style suit. It is usually straight collared, with coiled buttons down the front. Its color and design are in traditional Chinese style but tailoring is western.")
    $addtodb_cloth("Cheongsam (Qi Pao): Originated from the Manchu female clothes, it evolved by merging with western patterns that show off the beauty of a female body. Its features are straight collar, strain on the waist, coiled buttons and slits on both sides of the dress. Materials used are usually silk, cotton and linen. Cheongsam is the most popular Chinese attire in the world today.")
    $renpy.notify("New Chinese facts added to Journal")

    menu:
        "\"I know I am\"":
            pov "Yeah, I know I am."
            m "Wow you're so cocky."

        "\"Anything for you\"":
            pov "Not a problem. Anything for you, Michelle."
            m "Wow you're so sweet."

        "\"Thanks\"":
            pov "Thanks."
            m "Mhmm."

    m "Now I'll just ask everyone for their size for clothing and use the club's budget to buy the clothes!"

    menu:
        m "So what do you want to do? Now that we're done."

        "....":
            "...."
            $renpy.pause(3.0)
            jump m_family_dinner

        "\"We can just chill\"":
            pov "Nothing, really. We can just chill for a little bit."
            m "Okay, you got it."
            jump m_family_dinner

        "\"We could play a game\"":
            pov "We could play a game. Do you have anything in mind?"
            m "Yeah, let's practice some more Chinese poker."
            m "But this time, let's make it intresting."
            pov "I'm all ears."
            m "Everytime you lose, you have to answer a question truthfully. Okay?"

            menu:
                m "Do you want to play like that?"

                "\"Yes sure sounds like fun\"":
                    pov "Sure, let's play."

                    $renpy.pause(3.0)

                    "I lost the first game."
                    "Darn. I can't keep losing like that."
                    m "I get to ask any question now. So..."
                    m "What are your goals in life?"
                    pov "Finish high school and then go to college."
                    pov "Not sure what I want to do for a living."
                    m "Yeah, me too."
                    m "My parents want me to become a doctor or an accountant, but I'm not sure how I really feel about it."
                    pov "Don't worry, we both have a lot of time until we need to make that decision."
                    m "Next round!"

                    with vpunch
                    "Argh!"
                    "I lost again."
                    m "[povname]... what is your favorite food?"
                    pov "I like burgers, especially Shake Shack. It's reallly expensive, though. So sometimes I just eat Burger King."
                    m "I see. Well, I prefer pizza over burgers. Feels less of a mess."
                    m "Let's play again. Maybe this time you'll get to ask a question? Hahaha."
                    "I'll definetly win this time."
                    pov "Yes!"
                    "I jumped with excitement. I get to ask her something."
                    "Something she will have to answer truthfully..."
                    pov "I think I am getting better at this."
                    m "Mhmmm. I'm glad you are."
                    "What do I ask her now?"
                    "This is nerve wracking."
                    pov "So... Michelle..."
                    pov "What are things you dislike?"
                    "DOH!"
                    "Why did I ask her {i}that{/i}?!"
                    m "I hate bugs, ew."
                    m "And also when things do not go as planned."


                "\"No\"":
                    pov "No, I'd actually rather we don't play like that..."
                    jump m_family_dinner


label m_family_dinner:
    m "Oh, shoot!"
    m "My parents are coming at 6."
    m "They usually don't want any one of my friends to be here at this hour."
    pov "Oh. Okay. I'll head home now then."
    pov "Thanks for having me."
    m "Yes. It was nice having you here too."

    if m_likes >= 3:
        m "Oh, hey, [povname], before you go--"
        "I heard her tone of voice change."
        "She spoke more softly now."
        "More slowly..."
        m "Are you free tomorrow?"
        "I was startled."
        "Felt I couldn't bring my thoughts together."
        "What do I say?"
        "I cannot mess this up now!"
        pov "Yeah I'm free. What's up?"
        m "Would you like to go to Central Park?"
        pov "Of course!"
        m "We can meet up at two o'clock. I'll text you the location at the park where I will see you."
        pov "Okay, that sounds great. I'll be there. Tomorrow."
        m "Yes! Tomorrow!"
        m "Can't wait! Goodbye, [povname]."
        pov "Goodbye, Michelle."

        jump m_date

    else:
        jump neutral_ending_2
