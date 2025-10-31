marks = float(input("Enter your marks: "))
attendance = float(input("Enter your attendance percentage: "))

if marks >= 85:
    if attendance >= 90:
        print("Congratulations! You qualify for the scholarship.")
    else:
        print("You do not qualify — attendance below 90%.")
else:
    print("You do not qualify — marks below 85.")
