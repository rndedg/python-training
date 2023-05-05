# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sigh to indicate a positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma seperator

price1 = 30000.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:^10}")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3:}")
# prints value with + if positive, adds a comma at thousandths position, and shows 2 decimal places as a float
print(f"Price 1 is ${price1:+,.2f}")