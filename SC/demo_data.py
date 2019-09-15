# Question 1

import sqlite3

print('\n', 'Question 1 - Part 1 - Making/Querying a Database', '\n', '\n')

db = 'demo_data.sqlite3'

try:
     # establish connection for demo file
    print('PROCESSES:')
    print('attempting to connect to database...')

    demo_conn = sqlite3.connect(db)
    print('connection successful!')
except Exception as e:
     print("Error: ")
     print(e)

# run all actions through demo_conn using 'with' statement:
with demo_conn:
     # create cursor to manipulate database
     demo_curs = demo_conn.cursor()

     # 1.) establish 'delete table' query that deletes table; stops
     # error message from generating
     # only execute if demo table already exists
     delete_demo_table = """DROP TABLE IF EXISTS demo;"""

     # 2.) establish 'table_create' & 'insert_to_table' queries
     create_demo_table = """CREATE TABLE demo(
          s VARCHAR PRIMARY KEY,
          x INT,
          y INT
          );"""

     insert_to_table = """INSERT INTO demo(s, x, y) VALUES(?, ?, ?);"""

     # 3.) create data to go into table
     data = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]

     # 4.) create 'try' statement to run all queries and commit to database
     try:
          demo_conn.execute(delete_demo_table)
          print('previous table deleted successfully!')
          demo_conn.execute(create_demo_table)
          print('new table created successfully!')
          demo_conn.executemany(insert_to_table, data)
          print('data inserted into table successfully!')
          
          # save changes
          demo_conn.commit()
          print('changes committed successfully!', '\n')
     except Exception as e:
          print('error1...')
          print(e)
     
     # 5.) create query to make sure table created correctly
     table_query = """SELECT * FROM demo;"""

     # 6.) print results of query using try/except to test table creation success
     try:
          rows = demo_conn.execute(table_query)
          print('Question 1')
          print("'demo' table:")
          for row in rows:
               print(row)
          print('\n', '\n')
     except Exception as e:
          print('error2...')
          print(e)

     # Question 1, Part 2
     print('Question 1 - Part 2:', '\n', '\n')
     print('Question 2')
     print('Count how many rows you have - it should be 3!')

     # create query to count number of rows in 'demo' table
     row_query = """SELECT COUNT(*) FROM demo;"""

     # execute query
     try:
          row_count = demo_conn.execute(row_query).fetchall()
          print('number of rows:', row_count[0][0], '\n')
     except Exception as e:
          print('error3...')
          print(e)
     
     print('\n')
     print('Question 3')
     print('How many rows are there where both `x` and `y` are at least 5?')

     # create query to count number of rows where x and y are at least 5
     five_query = """SELECT COUNT(*)
                     FROM demo
                     WHERE x >= 5 AND y >= 5;"""
     try:
          five_count = demo_conn.execute(five_query).fetchall()
          print('number of rows where `x` and `y` are at least 5:', five_count[0][0], '\n')
     except Exception as e:
          print('error4...')
          print(e)

     print('\n')
     print('Question 4')
     print('How many unique values of `y` are there (hint - `COUNT()` can accept a keyword `DISTINCT`)?')

     # create query to count unique number of `y` values
     y_query = """SELECT DISTINCT COUNT(y)
                  FROM demo;"""
     try:
          y_count = demo_conn.execute(five_query).fetchall()
          print('number of unique `y` values:', y_count[0][0], '\n')
     except Exception as e:
          print('error5...')
          print(e)