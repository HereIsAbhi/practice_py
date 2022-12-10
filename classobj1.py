# instance variable - shared bw diff object
# static variable- we cant change static variable with objects we need to access class


class car:
    wheel=4
    def __init__(self,company,milage) :
        self.company=company
        self.mileage=milage
car1= car("BMW",10)
car2= car("TATA",20)
# car1.wheel=5
# car2.wheel=5

print(car1.company,car1.mileage,car1.wheel)        
print(car2.company,car2.mileage,car2.wheel)     
# print(car.wheel)   