name = input("What is your name? ")
age = int(input("How old are you? "))
# user input is always returned as a string
age = age + 1
print(f"Hello {name}")
print(f"Next year you will be {age} years old")

# Mab Libs game exercise
adjective1 = input("Enter an Adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an Adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an Adjective: ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun}.")
print(f"{noun} was {adjective2} and {verb}ing.")
print(f"I was {adjective3}.")

# Area Calculator exercise

length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))
height = float(input("Enter the height of a rectangle: "))

volume = length * width * height

print(f"The volume is: {volume}cm^3")


# Shopping cart program exercise

item = input("What item would you like to buy?: ")
price = float(input("What is the price: "))
quantity = int(input("How many would you like?: "))

total = price * quantity
# round(variable, numberOfDecimalPlaces)
print(f"You have bought {quantity} X {item}/s")
print(f"Your total is: ${round(total, 2)}")
