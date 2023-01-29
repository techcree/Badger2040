#load libaries 
import badger2040
import led
from inttext import settext, setroom, setcompany

#load badger
badger = badger2040.Badger2040()

#set fontstyles
COMPANY_HEIGHT = 30
DETAILS_HEIGHT = 20
COMPANY_TEXT_SIZE = 0.6
HEIGHT_TEXT_SIZE = 0.5
LEFT_PADDING = 5
NAME_PADDING = 20
DETAIL_SPACING = 10
OVERLAY_BORDER = 40
OVERLAY_SPACING = 20
OVERLAY_TEXT_SIZE = 0.6

#set badger
badger.pen(0)

#print text on badger
badger.thickness(3)
badger.text((setroom), 20, 20, 1)
badger.thickness(2)
badger.text((settext), 20, 70, 0.8)
badger.thickness(1)
badger.text((setcompany), 20, 100, 0.6)
badger.update()