import sqlite3

connection = sqlite3.connect("Movies.db")

cursor = connection.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS Movies 
#                (Title TEXT, Director TEXT, Year INT)''')
cursor.execute('''CREATE TABLE Movies 
               (Title TEXT, Director TEXT, Year INT)''')

connection.commit()
connection.close()