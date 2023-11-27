import sys

# checking if there are any values added into the argv, if not,return invalid inpt and exit
if len(sys.argv) < 2:
    print("Please enter valid integers.")
    sys.exit(1)

# for users to input as a list of integers
enter = sys.argv[1]
# split user input with a comma
enter = enter.split(',')
# checking if the input is a number/integer
for i in range(len(enter)):
    if enter[i].isdigit():
        enter[i] = int(enter[i])
    else:
        print("Please enter valid integers.")
        exit()

# sort the input via ascending order
enter.sort()

# Command line, to count even number, odd number and the sum, whilst setting it to count from the front or the back
even_count = 0
odd_count = 0
even_total = 0
odd_total = 0
# access the last element in the list, which in this case is the biggest number as we sorted it above
highest_number = enter[-1]
# access the first element in the list, which in this case is the lowest number as we sorted it above
lowest_number = enter[0]
total_value = 0
x = highest_number + lowest_number

for ent in enter:
    total_value += ent
    # checking for even number, which is divisible by 2
    if (ent % 2) == 0:
        # for all even number, count plus 1
        even_count += 1
        # for all even number, add into ent
        even_total += ent
    # check for odd number count
    else:
        odd_count += 1
        odd_total += ent

# counting the average with formula
centered_avg = int((total_value - x) / (len(enter) - 2))

# crafting the output in a single line
print(f"The sum of all even numbers is {even_total}, the sum of all odd numbers is {odd_total}, "
      f"the difference between the biggest and smallest number is {highest_number - lowest_number}, the "
      f"total number of even numbers is {even_count}, the total number of odd numbers is "
      f"{odd_count}, the centered average is {centered_avg:0.0f}.")
