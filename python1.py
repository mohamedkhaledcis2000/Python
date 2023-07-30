print("Hello world")
print(100)
name = "Mohamed"
print("Hello "+name)
print(name[3])
# x=0
# for(x=0;x<name.length;x++):
#     print(name[x])

# data types
# 1- string
x = "Ahmed"
# type of variable
print(type(x))
# 2-numbers [integer , float]
# num = 10 + "10"
# error can't add int to string
# print(num)
y = 10.5
print(type(y))
a = True
b = False 
print(type(a))
# \ or \n new line
q = "mohamed khaled abdelaziz 'abdelaziz' \
mohamed"
print(q)

print(name.upper())
print(name.isupper())
print(name.islower())

print(name.lower())
# capitalize first letter in string
print(name.capitalize())

# title => make first letter in any string capital
nm = "mohamed khaled"
print(nm.title())
# split the string into list and put anything i will give it in split function between them

print(nm.split( ))

print(nm.split('k'))


fname = 'Mohamed , khaled , abdelaziz'
print(fname.rsplit(','))
# length of string 
print(len(fname))
print(fname.index('k'))
# replace letters and strings
print(fname.replace("khaled","my father"))
# do math operation and convert it to string  ==>str()
print(str(5*5)+" Year")
# convert to any type of data
print(float(23))
print(type(str(20)))
# 1:02:52
# start from input

age = input('enter your age: ')
print('i am '+age+' years old')
# python list
myList = ["Mohamed","abdelaziz","khaled",2000,23,"teacher assistant",["React js","Django"]]
print(myList)
print(myList[3])
print(myList[6][1])
# append item to list
# add new item in the end of list
myList.append(3)
print(myList)
# insert item to my list in any index i want
# it take 2 parameters [index,value]
myList.insert(2,"Malak")
list1 = [1,2,3]
print(len(myList))
list2=["a","b","c"]
# append list to another list
list1.extend(list2)
print(list1)
# remove item
myList.remove(23)
print(myList)
# tuples => cannot update 
tuples = ("Mohamed","Khaled","Abdelaziz")
print(type(tuples))

# dictionary
dict = {
    "first":"Mohamed",
    "second":"Khaled",
    "twin":"Abdelaziz",
    "age":23
}
for a in dict:
    print(a)
    
print(dict)
print(dict["twin"])
# function
# built in functions
print(pow(3,3))
# user functions
def add(x,y):
    return x+y
print(add(4,6))

name = "Mohamed Khaled Abdelaziz"
for i in name:
    print(i)

for i in range(5):
    print("Hello")