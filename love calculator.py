print("The Love Calculator is calculating your score...")
name1 = input("Please Enter Your Name:")
name2 = input("Please Enter Your Name:") 
combine_name = name1+name2
lower_case=combine_name.lower()

T=lower_case.count("t")
R=lower_case.count("r")
U=lower_case.count("u")
E=lower_case.count("e")
first_digit=T+R+U+E

L=lower_case.count("l")
O=lower_case.count("o")
V=lower_case.count("v")
E=lower_case.count("e")
last_digit=L+O+V+E

score=int(str(first_digit)+str(last_digit))

if(score<=10) or (score>=90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif(score>=40) and (score<=50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

print('Thank You for using "LOVE CALCULATOR"')

