import sqlite3

item_connection = sqlite3.connect('database.db')
cursor = item_connection.cursor()

class Item:
    def __init__(self):
            cursor.execute('''CREATE TABLE IF NOT EXISTS Item
               (id TEXT,
                name TEXT,
                price TEXT)''')
            print("Item Table created")

    def add_item(self, id, name, price):
        cursor.execute("INSERT INTO Item VALUES ('{}','{}', '{}')".format(id, name, price))
        
        # do not know how we should do prices.
        
        print("Item Added!")
        # Commiting the changes to the database (be careful!)
        item_connection.commit()
        # Closing the connection
        item_connection.close()
        
    def delete_item(self, id, name, price):
        cursor.execute("DELETE FROM Item VALUES ('{}','{}', '{}')".format(id, name, price))
        
        # do not know how we should do prices.
        
        print("Item Removed!)
        # Commiting the changes to the database (be careful!)
        item_connection.commit()
        # Closing the connection
        item_connection.close()
    def update_item(self, id, name, price):
        cursor.execute("UPDATE THE Item VALUES ('{}','{}', '{}')".format(id, name, price))
        
        # not sure what to add here yet for updating the cart..
        
        print("Item Updated!)
        # Commiting the changes to the database (be careful!)
        item_connection.commit()
        # Closing the connection
        item_connection.close()
