
class student:
    collegename="LPU"
    collegebranch="btechcse"
    def __init__(self,python,web,math):
        self.subject1= python
        self.subject2= web
        self.subject3= math
    # def avg(python,web,math):
    #     print((python+web+math)/3)
    def avgcal(self):
        return((self.subject1+self.subject2+self.subject3)/3)
    def get_subject1(self):
        return self.subject1
    def set_mark(self,value):
        self.subject1 =value
    @classmethod    
    def collegeDetail(cls):
        return cls.collegename   
    @classmethod    
    def collegebranch(cls):
        return cls.collegebranch  
    @staticmethod    
    def staticMethod():
        print("static")          


        
student1= student(4,7,9)
student2= student(2,3,4)
# print(student1.get_subject1())
# print(student1.set_mark(6))
# print(student.collegeDetail())
print(student.staticMethod())


