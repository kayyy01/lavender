#classes are blueprints for creating objects
#objects are intances of class. they are created from a class

#blueprints: basically a structure of the actual thing

# class Person: #use Pascal casing when naming class
#     name = "" 
#     age = "" 
#     gender = ""

#     def speak(self): #anytime you're naming paramters in methods, start with self and others can continue
#         print(f'My name is {self.name}')

#     def getAge(self, number):
#         print(self.age + number)    
    

# Person1 = Person()
# Person1.name = "Kay"
# Person1.age = 50
# Person1.gender = 'Male'

# Person2 = Person()
# Person3 = Person() 


# class Animal:
#     name = ""
#     legs = ""
#     tail = False

# ant = Animal
# ant.name = "Ant"
# ant.legs = 4
# ant.tail = True

# print(vars(ant))

# frog = Animal
# frog.name = "Frog"
# frog.legs = 4
# frog.tail = False

# print(dir(frog))

# print(Person1.getAge(20))


#init method/ constructor

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


Person6 = Person("Sam", 24, "Male")
Person5 = Person("Mina", 54, "Female")

print(Person5.gender)


class Student:
    def __init__(self, name = " ", age = 0, programme = None, level = 100):
        self.name = name
        self.age = age
        self.programme = programme
        self.level = level

class Programme:
    name = ""
    department = ""

Programme1 = Programme() 

Student1 = Student("John", 14, "Industrial Eng")
print(vars(Student1))
Student1.programme = Programme1
