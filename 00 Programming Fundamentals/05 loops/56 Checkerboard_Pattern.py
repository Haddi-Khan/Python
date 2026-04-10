# 56.	Print a checkerboard pattern of *.
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()