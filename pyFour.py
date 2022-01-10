# prgram that remove vowels

import re #import regular expression
v = input("Enter ur word")
def removeVowel(v):
    return (re.sub('[aioueAIOUE]','',v))

print(removeVowel(v))        
    