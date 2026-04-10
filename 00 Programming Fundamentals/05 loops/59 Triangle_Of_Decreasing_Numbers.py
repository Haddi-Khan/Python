# 59.	Print a triangle of decreasing numbers.
n = int(input("Enter number of rows: "))
num = n * (n + 1) // 2   
for i in range(n, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num -= 1
    print()

