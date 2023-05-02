# variable = a container for a value. Behaves as the value it contains

# Working with Strings

first_name = "Gord"
last_name = "Letkeman"
full_name = first_name + " " + last_name
# type() prints what data type it is. ie String, Integer, Boolean
# print(type(name))
print("Hello " + full_name)

#---------------------------------

# Working with Numbers

age = 37
print("Your age is: " + str(age))
age += 1
print("Next year you will be: " + str(age))
# print(type(age))

# Float - can store a decimal point, whereas a regular Int cannot

height = 177.8
print("Your height is: " + str(height) + "cm")
# print(type(height))

# Working with Booleans

human = True
print("Are you a human? " + str(human))
# print(type(human))