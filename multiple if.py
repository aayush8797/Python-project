print("Welcome to the rolar coaster!")
height=float(input("Enter your height in cm:"))
bill=0

if (height>=120):
    print("You can ride on the rolar coaster!")
    age=int(input("Enter your age:"))
    if(age<12):
        bill=5
        print("You have to pay $5")
    elif(age<=18):
        bill=10
        print("You have to pay $10")
    elif(age<=25):
        bill=20
        print("You have to pay $20")
    else:
        bill=30
        print("You have to pay $30")

    wants_photo=input("Do you want a photo taken? Y or N :")
    if (wants_photo=="Y"):
        bill += 3
    
    print(f"Your bill is {bill}")

else :
    print("Sorry , You can't ride.")