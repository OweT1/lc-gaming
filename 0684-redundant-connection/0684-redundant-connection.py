class UF:
    def __init__(self, size: int):
        self.parents = [i for i in range(size+1)]
        self.rank = [1]*(size+1)
    
    def find(self, n: int) -> int:
        # assume n is 1-based
        while self.parents[n] != n:
            n = self.parents[n]
        return n
    
    def union(self, n1: int, n2: int) -> bool:
        # assume both n are 1-based
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False

        if self.rank[n1] > self.rank[n2]:
            n1, n2 = n2, n1
            p1, p2 = p2, p1
        
        self.rank[p2] += self.rank[p1]
        self.parents[p1] = self.parents[p2]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = len(set([e for edge in edges for e in edge]))
        uf = UF(size)

        for edge in edges:
            n1, n2 = edge
            if not uf.union(n1, n2):
                return edge
