import sys
n = len(sys.argv)

try:
    if sys.argv[1] == 'abc':
        raise IndexError("Your input is invalid!")

except (IndexError, ValueError):
    print("Your input is invalid!")

units = str(sys.argv[1])
height = float(sys.argv[2])
weight = float(sys.argv[3])

if units == 'metric':
    bmi = weight / (height ** 2)

    if bmi < 16:
        print("{:.2f}\tSevere Thinness".format(bmi))
    elif 16 <= bmi < 16.9:
        print("{:.2f}\tModerate Thinness".format(bmi))
    elif 17 <= bmi < 18.4:
        print("{:.2f}\tMild Thinness".format(bmi))
    elif 18.5 <= bmi <= 24.9:
        print("{:.2f}\tNormal".format(bmi))
    elif 25 < bmi < 29.9:
        print("{:.2f}\tOverweight".format(bmi))
    elif 30 <= bmi < 34.9:
        print("{:.2f}\tObese Class I".format(bmi))
    elif 35 <= bmi < 39.9:
        print("{:.2f})\tObese Class II".format(bmi))
    else:
        print("{:.2f}\tObese Class III".format(bmi))

elif units == 'imperial':
    bmi = (703 * weight) / (height ** 2)

    if bmi < 16:
        print("{:.2f}\tSevere Thinness".format(bmi))
    elif 16 <= bmi < 16.9:
        print("{:.2f}\tModerate Thinness".format(bmi))
    elif 17 <= bmi < 18.4:
        print("{:.2f}\tMild Thinness".format(bmi))
    elif 18.5 <= bmi <= 24.9:
        print("{:.2f}\tNormal".format(bmi))
    elif 25 <= bmi < 29.9:
        print("{:.2f}\tOverweight".format(bmi))
    elif 30 <= bmi < 34.9:
        print("{:.2f}\tObese Class I".format(bmi))
    elif 35 <= bmi < 39.9:
        print("{:.2f})\tObese Class II".format(bmi))
    else:
        print("{:.2f}\tObese Class III".format(bmi))

else:
    print("Your input is invalid!")
