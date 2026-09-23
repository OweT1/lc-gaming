class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if n == 1 and grid[0][0] == 0: return 1
        if grid[0][0] == 1 or grid[n-1][n-1] == 1: return -1

        visited = [[False]*n for _ in range(n)]
        visited[0][0] = True
        res = 1
        dq = [(0, 0)]
        while dq:
            temp = []
            for i, j in dq:
                for add_i in range(-1, 2):
                    for add_j in range(-1, 2):
                        new_i, new_j = i + add_i, j + add_j
                        if new_i == n-1 and new_j == n-1: return res + 1
                        if new_i >= 0 and new_i < n and \
                            new_j >= 0 and new_j < n and \
                            grid[new_i][new_j] == 0 and \
                        not visited[new_i][new_j]:
                            temp.append((new_i, new_j))
                            visited[new_i][new_j] = True
            dq = temp.copy()
            res += 1
        return -1

