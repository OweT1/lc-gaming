class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat: return [0]

        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        res = [[None]*n for _ in range(m)]

        neighbours = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    neighbours.append((i, j))
                    visited.add((i, j))
                    res[i][j] = 0

        curr = 0
        while len(visited) < m * n:
            new_neighbours = []
            curr += 1
            for t_i, t_j in neighbours:
                for add_i, add_j in directions:
                    new_i, new_j = t_i + add_i, t_j + add_j
                    if new_i >= 0 and new_i < m and \
                        new_j >= 0 and new_j < n and \
                        (new_i, new_j) not in visited:
                            new_neighbours.append((new_i, new_j))
                            visited.add((new_i, new_j))
                            res[new_i][new_j] = curr
            neighbours = new_neighbours.copy()
        return res