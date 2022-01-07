test1='''
Hello "hi" 'bonjour'
'''
print(test1)

# indexing  (Access single character)
myString='Mohamed Khaled'
print(myString[2]) #print h
print(myString[9]) #print k 
print(myString[11]) #print l

#Slicing (Access multiple items from string)
print(myString[1:3]) #oh
print(myString[1:]) #ohamed khaled
print(myString[:5]) #moham
print(myString[1::3]) #om ad
print(myString[1::2]) #oae hld  (skip each 2 chars) 
print(myString[::5]) #Mea

print(len(myString)) #nums of characters


# strip lstrip rstrip
char = '     I love H A Sh     '

# remove All spaces
print(char.strip())
print(len(char.strip()))

# remove right spaces
print(char.rstrip())
print(len(char.rstrip()))

# remove left spaces
print(char.lstrip())
print(len(char.lstrip()))



# strip lstrip rstrip
char = '#####I love H A Sh#####'

# remove char
print(char.strip('#'))
print(len(char.strip('#')))

# remove right spaces
print(char.rstrip('#'))
print(len(char.rstrip('#')))

# remove left spaces
print(char.lstrip('#'))
print(len(char.lstrip('#')))

# upper , lower
print(myString.upper())
print(myString.lower())


# split rsplit  (split strings to lists) =>by default detect spaces in string
a = 'I Love Python'
print(a.split())

b = 'I-Love-Python'
print(b.split('-'))

c = 'I Love Python very good language'
print(c.split(' ',3))
print(c.rsplit(' ',3))

#####################################
# center my char with characters
m = 'Mohamed'
print(m.center(5,'#'))
#####################################
f= 'I love python and python love me'
print(f.count('python'))

print(f.swapcase())

# replace
sub = 'Hello i love D'
print(sub.replace('diala','H S'))

# join (convert list to string)
myArr = ['mohamed','khaled','love','python']
print(' '.join(myArr))


