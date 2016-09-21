# python 2
# m.k.

import sqlite3

# >>> import sqlite3
# >>> sqlite3.sqlite_version
# '3.13.0'

# (id), name, mgr_id
employees = [
    ('Jonathan Archer', 11),
    ('Christopher Pike' , 12),
    ('James Kirk' , 13),
    ('Jean-Luc Picard', 14),
    ('Kathryn Janeway', 15),
    ('Ralph Wiggum', 11),
    ('Troy McClure' , 12),
    ('Waylon Smithers' , 17),
    ('Edna Krabappel' , 16),
    ('Ned Flanders', 15),
    ('Buffy Summers', None),
    ('Xander Harris', None),
    ('Willow Rosenberg', None),
    ('Rupert Giles', None),
    ('Oz Selbie', None),
    ('Dade Murphy', 11),
    ('Kate Libby', 13),
    ('Paul Cook', 17),
    ('Emmanuel Goldstein', 16),
    ('Winston Smith', 15),
    ('Thomas Anderson', 15),
    ('Agent Smith', 14),
    ('Malcolm Reynolds', 14),
    ('River Tam', 18),
    ('Jason Nesmith', 18),
]

# name, head
departments = [
    ('Operations', 11),
    ('Marketing', 12),
    ('IT', 13),
    ('HR', 14),
    ('Sales', 15),
]

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute('''
    create table employee (
        id INTEGER PRIMARY KEY,
        name TEXT,
        mgr_id INTEGER
    )
''')

c.execute('''
    create table department (
        name TEXT,
        head INTEGER
    )
''')

c.executemany('insert into employee values (NULL, ?, ?)', employees)
c.executemany('insert into department values (?,?)', departments)

# 5.  Write an SQL query to list the full name of every employee,
#     alphabetized by first name.

print('[#5] full names ordered by first name')

query = 'select name from employee order by name'

for row in c.execute(query):
    print '    ', row[0]

# 6.  Write an SQL query to list the full name of every employee,
#     alphabetized by last name.

print('[#6] full names ordered by last name')

query = '''
    select
        substr(name, 1, instr(name, ' ') - 1) as first_name,
        substr(name, instr(name, ' ') + 1) as last_name
    from employee
    order by last_name
'''

for row in c.execute(query):
    print '    ', row[1] + ',', row[0]

# 7.  Write an SQL query to list the full name of every employee along
#     with the full name of his/her manager.

print('[#7] full name and full name of manager')

query = '''
    select
        employee.name,
        manager.name
    from employee
    left join employee as manager
        on employee.mgr_id == manager.id
'''

for row in c.execute(query):
    print '    ', row[0], '->', row[1]
     
# 8.  Write an SQL query to list the full name of every employee in the
#     Sales department.

print('[#8] full name of everyone in sales')

query = '''
    select
        employee.name
    from employee
    inner join department
        on employee.mgr_id == department.head
    where
        department.name == 'Sales'
'''

for row in c.execute(query):
    print '    ', row[0]

# 9.  Write an SQL query to list the full name of every employee along
#     with name of his/her department.

print('[#9] full name and department name')

query = '''
    select
        employee.name,
        department.name
    from employee
    left join department
        on employee.mgr_id == department.head
'''

for row in c.execute(query):
    print '    ', row[0] + ',', row[1]


# 13. Write a function in the language of your choice performs the query
#    you wrote for question 7, and outputs the results as an HTML table.

#    - Write a function to output the query results from question 7
#      as an html table     

print('[#13] output result of question 7 as an html table')

def question13(connection):
    c = connection.cursor()

    query = '''
        select
            employee.name,
            manager.name
        from employee
        left join employee as manager
            on employee.mgr_id == manager.id
    '''

    print '<table>'
    print '  <tr><th>employee name</th><th>manager name</th></tr>'
    for row in c.execute(query):
        print '  <tr>'
        print '    <td>{0}</td>'.format(row[0])
        print '    <td>{0}</td>'.format(row[1])
        print '  </tr>'
    print '</table>'
    
question13(conn)