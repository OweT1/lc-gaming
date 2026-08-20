class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacencyList = {}
        for u, v, w in times:
            if u not in adjacencyList:
                adjacencyList[u] = {}
            adjacencyList[u][v] = w
 
        distances = {i: math.inf for i in range(1, n+1)}
        distances[k] = 0

        pq = [(0, k)]
        visited = set()
        while pq:
            dist, node = heapq.heappop(pq)
            if dist > distances[node] or node not in adjacencyList: continue
            for neighbour_node, neighbour_weight in adjacencyList[node].items():
                new_distance = neighbour_weight + dist
                if new_distance < distances[neighbour_node]:
                    distances[neighbour_node] = new_distance
                    visited.add(neighbour_node)
                    heapq.heappush(pq, (new_distance, neighbour_node))
        return -1 if len(visited) != n-1 else max(distances.values())