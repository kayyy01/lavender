print("Welcome to the Student Managemnt System")

#initialize student dictionary
students = {}

while True:
    print("Choose an option")
    print('''
          1. Add Student(name, age, grade, and list of course)
          2. Remove student
          3. View one student
          4. Exit
          ''')
    #taking input from user
    user_input = input("Enter your choice: ")

    if user_input == "1":
        name = input("Enter student name ").capitalize()
        age = input("Enter student age ")
        grade = input("Enter student grade ")
        course = input("Enter list of student's courses and separate with comma ")
        
        students[name] = {"age": age, "grade": grade, "courses": course}
        print(f"{name} has been added!")       

    if user_input == "2":
        #handling user error
        while True:
            try:
                print(students)  
                remove_student = input("which student do you want to remove? ").capitalize()
                print(f"you entered {remove_student}")
                removed_student = students.pop(remove_student)
                print(students)
                
                print(f'{remove_student} has been removed.')

            except KeyError:
                print(f'{(remove_student)} does not exist')    

            except Exception as e:
                print("Error", e)

            else:
                break    
        
    

    if user_input == "3":
        view_student = input("which student do you want to view ")
        view_student_input = students.get(view_student)
        print(view_student_input)
        

    if user_input == "4":
        print("BYE!:)")
        break

    

    




    
