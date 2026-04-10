def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return seen[diff], i
        seen[num] = i

arr = [1,2,2,3,3,3,3]
print(two_sum(arr, 4))