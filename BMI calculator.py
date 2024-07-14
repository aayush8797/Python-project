#BMI calculator

#take weight and height from user
weight=float(input("Enter your weight in kg:"))
height=float(input("Enter your height in Metre:"))

#calculate BMI=weight/height^2
BMI=round(weight/(height**2) ,2)

print("your BMI is" ,BMI)