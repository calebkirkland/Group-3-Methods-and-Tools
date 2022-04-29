import sqlite3
import os

# Importing the class files
from Inventory import Inventory
import Cart
import Item
import User

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

    # cursor.execute("SELECT * FROM 'Users' WHERE username = '{}' AND password = '{}'".format(username_input, password_input))
    # if cursor.rowcount:
    #     print("Found")
    # else:
    #     print("Not found")

    return

def create_account():
    username = input("Enter your username: ")
    ##TO DO: CHECK IF USERNAME EXISTS
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    ##TO DO: CHECK IF EMAIL EXISTS
    password = input("Enter your password: ")
    print("What is your shipping address?: ")
    street = input("\tEnter your house address and street: ")
    city = input("\tEnter your city: ")
    state = input("\tEnter your state: ")
    zip_code = input("\tEnter your zip code: ")

    cursor.execute('''CREATE TABLE IF NOT EXISTS Users
               (username TEXT,
                first_name TEXT, 
                last_name TEXT, 
                email TEXT, 
                password TEXT,
                street TEXT,
                city TEXT,
                state TEXT,
                zip TEXT)''')
    # TO DO : MAKE SURE THAT ACCOUND DOESNT ALREADY EXIST (CHECK THE DB)
    cursor.execute("INSERT INTO Users VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(username, first_name, last_name, email, password, street, city, state, zip_code))
    print("Account created!")

def print_menu():
    selection = input("1.) Account Information\n2.) Cart Information\n 3.)Inventory Information\nMake a selection (1, 2, or 3): ")
    return selection

def main():
    # Printing the welcome screen and taking input
    welcome_selection = welcome_screen()

    if welcome_selection == '1':
        os.system('cls' if os.name == 'nt' else 'clear') # Clearing the screen for the next menu
        log_in()
    elif welcome_selection == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        create_account()
    elif welcome_selection == '3':
        exit() # Exit the Program

    # Printing the menu and taking input
    menu_selection = print_menu()

    if menu_selection == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        ##TO DO: ACCOUNT INFO
    elif menu_selection == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        ##TO DO: CART INFO
    elif menu_selection == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        inventory1 = Inventory()
        inventory1.add_item("101010", "Sample Item", 999)

    # Commiting the changes to the database (be careful!)
    connection.commit()
    # Closing the connection
    connection.close()

if __name__ == "__main__":
    main()
