import os
import time
import json
passwords = {}

# if file exist, return True or else False

def exist(alias):
    f'.passwords/{alias}.key'
    if os.path.exists(f'.passwords/{alias}.key'):
        return True
    else:
        return False


# add folder

def add_folder():
    path = '.passwords'
    if os.path.exists(path):
        return True
    else:
        return False

# add passwords

def add_password():
    print("------------------------------------------")
    print("If you want to stop this process, then you can press 'controll^ + z' (Mac)")
    alias = str(input("Alias: "))
    username = str(input("Username: "))
    password = str(input("Password: "))
    passwords[alias] = {alias:{"Username": username, "Password": password}}
    with open(f'.passwords/{alias}.key', 'w') as f:
        f.write(str(passwords[alias]))
    print("------------------------------------------")
    print("Password is successfully updated!")
    print()

# get passwords

def get_password():
        alias = input("Alias: ")
        print("------------------------------------------")
        if exist(alias):
            with open(f'.passwords/{alias}.key', 'r') as f:
                password_data = f.read()
                password_dict = json.loads(password_data.replace("'", '"'))
                password_dict = password_dict[alias]
                username = password_dict["Username"]
                password = password_dict["Password"]
                print(f"Username: {username}")
                print(f"Password: {password}")
        else:
            print('Are you sure that it really exist?')
        print()

# show all aliases

def all_password():
    print("------------------------------------------")
    files = []
    for file in os.listdir('.passwords'):
        x = file.split(".")
        le = len(x)
        del x[le-1]
        files = '.'.join(x)
        print(files)
    print()

# delete alias

def del_password():
    alias = str(input("Alias: "))
    print("------------------------------------------")
    if exist(alias):
        with open(f'.passwords/{alias}.key', 'r') as f:
            password_data = f.read()
            password_dict = json.loads(password_data.replace("'", '"'))
            password_dict = password_dict[alias]
            username = password_dict["Username"]
            password = password_dict["Password"]
            print(f"Username: {username}")
            print(f"Password: {password}")
            print()
            thinking = input("Are you sure you want to delete it: [y/n] ")
            print("------------------------------------------")
            if thinking == "y":
                os.remove(f'.passwords/{alias}.key')
                if os.path.exists(alias):
                    print("Please, delete it manually.")
                else:
                    print(f"Alias '{alias}' has been deleted.")
            elif thinking == "n":
                print('That might be a good choice.')
            else:
                print("You wrote something wrong. IDK, what you were tiping, but it counts as a 'no' anyway.")
            print()
    else:
        print('Since when was this alias created?')
        print()

# combine everything

while True:
    if add_folder() == False:
        os.makedirs('.passwords')
    print()
    print("1. Add/Update Alias")
    print("2. Get Password From Alias")
    print("3. Show All Aliases")
    print("4. Remove Alias")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        get_password()
    elif choice == "3":
        all_password()
    elif choice == "4":
        del_password()
    elif choice == "5":
        break
    else:
        print("------------------------------------------")
        print("Invalid choice. Please try again.")
        print()