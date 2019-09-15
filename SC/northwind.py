import sqlite3

print('\n', 'Part 2 - The Northwind Database', '\n', '\n')

db = 'northwind_small (1).sqlite3'

try:
    print('PROCESSES:')
     # establish connection for northwind file
    print('attempting to connect to database...')
    nw_conn = sqlite3.connect(db)
    print('connection successful!', '\n', '\n')
except Exception as e:
    print("Error: ")
    print(e)

# run all actions through nw_conn using 'with' statement:
with nw_conn:
    # create cursor to manipulate database
    nw_curs = nw_conn.cursor()

    # 1.) What are the ten most expensive items (per unit price) in the database *and* their suppliers?
    exp_query = """SELECT x.ProductName, x.UnitPrice
                FROM Product AS x
                ORDER BY UnitPrice DESC
                LIMIT 10;"""

     # execute query
    try:
        exp_count = nw_curs.execute(exp_query).fetchall()
        print('Question 1')
        print('10 Highest Unit Price Items:')
        for item in exp_count:
            print(item)
        print('\n', '\n')
    except Exception as e:
        print('error3...')
        print(e)

    
    # 2.) What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
    emp_query = """SELECT AVG(x.HireDate - x.BirthDate)
                FROM Employee AS x;"""

    # execute query
    try:
        emp_count = nw_curs.execute(emp_query).fetchall()
        print('Question 2')
        print('Average Age of Employees When Hired:', round(emp_count[0][0],2), 'years old', '\n', '\n')
    except Exception as e:
        print('error3...')
        print(e)


    # 3.) (*Stretch*) How does the average age of employee at hire vary by city?
    emp_city_query = """SELECT x.City, AVG(x.HireDate - x.BirthDate) 
                FROM Employee AS x
                GROUP BY City;"""

    # execute query
    try:
        emp_city_count = nw_curs.execute(emp_city_query).fetchall()
        print('Question 3')
        print('Average Age of Employees When Hired - By City:')
        for employee in emp_city_count:
            print(employee)
        print('\n', '\n')
    except Exception as e:
        print('error3...')
        print(e)

    print('\n', 'Part 3 - Sailing The Northwind Seas', '\n', '\n')

    # 4.) What are the ten most expensive items (per unit price) in the database *and* their suppliers?
    exp_query = """SELECT x.ProductName, x.UnitPrice, y.CompanyName
                FROM Product AS x
                INNER JOIN Supplier as y
                ON x.SupplierID = y.ID
                ORDER BY UnitPrice DESC
                LIMIT 10;"""

     # execute query
    try:
        exp_count = nw_curs.execute(exp_query).fetchall()
        print('Question 4')
        print('10 Highest Unit Price Items (and their Suppliers):')
        for item in exp_count:
            print(item)
        print('\n', '\n')
    except Exception as e:
        print('error3...')
        print(e)
    


    # 5.) What is the largest category (by number of unique products in it)
    cat_query = """SELECT y.CategoryName, COUNT(DISTINCT x.ProductName) as z
                FROM Product AS x
                INNER JOIN Category as y
                ON x.CategoryID = y.ID
                GROUP BY CategoryName
                ORDER BY z DESC;"""

    # execute query
    try:
        cat_count = nw_curs.execute(cat_query).fetchall()
        print('Question 5')
        print('Largest Category (by Number of Products):', cat_count[0][0])
        print(f'Number of Products in {cat_count[0][0]}:', cat_count[0][1])
        print('\n', '\n')
    except Exception as e:
        print('error3...')
        print(e)

    
    # 6.) (*Stretch*) Who's the employee with the most territories? Use `TerritoryId`
    # (not name, region, or other fields) as the unique identifier for territories.
    terr_query = """SELECT x.FirstName, x.LastName, COUNT(y.TerritoryID) AS z
                FROM Employee AS x
                INNER JOIN EmployeeTerritory as y
                ON x.ID = y.EmployeeID
                GROUP BY x.ID
                ORDER BY z DESC;"""

    try:
        terr_count = nw_curs.execute(terr_query).fetchall()
        print('Question 6')
        print('Employee With The Most Territories:', terr_count[0][0], terr_count[0][1])
        print(f'Number of Territories for {terr_count[0][0]} {terr_count[0][1]}: {terr_count[0][2]}')
        print('\n')
    except Exception as e:
        print('error3...')
        print(e)