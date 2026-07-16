###############
### Imports ###
###############

from utils import theme
from database import database as db
from ui import ui_talker


####################
### SCREEN SETUP ###
####################

db.initialize_database()

ui_talker.launch_ui()