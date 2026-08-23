class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacencyList = {}
        for flight in flights:
            f, t, p = flight
            if f not in adjacencyList:
                adjacencyList[f] = {}
            adjacencyList[f][t] = p
        dists = {i: math.inf for i in range(n)}
        dists[src] = 0
        turns = 0
        start = [(dists[src], src)]
        while start:
            tmp = []
            if turns == k+1: break
            for curr_dist, node in start:
                if node not in adjacencyList: continue
                neighbours = adjacencyList[node]
                for nb, dist in neighbours.items():
                    if curr_dist + dist < dists[nb]:
                        dists[nb] = curr_dist + dist
                        tmp.append((dists[nb], nb))
            start = tmp.copy()
            turns += 1
        return dists.get(dst) if dists.get(dst) != math.inf else -1
        