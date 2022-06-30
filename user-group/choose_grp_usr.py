from apnd_usr_grp import add_usr_grp
from abstrct_usr_grp import delete_usr_grp

def append_usr_grp():
    confirm = input(f"\nAdd or Delete a user to/from a group? (A/D) ").upper()

    if confirm == 'A':
        add_usr_grp()
    elif confirm == 'D':
        delete_usr_grp()
    else:
        print("\nWrong input")
        append_usr_grp()
append_usr_grp()