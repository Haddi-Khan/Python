# 42.	Print a rectangle of * with given rows and columns.
rows=int(input("enter any number for rows  "))
columns=int(input("enter any number for columns "))
for i in range (rows):
    for j in range (columns):
        print("*",end="")
    print()