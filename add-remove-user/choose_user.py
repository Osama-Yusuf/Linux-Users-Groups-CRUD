from add_user import addUser
from remove_user import removeUser

def add_remove_user():
    confirm = input(f"\nAdd or Delete a user? (A/D) ").upper()

    if confirm == 'A':
        addUser()
    elif confirm == 'D':
        removeUser()
    else:
        print("Please type only A to Add or D to Delete a user")
        add_remove_user()
add_remove_user()