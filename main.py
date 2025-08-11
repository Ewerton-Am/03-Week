import tkinter as tk
from tkinter import messagebox
import pandas as pd
from company import my_company
from user_pass import managers
from auth import authenticate
from crud import menu_crud

# Main Execution 
if authenticate():
    menu_crud()
else:
    messagebox.showerror("Authentication", "Login failed.")
    

