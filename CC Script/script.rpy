# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

## init statement below initializes journal (chinese info database)
init:
    if not persistent.journal:
        $persistent.journal = []

## Characters
define pov = Character("[povname]", color ='#231f20')
define co = Character("Corey", color = "#231f20")
define ch = Character("Chris", color = "#380b0b")
define m = Character("Michelle", color = "#065c70")
define e = Character("Elaine", color = "#231072")
define l = Character("Linda", color = "#103972")
define who = Character("???", color = "#231f20")

## Soundtrack
define audio.main_theme = "Soundtrack/Cosmicosmo - Water Temple.mp3"
define audio.club_theme = "Soundtrack/Darren Ashley - Good Night.mp3"

## Images
image elaine normal = "elaine_normal.png"
image chris normal = "nick_normal.png"
image corey normal = "corey_normal.png"
image michelle normal = "michelle_normal.png"
image linda normal = "linda_normal.png"
image tomer normal = "tomer_normal.png"
image black = "black_screen.png"
image main bedroom = "sunset_room.png"
image school outside = "school_entrance.png"
image club room1 = "classroom2.png"
image school corridor = "school_corridor.png"
image hallway morning = "hallway_morning.png"
image hallway afternoon = "hallway_afternoon.png"
image cafeteria = "school_canteen.png"
image m bedroom = "bedroom1.png"


## Choices:
default clothing_choice = False
default music_choice = False
default food_choice = False

# The game starts here.
##Beginning of Scene1
label start:

    call tutorial_scene

## $renpy.block_rollback() will not allow the player to roll back to the tutorial_scene
    $renpy.block_rollback()

    play music main_theme fadein 1.0
    scene main bedroom
    with fade

    ## Provide player's input as character's name
    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

        if not povname:
            povname = "Jevon-Lee"


    # These display lines of dialogue.

    "It’s my second year in high school and I still haven’t made any friends."
    "All I did was watch Netflix shows all summer...."

    "Maybe I should join a club to meet new people."
    "Or I could just stay home and be comfortable and safe."
    "A very hard decision indeed. I’ll see at the club fair if I’m interested in anything."

    scene black
    with fade

    show text "{color=#ffffff}{b}Later that day at school...{/b}{/color}" at truecenter

    $renpy.pause(3.0)


    scene cafeteria
    with fade


    "What club should I join?"
    "Netflix club? Anime club? Fortnite club?"
    "Maybe a club with lots of girls?"

    show michelle normal
    with dissolve

    m "Hey, [povname], come here!"

    pov "Hi, who are you again?"
    pov "Oh, aren’t you in my gym class?"
    pov "What was your name again?"

    m "Oh, it’s Michelle, and I called you because you should join my club."
    m "The Chinese Culture Club."

    #show michelle happy

    m "I promise it’s going to be really fun, and there will be free food!"

    pov "Really? That sounds great."
    pov "I don’t know much about Chinese culture, but I’ll let you know if I want to join."

    m "Yeah, be sure to come to our room- 312 after class."
    m "I hope to see you there!"

    hide michelle
    with dissolve

    "After looking through all the clubs, nothing interested me..."
    "Except Fortnite club. But I suck at that game anyway."
    "I might as well check out the Chinese culture club because Michelle was the only one to call my name out."

##Beginning of Scene2
label first_club_meeting:

    play music club_theme fadeout 2.0 fadein 1.0
    scene club room1
    with fade

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

    m "Time's up everyone, move on to the next"

    hide michelle normal
    with dissolve

    show linda normal
    with dissolve

    l "Hi, ummm...."
    l "My name is Linda."
    pov "Hi, I'm [povname]."
    pov "So, what do you like to do for fun?"
    l "I like to play basketball and play a little bit of League of Legends."
    pov "Really?!"
    pov "I play League too, but I’m not so good at basketball."
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
    m "At the end of every club meeting, I will give you some facts and information about China and its culture,"
    m "So you can learn something new every time you stop by!"
    m "Can’t wait to see you guys next time!"

    $addtodb("When one is eating and wants more food, one has to eat everything on the plate to show that he/she wants seconds. If he/she is finished eating, the person leaves a little bit of food on his/her plate to show that he/she is finished.")

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

    menu:
        "Who should I choose to help me with \'Chinese Poker\'?"

        "Michelle":
            m "I'll gladly help you!"
            m "To get better, you need to work on how you organize your cards and the timing you put them down."
            pov "Really?"
            pov "And how do I do that?"
            m "Lets play a few more games and I'll show you."
            "As we were playing some more Chinese Poker together, I noticed Michelle was sliding closer to me to see my cards."
            "As she tried to adjust my cards to teach me how they should be organized,"
            "I could feel her hand touch mine."

            $renpy.pause(2.0)

            "I know it was just a touch, but I haven't touched a girl..."
            "Except my mom."
            "My heart was beating really quickly, but I tried my best to stay calm."
            m "Hey, are you good over there?"
            pov "UUUUHHH"
            pov "Yeah! Yeah...."
            pov "I was just having trouble remembering how to order the cards...."
            m "Oh, don't worry- if we keep playing you'll get used to it."
            m "I have to go in a few minutes. My parents want me home soon."
            m "But I'll see you at the next club meeting, right?"
            pov "Yeah, sure. See you then."


        "Elaine":
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

        "Linda":
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

    stop music fadeout 5.0

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


##Beginning of Scene3
label second_club_meeting:

    play music club_theme fadein 1.0

    show text "{color=#ffffff}{b}Second Club Meeting{/b}{/color}" at truecenter
    with fade

    $renpy.pause(3.0, hard = True)

    scene school corridor
    with fade

    pov "Finally, class is done."
    pov "Time to visit Chinese Club"

    scene club room1
    with fade

    "I come back to the club room, and everyone else was there...."
    "Except for Elaine."
    "I look for a seat, but then Elaine came in."

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

    e "I'll work on music. I know a few songs "

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
            l "I guess you're working with me."
            pov "Yes, I'd like to research on some foods!"

            hide linda
            with dissolve

        "Clothing":
            $clothing_choice = True
            m "Okay, you'll be working with me!"

        "Music":
            $music_choice = True
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

    $addtodb("Fortune cookies are often served as a dessert in Chinese restaurants in the United States and other Western countries, but are not a tradition in China.")

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

    jump to_be_cont

label culture_fair_food:

    $renpy.pause(3.0)

    show linda normal
    with dissolve

    l "Hey, [povname], right?"
    l "It seems like we are going to work together on foods for the Culture Fair!"
    pov "Yes, I am excited!"
    l "When do you want to meet?"
    pov "What day is good for you?"
    l "Saturday afternoon?"
    pov "That works. Where should we meet?"
    l "I guess you could come by my place, I will text you the address."
    pov "Great, see you then."
    "She smiled and left the room."

    jump to_be_cont

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

    jump to_be_cont


label to_be_cont:

    scene black
    with fade

    show text "{color=#ffffff}{b}To Be Continued...{/b}{/color}" at truecenter

    $renpy.pause(3.0)

    return

label bad_ending1:

    scene black
    with fade

    "I haven't gone to the club at all for the past few weeks...."
    "I don't think I will go back either."

    $renpy.pause(2.5, hard = True)

    "There was this one time, I saw Michelle in the hallway."
    show michelle normal
    with dissolve

    "She walked by me, and gave me a faint smile."
    "She did not look as vibrant as she usually does...."

    "I did not bother to speak with her."
    "I felt that I couldn't...."

    hide michelle
    with dissolve

    show text "{color=#ffffff}{b}Bad Ending{/b}{/color}" at truecenter

    $renpy.pause(3.0)

## $persistent.journal = [] turns the database into an empty list
## This statement is only used for development purposes; will delete when game releases
    # $persistent.journal = []
######## DELETE LATER ##########################################################


    # This ends the game ("return").
    return
