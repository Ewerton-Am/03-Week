import getpass
import pandas as pd
from company import my_company
from usuario_senha import managers, aut

mngr = managers()
#Authentification function
def authenticate():
    login = input("Login: ")
    passw = getpass.getpass("Password: ")
    if login in mngr and mngr[login] == passw:
       print('Access Successfully.')
       return True
    else:
       return aut(login, passw)
# My CRUD Function
def menu_crud():
    db = my_company()
    cursor = db.cursor()
    while True:
        print("\n --- MENU ---")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        option = input("Your choice: ")
        if option == "1":
            position = input("Key: ")
            name = input("Value: ")
            cursor.execute("INSERT INTO employees (position, name) VALUES (%s, %s)", (position, name))
            db.commit()
            print("Item add successfully!")
        elif option == "2":
            cursor.execute("SELECT * FROM employees")
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=['ID', 'Position', 'Name'])
            print(df.to_string(index=False))

        elif option == "3":
            id = input("ID to update: ")
            position = input("New Position: ")
            name = input("New Name: ")
            cursor.execute("UPDATE employees SET position = %s, name = %s WHERE id = %s", (position, name, id))
            db.commit()
            print("Item update successfully!")
        elif option == "4":
            id = input("ID to Delete: ")
            cursor.execute("DELETE FROM employees WHERE id = %s", (id,))
            db.commit()
            print("Item deleted.")
        elif option == "5":
            print("Program Closed.")
            break
        else:
            print("Invalid Option! Try Again.")

# Main Execution 
if authenticate():
    menu_crud()
else:
    print("Access denied.")

