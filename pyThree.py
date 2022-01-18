# get inputs from users
# fname = input("Enter Your first Name")
# lname = input("Enter your last name")
# assign frist name with last name
# lname+=fname
# print("Hello "+lname)
##########Python List############
# create list
myList = ["mohamed","Khaled","Omaima","Abdelaziz","baskota","gemy","mahmoud","Adel","Salah"]
print(myList)
# calling items with index
print(myList[0])
print(myList[1])
print(myList[5])
# remove and return the element
print(myList.pop(5))
print(myList)
# add item at the end of list
myList.append("Habiba")
print(myList)
# insert in sepecific position
myList.insert(4,"Diala")
print(myList)
# remove item without return
myList.remove("Diala")
print(myList)
# remove the last item
myList.pop()
print(myList)

newList=["nader","shrouk"]
# extend list to my list
myList.extend(newList)
print(myList)

##########Tuples###############3
myTuple = (1,"mohamed","khaled",2,4,5)
print(myTuple[0])
# myTuple[6]="Habiba"  error 
print(myTuple)

############Dictionary##################
myDictionary= {1:"mohamed",2:"abdelaziz",3:"khaled","city":"mansoura"}
print(myDictionary)
print(myDictionary[1])
print(myDictionary[2])
print(myDictionary["city"])
print(myDictionary.keys())
print(myDictionary.items())
newDict= {"faculty":"FCIS","Department":"Information System"}
print(myDictionary.update(newDict))
print(myDictionary)

#############Functions#####################
def temp():
    return 'temp'

print(temp())

def myAge(a):
    return 'my age is '+a

print(myAge('mohamed khaled'))

def sum(*args):
    sum = 0
    for i in args:
        sum+=1
    print(sum)

sum(1,2,4,5)  # it print 4
    
