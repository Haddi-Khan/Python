arr = [10,20,30,40,50]
largest = arr[0]
second_largest = float('-inf')

for i in range(1, len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print("Second Largest:", second_largest)