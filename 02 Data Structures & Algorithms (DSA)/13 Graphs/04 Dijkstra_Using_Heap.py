import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    while heap:
        curr_dist, node = heapq.heappop(heap)

        for neighbor, weight in graph[node]:
            if curr_dist + weight < dist[neighbor]:
                dist[neighbor] = curr_dist + weight
                heapq.heappush(heap, (dist[neighbor], neighbor))

    return dist
