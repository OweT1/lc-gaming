class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dists = [math.inf if i != k-1 else 0 for i in range(n)]
        neighbours = {}
        visited = {k}
        for time in times:
            u, v, w = time
            if u not in neighbours:
                neighbours[u] = {}
            neighbours[u][v] = w
            visited.add(v)
        
        if len(visited) != n: return -1
        
        queue = [(0, k)]
        while queue:
            curr_dist, ele = queue.pop()
            if curr_dist > dists[ele-1] or ele not in neighbours: continue
            neighbour = neighbours[ele]
            for v, w in neighbour.items():
                if curr_dist + w < dists[v-1]:
                    dists[v-1] = curr_dist + w
                    queue.append((dists[v-1], v))
        print(dists)
        return max(dists)


        