import os, json, getpass, pyperclip, time, threading, signal, sys
from colorama import Fore

# add folder/file
def setup() -> None:
    try:os.makedirs('.passwords')
    except:pass
    try:open('.passwords/passwords.json', 'a').close()
    except:pass

def show_result(result, message="") -> None:
    print("")
    print(f'Result: \033[1m{result}\033[0m')
    print("------------------------------------------")
    print(f"{message}\n")

def ctrz(signum="", frame=""):
    print("")
    pyperclip.copy("")
    print("ctr + z kills this programm. Don't worry, there is nothing in the clipboard. See you next time!")
    print("It takes some time. :)")
    sys.exit(0)

signal.signal(signal.SIGTSTP, ctrz)

def copy_nothing():
    time.sleep(10)
    pyperclip.copy("")



def add_password():
    print("------------------------------------------")

    website = input('Website: ')

    new_username = input('Username: ')
    new_password = getpass.getpass("Password: ")

    with open('.passwords/passwords.json', 'r') as f:
        data = f.read()
        password_dict = json.loads(data)
        try:
            password_dict[website]
        except:
            password_dict[website] = []
        user = []
        for users in password_dict[website]:
            user.append(users["Username"])
        if not new_username in user:
            password_dict[website].append({"Username": new_username, "Password": new_password})
            with open('.passwords/passwords.json', 'w') as f:
                f.write(json.dumps(password_dict, indent=4))
            report = f"{Fore.GREEN}Successfull!{Fore.RESET}"
            answer = "Password is successfully added!"
            show_result(report, answer)
        else:
            result = f"{Fore.RED}Username already exist."
            message = "Try something else."
            show_result(result, message)

    ######### probably for updating the password. But I will check later.

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
    password_dict = {}


def get_password():
    website = input("Website: ")
    username = input("Username: ")
    try:
        user_list = []
        with open('.passwords/passwords.json', 'r') as f:
            input(f"\033[1m{Fore.RED}Please make sure that you don't paste this password somewhere dangerous. Press Enter to continue.{Fore.RESET}\033[0m")
            data = f.read()
            password_dict = json.loads(data)
            try:
                for user in password_dict[website]:
                    user_list.append(user["Username"])
                pyperclip.copy(password_dict[website][user_list.index(username)]["Password"])
                threading.Thread(target=copy_nothing, args=()).start()
                result = f"{Fore.GREEN}Success{Fore.RESET}"
                message = "Password has been copied to clipboard."
                show_result(result, message)
            except Exception as e:
                message = "Website doesn't exist."
                report = f"{Fore.RED}Error{Fore.RESET}"
                show_result(report)
                print(e)
            password_dict = {}
    except:
        print("")
        

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
            print("     1. Add a new password")
            print("     2. Get Password From Alias")
            print("     3. Show All Aliases")
            print("     4. Remove Alias")
            print("     5. Quit\n")
            choice = input("> ")

            if choice == "1":
                add_password()
            elif choice == "2":
                get_password()
            # elif choice == "3":
            #     all_password()
            # elif choice == "4":
            #     del_password()
            elif choice == "5":
                break
            else:
                result = f"{Fore.RED}Error{Fore.RESET}"
                message = "Invalid choice. Please try again."
                show_result(result, message)
            pass
    except KeyboardInterrupt:
        print()
        print('You interrupted this programm. This programm will stop.')
        print('And clipboard has been cleaned.')
    pyperclip.copy("")   
        

if __name__ == '__main__':
    main()