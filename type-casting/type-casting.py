# typecasting = The process of converting a value of one data type to another
#               (string, integer, float, boolean)
#               Explicit vs Implicit
#               user input is always returned as a string


name = "Gord"
age = 37
gpa = 3.4
student = True

# Explicit
# age = float(age)
# print(type(age))
# gpa = int(gpa)
# print(gpa)
# student = str(student)
# print(type(student))
# age = bool(age)
# print(age)

# Implicit - when a variables data type is automatically converted

x = 2
y = 2.0
x = x / y

print(x)