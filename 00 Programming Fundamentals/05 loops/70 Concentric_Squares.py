# 70.	Print concentric squares of numbers.
n = 4 
size = 2 * n - 1
matrix = [[0 for _ in range(size)] for _ in range(size)]
start = 0
end = size - 1
current_val = n
while start <= end:
    for i in range(start, end + 1):
        for j in range(start, end + 1):
            if i == start or i == end or j == start or j == end:
                matrix[i][j] = current_val
    start += 1
    end -= 1
    current_val -= 1
for i in range(size):
    for j in range(size):
        print(f"{matrix[i][j]}", end=" ")
    print()
