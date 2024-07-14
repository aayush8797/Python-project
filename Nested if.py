#NESTED IF STATEMENTS
print("Welcome to the rolar coaster!")
height=float(input("Enter your height in cm:"))

if (height>=120):
    print("You can ride on the rolar coaster!")
    age=int(input("Enter your age:"))
    if (age>=18):
        print("You have to pay $18")
    else :
        print("You have to pay $7")
else :
    print("Sorry , You can't ride.")