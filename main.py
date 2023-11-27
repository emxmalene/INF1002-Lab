import sys
n = len(sys.argv)

a = str(sys.argv[1])
b = str(sys.argv[2])
c = str (sys.argv[3])

if a.isdigit() and b.isdigit() and c.isdigit():
    add = float(a) + float (b) + float (c)
    avg = add /3
    print ("The average of the three numbers is \n {avg:.2f}")
else:
    print ("Your input is invalid!")