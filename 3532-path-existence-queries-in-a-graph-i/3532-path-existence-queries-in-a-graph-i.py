class UF:
    def __init__(self, size: int):
        self.size = size
        self.parents = list(range(size))
        self.rank = [1]*size
    
    def find(self, node: int) -> int:
        if node == self.parents[node]: return node

        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False

        if self.rank[p1] > self.rank[p2]:
            self.parents[n2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parents[n1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        uf = UF(n)
        for i in range(n-1):
            if nums[i+1] - nums[i] <= maxDiff:
                uf.union(i, i+1)
        res = []
        for q in queries:
            n1, n2 = q
            res.append(True) if uf.find(n1) == uf.find(n2) else res.append(False)
        return res   
        