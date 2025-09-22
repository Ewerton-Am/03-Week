import customtkinter as ctk
import pandas as pd
import db

db.db_connection()
def read_item(root):
    root.withdraw()  # Hide main window
    
    def rd():
        conn = db.db_connection()
        query = "SELECT * FROM employees"
        df = pd.read_sql(query, conn)
        conn.close()
        return df

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    form_window = ctk.CTk()
    form_window.title("Read Items")
    form_window.geometry("600x500")
    
    try:
        df = rd()
    except Exception as e:
        df = pd.DataFrame({"Erro": [str(e)]})
    
    # Create TextBox to display data
    textbox = ctk.CTkTextbox(form_window, width=580, height=350)
    textbox.pack(pady=20)

    # Show Dataframe
    textbox.insert("0.0", df.to_string(index=False))

    # Close Button
    def go_back():
        form_window.destroy()
        root.deiconify()
    botao_fechar = ctk.CTkButton(form_window, text="close", command=go_back)
    botao_fechar.pack(pady=10)

    form_window.mainloop()
