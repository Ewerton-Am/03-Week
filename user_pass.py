import getpass
import secrets
import string

#dict with access info 
def managers():
    return {'admin':'admin'}
#Authentification
def aut(login,passw):
    x = managers()
    print('Login authorized required:')
    login = input("Login: ")
    passw = getpass.getpass("Password: ")
    if login in x and x[login] == passw:
        print("Login successfully!\n")
        return True
        
