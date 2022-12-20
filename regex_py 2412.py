import re

value= "This is a string"
output=re.search("^This.*string$",value)
print(output)
if output:
    print("it's matched")
else:
    print("not matched")    


# pattern=r"^(?=.[a-z])(?=.[A-Z])(?=.[!@#$%^&()_+=-])(?=.{8,})"
# print(pattern)

# start with=^ zero or one occurence=?   any character.    zero or more occurence*    return match for any lower case[a-z]   
# [] set of characters
# {} no of occurences 
 
# datahiding
# filehandling
# exceptionhandle