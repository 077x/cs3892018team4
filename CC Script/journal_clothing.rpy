## Journal: Clothing facts
## To add information to the database, write $addtodb_cloth("Your info here")
init python:
  def addtodb_cloth(cloth_item):
      if cloth_item not in persistent.journal_clothing:
          persistent.journal_clothing.append(cloth_item)


screen journal_clothing():
    $count = 0
    vbox:
        vbox:
            label ("Entries:")
        vbox:
            spacing 15
            for cloth_item in persistent.journal_clothing:
                $count += 1
                hbox:
                    spacing 15

                    label ("[count].")
                    text cloth_item
