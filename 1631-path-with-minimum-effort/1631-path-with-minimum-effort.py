class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        rows, cols = len(heights), len(heights[0])
        distances = [[math.inf] * cols for _ in range(rows)]
        distances[0][0] = 0

        pq = [(0, (0, 0))] # origin
        visited = set()
        while pq:
            w, (i, j) = heapq.heappop(pq)

            if (i, j) in visited or w > distances[i][j]: continue
            if i == rows-1 and j == cols-1: return w
            
            for d_i, d_j in directions:
                new_i, new_j = i + d_i, j + d_j
                if (
                    new_i >= 0 and
                    new_i < rows and
                    new_j >= 0 and
                    new_j < cols and
                    (new_i, new_j) not in visited and
                    abs(heights[new_i][new_j] - heights[i][j]) < distances[new_i][new_j]
                ):
                    distances[new_i][new_j] = max(w, abs(heights[new_i][new_j] - heights[i][j]))
                    heapq.heappush(pq, (distances[new_i][new_j], (new_i, new_j)))
            visited.add((i, j))
        return distances[-1][-1]
        