n = int(input("Enter number of rows: "))

for i in range(n):
    
    for j in range(n - i + 1):
        print(" ", end="")

    
    num = 1
    for k in range(i + 1):
        print(num, end=" ")
        num = num * (i - k) // (k + 1)
    print()  
