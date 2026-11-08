import random
while True:
    particepents=["muaaz","sana","ali","ahmad","mumtaz","berlin","jack","jill","kamal","kashif","john","jerry"]
    prize=["laptop","moblie","bike","car","house","tv","fridge"]
    user=input("how many you want 1,,2,,3")
    if user=="1":
        print("partiepent name:",random.choice(particepents))
        print("he / she won:",random.choice(prize))
    elif user=="2":
        print(random.choice(particepents))
        print("he / she won:",random.choice(prize))
        print(random.choice(particepents))
        print("he / she won:",random.choice(prize))
    elif user=="3":
        print(random.choice(particepents))
        print("he / she won:",random.choice(prize))
        print(random.choice(particepents))
        print("he / she won:",random.choice(prize))
        print(random.choice(particepents))
        print("he / she won:",random.choice(prize))
    else:
        print("you cannot select more than two participents")