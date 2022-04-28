import sqlite3
import os

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
    print("Logging in...\n")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    return

def create_account():
    username = input("Enter your username: ")
    # TO DO: CHECK IF USERNAME EXISTS
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    # TO DO: CHECK IF EMAIL EXISTS
    password = input("Enter your password: ")
    print("What is your shipping address?: ")
    street = input("\tEnter your house address and street:")
    city = input("\tEnter your city:")
    state = input("\tEnter your state: ")
    zip_code = input("\tEnter your zip code: ")

    cursor.execute('''CREATE TABLE IF NOT EXISTS Users
               (username text,
                first_name text, 
                last_name text, 
                email text, 
                password text,
                street text,
                city text,
                state text,
                zip text)''')

    cursor.execute("INSERT INTO Users VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(username, first_name, last_name, email, password, street, city, state, zip_code))

def main():
    # Printing the welcome screen
    user_selection = welcome_screen()

    if user_selection == '1':
        os.system('cls' if os.name == 'nt' else 'clear') # Clearing the screen for the next menu
        log_in()
    elif user_selection == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        create_account()
    elif user_selection == '3':
        exit() # Exit the Program

    # Commiting the changes to the database (be careful!)
    connection.commit()
    # Closing the connection
    connection.close()

if __name__ == "__main__":
    main()