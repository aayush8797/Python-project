print("Welcome to the rolar coaster!")
height=float(input("Enter your height in cm:"))

if (height>=120):
    print("You can ride on the rolar coaster!")
    age=int(input("Enter your age:"))
    if(age<12):
        print("You have to pay $5")
    elif(age<=18):
        print("You have to pay $10")
    elif(age<=25):
        print("You have to pay $20")
    elif (age >=45 & age <=55):
        print("Everything is going to be okay. Have a free ride.")
    else:
        print("You have to pay $30")
else :
    print("Sorry , You can't ride.")