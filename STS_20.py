class Student:
    school = "slightly techie"
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade


    def introduceStudent(self):
        return f'My name is {self.name} and I am {self.age} years old. I attend {self.school}'

    def giveGrade(self):
        print(f'{self.name} has grade {self.grade}')

    def newGrade(self, newGrade):
        self.grade = newGrade
        return newGrade    
    
    #classMethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def school_rules():
        return "School must start by 7:00"




s1 = Student("Kay", 24, 70)
# Student1.name = "Jayy"
# Student1.age = 24
# Student1.school = "Stanford"
# Student1.grade = 70

print(s1.getSchool())
s1.introduceStudent()

# s1.newGrade(20)
# use_grade = s1.introduceStudent()
# print(use_grade)

# intro = Student1.introduceStudent()
# print(intro)