import sys

if len(sys.argv) < 2:
    print("Your input is invalid!")
    sys.exit(1)

enter = sys.argv[1]  # fit argument as one input
enter = enter.lower()  # convert to all lower case
letters_dict = {}  # to store letter count

# To loop characters for storage
for letters in enter:
    if letters not in letters_dict:
        letters_dict[letters] = 1
    else:  # Check if letter is in dictionary
        letters_dict[letters] += 1  # increment of letter count
letters_dict = dict(sorted(letters_dict.items(), key=lambda x: (-x[1], x[0])))
#   letters_dict.items : gets all key values pairs items from letter_dict dictionary. returns a list of tuples
#   dict : convert all sorted list of tuples back into dict
#   sorted : sorts the list of tuples
#   key = lambda : defines the sorting key
#   sort by descending order with -x[1], x[0]
count = 0
output = ""

for pair, in letters_dict:  # for all letters in dict, add count +1
    if count < 5:
        output += f"{pair}:{letters_dict[pair]}"
# output variable accumulates formatted strings for each "pair" and "count" combination, separated by a comma and space
# this is often used to build a string that will be printed or displayed as a final output
        count += 1
        output += ","

print(output[:-1])
