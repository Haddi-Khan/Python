# 43.	Print a right-angled triangle of *.
n=int(input("enter any numer "))
for i in range (1,n+1):
    for j in range (i):
        print("*",end="")
    print()