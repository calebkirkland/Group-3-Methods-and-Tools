import sqlite3

users_connection = sqlite3.connect('database.db')
cursor = users_connection.cursor()


class User:
    def __init__(self):
        cursor.execute('''CREATE TABLE IF NOT EXISTS User
               (username TEXT,
                first_name TEXT, 
                last_id TEXT,
                email TEXT, 
                password TEXT,
                street TEXT, 
                city TEXT,
                state TEXT, 
                zip_code TEXT
                admin BOOL)''')

    def add_user(self, username, first_name, last_name, email, password, street, city, state, zip_code, admin):

        cursor.execute(
            "INSERT INTO Users VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(username, first_name,
                                                                                                  last_name, email,
                                                                                                  password,
                                                                                                  street, city, state,
                                                                                                  zip_code, admin))
        print("Account Created")
        # Commiting the changes to the database (be careful!)
        users_connection.commit()
        # Closing the connection
        users_connection.close()

    def account_info(self, username):
        cursor.execute("Select * FROM Users WHERE username = '{}'".format(username))

        acc = cursor.fetchall()

        print("Username |  First |    Last  |    Email         |  Pass |    Address |    City |  State  |  Zip  |  Admin ")
        for row in acc:
            print(row, "\n")

##constructor/destructor (delete account)
##delete data
##cursor_obj.execute("DELETE FROM User WHERE user_id = ")

    def delete_user(self, username):
        cursor.execute("DELETE  FROM Users WHERE username = '{}'".format(username))

        print("Account has been Deleted")
        # Commiting the changes to the database (be careful!)
        users_connection.commit()
        # Closing the connection
        users_connection.close()

    def account_change(self, choice, changeto, username):

        if choice == '1':

            cursor.execute("SELECT * FROM 'Users' WHERE username = '{}'".format(changeto))

            if not cursor.fetchone():  # An empty result evaluates to False.
                check = False
            else:
                check = True

            while check == True:
                changeto = input("Username Already Taken\nEnter your username: ")
                cursor.execute("SELECT * FROM 'Users' WHERE username = '{}'".format(changeto))
                if not cursor.fetchone():  # An empty result evaluates to False.
                    check = False
                    break
                else:
                    check = True

            cursor.execute("UPDATE Users SET username = '{}' WHERE username = '{}'".format(changeto, username))

            print("Account username has been changed")
            # Commiting the changes to the database (be careful!)
            users_connection.commit()
            # Closing the connection
            users_connection.close()

        elif choice == '2':
            cursor.execute("UPDATE Users SET first_name = '{}' WHERE username = '{}'".format(changeto, username))

            print("Account username has been changed")
            # Commiting the changes to the database (be careful!)
            users_connection.commit()
            # Closing the connection
            users_connection.close()
        elif choice == '3':
            cursor.execute("UPDATE Users SET last_name = '{}' WHERE username = '{}'".format(changeto, username))

            print("Account username has been changed")
            # Commiting the changes to the database (be careful!)
            users_connection.commit()
            # Closing the connection
            users_connection.close()
        elif choice == '4':

            cursor.execute("SELECT * FROM 'Users' WHERE email = '{}'".format(changeto))
            if not cursor.fetchone():  # An empty result evaluates to False.
                check = False

            else:
                check = True

            while check == True:
                changeto = input("That email is already in use\nEnter your email address: ")
                cursor.execute("SELECT * FROM 'Users' WHERE email = '{}'".format(changeto))
                if not cursor.fetchone():  # An empty result evaluates to False.
                    check = False
                    break
                else:
                    check = True

            cursor.execute("UPDATE Users SET email = '{}' WHERE username = '{}'".format(changeto, username))

            print("Account username has been changed")
            # Commiting the changes to the database (be careful!)
            users_connection.commit()
            # Closing the connection
            users_connection.close()
        elif choice == '5':
            cursor.execute("UPDATE Users SET password = '{}' WHERE username = '{}'".format(changeto, username))

            print("Account username has been changed")
            # Commiting the changes to the database (be careful!)
            users_connection.commit()
            # Closing the connection
            users_connection.close()
        elif choice == '6':
            cursor.execute("UPDATE Users SET street = '{}' WHERE username = '{}'".format(changeto, username))

            print("Account username has been changed")
            # Commiting the changes to the database (be careful!)
            users_connection.commit()
            # Closing the connection
            users_connection.close()

        elif choice == '7':
            cursor.execute("UPDATE Users SET city = '{}' WHERE username = '{}'".format(changeto, username))

            print("Account username has been changed")
            # Commiting the changes to the database (be careful!)
            users_connection.commit()
            # Closing the connection
            users_connection.close()
        elif choice == '8':
            cursor.execute("UPDATE Users SET state = '{}' WHERE username = '{}'".format(changeto, username))

            print("Account username has been changed")
            # Commiting the changes to the database (be careful!)
            users_connection.commit()
            # Closing the connection
            users_connection.close()
        elif choice == '9':
            cursor.execute("UPDATE Users SET zip = '{}' WHERE username = '{}'".format(changeto, username))

            print("Account username has been changed")
            # Commiting the changes to the database (be careful!)
            users_connection.commit()
            # Closing the connection
            users_connection.close()

    def display_allUsers(self):

        cursor.execute("SELECT * FROM Users ORDER BY username")

        user = cursor.fetchall()
        print("Username |  First |    Last  |    Email         |  Pass |    Address |    City |  State  |  Zip  |  Admin ")
        for row in user:
            print(row, "\n")
##def AddToHistory():
##cursor.execute()
## '''INSERT INTO History(username, first_name, last_name, email, password, street, city, state, zip_code)
## VALUES ('', '', '', '')''')


##def PrintOrderHistory():
##print("Print Order History Table: ")
## data = cursor.execute('''SELECT * FROM OrderHistory`''')
## for row in data:
##     print(row)


##def PrintShoppingCart():
##print("Print Shopping Cart: ")
##  data = cursor.execute('''SELECT * FROM ShoppingCart''')
## for row in data:
##    print(row)


##def UpdateShippingInfo():
##connection.execute("UPDATE ShippingInfo SET column_name1=value1, column_name2=value2")


##def LogOut():
