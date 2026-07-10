###############
### Imports ###
###############

import customtkinter as ctk #Primary
from utils import theme, helpers as help
from PIL import Image

def create_header(root):
    head = ctk.CTkFrame(root, height=120, corner_radius=0)
    head.pack(
        fill="x",
        side="top"
    )
    head.configure(fg_color=theme.CARD_BACKGROUND)
    head.pack_propagate(False)
    bottom_border = ctk.CTkFrame(root,height=4,fg_color=theme.PRIMARY_YELLOW, corner_radius=0)
    bottom_border.pack(fill="x")
    bottom_border.pack_propagate(False)
    add_logo(head)



def add_logo(head):
    LOGO_WIDTH = 713
    LOGO_HEIGHT = 823
    LOGO_DIVIDE = 8
    logo_image = ctk.CTkImage(
        light_image=Image.open(theme.APP_LOGO),
        size=(LOGO_WIDTH/LOGO_DIVIDE, LOGO_HEIGHT/LOGO_DIVIDE)
    )
    logo = ctk.CTkLabel(head, image=logo_image, text=None)
    logo.place(relx=0.5, rely=0.5, anchor="center")