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


################################################
### CLOSES THE APP AND DATABASE ON APP CLOSE ###
################################################

def close_app():
    db.close_database()
