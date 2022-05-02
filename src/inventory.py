import sqlite3

inventory_connection = sqlite3.connect('database.db')
cursor = inventory_connection.cursor()

class Inventory:
    def __init__(self):
            cursor.execute('''CREATE TABLE IF NOT EXISTS Inventory
               (item_id TEXT,
                item_name TEXT, 
                remaining_stock REAL)''')

    def add_item(self, item_id, item_name, remaining_stock):
        cursor.execute("INSERT INTO Inventory VALUES ('{}','{}','{}')".format(item_id, item_name, remaining_stock))
        print("Item Added!")
        # Commiting the changes to the database (be careful!)
        inventory_connection.commit()
        # Closing the connection
        inventory_connection.close()

    def show_inventory(self):
        cursor.execute("SELECT * FROM 'Inventory' ORDER BY item_name")

        table = cursor.fetchall()
        print("Item ID    Item Name     Stock")
        for row in table:
            print(row, "          ", "\n")


    def update_partialItem(self, id, choice, changeto):
        if choice == '1':
            cursor.execute("UPDATE Inventory SET  item_id = '{}' WHERE item_id = '{}'".format(changeto, id))
            cursor.execute("SELECT * FROM Inventory WHERE item_id = '{}'".format(changeto))

            if not cursor.fetchone():  # An empty result evaluates to False.
                check = False
            else:
                check = True

            while check == True:
                changeto = input("Item Id taken\n Enter a new ID: ")

                cursor.execute("SELECT * FROM Inventory WHERE item_id = '{}'".format(changeto))
                if not cursor.fetchone():  # An empty result evaluates to False.
                    check = False
                    break
                else:
                    check = True

                cursor.execute("UPDATE Inventory SET  item_id = '{}' WHERE item_id = '{}'".format(changeto, id))
            print("Item Id Changed ")
            # Commiting the changes to the database (be careful!)
            inventory_connection.commit()
            # Closing the connection
            inventory_connection.close()
        elif choice == '2':
            cursor.execute("UPDATE Inventory SET item_name = '{}' WHERE item_id = '{}'".format(changeto, id))

            print("Item name Changed")
            # Commiting the changes to the database (be careful!)
            inventory_connection.commit()
            # Closing the connection
            inventory_connection.close()

        elif choice == '3':
            cursor.execute("UPDATE Inventory SET  remaining_stock = '{}' WHERE item_id = '{}'".format(changeto, id))

            print("Item Stock has been changed")
            # Commiting the changes to the database (be careful!)
            inventory_connection.commit()
            # Closing the connection
            inventory_connection.close()

    def delete_item(self, id):
        cursor.execute("DELETE  FROM Inventory WHERE item_id = '{}'".format(id))

        print("Item has been deleted")
        # Commiting the changes to the database (be careful!)
        inventory_connection.commit()
        # Closing the connection
        inventory_connection.close()

