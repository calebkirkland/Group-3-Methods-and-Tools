import pandas

# Reading users.csv into the pandas dataframe
df = pandas.read_csv('users.csv', index_col = "Username")

# Printing the data in the dataframe
print("\n PRINTING USER DATA FROM DATAFRAME: \n")
print(df)

# Example Query (Printing the user where last name is Jones)
# https://www.geeksforgeeks.org/python-filtering-data-with-pandas-query-method/
# Since "Last Name" has a space, we must put it in backticks.
print("\n EXAMPLE QUERY: \n")
print(df.query('`Last Name` == "Jones"')) 

# Example dropping a row
# https://www.shanelynn.ie/pandas-drop-delete-dataframe-rows-columns/
print("\n AFTER DROPPING A ROW\n")
df.drop("Jsmith2", inplace = True)
print(df)



# Example of (Trying to) add a new row via a dictionary and the append() function
entry = {'Username': ['calebkirkland'],
        'First Name': ['Caleb'],
        'Last Name': ['Kirkland'],
        'Email': ['cok18@msstate.edu'],
        'Password': ['myPassword'],
        'Street': ['myStreet'],
        'City': ['Starkville'],
        'Zip': ['39759']}
entry = pandas.DataFrame(entry)
df = pandas.concat([df, entry], ignore_index = True)
#df.reset_index()
print("\n ADDING A NEW ROW:\n")
print(df)