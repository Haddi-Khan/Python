# 44.	Print an inverted right-angled triangle of *.
rows=int(input("enter any number for rows  "))
for i in range (rows,0,-1):
    for j in range (i):
        print("*",end="")
    print()