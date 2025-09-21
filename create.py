import customtkinter as ctk
from company import my_company
from tkinter import messagebox


def create_item(root):
    root.withdraw()  # Hide main window
    
    form_window = ctk.CTk()
    form_window.title("Add employeer")
    form_window.geometry("400x300")

    # --- Labels and Entrys ---
    label_position = ctk.CTkLabel(form_window, text="Positions:")
    label_position.pack(pady=(20, 5))

    entry_position = ctk.CTkEntry(form_window, placeholder_text="Positions, e.g., Manager, Developer")
    entry_position.pack(pady=(0, 10), padx=20)

    label_name = ctk.CTkLabel(form_window, text="Name:")
    label_name.pack(pady=(10, 5))

    entry_name = ctk.CTkEntry(form_window, placeholder_text="Enter name")
    entry_name.pack(pady=(0, 20), padx=20)

    # --- Function to save ---
    def save_employee():
        position = entry_position.get()
        name = entry_name.get()

        if not position or not name:
            messagebox.showwarning("Empty fields", "Please fill in all fields.")
            return

        try:
            connection = my_company()
            cursor = connection.cursor()

            cursor.execute("INSERT INTO employees (position, name) VALUES (%s, %s)", (position, name))
            connection.commit()

            messagebox.showinfo("Success", f"{name} added successfully!")
           
        except Exception as e:
            messagebox.showerror("Error", f"Error adding employee:\n{e}")

    # --- Buttons ---
    button_save = ctk.CTkButton(form_window, text="Save", command=save_employee)
    button_save.pack(pady=10)

    def go_back():
        form_window.destroy()
        root.deiconify()

    button_back = ctk.CTkButton(form_window, text="Back", command=go_back)
    button_back.pack(pady=10)

    form_window.mainloop()

        