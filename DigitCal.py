import sys

# defining digit x function
def digit(x):
    if x == 0:
        # if x is 0, return value 0 as there is nothing to calculate
        return 0
    # This will check for single digit input, if single digit, return value 1
    elif x < 10:
        return 1
    # This will get the digit number for all other value from 10 onwards
    else:
        # taking the input x, dividing it by 10, taking to remainder then adding a count + 1 afterwards
        return digit(x//10) + 1


# Defining iterative function
def digit_iterative(x):
    # initiate count at 0
    count = 0
    # using while loop to counts the number of digits
    # while x >0, the count will automatically add 1 for every division of 10 
    while x > 0:
        count += 1
        x = x//10
    return count

# Create an input via sys.argv
user_input = int(sys.argv[1])

# Create variables to store value dervied from functions
digit = digit(user_input)
digitIterative = digit_iterative(user_input)


# print statement
print("The number of digit(s) calculated by recursive is %d and by iterative is %d." % (digit, digitIterative))
