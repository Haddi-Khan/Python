# 46.	Print a half pyramid of alphabets.
n = int(input("Enter number of rows: "))
for i in range(1, n+1):              
    for j in range(1, i+1):          
        print(chr(65 + j - 1), end=" ")
    print()