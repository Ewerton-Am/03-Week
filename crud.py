import pandas as pd
from company import my_company
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
    button_create = ctk.CTkButton(root, text="Create", command=create_item)
    button_create.pack(pady=(10, 0))

    button_read = ctk.CTkButton(root, text="Read", command=read_item)
    button_read.pack(pady=(10, 0))

    button_update = ctk.CTkButton(root, text="Update", command=update_item)
    button_update.pack(pady=(10, 0))

    button_delete = ctk.CTkButton(root, text="Delete", command=delete_item)
    button_delete.pack(pady=(10, 0))
    
    button_exit = ctk.CTkButton(root, text="Exit", command=root.destroy)
    button_exit.pack(pady=(10, 0))

    root.mainloop()

    
