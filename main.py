###############
### Imports ###
###############

import customtkinter as ctk #Primary gui library
from ui import header, home
from utils import theme
from database import database as db


####################
### SCREEN SETUP ###
####################

db.initialize_database()

root = ctk.CTk()
root.title("DuckTape Dock")
root.geometry("1000x650")
root.minsize(800,500)
root._set_appearance_mode("Dark")

root.iconbitmap(theme.APP_ICON)

head = header.create_header(root)


################################################
### CLOSES THE APP AND DATABASE ON APP CLOSE ###
################################################

def close_app():
    db.close_database()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", close_app)

root.mainloop()
