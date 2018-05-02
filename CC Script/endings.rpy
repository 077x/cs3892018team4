## Bad Ending 1
label bad_ending1:
    stop music fadeout 5.0
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

    scene black

    show text "{color=#ffffff}{b}Bad Ending{/b}{/color}" at truecenter

    $renpy.pause(3.0)

    return


label bad_ending2:
    stop music fadeout 5.0
    scene black
    with fade

    "I have decided I could not make the move."
    "I stopped seeing Elaine...."
    "Weirdly enough, I didn't know what to feel about this."
    "On one hand, it felt terrible--"
    "Breaking up this friendship hurt."
    "On the other hand--"
    "I've always been lonely. So this might not be too bad."
    "Only time will tell...."
    "Will I stay by myself, or will I find true friends?"

    return

label neutral_ending1:
    stop music fadeout 5.0
    scene school outside
    with fade

    "Today's the last club meeting before the Culture Fair."
    "I am feeling excited."

    scene hallway morning
    with fade

    "I haven't talked much with the girls, though."
    "\"I hope they still remember me...\" I thought to myself..."
    "...feeling a slight sting..."

    scene school corridor
    with fade

    "But what if they actually forgot about me?"

    scene club room1
    with fade

    "The room was empty."
    "Why is nobody here right now?"
    $renpy.pause(2.0)
    "It felt lonely in there. Like how I {i}am{/i} usually..."
    "Suddenly, the door behind me creaked."

    show corey_shadow
    with dissolve

    who "Hello, [povname], nice to see you here..."

    scene black
    with fade

    show text "{color=#ffffff}{b}To be continued...{/b}{/color}" at truecenter
    with dissolve

    $renpy.pause(3.0, hard = True)

    return

label neutral_ending_2:
    scene black
    with fade

    show text "{color=#ffffff}{b}The next day{/b}{/color}" at truecenter

    $renpy.pause(3.0)

    scene school corridor

    pov "Class is finally over. I can't wait for the club meeting."
    pov "Hope I can get closer to the members."
    jump to_be_cont


label to_be_cont:
    scene black
    with fade

    show text "{color=#ffffff}{b}To be continued...{/b}{/color}" at truecenter
    with dissolve

    $renpy.pause(3.0)


    return
