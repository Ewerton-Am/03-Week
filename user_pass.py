import customtkinter as ctk
from tkinter import messagebox
import db

#dict with access info 
def managers():
    conection = db.db_connection()
    
    point = conection.cursor()

    # Create table if not exist
    point.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE,
            password_hash VARCHAR(255)
            );
    """)

    # Insert data only if empty
    point.execute("SELECT COUNT(*) FROM users")
    if point.fetchone()[0] == 0:
        point.execute("""
            INSERT INTO users (username, password_hash) VALUES
            ('admin', 'admin')""")
        conection.commit()

    point.close()
    return conection

# Cadastral function
def cad():
    mngr = managers()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    def cad_1():
        # Entry for user
        new_login = entry_login.get()
        new_passw = entry_passw.get()
        if not new_login or not new_passw:
            messagebox.showwarning("Cadastral", "Please fill in all fields.")
            return
        
        point = mngr.cursor()
        
        # Check if user already exists
        point.execute("SELECT * FROM users WHERE username = %s", (new_login,))
        if point.fetchone():
            messagebox.showwarning("Cadastral", "User already exists.")
            return

        # Insert new user into the database
        point.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (new_login, new_passw))
        mngr.commit()
        point.close()
        messagebox.showinfo("Cadastral", "User registered successfully!")
        window.destroy()

    # GUI setup
    window = ctk.CTk()
    window.title("Cadastral")
    window.geometry("500x300")
    window.resizable(False, False)

    # Field of entry for user
    label_login = ctk.CTkLabel(window, text="Login:")
    label_login.pack(pady=(20,5))
    entry_login = ctk.CTkEntry(window)
    entry_login.pack(pady=(0,20))

    # Field of entry for password
    label_passw = ctk.CTkLabel(window, text="Password:")
    label_passw.pack(pady=(20,5))
    entry_passw = ctk.CTkEntry(window, show="*")
    entry_passw.pack(pady=(0,20))

    # Authentication button
    button_cad = ctk.CTkButton(window, text="Cadastral", command=cad_1)
    button_cad.pack(pady=(20,0))

    window.mainloop()
