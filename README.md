# **Password manager**
I created a password manager for you and me. Yes, I know it has a few problems, but I will try to solve these problems by learning python. I also said in my profile, that I am still learning python, but I am also greateful, if you can help me.

## **What does it do?**
1. First, the programm is looking for a specific folder named '`.passwords`'. I will create a folder, if it doesn't exist. Please, don't be suprise by that. If it exist then we finished the first step and we go to the second step.

2. Which option do you want to choose?
```
1. Add/Update Alias
2. Get Password From Alias
3. Show All Aliases
4. Remove Alias
5. Quit
Enter your choice:
```
You can choose one of these options: `1`, `2`, `3`, `4` and `5`

### **Add/Update Alias**
In this option you can create an alias.
```
Enter your choice: 1
------------------------------------------
If you want to stop this process, then you can stop it by holding 'controll^ + z' (Mac)
Alias: alias/google.what?
Username: ThienViet
Password: Hey, it's me.
```
You can create aliases, usernames and passwords. 


You added a new alias for your new password and you are finished:
```
------------------------------------------
Password is successfully added/updated!
```
**!!! Please, remember that I am still learning Python. It means it takes time until this programm can encrypt and decrypt.**

### **Get Password From Alias**
In this option you can see your passwords and username. Just write one of your aliases.
```
Enter your choice: 2
Alias: alias/google.what?
------------------------------------------
Username: ThienViet
Password: Hey, it's me.
```
### **Show All Aliases**
It will show all of your aliases
```
Enter your choice: 3
------------------------------------------
google
alias/google.what
Hi Github
```
### **Remove Alias**
You will remove one of your alias.
```
Enter your choice: 4
Alias: alias/google.what
------------------------------------------
Username: Thien
Password: 1234567890

Are you sure you want to delete it: [y/n]
```
I will just ask you one more time.
You only has two options: `y` for 'yes' and `n` for 'no'.

If you enter `y` then it will check, if the alias has been 'deleted' or not.

### **Quit**
You just quit.

## **What will happen in the future?**
It should do these things:
* should be good in all situations
* alternative for `.eval()`
* Encrypt and decrypt your password
* verify by tiping your masterkey and/or 2FA (2FA is only an option)
* it will look better

## **My plan**
This is my plan to finish this project. You can follow me by looking at my plan.

✅ | My plan
:-- | :--
❌ | Looking for all possible situations
✅ | Alternatives for `.eval()`
❌ | Encrypt / Decrypt
❌ | Masterkey
❌ | 2FA (Optional)
❌ | Designs
