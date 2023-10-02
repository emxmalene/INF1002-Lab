import sys

n = len(sys.argv)
normal_Workinghours = float(sys.argv[1])
normal_Workingrate = float(sys.argv[2])
overtime_Workingrate = float(sys.argv[3])

try:
    if n != 4 or normal_Workinghours > 168:
        raise IndexError("Invalid number of arguments")

except (IndexError, ValueError):
    print("Your input is invalid!")
else:
    if normal_Workinghours <= 40:
        normal_totalPayment = normal_Workinghours * normal_Workingrate
        overtime_Workinghours = 0
        overtime_payment = 0
        total_payment = normal_totalPayment + overtime_payment
        print("Normal Salary:{:.2f}, Extra Salary:{:.2f}, Total Salary:{:.2f}".format(normal_totalPayment, overtime_payment, total_payment))

    else:
        overtime_hours = normal_Workinghours - 40
        normal_payment = normal_Workingrate * 40
        overtime_payment = overtime_Workingrate * overtime_hours
        total_payment = normal_payment + overtime_payment
        print("Normal Salary:{:.2f}, Extra Salary:{:.2f}, Total Salary:{:.2f}".format(normal_payment, overtime_payment, total_payment))