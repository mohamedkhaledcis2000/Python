# encapsulation
from ast import For
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

############inheritance#################

# parent class
class Person(object):

    # constructor
    def __init__(self,name):
        self.name = name

    # to get name
    def getName(self):
        return self.name

    def isEmployee(self):
        return False


# child class
class Employee(Person):

    def isEmployee(self):
        return True 

emp = Person("Mohamed")
print(emp.getName(),emp.isEmployee())

emp = Employee("Abdelaziz")
print(emp.getName(),emp.isEmployee())

########polymorphism#############
# it means haveing many forms for the same function

class Egypt():

    def Capital(self):
        print('Cairo Is The Capital Of Egypt')

    def Language(self):
        print("Arabic is the language of egypt")

    def Type(self):
        print("Egypt is developed country")


class Terkiya():
    
    def Capital(self):
        print('Ankara Is The Capital Of Terkiya')

    def Language(self):
        print("Terkish is the language of Terkishya")

    def Type(self):
        print("Terkiya is developed countryya")



obj_Egy = Egypt()
obj_Ter=Terkiya()

for country in(obj_Egy,obj_Ter):
    country.Capital()
    country.Language()
    country.Type()

############################
class Car:
    def __init__(self,color,price,model):
        self.color=color
        self.price=price
        self.model=model

    def myCar(self):
        if(self.model>2018):
            self.price +=100000
            print(f"My model {self.model} My Price {self.price}")
        else:
            self.price -=100000
            print(f"My model {self.model} My Price {self.price}")

        
BMW = Car('Black',1000000,2020)
Ford = Car('Red' ,2000000,2017)
print(BMW.color)
print(BMW.price)
print(BMW.model)

BMW.myCar()
Ford.myCar()
        

