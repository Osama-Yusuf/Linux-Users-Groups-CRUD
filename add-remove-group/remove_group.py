import os

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