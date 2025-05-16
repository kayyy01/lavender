# Library management System

#  Design and  implement a Python program to manage a library's collection of books/

# The program should be able to allow user to add a book, remove books, search for a book by title and author

# and display all the books in the library.


# LIBRARY MANAGEMENT SYSTEM

# 1. Add a Book

# 2. Remove a Book

# 3. Search for a Book

# 4. Display All books

# 5. Exit program


# BRAINSTORM


# 1. Welcome page

# 2. Functions to add, remove, search and display books

# 3. storage type Dictionary {}


# Program Flow

# Technical Design

    # Initialize the library

    # Functions to add, remove, search and display books

    # Main program to run the library

# User Interface Design

    # Welcome page

    # Menu options

    # User input

    # Error handling




class Library:
    def __init__(self):
        self.books = {}

    def add_book(self,title,details):
        title = {}
        title = input("What is the title of the book ").title()
        author = input("What is the author ")
        year = input("Publication year of the book. ")
        details = {"author": author, "year": year}
        self.books[title] = details
        print(f"{title} has been added: {details}")

    def remove_book(self):
        remove_books = input("what book do you want to remove? ").title()
        book_removed = self.books.pop(remove_books)
        print(f"{book_removed} has been removed")

    def search_book(self):
        user_search = input("What book are you looking for? ")
        found_book = self.books.get(user_search)
        print(found_book)

    def display_book(self):
        for book in self.books:
            print(book)      
 
# books = {}

print("Welcome to the Library Management System")
while True:
    print(
        '''
    1. Add a book
    2. Search for a book
    3. Remove a book
    4. Display all books
    5. Exit 
        '''
    )
    user_input = input("Enter choice: ")

    if user_input == "1":
        library = Library()
        library.add_book(title= "",details= "")

    if user_input == "2":
        library = Library()
        library.search_book()

    if user_input == "3":
        library = Library()
        library.remove_book()

    if user_input == "4":
        library = Library()
        library.display_book()

    if user_input == "5":
        print("See you later")
        break


   

   






