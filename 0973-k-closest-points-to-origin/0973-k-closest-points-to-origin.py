class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            heapq.heappush(pq, (math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2)), point))

        closest = []
        for _ in range(k):
            closest.append(heapq.heappop(pq)[1])
        return closest