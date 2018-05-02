## Scene 2
label first_club_meeting:
    # $scene1 = True

    play music club_theme fadeout 2.0 fadein 3.0
    scene club room1
    # with fade

    show michelle normal
    with dissolve

    m "Hey, [povname]! Glad to see you here."
    m "Take a seat anywhere you like."

    $renpy.pause(1.0)

    m "I guess I’ll start..."
    m "Hello everyone, welcome to Chinese Culture club."
    m "If anyone forgot, my name is Michelle, and I’m the president of the club."
    m "In this club we’ll do activities to learn about Chinese culture,"
    m "But for now, we’re going to do an icebreaker, so everyone can get to know each other."
    m "The way the icebreaker works is that we form two lines in which both lines face each other."
    m "Then you talk for a minute to whomwever is in front of you."
    m "This repeats until you have talked with everyone."
    m "This icebreaker is called \'speed-dating\'"
    m "So have fun with it!"
    m "Okay guys, be ready to form two lines."

    hide michelle
    with dissolve

    "Hmmm"
    "What should I ask first?"
    "Probably why they joined the club and their hobbies."
    "Yeah, that sounds good."

    show chris normal
    with dissolve

    pov "Hello, so why did you join the club?"
    who "Oh, don’t tell anyone, but I joined to meet a Chinese girl..."
    who "Or any asian girl."
    who "I just want a girlfriend. How about you though?"
    pov "I don't think you should see girls like that, but I won't try to change your mind."
    pov "I'm just here to make friends."
    pov "Maybe get a girlfriend like you hahaha."
    pov "So what do you like to do for fun?"
    who "I like to play League and watch anime. How about you?"
    pov "I just watch Netflix, that’s all."
    ch "Oh yeah, by the way, my name is Chris. What’s yours?"
    pov "My name is [povname], what’s your--"

    hide chris normal
    with dissolve

    show michelle normal
    with dissolve

    m "Okay guys, the one minute is up! Move on to the next person."

    hide michelle
    with dissolve

    show elaine normal
    with dissolve

    pov "Hello, my name is [povname], what--"
    e "Hey, I'm Elaine."
    "....."
    "She didn’t ask me any questions. I guess I’ll ask"
    pov "So, what do you like to do for fun?"
    e "I like to eat food and sleep."
    pov "So why did you join this club?"
    e "Eh, it's just to get the required credits to graduate...."
    pov "Oh, thats cool, heh."
    "I ran out of questions, what should I do now??"

    "{i}There’s an awkward silence for a few seconds....{/i}"

    $renpy.pause(3.0, hard = True)

    hide elaine
    with dissolve


    "She just left...."

    show michelle normal
    with dissolve

    m "Okay, time is up again, now move to the next person."
    m "Hey, [povname], what do you think of my club so far?"
    pov "It’s nice."
    m "Yeah, but I think I could get a few more people."
    m "It is a new club and all, but I want it to succeed."
    m "I hope you’ll be coming to more club meetings."
    pov "I might come back. I think I want to see the other clubs first"

    #show michelle disappointed

    m "Oh, okay that’s fine."
    m "I hope you stay with us...."

    "{i}{size=+10}RING RING{/size}{/i}"

    #show michelle normal

    m "Time's up everyone, now go to the next person."

    hide michelle normal
    with dissolve

    show linda normal
    with dissolve

    l "Hi, ummm...."
    l "My name is Linda."
    pov "Hi, I'm [povname]."
    pov "So, what do you like to do for fun?"
    l "I like to play League of Legends."
    pov "Really?!"
    pov "I play League too, it's one of my favorites. I am not too great at it, though."
    l "Hehe, it just takes practice..."
    l "If you want, I can help you."
    pov "Ummmm"
    pov "I’ll think about it."
    l "What’s your favorite food?"
    pov "I love burgers!"
    l "Oh, I like pizza more."
    l "Do you... do you like pineapple on your pizza..."
    l "Or...?"
    pov "I don’t mind it, but I prefer not to have any pineapple."
    m "Alright people, that was the last of it for the speed-dating!"

    hide linda
    with dissolve

    show michelle normal
    with dissolve

    m "Okay now that everyone’s got to know a little about each other, I’ll introduce you to one of my favorite chinese card games."
    m "It’s called \'Chinese Poker\'"
    "After Michelle explained the game, we gave it a try and played."

    show chris normal at left
    with dissolve

    ch "Ummm... huh."
    ch "I think I’ll just watch you guys play first, 'cause I still don’t understand how to play."

    hide chris
    with dissolve

    show elaine normal at right
    show linda normal at left
    with dissolve

    "Linda, Michelle, Elaine, and I were playing and surprisingly- Elaine was winning most of the games!"

    m "How are you so good Elaine?!"
    e "Oh, my dad taught me."
    l "I don't believe it."
    l "I think you’re cheating...."
    pov "Or maybe she’s actually that good."
    e "Well, I don’t need to cheat against you guys anyways."

    hide michelle
    hide elaine
    hide linda
    with dissolve

    show chris normal
    with dissolve

    ch "Damn, you guys just got roasted!"

    hide chris
    with dissolve

    show michelle normal
    show elaine normal at right
    show linda normal at left
    with dissolve

    pov "Hey, I’m only a beginner!"
    l "Hmmm"
    l "I was actually going easy on you guys!"
    m "Let’s play again- see who’s the best."
    "It was a clash between Elaine and Michelle for most of the game."
    "But Elaine still won."

    hide elaine
    hide linda
    with dissolve

    m "Okay everyone, that's it for the meeting today!"
    m "But before you all leave, here's a quick Chinese culture fact:"
    m "When you finish your plate of food, that means you want more food."
    m "But if you're done eating, you leave a little bit of food on your plate."

    $addtodb_gen("When one is eating and wants more food, one has to eat everything on the plate to show that he/she wants seconds. If he/she is finished eating, the person leaves a little bit of food on his/her plate to show that he/she is finished.")
    $renpy.notify("New Chinese fact added to Journal")

    m "At the end of every club meeting, I will give you some facts and information about China and its culture,"
    m "So you can learn something new every time you stop by!"
    m "Can’t wait to see you guys next time!"


    hide michelle
    with dissolve

    scene school corridor:
    with fade

    "As I head outside to the hallway, Michelle comes up to me."

    show michelle normal
    with dissolve

    m "Hey, I know I've asked you already,"
    m "But what do you think of the club so far?"
    pov "It’s fun. I enjoyed the first meeting. I wanna get better at chinese poker though!"
    m "mhmm..."
    m "If anything, I can help you, haha."

label poker_help_choice:
    default m_poker_help = False
    default e_poker_help = False
    default l_poker_help = False

    menu:
        "Who should I choose to help me with \'Chinese Poker\'?"

        "Michelle":
            $m_poker_help = True
            $m_likes += 1
            m "I'll gladly help you!"
            m "To get better, you need to work on how you organize your cards and the timing you put them down."
            pov "Really?"
            pov "And how do I do that?"
            m "Let's play a few more games and I'll show you."
            "As we were playing some more Chinese Poker together, I noticed Michelle was sliding closer to me to see my cards."
            "As she tried to adjust my cards to teach me how they should be organized,"
            "I could feel her hand touch mine."

            $renpy.pause(2.0)

            "I know it was just a touch, but I haven't touched a girl..."
            "Except my mom."
            "My heart was racing, but I tried my best to stay calm."
            m "Hey, are you good over there?"
            with vpunch
            pov "UUUUHHH"
            pov "Yeah! Yeah...."
            pov "I was just having trouble remembering how to order the cards...."
            m "Oh, don't worry- if we keep playing you'll get used to it."
            m "I have to go in a few minutes. My parents want me home soon."
            m "But I'll see you at the next club meeting, right?"
            pov "Yeah, sure. See you then."


        "Elaine":
            $e_poker_help = True
            $e_likes += 1
            hide michelle
            with dissolve

            show elaine normal
            with dissolve

            e "Who are you again?"
            pov "Uhhh"
            pov "I'm [povname], we just met at the meeting...."
            "Wow, she doesn't seem to really care about things."
            "But, for some reason, she interests me."
            "I would actually like to get to know her better."
            e "Let's play then, huh?"
            pov "Oh, right, yes."
            e "You see, you need to learn how to organize your cards right."
            e "Also, you'd need to work on your timing, for when you put your cards down."
            pov "That sounds hard. I will have to practice."
            e "Definitely."
            e "Your performance back at the club wasn't impressive at all..."
            pov "Oh... ummm, yeah. I'm just a rookie."
            e "Besides organizing and timing your cards, there's one key component you need to learn."
            pov "Which is...?"
            e "Learning to adapt to your opponents."
            e "You need to find out how to read their faces; find out if they are going to play a combo, or a pair,"
            e "Figure out if they are splitting their combos."
            pov "Whoa, where'd you learn all of that?"
            e "Eh, my parents taught me this game when I was younger."
            pov "So you weren't lying when you said your dad taught you?"
            e "They play it a lot..."
            e "Especially when they go to gamble."
            pov "Gamble?! You can gamble with Chinese Poker?"
            e "Of course. You can gamble with anything."
            pov "Do you gamble?"
            e "Not really. But when I do, I always win."
            e "Anyway, I gotta go now. See ya."
            "She seems to be in a rush."
            pov "Bye Elaine...."


        "Linda":
            $l_poker_help = True
            $l_likes += 1
            hide michelle
            with dissolve

            show linda normal
            with dissolve

            l "Hmmmm"
            l "Why do you want me to help you play better?"
            l "I am not that great myself."
            "She's right. She sucks at Chinese Poker."
            "She might not help me out with the game, but I could definitely use her company."
            "She seems nice enough, although she is quite shy."
            pov "Well..."
            pov "I thought it would be nice to hang out with you."
            l "I can't stay for too long now, but I'll see you later!"
            pov "Oh, yeah. Sure."
            pov "See you later."
            l "Bye [povname]!"

    play music main_theme fadeout 5.0 fadein 5.0

    scene hallway afternoon
    with fade

    "The club meeting wasn't too bad."
    "There were a lot of people I can make friends with."
    "There's Michelle, Elaine, and Linda...."

    scene black
    with fade

    "I think I should go to club again. Maybe something special will happen."
    "I hope...."

    "Should I actually go to the next club meeting?"

## Go to second club meeting choice
    menu:
        "Yes":
            jump second_club_meeting
        "No":
            jump bad_ending1
