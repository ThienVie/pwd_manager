import os, json, getpass
from colorama import Fore
# add folder/file

def setup() -> None:
    try:os.makedirs('.passwords')
    except:pass
    try:open('.passwords/passwords.json', 'a').close()
    except:pass

def result(result, message) -> None:
    print("")
    print(f'Result: {result}')
    print("------------------------------------------")
    print(f"{message}\n")


# add passwords

def add_password():
    print("------------------------------------------")
    print("If you want to stop this process, then you can press 'control^ + z'")
    print("or 'ctr + c'.")

    alias:str = input('Website: ')

    username:str = input('Username: ')
    print(username)
    password:str = getpass.getpass("Password: ")
    print(password)

    with open('.passwords/passwords.json', 'r') as f:
        encrypted_data = f.read()
        password_dict = json.loads(encrypted_data)
        try:
            password_dict[alias]
        except:
            password_dict[alias] = []
        
    password_dict[alias].append({"Username": username, "Password": password})

    #     with open(f'.passwords/passwords.json', 'r'):
    #         password_dict2 = json.loads(encrypted_data)
    #         password_dict2 = password_dict2[alias]
    #         username2 = password_dict2["Username"]
    #         password2 = password_dict2["Password"]
    #     print("------------------------------------------")
    #     if password_dict2["Username"] == username and password_dict2["Password"] == password:
    #         answer = "Username and Passwords are the same. There will be no changes."
    #     else:
    #         print("There is an alias with the same name:")
    #         print(f'Old Username: {username2}')
    #         print(f'Old Password: {password2}')
    #         copy = input("It will be updated. Are you sure you want to update it: [y/n] ")
    #         if copy == 'y':
    #             with open('.passwords/passwords.json', 'w') as f:
    #                 f.write(json.dumps(password_dict, indent=4))
    #             answer = "Password is successfully updated!"
    #         elif copy == 'n':
    #             answer = "No changes and that might be a good choice."
    #         else:
    #             answer = 'Thst is an invalid choice. No password will be changed.'
    with open('.passwords/passwords.json', 'w') as f:
        f.write(json.dumps(password_dict, indent=4))
    password_dict = []
    report = f"{Fore.GREEN}Successfull!{Fore.RESET}"
    answer = "Password is successfully added!"
    result(report, answer)



# def get_password():
#     alias = input("Alias: ")
#     print("------------------------------------------")
#     print("Result:")
#     print("------------------------------------------")
#     if exist(alias):
#         with open('.passwords/passwords.json', 'r') as f:
#             password_data = f.read()
#             password_dict = json.loads(password_data)
#             password_dict = password_dict[alias]
#             username = password_dict["Username"]
#             password = password_dict["Password"]
#             print(f"Username: {username}")
#             print(f"Password: {password}")
#     else:
#         print('Are you sure that it really exist?')
#     print()


# show all aliases

# def all_password():
#     print("------------------------------------------")
#     print("Result:")
#     print("------------------------------------------")
#     with open('.passwords/passwords.json', 'r') as f:
#         password_data = f.read()
#         password_dict = json.loads(password_data)
#         dict = password_dict.keys()
#     for l in dict:
#         print(l)
#     print()


# delete alias

# noinspection PyAssignmentToLoopOrWithParameter
# def del_password():
#     alias = str(input("Alias: "))
#     print("------------------------------------------")
#     if exist(alias):
#         with open(f'.passwords/passwords.json', 'r') as f:
#             password_data = f.read()
#             password_dict = json.loads(password_data)
#             confirm = password_dict[alias]
#             username = confirm["Username"]
#             password = confirm["Password"]
#             print(f"Username: {username}")
#             print(f"Password: {password}")
#             print()
#             thinking = input("Are you sure you want to delete it: [y/N] ")
#             print("------------------------------------------")
#             print('Result:')
#             print("------------------------------------------")
#             if thinking.lower() == "y":
#                 del password_dict[alias]
#                 with open(f'.passwords/passwords.json', 'w') as f:
#                     f.write(str(password_dict))
#                 print(f"Alias '{alias}' has been deleted.")
#             else:
#                 print('No passwords will be deleted.')
#             print()
#     else:
#         print("------------------------------------------")
#         print("Alias doesn't exist.")
#         print()


# combine everything

def main():
    try:
        while True:
            setup()

            with open('.passwords/passwords.json', 'r+') as f:
                file = f.read()
                if file == '':
                    f.write('{}')

            print()
            print("     1. Add new password")
            print("     2. Get Password From Alias")
            print("     3. Show All Aliases")
            print("     4. Remove Alias")
            print("     5. Quit\n")
            choice = input("> ")

            if choice == "1":
                add_password()
            # elif choice == "2":
            #     get_password()
            # elif choice == "3":
            #     all_password()
            # elif choice == "4":
            #     del_password()
            elif choice == "5":
                break
            else:
                print("------------------------------------------")
                print("Invalid choice. Please try again.")
                print()
    except KeyboardInterrupt:
        print()
        print('You interrupted this programm. This programm will stop.')
        

if __name__ == '__main__':
    main()