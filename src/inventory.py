import sqlite3

inventory_connection = sqlite3.connect('database.db')
cursor = inventory_connection.cursor()

class Inventory:
    def __init__(self):
            cursor.execute('''CREATE TABLE IF NOT EXISTS Inventory
               (item_id TEXT,
                item_name TEXT, 
                remaining_stock REAL)''')
            print("Inventory Table created")

    def add_item(self, item_id, item_name, remaining_stock):
        cursor.execute("INSERT INTO Inventory VALUES ('{}','{}','{}')".format(item_id, item_name, remaining_stock))
        print("Item Added!")
        # Commiting the changes to the database (be careful!)
        inventory_connection.commit()
        # Closing the connection
        inventory_connection.close()
