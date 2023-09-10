import sys
n = len(sys.argv)

try:
    type = sys.argv[1]
    height = sys.argv[2]
    weight = sys.argv[3]
except (IndexError, ValueError):
    print("Your input is invalid!")

else:
    height = float(height)
    weight = float(weight)
    bmi = 0
    category = ""
    if type == "metric":
        bmi = weight/(height**2)
    elif type == "imperial":
        bmi = (703*weight)/(height**2)
    if bmi <= 16:
        category = "Severe Thinness"
    elif bmi <= 17:
        category = "Moderate Thinness"
    elif bmi <= 18.5:
        category = "Mild Thinness"
    elif bmi <= 25:
        category = "Normal"
    elif bmi <= 30:
        category = "Overweight"
    elif bmi <= 35:
        category = "Obese Class I"
    elif bmi <= 40:
        category = "Obese Class II"
    else:
        category = "Obese Class III"

    print("%0.2f"%bmi+"\t"+category)
