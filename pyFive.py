# encapsulation
from mimetypes import init


class Student:
    no_stdudents = 0
    # constructor
    def __init__(self,name,age,courses):
        self.name=name
        self.age=age
        self.courses=courses
        Student.no_stdudents +=1
        # self is refered to any new object
        


student1 = Student('mohamed',21,'computer Sciences')
student2 = Student('alanod',18,'medicine')

print(id(student1),id(student2))
print(student1.name,student2.name)
print(student1.age,student2.age)
print(student1.courses,student2.courses)