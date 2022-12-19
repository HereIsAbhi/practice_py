# poly-many, morph- forms i.e function that we can use in many form eg: length

# print(len("hello"))
# print(len([10,20,30]))

# def add(x,y,z=0):
#     return x+y+z

# print(add(3,4))
# print(add(3,4,5))

# class India:
#     def capital(self):
#         print("New Delhi")
#     def language(self):
#         print("Hindi")
#     def type(self):
#         print("Developing")
# class USA:
#     def capital(self):
#         print("Washington DC")
#     def language(self):
#         print("Eng")
#     def type(self):
#         print("Developed")

# obj1= India()
# obj2= USA()
# for i in (obj1,obj2):
#     i.capital()
#     i.language()
#     i.type()

class Bird:
    def wings(self):
        print("Bird has two wings")
    def eyes(self):
        print("Bird has two eyes")
    def fly(self):
        print("Most of birds can fly")         

class sparrow:
    def fly(self):
        print("are beautiful")
class Ostrich(Bird):
    def fly(self):
        print("ostrich can not fly")        

bird= Bird()
sparrow=sparrow()
ostrich=Ostrich()

bird.eyes()
sparrow.fly()
ostrich.fly()

