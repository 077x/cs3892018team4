## Journal: Music facts
## To add information to the database, write $addtodb_cloth("Your info here")
init python:
  def addtodb_mus(mus_item):
      if mus_item not in persistent.journal_music:
          persistent.journal_music.append(mus_item)


screen journal_music():
    $count = 0
    vbox:
        vbox:
            label ("Entries:")
        vbox:
            spacing 15
            for mus_item in persistent.journal_music:
                $count += 1
                hbox:
                    spacing 15

                    label ("[count].")
                    text mus_item
