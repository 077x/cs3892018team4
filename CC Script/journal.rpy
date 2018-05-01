## Chinese culture, facts, and stories database
## Information in the database should update upon reaching certain points in the game that provide the information

screen journal():

    tag menu

    default journal = "general"

    predict False

    use game_menu(_("Journal"), scroll="viewport"):

        style_prefix "about"

        hbox:

            spacing 25

            textbutton _("General") action SetScreenVariable("journal", "general")

            textbutton _("Clothing") action SetScreenVariable("journal", "clothing")

            textbutton _("Music") action SetScreenVariable("journal", "music")

            textbutton _("Food") action SetScreenVariable("journal", "food")

        if journal == "general":
            use journal_general
        elif journal == "clothing":
            use journal_clothing
        elif journal == "music":
            use journal_music
        elif journal == "food":
            use journal_food
