import sqlite3

user_connection = sqlite3.connect('database.db')
cursor = user_connection.cursor()


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
        print("User Table created")

    def add_user(self, username, first_name, last_name, email, password, street, city, state, zip_code, admin):

        cursor.execute("DELETE FROM users WHERE username = 'John'")
        cursor.execute(
            "INSERT INTO Users VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(username, first_name,
                                                                                                  last_name, email,
                                                                                                  password,
                                                                                                  street, city, state,
                                                                                                  zip_code, admin))
        print("Account Created")
        # Commiting the changes to the database (be careful!)
        user_connection.commit()
        # Closing the connection
        user_connection.close()



##constructor/destructor (delete account)
##delete data
##cursor_obj.execute("DELETE FROM User WHERE user_id = ")


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
