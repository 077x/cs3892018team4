## Chinese culture, facts, and stories database
## Information in the database should update upon reaching certain points in the game that provide the information

## To add information to the database, write $addtodb("Your info here")

init python:
  def addtodb(item):
      if item not in persistent.journal:
          persistent.journal.append(item)


screen journal():

    tag menu

    predict False

    use game_menu(_("Journal"), scroll="viewport"):

        $count = 0

        style_prefix "about"

        vbox:
            label ("Entries:")
        vbox:
            spacing 15
            for item in persistent.journal:
                $count += 1
                hbox:
                    spacing 15

                    label ("[count].")
                    text item
