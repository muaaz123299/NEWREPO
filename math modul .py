import math
user=int(input("enter number"))
user1=input("what you want to do with this number sqrt,factorial,,ceil,floor, tan function ")
if user1=="sqrt":
    print("square root of your number is :",math.sqrt(user))
elif user1=="factorial":
    print("factoral of your number is :",math.factorial(user))
elif user1=="ceil":
    print("ceil of your nuumber is:",math.ceil(user))
elif user1=="floor":
    print("floor of your nuumber is:",math.floor(user))
elif user1=="tan":
    print("tan of your number is:",math.tan(user))
else:
    print("invalid operation")