import sys

# defining the check elfish function
def check_elfish(x, check = "elf"):
    # checking all the required letters
    if not check:
        return True

    # checking the first letter in elf is present in the word
    if check[0] in x:
        # if letter is found, call the function check_elfish, then repeating the process until it has run through the other 2 letters, l and f
        return check_elfish(x, check[1:]) # [1:] is a slicing function
    # If the letters are not found, they will return a false value
    return False

# Creating an input for the user to enter
user_input = sys.argv[1]

# the if loop will run the function to check, if letters present then print first statement, else print the other.
if check_elfish(user_input):
    print("%s is one elfish word!" % (user_input))
else:
    print("%s is not an elfish word!" % (user_input))
