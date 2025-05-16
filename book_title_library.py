#display to user
print("Welcome to the book title library")

 #initialize list
book = []

while True:
    print('''
        1. Add a book
        2. Remove book
        3. View book
        4. Exit
    ''')
    #take info from user
    user_input = input("Choose an option: ")

   

    if user_input == "1":
        add_book = input("Add book(s) and separate with commas ")
        add_book_list = add_book.split(",")
        book = add_book_list
        print(book)

    if user_input == "2":
        #error handling user input
        try:
            remove_book = input("what book do you want to remove? ")
            book.remove(remove_book)
            print(f"This is your current book {book}")
        except Exception as e:
            print("Error", e)  

    if user_input == "3":
        #loop through list and print individually
        for i in book:
            print(i)    

    if user_input == "4":
        print("We hope to see you next time. BYE!:)")
        break 
    
