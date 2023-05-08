# for-loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# range(starting point, exclusive end point, step *optional*)
credit_card = "1234-5678-0123-4567"

for x in credit_card:
    print(x)

# continue - skips that iteration of the code
# break - stops code at that point

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)