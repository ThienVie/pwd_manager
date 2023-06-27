import os
import json

# test

with open('.passwords/passwords.key', 'r') as f:
    try:
        password_data = f.read()
        password_dict = json.loads(password_data.replace("'", '"'))
    except json.decoder.JSONDecodeError:
        list = {}
    # alias = input('Alias: ')
    # username = input('Username: ')
    # password = input('Password: ')
    # password_dict[alias] = {"Username": username, "Password": password}
    # with open('.passwords/passwords.key', 'w') as f:
    #     f.write(str(password_dict))
    # print("------------------------------------------")
    # print("Password is successfully added/updated!")
    # print()
    list = list(password_dict.keys())
    print(list)
    for l in list:
        print(l)

# if file exist, return True or else False

def exist(a):
    with open('.passwords/passwords.key', 'r') as f:
        list = []
        password_data = f.read()
        password_dict = json.loads(password_data.replace("'", '"'))
        dict = password_dict.keys()
        for l in dict:
            list.append(l)
    if a in list:
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
    with open('.passwords/passwords.key', 'r') as f:
        try:
            password_data = f.read()
            password_dict = json.loads(password_data.replace("'", '"'))
        except json.decoder.JSONDecodeError:
            print('But because there is nothing in the file you can create one safetly.')
    alias = input('Alias: ')
    username = input('Username: ')
    password = input('Password: ')
    password_dict[alias] = {"Username": username, "Password": password}
    if exist(alias) == True:
        copy = input("There is an alias with the same name. It will be updated. \nAre you sure you want to update it: [y/n] ")
        print("------------------------------------------")
        if copy == 'y':
            with open('.passwords/passwords.key', 'w') as f:
                f.write(str(password_dict))
            answer = "Password is successfully updated!"
        elif copy == 'n':
            answer = "That might be a good choice."
        else:
            answer = 'Thst is an invalid choice. No password will be change.'
    else:
        answer = "Password is successfully added!"
    print("------------------------------------------")
    print(answer)
    print()

def get_password():
        alias = input("Alias: ")
        print("------------------------------------------")
        print("------------------------------------------")
        if exist(alias):
            with open('.passwords/passwords.key', 'r') as f:
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
    with open('.passwords/passwords.key', 'r') as f:
        password_data = f.read()
        password_dict = json.loads(password_data.replace("'", '"'))
        dict = password_dict.keys()
        print("All aliases:")
    for l in dict:
        print(l)
    print()

# # delete alias

# def del_password():
#     alias = str(input("Alias: "))
#     print("------------------------------------------")
#     if exist(alias):
#         with open(f'.passwords/passwords.key', 'r') as f:
#             password_data = f.read()
#             password_dict = json.loads(password_data.replace("'", '"'))
#             password_dict = password_dict[alias]
#             username = password_dict["Username"]
#             password = password_dict["Password"]
#             print(f"Username: {username}")
#             print(f"Password: {password}")
#             print()
#             thinking = input("Are you sure you want to delete it: [y/n] ")
#             print("------------------------------------------")
#             if thinking == "y":
#                 os.remove(f'.passwords/{alias}.key')
#                 if os.path.exists(alias):
#                     print("Please, delete it manually.")
#                 else:
#                     print(f"Alias '{alias}' has been deleted.")
#             elif thinking == "n":
#                 print('That might be a good choice.')
#             else:
#                 print("You wrote something wrong. IDK, what you were tiping, but it counts as a 'no' anyway.")
#             print()
#     else:
#         print('Since when was this alias created?')
#         print()

# # combine everything

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
    # elif choice == "4":
    #     del_password()
    elif choice == "5":
        break
    else:
        print("------------------------------------------")
        print("Invalid choice. Please try again.")
        print()
