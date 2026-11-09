with open ("student.txt","w")as file:
    p=file.write("student name=muaaz \n age=18\n degree=bs english")
with open ("student.txt","r")as file:
    o=file.read()
    print(o)