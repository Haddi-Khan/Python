import heapq

max_heap = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -30)
heapq.heappush(max_heap, -5)

print(-heapq.heappop(max_heap))  
