import os

def removeUser():
    print("Users in the system:\n")
    os.system(f"tail /etc/passwd | cut -d: -f1")
    
    username = input("\nEnter the name of the user to remove: ")
    confirm = input(f"\nAre you sure that you want to remove the user '{username}'? (Y/N) ").upper()

    if confirm == "Y":
        os.system(f"sudo userdel -r {username}")
        print("User deleted")
    elif confirm == 'N':
        print("Ok Bye")
    else:
        print("Wrong input")
        removeUser()
        
# removeUser()