name = input("Enter your full name: ")
phone_number = input("What is your phone number?: ")


result = len(name)
# find() returns the first occurrence of a given character
# rfind() returns the last occurrence of a given character
result = name.find("o")
result = name.rfind("o")
# capitalizes the first letter of a string
name = name.capitalize()
# capitalizes all the letters in a string
name = name.upper()
# makes all letters in a string lower case
name = name.lower()
# isdigit() returns True or False if string is all digits
result = name.isdigit()
# isalpha() returns True or False if string is all alphabetical characters
result = name.isalpha()
# count() counts how many times a character occurs in a string
result = phone_number.count("-")
phone_number = phone_number.replace("-", " ")

# help(X) returns all the methods of the data type
print(help(str))


print(phone_number)


# Username validation
# 1. username is no more than 12 characters long
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username must be shorter than 12 characters")
elif not username.find(" ") == -1:
    print("Your username cannot contain spaces")
elif not username.isalpha():
    print("Your username must cannot contain numbers")
else:
    print(f"Welcome {username}")