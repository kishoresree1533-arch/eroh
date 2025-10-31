age = int(input("Enter your age: "))
experience = input("Do you have experience? (yes/no): ")

if age > 18:
    if experience.lower() == "yes":
        print("You are eligible for the job.")
    else:
        print("You are not eligible — experience required.")
else:
    print("You are not eligible — must be above 18.")
