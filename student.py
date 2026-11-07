class Student:
    def __init__(self,student_name,roll_no,age,marks):
        self.student_name=student_name
        self.roll_no=roll_no
        self.age=age
        self.__marks=marks
    def display_info(self):
        print("student name:",self.student_name,"student roll:",self.roll_no,"age:",self.age,"marks:",self.__marks)
    def check_grades(self):
        if self.__marks>=90:
            print("GRADE A")
        elif self.__marks>=80:
            print("grades b")
        elif self.__marks>=70:
            print("grade c")
        elif self.__marks>=60:
            print("grade d")
        else:
            print("grade fail")
    def get_marks(self):
        print("student marks:",self.__marks)
        return self.__marks
    def set_marks(self):
        if self.__marks<=0 or self.__marks>100:
            print("invalid marks entered")
    def update_marks(self,new_marks):
        self.__marks=new_marks
        print("student marks has offically updated")
    def update_student_name(self,new_name):
        self.student_name=new_name
        print("student name has sucessfully updated")
s1=Student("muaaz",201,18,96)
s2=Student("sana",202,19,99)
s3=Student("ali",203,20,90)
s1.display_info()
s2.check_grades()
s3.display_info()
s3.check_grades()
s1.get_marks()
s1.set_marks()
s1.display_info()
s1.update_marks(100)
s1.display_info()