import mysql.connector
from tkinter import messagebox
def db_connection():
    try:
        conection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2t2o3n6Ok15ago1996.",
            database="my_company"
        )
        if conection.is_connected():
            messagebox.showinfo("Conection", f"Conection successful")
            return conection
        else:
            messagebox.showerror("Conection", f"Conection failed")
            return None
    except mysql.connector.Error as erro:
        messagebox.showerror("Conection", f"Login failed: {erro}")
        return None