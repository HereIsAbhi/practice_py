# create a class without any variable and methods
class car :
    pass
car1=car

# create a child class Bus with parent class vehicle 
# pass is used if no method or variable are given

class Vehicle:
    def __init__(self,name,mileage):
        self.name=name
        self.mileage=mileage
class Bus(Vehicle):
    pass

obj= Bus("ABC",10)
print(obj.mileage,obj.name)

