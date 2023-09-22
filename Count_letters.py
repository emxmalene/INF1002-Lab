import sys

# This is the function to store user input as a list
list_input = tuple(sys.argv[1].split(','))



# This function will take in one word, count it and return it to a dictionary with the frequency
# counts of the letters
def letter_count(string, destination={}):
    for letters in string:
        if letters in destination:
            destination[letters]+= 1 
        else:
            destination[letters] = 1


# This is to take in two words and returns a dictionary with
# the frequency counts of the various letters

def double_count(str1, str2):
    # calling for the dictionary named x
    x_dict = {}
    # count the number of letters in the respective string
    letter_count(str1, x_dict)
    letter_count(str2, x_dict)
    return x_dict

# This various count function will take in any number of words and return a dictionary
def various_count(*str):
    # calling for the dictionary named x
    x_dict = {}
    # This stores the number of strings input into a list
    y = list(*str)
    # This function will then read the string in the list, then count and store in the dict
    for string in y:
        letter_count(string, x_dict)
    return x_dict

sorted_total = sorted(various_count(list_input).items(), key=lambda x:x[0], reverse = True)
output = ''

for items in sorted_total:
    output += '%s:%d ' % (items[0], items[1])

print(output)
         
