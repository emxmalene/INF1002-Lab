import sys


# defining sum recursive formula
def sum_recursive(x):
    if x == 0:
        return 0
    # If input/ x value is != 0, then it will run the else. This will run until the input reaches base which is 0
    # formula for recursive will be (x-1) + x, where the formula will run till x hits 0
    else:
        return sum_recursive(x - 1) + x


# defining sum iterative。 sum iterative takes only one argument x
def sum_iterative(x):
    # count starts from 0
    total = 0
    # Creates a loop that starts from 0 to x
    for i in range(x + 1):
        # This will add the integers to get the sum
        total += i
    return total


# Creating an inout line with it taking is as an integer
user_input = int(sys.argv[1])

iterative = sum_iterative(user_input)
recursive = sum_recursive(user_input)

print("The SUM value calculated by recursive is %d and by iterative is %d." % (recursive, iterative))
