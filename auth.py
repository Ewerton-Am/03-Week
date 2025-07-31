import getpass
import tkinter as tk
from tkinter import messagebox
from user_pass import managers, aut

#Authentification function
def authenticate():
    mngr = managers()
    login = input("Login: ")
    passw = getpass.getpass("Password: ")


    if login in mngr and mngr[login] == passw:
       print('Access Successfully.')
       return True
    else:
       return aut(login, passw)