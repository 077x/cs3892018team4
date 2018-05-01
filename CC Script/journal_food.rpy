## Journal: Food facts
## To add information to the database, write $addtodb_cloth("Your info here")
init python:
  def addtodb_foo(foo_item):
      if foo_item not in persistent.journal_food:
          persistent.journal_food.append(foo_item)


screen journal_food():
    $count = 0
    vbox:
        vbox:
            label ("Entries:")
        vbox:
            spacing 15
            for foo_item in persistent.journal_food:
                $count += 1
                hbox:
                    spacing 15

                    label ("[count].")
                    text foo_item
