# Ascending order
arr = [5, 2, 3, 1, 4, 6]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted array:", arr)

# Hint
a=5
b=6
print(f"Before: a={a}, b={b}")
a,b=b,a
print(f"After: a={a}, b={b}")