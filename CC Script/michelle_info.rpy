## Michelle character information
## To add information to the database, write $add_m_info("Your info here")
init python:
    ## Michelle
  def add_m_info(m_item):
      if m_item not in persistent.michelle_info:
          persistent.michelle_info.append(m_item)


screen michelle_info():

    vbox:
        label ("Michelle:")

        vbox:
            spacing 10
            for m_item in persistent.michelle_info:
                text m_item
