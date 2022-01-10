# prgram that remove vowels

import re #import regular expression
v = input("Enter ur word")
def removeVowel(v):
    return (re.sub('[aioueAIOUE]','',v))

print(removeVowel(v))      
################################################

# character locator
char = 'a'
myChar= "mohamed"
def findChar(char):
    for i in myChar:
        if(i==char):
            return(i)

print(findChar(char))