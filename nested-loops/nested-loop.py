# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")


# print() typically ends in a new line, adding end="" negates that, or sets it to what you put in the string
for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    # create new line after each outer loop iteration
    print()