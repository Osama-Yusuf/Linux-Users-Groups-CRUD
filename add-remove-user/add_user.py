import os

def addUser():
    username = input("Enter the name of the user to add: ")
    confirm = input(f"\nAre you sure that you want to create the user '{username}'? (Y/N) ").upper()

    if confirm == 'Y':
        os.system(f"sudo adduser {username}")
        print("User added")
    elif confirm == 'N':
        print("Ok Bye")
    else:
        print("Wrong input")
        addUser()
        
# addUser()