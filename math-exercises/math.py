friends = 10

friends += 1
friends -= 2
friends *= 3
friends /= 2
friends **= 2
remainder = friends % 3

print(friends)
print(remainder)

x = 3.14
y = 4
z = 5

result = round(x)
# abs: absolute value, distance from 0 as a whole number
result = abs(y)
pow(base, exponent)
result = pow(y, 3)
# max: maximum value of various values
# min: minimum value of various values
result = max(x, y, z)
result = min(x, y, z)
print(result)



# import math module to project
import math

x = 9.1

print(math.pi)
print(math.e)
result = math.sqrt(x)
# ceil: always rounds a floating point up
result = math.ceil(x)
# floor: always rounds a floating point down
result = math.floor(x)

print(result)

# Calculate the circumference of a circle
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}cm")

# Calculate the radius of a circle
radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)}cm^2")

# Find the hypotenuse of a triangle
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {c}")