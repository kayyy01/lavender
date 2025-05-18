import psycopg2

connection = psycopg2.connect(dbname= "stsdb", user= "postgres", password ="1745", host= "localhost", port ="5432") #connect to db
cursor = connection.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS students
#                (id SERIAL PRIMARY KEY, 
#                name VARCHAR(50) NOT NULL, 
#                student_int CHAR(8) UNIQUE NOT NULL, 
#                program TEXT NOT NULL);""")


# cursor.execute(""" INSERT INTO students(name, student_int,program)
#                VALUES ('Kay', '20963627', 'CS')             
#  """)

cursor.execute(""" INSERT INTO students(name, student_int,program)
               VALUES(%s,%s, %s)
                           
 """, ('Kay', '20673453', 'Frontend'))





#persist changes to db
connection.commit()

#close connection
cursor.close
connection.close
