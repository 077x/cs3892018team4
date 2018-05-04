# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

## init statement below initializes journal (chinese info database)
init:
    if not persistent.journal_general:
        $persistent.journal_general = []

    if not persistent.journal_clothing:
        $persistent.journal_clothing = []

    if not persistent.journal_music:
        $persistent.journal_music = []

    if not persistent.journal_food:
        $persistent.journal_food = []

## The following 'persistent' conditions initialize the characters information data
    # if not persistent.michelle_info:
    #     $persistent.michelle_info = []
    #
    # if not persistent.elaine_info:
    #     $persistent.elaine_info = []
    #
    # if not persistent.linda_info:
    #     $persistent.linda_info = []


## Characters
define pov = Character("[povname]", color ='#FEF6B1')
define co = Character("Corey", color = '#231f20')
define ch = Character("Chris", color = '#fc8d8d')
define m = Character("Michelle", color = '#fffedb')
define e = Character("Elaine", color = '#9482db')
define l = Character("Linda", color = '#88aee2')
define t = Character("Tyler", color = '#630aff')
define who = Character("???", color = '#807175')

## Soundtrack
define audio.main_theme = "Soundtrack/Cosmicosmo - Water Temple.mp3"
define audio.club_theme = "Soundtrack/Darren Ashley - Good Night.mp3"
define audio.dim_sum = "Soundtrack/1991 - Dim Sum.mp3"
define audio.mym = "Soundtrack/1991 - Mayk Yu Myne.mp3"
define audio.quirk = "Soundtrack/Flume - Quirk.mp3"
define audio.thoughts_of_you = "Soundtrack/vbnd - Thoughts of You.mp3"
define audio.take_give = "Soundtrack/zotti - take_give.mp3"

## Images
image elaine normal = "elaine_normal.png"
image chris normal = "nick_normal.png"
image corey normal = "corey_normal.png"
image corey shadow = "corey_shadow.png"
image michelle normal = "michelle_normal.png"
image linda normal = "linda_normal.png"
image tomer normal = "tomer_normal.png"
image black = "black_screen.png"
image main bedroom = "sunset_room.png"
image school outside = "school_entrance.png"
image club room1 = "classroom2.png"
image club room2 = "classroom3.png"
image school corridor = "school_corridor.png"
image hallway morning = "hallway_morning.png"
image hallway afternoon = "hallway_afternoon.png"
image cafeteria = "school_canteen.png"
image michelle bedroom = "michelle_bedroom.png"
image elaine bedroom = "elaine_apartment.png"
image linda bedroom = "linda_bedroom.png"
image diner night = "diner_night.png"
image bus_stop = "bus_stop.png"
image park = "park_evening.png"


## Choices:
default clothing_choice = False
default music_choice = False
default food_choice = False
default m_likes = 0
default e_likes = 0
default l_likes = 0

## Scenes:
# $scene1 = False
# $scene2 = False
# $scene3 = False
# $scene4 = False
# $scene5 = False
#
# $persistent.scene1 = False
# $persistent.scene2 = False
# $persistent.scene3 = False
# $persistent.scene4 = False
# $persistent.scene5 = False

# The game starts here.

label start:

    call tutorial_scene

##Beginning of Scene1
    call intro


    # This ends the game ("return").
    return
