#simple function
def greet():
    print("Good Morning")
    print("hello ASR!")
    print("Welcome to My Place.")
greet() 

#functons that allows for input
def greet_with_name(name): # Here name is the parameter
    print(f"hello {name}")
    print(f"How are you {name}?")
greet_with_name("Aayush") # Here "Aayush" is the argument

#function with more than 1 input
def greet_with(name,locations):
    print(f"my name is {name}")
    print(f"i am live in {locations}")
greet_with("aayush","bihar") #positional argument

#Functions with keyword argument
def new_greet(name="ASR",location="Bihar"):
    print(f"my name is {name}")
    print(f"i am live in {location}")
new_greet("Aayush")

