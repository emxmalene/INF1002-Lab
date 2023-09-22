import sys
# This line is to import all functions done up in myMath.py
from myMath import *


def main():
    if len(sys.argv) != 2:
        print("Please enter a valid number")
        return
    
    # Split the input string into a list of numbers
    input_numbers = sys.argv[1].split(',')
    
    # Defining the string name and checking/converting the input into integers before storing them into a list
    numbers = [int(num) for num in input_numbers]

    # If the number is not valid, or not integer or cannot be converted to an integer, return value of "Please enter
    # a valid number
    if not numbers:
        print("Please enter a valid number")
        return  # This is to return the user back to the input function

    # Checking for the max value in numbers list
    highest_value = maximum(numbers)
    # Checking for the min value in numbers list
    lowest_value = minimum(numbers)
    # Checking for the difference of max and min in numbers list
    diff = subtraction(highest_value, lowest_value)
    # Checking for the sum of value of max and min in numbers list
    summation = add(highest_value, lowest_value)
    # Checking for the sum of all values in numbers list
    total = sumTotal(numbers)
    # Checking for even number
    even = evenNum(numbers)
                            

    # If the smallest number in the list is smaller than 5, set all the value to 0. Otherwise, remain the
    # same. Print all the values in the list in the end.
    if lowest_value < 5:
        numbers = clear(numbers)

    print("The difference is:%d The summation is:%d The summation of all input is:%d The number of even numbers is:%d The values in the list are: %s" % (diff, summation, total, even, numbers)) 
if __name__ == "__main__":
    main()

