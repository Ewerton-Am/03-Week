from logging import root
import customtkinter as ctk
from create import create_item
from read import read_item
from update import update_item  
from delete import delete_item

def menu_crud():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()  # <- Janela principal
    root.title("Menu CRUD")
    root.geometry("300x400")

    # Buttons for options
    button_create = ctk.CTkButton(root, text="Create", command=lambda: create_item(root))
    button_create.pack(pady=(10, 0))

    button_read = ctk.CTkButton(root, text="Read", command=lambda: read_item(root))
    button_read.pack(pady=(10, 0))

    button_update = ctk.CTkButton(root, text="Update", command=lambda: update_item(root))
    button_update.pack(pady=(10, 0))

    button_delete = ctk.CTkButton(root, text="Delete", command=lambda: delete_item(root))
    button_delete.pack(pady=(10, 0))

    root.mainloop()

    
