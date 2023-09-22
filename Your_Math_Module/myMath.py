# This is to define the Math module functions that we want to create

# Function 1 Addition of x and y
def add(x, y):
    return x + y


# Function 2 Subtraction of x and y
def subtraction(x, y):
    return x - y

# Function 3 Checking for even number in the sys.argv input, where it will sort all the values and print out even
# number
def evenNum(x):
    return len([num for num in x if num % 2 == 0])

# Function 4 Checking for the max value of sys.arv input
def maximum(x):
    return max(x)


# Function 5 Checking for the min value of sys.argv input
def minimum(x):
    return min(x)


# Function 6 Checking for the absolute value of sys.argv input and returning it
def absolute(x):
    return abs(x)


# Function 7 Checking for the total sum of sys.argv input
def sumTotal(x):
    return sum(x)


# Function 8 Sets all the elements into 0 for a given list x
def clear(x):
    return [0] * len(x)
