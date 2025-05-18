import psycopg2

#establish connection with postgres
try:
    connection = psycopg2.connect(
        dbname = 'stsdb',
        host = 'localhost',
        user = 'postgres',
        password = '1745',
        port = '5432',
    )

    print("Connected")

except:
    print("Unable to connect")

cursor = connection.cursor()
connection.autocommit = True #automatically persist changes

#create table
cursor.execute(""" CREATE TABLE IF NOT EXISTS employees(
               id SERIAL PRIMARY KEY,
               name VARCHAR(50) NOT NULL,
               age INT NOT NULL,
               department VARCHAR(50) NOT NULL );

""")

def add_employee(name,age, department): #add employee to database
    try:
        add_employee = "INSERT INTO employees(name,age,department) VALUES(%s,%s,%s)"
        cursor.execute(add_employee, (name,age,department))

    except Exception as e:
        print(f"Error inseritng data", {e})
        return
       
def view_employee(name): #view an employee from databse
    cursor.execute("SELECT name, age, department FROM employees WHERE name= %s", (name,))
    view_employee = cursor.fetchall()
    if view_employee:
        for employee in view_employee:
            print(f"Name: {employee[0]}, Age: {employee[1]}, Department: {employee[2]}")
    else:
        print("No such employee found")        
    

def update_employee(id,name,age,department):  #update an employee
   cursor.execute("UPDATE employees SET name= %s, age= %s, department= %s WHERE id= %s", (name,age,department,id))
   print("Employee Info Updated Successfully")
   
   connection.commit()
   
   

def delete_employee(id): #delete an employee
    cursor.execute("SELECT id, name, department FROM employees WHERE id= %s", (id,))
    delete_employee = cursor.fetchone()

    if delete_employee:
        cursor.execute("DELETE FROM employees WHERE id = %s", (id,))
        connection.commit()
        print(f"Employee {delete_employee[1]} with Employee ID {id} deleted successfully")


    else:
        print("NOT FOUND!")

def all_employees(): #view all employees
    cursor.execute("SELECT * FROM employees")
    all_employees_query = cursor.fetchall()
    for employees in all_employees_query:
        print(employees)




print("WWELCOME TO THE EMPLOYEE MANAGEMENT SYSTEM")

while True:
    print("""
        1. Add Employee
        2. View Employee
        3. View all Employees  
        4. Update Employee
        5. Delete Employee
        6. Exit
    """)

    user_input = input("Choose an option(1-5)")


    if user_input == "1":
        name = input("Enter Employee name ")
        age = input("Enter Employee age ")
        department = input("Enter Employee department ")
        add_employee(name, age, department)

    if user_input == "2":
        name = input("What is the employees name? ")
        view_employee(name)

    if user_input == "3":
        all_employees()   

    if user_input == "4":
        id = input("Enter Employee ID ")
        name = input("Enter new Employee name ")
        age = input("Enter new employee age")
        department = input("Enter new employee department ")
        update_employee(id,name,age,department)

    if user_input == "5":
        id = input("Enter Employee id")
        delete_employee(id)

    if user_input == "6":
        print("see you around")
        break                

#close connection
cursor.close()
connection.close()





