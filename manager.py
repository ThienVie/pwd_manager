import os
import json


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


# add folder/file

def add_folder():
    path = '.passwords'
    if os.path.exists(path):
        return True
    else:
        return False

def add_file():
    path = '.passwords/passwords.key'
    if os.path.exists(path):
        return True
    else:
        return False


# add passwords

def add_password():
    print("------------------------------------------")
    print("If you want to stop this process, then you can press 'control^ + z' (Unix)")
    print("or 'ctr + c' (Windows).")
    with open('.passwords/passwords.key', 'r') as f:
        password_data = f.read()
        if password_data == '{}':
            print('But because there is nothing in the file you can create one safely.')
        password_dict = json.loads(password_data.replace("'", '"'))
    alias = input('Alias: ')
    username = input('Username: ')
    password = input('Password: ')
    password_dict[alias] = {"Username": username, "Password": password}
    if exist(alias):
        with open(f'.passwords/passwords.key', 'r'):
            password_dict2 = json.loads(password_data.replace("'", '"'))
            password_dict2 = password_dict2[alias]
            username2 = password_dict2["Username"]
            password2 = password_dict2["Password"]
        print("------------------------------------------")
        if password_dict2["Username"] == username and password_dict2["Password"] == password:
            answer = "Username and Passwords are the same. There will be no changes."
        else:
            print("There is an alias with the same name:")
            print(f'Old Username: {username2}')
            print(f'Old Password: {password2}')
            copy = input("It will be updated. Are you sure you want to update it: [y/n] ")
            if copy == 'y':
                with open('.passwords/passwords.key', 'w') as f:
                    f.write(str(password_dict))
                answer = "Password is successfully updated!"
            elif copy == 'n':
                answer = "No changes and that might be a good choice."
            else:
                answer = 'Thst is an invalid choice. No password will be changed.'
    else:
        with open('.passwords/passwords.key', 'w') as f:
            f.write(str(password_dict))
        answer = "Password is successfully added!"
    print("------------------------------------------")
    print('Result:')
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
    print("All aliases:")
    print("------------------------------------------")
    with open('.passwords/passwords.key', 'r') as f:
        password_data = f.read()
        password_dict = json.loads(password_data.replace("'", '"'))
        dict = password_dict.keys()
    for l in dict:
        print(l)
    print()


# delete alias

# noinspection PyAssignmentToLoopOrWithParameter
def del_password():
    alias = str(input("Alias: "))
    print("------------------------------------------")
    if exist(alias):
        with open(f'.passwords/passwords.key', 'r') as f:
            password_data = f.read()
            password_dict = json.loads(password_data.replace("'", '"'))
            confirm = password_dict[alias]
            username = confirm["Username"]
            password = confirm["Password"]
            print(f"Username: {username}")
            print(f"Password: {password}")
            print()
            thinking = input("Are you sure you want to delete it: [y/n] ")
            print("------------------------------------------")
            print('Result:')
            print("------------------------------------------")
            if thinking == "y":
                del password_dict[alias]
                with open(f'.passwords/passwords.key', 'w') as f:
                    f.write(str(password_dict))
                print(f"Alias '{alias}' has been deleted.")
            elif thinking == "n":
                print('No deletion and that might be a good choice.')
            else:
                print("You wrote something wrong. IDK, what you were typing, but it counts as a 'no' anyway.")
            print()
    else:
        print("------------------------------------------")
        print("Alias doesn't exist.")
        print()


# combine everything

def main():
    try:
        while True:
            if not add_folder():
                os.makedirs('.passwords')
                open('.passwords/passwords.key', 'w').close()

            with open('.passwords/passwords.key', 'r+') as f:
                test = f.read()
                if test == '':
                    f.write('{}')

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
    except KeyboardInterrupt:
        print()
        print('You interrupted this programm. This programm will stop.')
        

if __name__ == '__main__':
    main()