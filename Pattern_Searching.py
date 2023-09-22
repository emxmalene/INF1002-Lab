import sys


# This is to define the function count_pattern,with 2 variables candidate and pattern
def count_pattern(candidate, pattern):
    # This is to get the length of the candidate and pattern
    candidate_length = len(candidate)
    pattern_length = len(pattern)

    # Count the number of pattern occuring
    count = 0

    # Checking the substring of the candidate, and matching it to the pattern recognise
    for i in range(candidate_length - pattern_length +1):
        if candidate[i:i + pattern_length] == pattern:
            # Increase count for every pattern found
            count +=1
    return count

# This is to check whether there are 3 command line arguements
if len(sys.argv) != 3:
    print("Please enter a valid number and sequence")
else:
    candidate = sys.argv[1]
    pattern = sys.argv[2]
    # This counts the pattern using the fuction above
    result = count_pattern(candidate, pattern)
    print("Pattern appears", str(result), "time!")

