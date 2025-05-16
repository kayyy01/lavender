#Design a Student Tracker
#should add, remove, display, update

students = []
#take list from user and add to initalized list
students_list = input("enter student list and separate with space: ")
students = students_list.split(" ")
print(students)

#remove item from list
remove_student = input("which student do you want to remove: ")
students.remove(remove_student)
print(students)

#update list
update_student_input = input("add new students to list and separate with space: ").split()
students.extend(update_student_input)

print(students)