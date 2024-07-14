#TIP CALCULATOR
print("Welcome to tip calculator!")
bill=float(input("What was your total bill?"))
tip=int(input("How much tip would you like to give?"))
person=int(input("How many person to split the bill?"))

tip_as_percent=float(tip/100)
total_tip=float(bill*tip_as_percent)
total_bill=float(bill+total_tip)
bill_per_person=round(total_bill/person ,2)
print(f"Each person should pay {bill_per_person}")

print("Thank You")