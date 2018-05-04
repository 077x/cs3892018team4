## Scene 1
label intro:
    ## $renpy.block_rollback() will not allow the player to roll back to the tutorial_scene
    $renpy.block_rollback()
    play music main_theme fadein 1.0
    scene main bedroom
    with fade

    "It's that time again."
    "Time for school."
    "I can't say I am excited..."
    "It’s my second year in high school and I still haven’t made any friends."
    "I must be some kind of a special case."
    "Maybe it has something to do with the fact that I watched Netflix shows all summer...."

    scene school outside
    with fade

    "Maybe I should join a club to meet new people."
    "Or, I could just stay home and be comfortable and safe."
    "A very hard decision indeed."
    "I’ll see at the club fair if I’m interested in anything."

    scene black
    with fade

    show text "{color=#ffffff}{b}Later that day at school...{/b}{/color}" at truecenter
    with dissolve

    $renpy.pause(3.0, hard = True)


    scene cafeteria
    with fade


    "What club should I join?"
    "Netflix club? Anime club? Fortnite club?"
    "Maybe a club with--"

    who "Hey, [povname], come here!"

    show michelle normal
    with dissolve

    pov "Hi, who are you again?"
    pov "Oh, wait, aren’t you in my gym class?"
    pov "What was your name again?"

    m "It’s Michelle, and I called you because you should join my club!"
    m "The Chinese Culture Club."

    "She seemed so vibrant, and full of joy."
    "Her face was glowing."

    #show michelle happy

    m "I promise it’s going to be really fun, and there will be free food!"

    pov "Really? That sounds great."
    pov "I don’t know much about Chinese culture, but I’ll let you know if I want to join."

    m "Yeah, be sure to come to our room- 312 after class."
    m "I hope to see you there!"

    hide michelle
    with dissolve

    "After looking through all the clubs, nothing interested me..."
    "Except Fortnite club."
    "But I suck at that game anyway."
    "I might as well check out the Chinese culture club..."
    "Michelle really intrigues me, and I'd like to see ."

    jump first_club_meeting
