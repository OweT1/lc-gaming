class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = list(range(n))
        self.size = [1]*n
    
    def find(self, n: int) -> int:
        if self.parents[n] == n: return n

        self.parents[n] = self.find(self.parents[n])
        return self.parents[n]

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False

        if self.size[p1] < self.size[p2]: # p1 will always be largest
            p1, p2 = p2, p1

        self.parents[p2] = p1
        self.size[p1] += self.size[p2]
        return True

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                point1, point2 = points[i], points[j]
                man_dist = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                edges.append((i, j, man_dist))
        
        uf = UnionFind(n)
        res = 0
        for u, v, w in sorted(edges, key=lambda x: x[2]):
            if uf.union(u, v):
                res += w
        return res

        
