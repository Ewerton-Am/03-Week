import getpass
import pandas as pd
from company import my_company
from user_pass import managers, aut
from auth import authenticate
from crud import menu_crud

# Main Execution 
if authenticate():
    menu_crud()
else:
    print("Access denied.")

