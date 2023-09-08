import sys
n = len(sys.argv)

a = str(sys.argv[1])
b = str(sys.argv[2])
c = str(sys.argv[3])

if a.isdigit():
    add = float(a) + float(b) + float(c)
    average = (add/3)
    print("Average:%.2f" % average)
else:
    print("Your input is invalid!")