def heap_sort(arr):
    import heapq
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]


arr=[1,2,4,5]
print (heap_sort(arr))