# import subprocess
import os

def delete_usr_grp():
    print("here's a list of existing Users:\n")
    os.system(f"tail /etc/passwd | cut -d: -f1")
    
    username = input("\nEnter the name of the user to remove from a group: ")
    
    print("here's a list of existing groups:\n")
    os.system("tail /etc/group | cut -d: -f1") # to list all groups seperated by a comma
    
    group = input("\nEnter the group name to abstract the user from: ")
    confirm = input(f"\nAre you sure that you want to abstract the user '{username}' from group '{group}'? (Y/N) ").upper()

    if confirm == 'Y':
        os.system(f"sudo deluser { username } { group }")       # os.system(f"sudo deluser " + username + ' ' + group)
        print(f"the user '{username}' deleted from group '{group}'")
    elif confirm == 'N':
        print("Ok Bye")
    else:
        print("Wrong input")
        delete_usr_grp()

# delete_usr_grp()