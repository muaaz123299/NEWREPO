class Student:
    def __init__(self,student_name,roll_no,age,marks):
        self.student_name=student_name
        self.roll_no=roll_no
        self.age=age
        self.marks=marks
    def display_info(self):
        print("student name:",self.student_name,"student roll:",self.roll_no,"age:",self.age,"marks:",self.marks)
    def check_grades(self):
        if self.marks>=90:
            print("GRADE A")
        elif self.marks>=80:
            print("grades b")
        elif self.marks>=70:
            print("grade c")
        elif self.marks>=60:
            print("grade d")
        else:
            print("grade fail")

s1=Student("muaaz",201,18,96)
s2=Student("sana",202,19,99)
s3=Student("ali",203,20,90)
s1.display_info()
s2.check_grades()
s3.display_info()
s3.check_grades()