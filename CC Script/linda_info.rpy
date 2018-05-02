## Linda character information
## To add information to the database, write $add_l_info("Your info here")
init python:
    ## Michelle
  def add_l_info(m_item):
      if m_item not in persistent.linda_info:
          persistent.linda_info.append(l_item)


screen linda_info():

    vbox:
        label ("Linda:")

        vbox:
            spacing 10
            for l_item in persistent.linda_info:
                text l_item
