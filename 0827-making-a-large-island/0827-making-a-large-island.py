class UnionFind:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.size = [1]*n

    def find(self, n: int) -> int:
        if self.parents[n] == n: return n

        self.parents[n] = self.find(self.parents[n])
        return self.parents[n]
    
    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False

        if self.size[p1] < self.size[p2]:
            p2, p1 = p1, p2
        
        self.parents[p2] = self.parents[p1]
        self.size[p1] += self.size[p2]


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        uf = UnionFind(n*n)

        zeros = []
        visited = [[False]*n for _ in range(n)]
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1 and not visited[row][col]:
                    node = row * n + col
                    dq = deque([(row, col)])
                    while dq:
                        r, c = dq.popleft()
                        for add_r, add_c in directions:
                            new_r, new_c = r + add_r, c + add_c
                            if new_r >= 0 and new_r < n and new_c >= 0 and new_c < n and not visited[new_r][new_c] and grid[new_r][new_c] == 1:
                                new_node = new_r * n + new_c
                                uf.union(node, new_node)

                                dq.append((new_r, new_c))
                                visited[new_r][new_c] = True
                elif grid[row][col] == 0:
                    zeros.append((row, col))
        
        if not zeros: return n*n

        res = -math.inf
        for r, c in zeros:
            temp = 1
            parents = set()
            for add_r, add_c in directions:
                new_r, new_c = r + add_r, c + add_c
                if new_r >= 0 and new_r < n and new_c >= 0 and new_c < n and grid[new_r][new_c] == 1:
                    new_node = new_r * n + new_c
                    new_p = uf.parents[new_node]
                    if new_p not in parents:
                        temp += uf.size[new_p]
                        parents.add(new_p)
            res = max(res, temp)
        return res


