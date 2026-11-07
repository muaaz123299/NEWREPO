class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,roll_no,marks,name,age):
        self.roll_no=roll_no
        self.marks=marks
        super().__init__(name,age)
        print("student name:",self.name,"student roll no:",self.roll_no,"student marks:",self.marks,"stuent age:",self.age)
class Teacher(Person):
    def __init__(self,subject,salary,name,age): 
        super().__init__(name,age)
        self.subject=subject
        self.salary=salary
    def display_teacher_info(self):        
        print("teacher name:",self.name,"teacher age: ",self.age,"teacher subject :",self.subject,"teacher salary:",self.salary)
t1=Teacher("maths",50000,"ali",30)
t2=Teacher("english",60000,"sana",35)
t2.display_teacher_info()

    