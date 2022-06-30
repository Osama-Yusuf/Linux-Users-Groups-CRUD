import sys

sys.path.append('/home/osama/py/add-remove-user')     # add or remove user module     
sys.path.append('/home/osama/py/add-remove-group')    # add or remove group module
sys.path.append('/home/osama/py/user-group')    # append / abstract a user to/from group module

def choose():
    confirm = input("""Which of the following tasks would you like to achieve
                    
    1- Add or Delete a user
    2- Add or Delete a group
    3- Add or Delete a user to/from a group
    
    (1),(2),(3): """)

    if confirm == '1':
        from choose_user import add_remove_user
    elif confirm == '2':
        from choose_group import add_remove_group
    elif confirm == '3':
        from choose_grp_usr import append_usr_grp
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