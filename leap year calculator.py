import sys
from typing import List

# Check if argument are 3 inputs
if len(sys.argv) != 3:
    print("Your input is invalid!")
    sys.exit(1)
# To try to fit arguments
try:
    start_year = int(sys.argv[1])
    end_year = int(sys.argv[2])

# user handles the error
except ValueError:
    print("Your input is invalid!")
    sys.exit(1)

# Check if provided years are valid
if start_year > end_year:
    print("Your input is invalid!")
    sys.exit(1)

# Start program
# [] a set of array
leap_year = []
# start from 0
leap_year_count = 0

for year in range(start_year, end_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_year.append(year)  # append return value to list
        leap_year_count += 1

print(f"The number of Leap Years is {leap_year_count}, the Leap Years are {', '.join(map(str, leap_year))}")
# map function for variables without a loop
# join function to combine leap year count and leap year tgt
