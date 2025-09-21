import customtkinter as ctk
from company import my_company
from tkinter import messagebox

def update_item(root):
    root.withdraw()  # Hide main window
    
    window = ctk.CTk()
    window.title("Update Employee")
    window.geometry("400x350")

    ctk.CTkLabel(window, text="ID do Funcionário:").pack(pady=(20, 5))
    entry_id = ctk.CTkEntry(window, placeholder_text="Digite o ID")
    entry_id.pack(pady=5)

    ctk.CTkLabel(window, text="New position:").pack(pady=5)
    entry_position = ctk.CTkEntry(window, placeholder_text="New position")
    entry_position.pack(pady=5)

    ctk.CTkLabel(window, text="New Name:").pack(pady=5)
    entry_name = ctk.CTkEntry(window, placeholder_text="New Name")
    entry_name.pack(pady=5)

    def update_employee():
        emp_id = entry_id.get()
        pos = entry_position.get()
        nome = entry_name.get()

        if not emp_id or not pos or not nome:
            messagebox.showwarning("Empty Fields", "Please fill in all fields.")
            return

        try:
            conn = my_company()
            cursor = conn.cursor()
            cursor.execute("UPDATE employees SET position=%s, name=%s WHERE id=%s", (pos, nome, emp_id))
            conn.commit()

            if cursor.rowcount:
                messagebox.showinfo("Success", "Employee updated.")
            else:
                messagebox.showwarning("Warning", "ID not found.")

        except Exception as e:
            messagebox.showerror("Error", f"Error updating:\n{e}")

    btn = ctk.CTkButton(window, text="Update", command=update_employee)
    btn.pack(pady=20)

    ctk.CTkButton(window, text="Back", command=window.destroy).pack(pady=10)

    window.mainloop()
