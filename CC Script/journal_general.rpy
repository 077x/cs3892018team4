## Journal: General facts
## To add information to the database, write $addtodb_gen("Your info here")
init python:
  def addtodb_gen(gen_item):
      if gen_item not in persistent.journal_general:
          persistent.journal_general.append(gen_item)


screen journal_general():
    $count = 0
    vbox:
        vbox:
            label ("Entries:")
        vbox:
            spacing 15
            for gen_item in persistent.journal_general:
                $count += 1
                hbox:
                    spacing 15

                    label ("[count].")
                    text gen_item
