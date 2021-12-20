<<<<<<< HEAD
# Class for DB operation
    https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.htmls
    
## Cursor
    '''
    import mysql.connector
    cnx = mysql.connector.connect(database='dbname)
    cursor = cnx.cursor()
    '''

## Execute
    '''
    cursor.execute(operation, params=None, multi=False)
    iterator = cursor.execute(operation, params=None, multi=True)

    insert_stmt = (
      "INSERT INTO employees (emp_no, first_name, last_name, hire_date) "
      "VALUES (%s, %s, %s, %s)"
    )
    data = (2, 'Jane', 'Doe', datetime.date(2012, 3, 23))
    cursor.execute(insert_stmt, data)
    
    select_stmt = "SELECT * FROM employees WHERE emp_no = %(emp_no)s"
    cursor.execute(select_stmt, { 'emp_no': 2 })
    '''

## Fetchall
    '''
    rows = cursor.fetchall()

    cursor.execute("SELECT * FROM employees ORDER BY emp_no")
    head_rows = cursor.fetchmany(size=2)
    remaining_rows = cursor.fetchall()
           
    '''    
=======
# Class for DB operations
>>>>>>> origin/master
