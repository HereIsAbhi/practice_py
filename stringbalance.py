# s1= input("string1:")
# s2= input("string2:")
# f=0
# for i in s1:
#     if i not in s2:
#         print("True")
#         f+=1
#         break
# if f==0:
#     print("False")  
# upper case at frist
# a= input()
# b=""
# c=""
# for i in a:
#     if i.isupper():
#         b+=i
#     else:
#         c+=i   
# print(b+c) 
# 
# ### upper to lower and viceversa

a= input("enter:")
x=""
for i in a:
    if i.islower():
        x+=i.upper()
    else:
        x+= i.lower()
print(x)                    