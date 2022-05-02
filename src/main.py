import sqlite3
import os

# Importing the class files
from inventory import Inventory
import Cart
from item import Item
from user import User

# Connecting to our database and creating the cursor object
connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def welcome_screen():
    # Print the initial welcome Screen
    print("-----------------------------")
    print("Welcome to our online store!")
    print("-----------------------------")

    selection = input("1.) Login\n2.) Create Account\n3.) Exit Program\nMake a selection (1, 2, or 3): ")

    while selection != '1' and selection != '2' and selection != '3':
        print("Invalid Selection! Try again: ")
        selection = input("1.) Login\n2.) Create Account\n3.) Exit Program\nMake a selection (1, 2, or 3): ")
    return selection


def log_in():
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    # TO DO: AUTHENTICATE INPUT FROM THE DB

    cursor.execute(
        "SELECT * FROM 'Users' WHERE username = '{}' AND password = '{}'".format(username_input, password_input))

    if not cursor.fetchone():  # An empty result evaluates to False.
        print("Login failed")

        return False, False, ""
    else:
        cursor.execute("SELECT admin FROM 'Users' WHERE username = '{}'".format(username_input))
        a = cursor.fetchone()
        username = username_input
        if a == ('True',):  # An empty result evaluates to False.
            print("Welcome Admin")

            return True, True, username
        else:
            print("Welcome")

            return True, False, username


def create_account():
    ##Checks if username is in use
    username = input("Enter your username: ")
    cursor.execute("SELECT * FROM 'Users' WHERE username = '{}'".format(username))

    if not cursor.fetchone():  # An empty result evaluates to False.
        check = False
    else:
        check = True

    while check == True:
        username = input("Username Already Taken\nEnter your username: ")
        cursor.execute("SELECT * FROM 'Users' WHERE username = '{}'".format(username))
        if not cursor.fetchone():  # An empty result evaluates to False.
            check = False
            break
        else:
            check = True

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    ##CHECK IF EMAIL EXISTS

    email = input("Enter your email address: ")
    cursor.execute("SELECT * FROM 'Users' WHERE email = '{}'".format(email))
    if not cursor.fetchone():  # An empty result evaluates to False.
        check = False

    else:
        check = True

    while check == True:
        email = input("That email is already in use\nEnter your email address: ")
        cursor.execute("SELECT * FROM 'Users' WHERE email = '{}'".format(email))
        if not cursor.fetchone():  # An empty result evaluates to False.
            check = False
            break
        else:
            check = True

    password = input("Enter your password: ")
    print("What is your shipping address?: ")
    street = input("\tEnter your house address and street: ")
    city = input("\tEnter your city: ")
    state = input("\tEnter your state: ")
    zip_code = input("\tEnter your zip code: ")

    adminCheck = input("Enter admin code or type 1: ")

    if adminCheck == "1010":
        admin = True
    else:
        admin = False

    user1 = User()
    user1.add_user(username, first_name, last_name, email, password, street, city, state, zip_code, admin)


def print_menu():
    selection = input(
        "1.) Account Information\n2.) Cart Information\n3.)Inventory Information \n4.)Logout \nMake a selection (1, 2, 3, or 4): ")
    return selection


def print_adminMenu():
    selection = input(
        "1.)Account Information \n2.)User information \n3.)Edit Inventory \n4.)Logout  \nMake a selection (1, 2, 3, or 4): ")
    return selection

def account_infoMenu():
    selection = input(
        "1.) View account info\n 2.)Edit info\n 3.)Delete Account \n4.)Back\nMake a selection (1, 2, 3, or 4):  ")
    return selection

def account_info(username):
    user1 = User()

    out = 0

    select_info = account_infoMenu()
    if select_info == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        ##Display account
        user1.account_info(username)
        return False

    elif select_info == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        ##TO DO: User information

        choice = input("1.)Username\n 2.)First Name\n 3.)Last Name\n 4.)Email\n 5.)Password\n6.)Street\n7.)City\n8.)State\n9.)Zip\nMake a selection 1-9: ")
        changeTo = input("What do you want it to change to?: ")

        user1.account_change(choice, changeTo, username)
        print("Log back in to see changes!")
        return True

    elif select_info == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        user1.delete_user(username)
        return True

    elif select_info == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        return False

def edit_inventoryMenu():
    selection = input(
        "1.)Remove Item \n2.)Edit Item \n3.)Edit Inventory \n4.)Back  \nMake a selection (1, 2, 3, or 4): ")
    return selection

def edit_inventory():
    select_inventory = edit_inventoryMenu()

    while(select_inventory != 4):
        if select_inventory == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            ##TO DO: Account Information 3.)User information \n 3.)Edit Inventory \n4.)Logout
        elif select_inventory == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            ##TO DO: User information
        elif select_inventory == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            ##Edit Inventory
        elif select_inventory == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            ##Logout
            return




def main():
    # Printing the welcome screen and taking input
    log = False  ##Check for T/F if user was able to log in
    admin = False  ##Check for if user is an admin
    username = ""
    ##leave = False  ##Loops menu till exited
    os.system('cls' if os.name == 'nt' else 'clear')
    while (log != True):
        welcome_selection = welcome_screen()
        if welcome_selection == '1':
            os.system('cls' if os.name == 'nt' else 'clear')  # Clearing the screen for the next menu
            log, admin, username = log_in()
        elif welcome_selection == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            create_account()
        elif welcome_selection == '3':
            exit()

    # Printing the menu and taking input
    logout = False
    while logout == False:
        os.system('cls' if os.name == 'nt' else 'clear')
        if admin == True:
            menu_selection = print_adminMenu()
            if menu_selection == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                ##TO DO: Account Information
                deleted = False
                deleted = account_info(username)

                if deleted:
                    break

            elif menu_selection == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                ##TO DO: User information
            elif menu_selection == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                ##Edit Inventory
                edit_inventoryMenu()

            elif menu_selection == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                ##Logout
                break
        else:
            menu_selection = print_menu()

            if menu_selection == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                ##TO DO: ACCOUNT INFO
                deleted = False
                deleted = account_info(username)

                if deleted:
                    break
            elif menu_selection == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                ##TO DO: CART INFO
            elif menu_selection == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                inventory1 = Inventory()
                ##shows inventory
                inventory1.show_inventory()

            elif menu_selection == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                ##logsout
                break

    ##Bad way to repeat function, but can we fixed later
    main()

if __name__ == "__main__":
    main()
