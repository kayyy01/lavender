# first_name =input("What is your first name? ")
# last_name =input("What is your last name? ")

# print(f"welcome on board, {first_name} {last_name}")


#every input from the user is a string
#when this happens we do casting. Casting refers to changing from one data type to another
# age = int(input("what's your current age? "))
# print(type(age))

# print(age + 2)


#error handling
#never trust input coming from the user
#use try except to catch errors

# try:
#     age = int(input("what is your current age(numbers only)? "))
# except:
#     print("your age should be a number")

#when working on software account for the users mistakes
# handle every error individually

# try:
#     age = int(input("what is your current age(numbers only)? "))
# except ValueError:
#     print("your age should be a number")
# except NameError:
#     print("Something went wrong")  


#you can also handle error in this way. the lazy way!
#any type of error that comes up is an exception. exception is a default for all forms of error
# try:
#     age = int(input("what is your current age(numbers only)? "))
# except ValueError:
#     print("your age should be a number")
# except Exception as e:
#     print("Error: ",e)       


############### LIST ##########################
#data type. iterable. denoted by []
#allows to store multiple items in a variable

names = ["kay", "mina", "john"]

#x'tics
# 1. ordered 2. mutable/changeable 3. allows duplicate items 3. indexed

new_names = list(("jake", "ren"))
print(names[1:3])

#changing
names[2] = "suzuki"
print(names)

names.insert(1, "Rex Omoar")
print(names)

#add items
# names.append("Rex Omoar")
# print(names)

#removing items
# names.pop(1)
# print(names)


# del names[1:3]
# print(names)

#creating a copy of the list

list = names.copy()
names[0] = "Chief Amuzu"

print(names)


#concatenate 2 lists together
