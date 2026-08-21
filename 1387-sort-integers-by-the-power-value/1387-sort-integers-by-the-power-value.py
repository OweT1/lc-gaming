class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        cache = {1: 0}
        def solve(x: int) -> int:
            res = 0

            if x in cache: return cache[x]
            
            if x % 2 == 0:
                res = solve(x // 2) + 1
            else:
                res = solve(3*x + 1) + 1

            cache[x] = res
            return res
        
        pq = []
        for i in range(lo, hi+1):
            heapq.heappush(pq, (solve(i), i))

        for _ in range(k-1):
            heapq.heappop(pq)
        return heapq.heappop(pq)[1]