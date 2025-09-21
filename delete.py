import customtkinter as ctk
from company import my_company
from tkinter import messagebox

def delete_item(root):
    root.withdraw()  # Hide main window

    window = ctk.CTk()
    window.title("Delete Employee")
    window.geometry("300x250")

    ctk.CTkLabel(window, text="ID of the employee to delete:").pack(pady=(20, 5))
    entry_id = ctk.CTkEntry(window, placeholder_text="Enter ID")
    entry_id.pack(pady=5)

    def delete_employee():
        emp_id = entry_id.get()
        if not emp_id:
            messagebox.showwarning("Empty Field", "Please enter the ID.")
            return

        try:
            conn = my_company()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employees WHERE id=%s", (emp_id,))
            conn.commit()

            if cursor.rowcount:
                messagebox.showinfo("Success", "Employee deleted.")
            else:
                messagebox.showwarning("Warning", "ID not found.")

        except Exception as e:
            messagebox.showerror("Error", f"Error deleting:\n{e}")

    btn_delete = ctk.CTkButton(window, text="Delete", command=delete_employee)
    btn_delete.pack(pady=20)

    ctk.CTkButton(window, text="Back", command=window.destroy).pack(pady=10)

    window.mainloop()
