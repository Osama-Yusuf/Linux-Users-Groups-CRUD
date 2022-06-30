import os

def add_usr_grp():
    
    print("here's a list of existing Users:\n")
    os.system(f"tail /etc/passwd | cut -d: -f1")
    
    username = input("\nEnter UserName to add to a group: ")
    
    print("here's a list of existing Groups:\n")
    os.system("tail /etc/group | cut -d: -f1") # to list all groups seperated by a comma
    # os.system("groups $FT_USER | tr ' ' ','") # to list all groups seperated by a comma
    
    group = input("\nEnter GroupName to append the user to: ")
    confirm = input(f"\nAre you sure that you want to append the user '{username}' to group '{group}'? (Y/N) ").upper()

    if confirm == 'Y':
        os.system(f"sudo usermod -aG {group} {username}")
        print("User added")
        print("\nUsers under that group")
        os.system(f"getent group {group} | cut -d: -f4")
    elif confirm == 'N':
        print("Ok Bye")
    else:
        print("Wrong input")
        add_usr_grp()
        
# add_usr_grp()