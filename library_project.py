import psycopg2

connection = psycopg2.connect(dbname = "stsdb", user = "postgres", password = "1745", host = "localhost", port = "5432")
cursor = connection.cursor()

def create_tabele(table_name):  #create table into db
    cursor.execute("""CREATE TABLE IF NOT EXISTS Library
                (id SERIAL PRIMARY KEY, 
                title VARCHAR(50) NOT NULL, 
                author VARCHAR(50) NOT NULL,
                published_date DATE);""")

def insert_book(title,author, published_date): #insert data into db
    try:
       insert_book = "INSERT INTO books(title,author,published_date) VALUES(%s, %s, %s)"
       cursor.execute(insert_book, (title, author, published_date))

       connection.commit() #persist query
       print(f"{title} by {author} added")

        

    except Exception as e:
        print(f"Error inserting data: {e}")    
    
    finally:
        cursor.close()
        connection.close()


def add_book(title,author):
    cursor.execute("SELECT title, author FROM books")
    all_books = cursor.fetchall()
    for books in all_books:
        if title in books and author in books:
            connection.commit()
            print("Book already exists")
            return


def remove_book(title,author):
    cursor.execute("SELECT title, author FROM books WHERE title = %s and author = %s", (title,author))
    book = cursor.fetchone
    print(book)

    if book:
        #delte book if
        cursor.execute("DELETE FROM books WHERE title = %s and author = %s", (title,))
        connection.commit()
        print(f"the book {title} removed successfully")

    else:
        print(f"{title} not found")

# def view_book(title, author):
#     cursor.execute("SELECT title, author FROM books WHERE title = %s and author = %s", (title,author))
#     book = cursor.fetchone
#     print(book)

def view_books(size):
    cursor.execute("SELECT * FROM books LIMIT %s", [size])
    all_books = cursor.fetchall()

def view_book(id):
    cursor.execute("SELECT * FROM books WHERE id = %s", (id,))
    book = cursor.fetchone()
    print(book)


def update_book(id, title, author, published_date):
    cursor.execute("UPDATE books SET title = %s, author =%s, published_date = %s WHERE id = %s", (title,author,published_date, id,))
    book = cursor.fetchone()

    connection.commit()
    print(book)




connection.commit()

cursor.close
connection.close    