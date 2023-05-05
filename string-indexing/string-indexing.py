# indexing = accessing elements of a sequence using []
#            (indexing operator) [start : end : stop]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
# Python assumes starting point is 0 when the parameter is blank
print(credit_number[:4])
print(credit_number[5:9])
# Python assumes end point is the end if the parameter is blank
print(credit_number[5::])
# Get last character in string
print(credit_number[-1])
# Prints every character at defined steps in the string
print(credit_number[::2])

# Get last four digits of a credit card number
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
# Reverse characters in the string
credit_number = credit_number[::-1]
print(credit_number)