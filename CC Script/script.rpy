# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jevon")
define m =  Character("michelle")
define c =  Character("chris")
define e = Character("elaine")
define n = Character("")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene sidewalk

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    j "It’s my second year in high school and I still haven’t made any friends.
    All I did was watch Netflix shows all summer."

    j "Maybe I should join a club to meet new people or just stay home and be comfortable and safe.
    A very hard decision indeed I’ll see at the club fair if I’m interested."

    scene lunchroom
    j " What club should I join? Netflix club? Anime Club? Fortnite club? Maybe a club with a lot of girls?
    Trying to find friends club? Eat as…"

    show michelle

    m "Hey Jevon-Lee come here!"

    j "Hi who are you again? Oh aren’t you in my gym class.
    What was your name again?"

    show michelle

    m "Oh it’s michelle and I called you because you should join my club  Chinese Culture Club.
     I promise it’s going to be really fun and there will be free food."

    j "Really that sounds great. Don’t know much about Chinese culture, but I’ll let you know if I want to join."

    show michelle

    m "Yeah be sure to come to our room 312 after class. I hope to see you there"

    j "After looking through all the clubs nothing interested me except fortnite club, but I suck at that game.
    I might check out the Chinese culture because michelle was the only one to call my name out."

    scene clubroom
    show michelle
    m "Hey Jevon glad to see you here. Take a seat anywhere you like."
    m " Guess I’ll start. Hello everyone welcome to Chinese Culture club. If anyone forgot, my name it is michelle and I’m the president of the club."
    m " In this club we’ll do activities to learn about Chinese culture, but for now we’re going to do an icebreaker So everyone can get to know eachother."
    m " How the ice breaker works is that we form two lines in which both lines face each other. Then you talk for a minute to who is in front of you."
    m " This repeats until you have talked to everyone. This icebreaker is called speed dating so have fun with it. Okay guys be ready to form two lines."
    j "Hmm what should I ask first? Probably why they joined the club and their hobbies. Yeah that sounds good."
    scene clubroom
    show chris
    j "Hello so why did you join the club?"
    c "Oh don’t tell anyone but I joined to meet a Chinese girl or any asian girl. I just want a girlfriend. How about you tho?"
    j "Ha you must got that yellow fever. Well to each their own. I’m here to make some friends. Maybe get a girlfriend like you hahaha. So what do you like to for fun?"
    c "I like to play league and watch anime. How about you?"
    j "I just watch netflix that’s all."














    # This ends the game.

    return
