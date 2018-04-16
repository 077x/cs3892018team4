##Tutorial Script
label tutorial_scene:
    scene black
    stop music fadeout 1.0

    "Hello, and welcome to Chinese Club."

    menu:
        "Before you jump into the game, would you like to go through a quick tutorial?"
        "Yes":
            jump yes_tutorial
        "No":
            jump end_tutorial

    label yes_tutorial:

        "This is the textbox where characters you'll meet will talk."
        "You may want to use the arrow buttons on the sides to go back and forth in the dialogue."
        "You can pause the game at any time and save whenever you want"
        "So when you come back, you can jump right back into where you've left off."
        "This should cover the basics."
        "In case you forget how to play the game, the \"help\" screen will assist you."
        "Now let's get to the game...."
        return

    label end_tutorial:

        "Seems like you know your stuff."
        "In case you forget how to play the game, the \"help\" screen will assist you."
        "Have fun playing!"
        return
