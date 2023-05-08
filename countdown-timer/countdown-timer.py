# Import time module
import time

my_time = int(input("Enter the time in seconds: "))

# reverse loop -  range(start, end, negative step)

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    # could add % 24 to hours if we were to add Days to the timer as well
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)




print("TIME'S UP!")