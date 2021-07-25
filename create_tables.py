import sqlite3

connection = sqlite3.connect('mydb.db')
cursor = connection.cursor()
create_table_query = "create table if not exists usertable (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table_query)
create_table_query = "create table if not exists itemstable (id INTEGER PRIMARY KEY, name text, price real)"

cursor.execute(create_table_query)

#insert_q = "insert into itemstable values ('test', 10.99)"
#cursor.execute(insert_q)

connection.commit()
connection.close()
