from add_group import addGroup
from remove_group import removeGroup

def add_remove_group():
    confirm = input(f"\nAdd or Delete a group? (A/D) ").upper()

    if confirm == 'A':
        addGroup()
    elif confirm == 'D':
        removeGroup()
    else:
        print("Wrong input")
        add_remove_group()
add_remove_group()