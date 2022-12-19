# a is the parent class common thungs in parent class
# b is the child class diff things in child class
# c(a,b) multiple inheritance
# we use inheritance to prevent repeatation

class a:
    def __init__(self):
        print("init is a ")
        
        
    def method1(self):
        print("This is method 1")
    def method2(self):
        print("This is method 2")

class b:
    def __init__(self):
       
        print("init is b ")
        # print("init the 2")
    # def __init__(self):
    #     super().__init__()
    #     print("init the 2 ")   
    def method3(self):
        print("this is method 3")            
    def method4(self):
        print("this is method 4")            
class c(b,a):
    def __init__(self):
        super().__init__()
        print("init is c")
    def method5(self):
        print("this is method 3")            
    def method6(self):
        print("this is method 4")            
    
obj =c()

