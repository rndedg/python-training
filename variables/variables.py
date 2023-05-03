# variable: a reusable container for storing a value
#           behaves as if it were the value it contains

# age = 37
# print("You are " + str(age) + " years old")
# print("You are", age, "years old")
# # more popular way of doing this - fString(like a template literal in JS)
# print(f"You are {age} years old")

# INTEGER - whole numbers
# age = 37
# players = 2
# quantity = 5
#
# print(f"You are {age} years old")
# print(f"There are {players} players online")
# print(f"You would like to buy {quantity} items")


# FLOAT - numbers with a decimal

# gpa = 3.4
# distance = 2.5
# price = 10.99
#
# print(f"Your gpa is {gpa}")
# print(f"You ran {distance}Km")
# print(f"The price is ${price}")

# STRING

# name = "Gord"
# food = "pizza"
# email = "helloWorld@gmail.com"
#
# print(f"Hello, {name}")
# print(f"Your favorite food is {food}")
# print(f"Your email is: {email}")

# BOOLEAN - must be capitalized
#         - typically run internally
#         - not used within quotes

# online = True
# for_sale = False
# running = False

# print(f"Are you online?: {online}")
# print(f"Is the item for sale?: {for_sale}")
# print(f"Is the game running?: {running}")
#
# if running:
#     print("The game is running")
# else:
#     print("The game is over")


# Multiple Assignment - declare multiple variables on the same line
# x = 1
# y = 2
# z = 3
# independant values
# x, y, z = 1, 2, 3
# same value
x = y = z = 0

print(x)
print(y)
print(z)
