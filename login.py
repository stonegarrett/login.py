# This program will prompt the user if they
# would like to login or create and account
# This is merely an exercise and is not the
# proper way to store or check credentials

import csv

# Declare global variables
filename = 'db.csv'


# Prompts the user to select if they would like to login or Create an Account
def welcome_prompt():
    choice = input("Welcome! Would you like to (L)Login "
                   "or (C)Create an Account?: \n")
    login_choice(choice)


# Based on user choice, presents either the
# login prompt, create account prompt, or
# informs the user they have made an invalid choice
def login_choice(choice):
    if choice.lower() == "l":
        login_prompt()
    elif choice.lower() == "c":
        create_account_prompt()
    else:
        print("Sorry I did not understand that.")
        welcome_prompt()


# Prompts for username and Password then passes that
# information to the check password function
def login_prompt():
    user_name = input("UserName: ")
    pw = input("Password: ")
    check_password(user_name, pw)


# Displays create account prompt. User is prompted for username and password.
# If username already exists, user is prompted for a new username.
# If username does not exist, user is prompted for password.
# Once user enters password the create_account function is called.
def create_account_prompt():
    print("Please provide the following details to create your account")
    user_name = input("Select a UserName: ")
    if username_exists(user_name):
        print("Sorry, that username is not available. "
              "Please select a different username")
        create_account_prompt()
    else:
        pw = input("Select a Password: ")
        create_account(user_name, pw)
        login_prompt()


# Appends the CSV file with username and password provided
def create_account(user_name, pw):
    with open(filename, 'a', newline="") as file:
            file_writer = csv.writer(file)
            file_writer.writerow([user_name, pw])
    file.close()
    print("Your account has been created")
    print("You can now login using your account name and password")


# Opens CSV and determines if username is already in use
def username_exists(username):
    with open(filename, 'r') as file:
        file_reader = csv.reader(file)
        for line in file_reader:
            if username in line:
                return True
        return False
    file.close()


# Determines if password matches username in CSV file
def check_password(username, pw):
    with open(filename, "r") as file:
        file_reader = csv.reader(file)
        for line in file_reader:
            if username in line:
                if pw == line[1]:
                    login(username)
                    return
        file.close()
        print("Please check your Username and Password and try again")
        login_prompt()


# Thanks the user for logging in
def login(username):
    print("Thank you for logging in " + username)


# Calls welcome function
def main():
    welcome_prompt()


main()
