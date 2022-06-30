import os

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