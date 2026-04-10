def linear_search_with_count(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1  
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons


data = [10, 23, 45, 70, 11, 15]
search_target = 70
index, count = linear_search_with_count(data, search_target)
if index != -1:
    print(f"Target {search_target} found at index: {index}")
    print(f"Total comparisons made: {count}")
else:
    print(f"Target {search_target} not found after {count} comparisons.")