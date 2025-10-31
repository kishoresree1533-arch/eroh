username = "admin"
password = "12345"

# Get user input
user = input("Enter username: ")
pwd = input("Enter password: ")

# Check username and password using nested if
if user == username:
    if pwd == password:
        print("Login successful! Welcome,", user)
    else:
        print("Incorrect password!")
else:
    print("Invalid username!")
