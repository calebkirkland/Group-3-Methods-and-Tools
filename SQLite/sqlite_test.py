import sqlite3

connection = sqlite3.connect('users.db')

# Creating a Curosr object and calling its execute() method to perfom
# SQL commands
cur = connection.cursor()

# Create table
cur.execute('''CREATE TABLE Users
               (username text,
                first_name text, 
                last_name text, 
                email text, 
                password text,
                street text,
                city text,
                state text,
                zip real)''')


cur.execute("INSERT INTO Users VALUES ('calebkirkland','Caleb','Kirkland','cok18@msstate.edu','myPassword','myStreet','Starkville','MS',39759)")

connection.commit()
connection.close()

# ALL INFO ABOUT SQLITE INTERFACING WITH PYTHON CAN BE FOUND HERE: https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
# DRAG AND DROP THE DB FILES HERE: https://inloop.github.io/sqlite-viewer/ TO VIEW THEM
