import customtkinter as ctk
from tkinter import messagebox
from user_pass import managers, cad

# Authentication function
def authenticate():
   auth_success = {"status": False}
   ctk.set_appearance_mode("dark")
   ctk.set_default_color_theme("blue")
   
   def auth_1():
      mngr = managers()
      login = entry_login.get()
      passw = entry_passw.get()
      cursor = mngr.cursor()
      cursor.execute("SELECT * FROM users WHERE username = %s AND password_hash = %s", (login, passw))
      if cursor.fetchone():
         messagebox.showinfo("Authentication", "Welcome, " + login + "!")
         auth_success["status"] = True
         window.destroy()
      else:
         messagebox.showerror("Authentication", "Login failed.")
      cursor.close()


   # GUI setup
   window = ctk.CTk()
   window.title("Authentication")
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
   button_auth = ctk.CTkButton(window, text="Authenticate", command=auth_1)
   button_auth.pack(pady=(20,0))

   # Cadastral button
   button_cadastral = ctk.CTkButton(window, text="Cadastral", command=cad)
   button_cadastral.pack(pady=(20,0))
   window.mainloop()
   
   return auth_success["status"]