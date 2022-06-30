#!/usr/bin/env python3

import sys
import os

# --------------------------- create or delete user -------------------------- #

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

def add_remove_user():
    confirm = input(f"\nAdd or Delete a user? (A/D) ").upper()

    if confirm == 'A':
        addUser()
    elif confirm == 'D':
        removeUser()
    else:
        print("Please type only A to Add or D to Delete a user")
        add_remove_user()
# add_remove_user()

# --------------------------- create or delete user -------------------------- #

# -------------------------- create or delete group -------------------------- #

def addGroup():
    group = input("Enter the name of the group to add: ")
    confirm = input(f"\nAre you sure that you want to create the group '{group}'? (Y/N) ").upper()

    if confirm == 'Y':
        os.system(f"sudo addgroup {group}")
        print("group added")
    elif confirm == 'N':
        print("Ok Bye")
    else:
        print("Wrong input")
        addGroup()
# addGroup()

def removeGroup():
    
    print("\nGroups in the system:")
    os.system(f"groups | cut -d: -f4")
    
    group = input("\nEnter the name of the group to remove: ")
    confirm = input(
        f"\nAre you sure that you want to remove the group '{group}'? (Y/N) ").upper()

    if confirm == "Y":
        os.system(f"sudo groupdel -f {group}")
        print("group deleted")
    elif confirm == 'N':
        print("Ok Bye")
    else:
        print("Wrong input")
        removeGroup()
# removeGroup()

def add_remove_group():
    confirm = input(f"\nAdd or Delete a group? (A/D) ").upper()

    if confirm == 'A':
        addGroup()
    elif confirm == 'D':
        removeGroup()
    else:
        print("Wrong input")
        add_remove_group()
# add_remove_group()

# -------------------------- create or delete group -------------------------- #

# ------------------ append or abstract a user from a group ------------------ #

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

def append_usr_grp():
    confirm = input(f"\nAdd or Delete a user to/from a group? (A/D) ").upper()

    if confirm == 'A':
        add_usr_grp()
    elif confirm == 'D':
        delete_usr_grp()
    else:
        print("\nWrong input")
        append_usr_grp()
# append_usr_grp()

# ------------------ append or abstract a user from a group ------------------ #

def choose():
    confirm = input("""Which of the following tasks would you like to achieve
                    
    1- Add or Delete a user
    2- Add or Delete a group
    3- Add or Delete a user to/from a group
    
    (1),(2),(3): """)

    if confirm == '1':
        add_remove_user()
    elif confirm == '2':
        add_remove_group()
    elif confirm == '3':
        append_usr_grp()
    else:
        print("Wrong input")
        choose()
        
choose()

print ("""
Made By Osama-Yusuf
My Linkedin: https://www.linkedin.com/in/osama--youssef/
GitHub Repo: https://github.com/Osama-Yusuf/Linux-Users-Groups-CRUD
""")

# Made by Osama-Yusuf
# GitHub Repo: https://github.com/Osama-Yusuf/Linux-Users-Groups-CRUD
# My Linkedin: https://www.linkedin.com/in/osama--youssef/