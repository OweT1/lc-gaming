class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def traverse(i, j):
            if (i, j) in cache: return cache[(i, j)]
            elif i <= 0 or j <= 0: return 0
            elif i == 1 or j == 1: return 1
            cache[(i, j)] = traverse(i-1, j) + traverse(i, j-1)
            return cache[(i, j)]
        
        return traverse(m, n)