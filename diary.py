name=input("ënter your name")
age=int(input("ënter your age"))
ask=input("descrbe your daily rotien")
with open("diaryy.txt","w")as file:
    file.write("name:{name}\n")
    file.write("age:{age}\n")
    file.write("daily rotien {ask}")


with open("diaryy.txt","r")as file:
    d=file.read()

print("this is your diary")
print(d)