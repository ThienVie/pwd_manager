import os
import time
passwords = {}
# ------------ add passwords -------------

def add_password():
    alias = str(input("Alias: "))
    username = str(input("Username: "))
    password = str(input("Password: "))
    passwords[alias] = {alias:{"Username": username, "Password": password}}
    with open(f'.passwords/{alias}.key', 'w') as f:
        f.write(str(passwords[alias]))
    print("------------------------------------------")
    print("Password was successfully updated!")
    print()

# -------------- get passwords --------------

def get_password():
        alias = input("Alias: ")
        if os.path.exists(f'.passwords/{alias}.key'):
            with open(f'.passwords/{alias}.key', 'r') as f:
                password_data = f.read()
                password_dict = eval(password_data)
            if alias in password_dict:
                password_dict = password_dict[alias]
                username = password_dict["Username"]
                password = password_dict["Password"]
                print("------------------------------------------")
                print(f"Username: {username}")
                print(f"Password: {password}")
            else:
                print("------------------------------------------")
                print("Alias is not found. Make sure that you wrote everything.")
            print()
        else:
            print("------------------------------------------")
            print('Are you sure that it really exist?')
            print()
# -------------- all passwords ---------------

def all_password():
    files = []
    for file in os.listdir('.passwords'):
        file = file.replace(".key", '')
        files.append(file)
    print("------------------------------------------")
    print(files)
    print()

# ------------- delete password --------------

def del_password():
    alias = str(input("Alias: "))
    file = f'.passwords/{alias}.key'
    if os.path.exists(file):
        with open(f'{file}', 'r') as f:
            password_data = f.read()
            password_dict = eval(password_data)
        if alias in password_dict:
            password_dict = password_dict[alias]
            username = password_dict["Username"]
            password = password_dict["Password"]
            print("------------------------------------------")
            print(f"Username: {username}")
            print(f"Password: {password}")
            print()
            thinking = input("Are you sure you want to delete it: [y/n] ")
            if thinking == "y":
                os.remove(alias)
                print(f'Delete {alias}')
                print("Wait 5 seconds")
                time.sleep(1)
                print("Making sure that it's deleted.")
                time.sleep(4)
                if os.path.exists(alias):
                    print("------------------------------------------")
                    print("Please, delete it manually.")
            elif thinking == "n":
                print("------------------------------------------")
                print('That might be a good choice.')
            else:
                print("------------------------------------------")
                print("You wrote something wrong. IDK, what you were tiping, but it counts as a 'no' anyway.")
            print()
    else:
        print("------------------------------------------")
        print('Since when was this website created?')
        print()

# ----------- combine everything ------------

while True:
    print("1. Add/Change Alias [a/c]")
    print("2. Get Password From Alias [get]")
    print("3. Show All Aliases[sall]")
    print("4. Remove Alias[rm]")
    print("5. Quit[q]")
    choice = input("Enter your choice: ")

    if choice == "1" or 'a' or 'c':
        add_password()
    elif choice == "2" or 'get':
        get_password()
    elif choice == "3" or 'sall':
        all_password()
    elif choice == "4" or 'rm':
        del_password()
    elif choice == "5" or 'q':
        break
    else:
        print("------------------------------------------")
        print("Invalid choice. Please try again.")
        print()
