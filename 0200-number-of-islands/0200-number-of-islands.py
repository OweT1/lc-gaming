class Solution:
    def get_neighbours(
        self, r: int, c: int, rows: int, cols: int, visited: List[List[int]]
    ) -> List[Tuple[int]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        valid_neighbours = []
        for d in directions:
            new_r, new_c = r + d[0], c + d[1]
            if new_r >= 0 and new_r < rows and new_c >= 0 and new_c < cols and not visited[new_r][new_c]:
                valid_neighbours.append((new_r, new_c))
        return valid_neighbours

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        to_check = deque()
        
        rows, cols = len(grid), len(grid[0])
        visited = [[0]*cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c]:
                    visited[r][c] = 1

                    if grid[r][c] == "1":
                        to_check.extend(self.get_neighbours(r, c, rows, cols, visited))
                        
                        while to_check:
                            neighbour = to_check.popleft()
                            n_r, n_c = neighbour[0], neighbour[1]
                            if not visited[n_r][n_c] and grid[n_r][n_c] == "1":
                                to_check.extend(self.get_neighbours(n_r, n_c, rows, cols, visited))
                            visited[n_r][n_c] = 1
                        islands += 1
        return islands

                    

                    