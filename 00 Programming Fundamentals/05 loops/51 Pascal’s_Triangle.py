# 51.	Print Pascal’s triangle.
rows = 5
for i in range(rows):    
    print(" " * (rows - i), end="")    
    val = 1
    for j in range(i + 1):       
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()
