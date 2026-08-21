class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        cache = {}
        def solve(x: int) -> int:
            res = 0

            if x in cache:
                return cache[x]
            y = x
            while y > 1:
                if y in cache:
                    return res + cache[y]
                if y % 2 == 0:
                    y = y // 2
                else:
                    y = y*3 + 1
                res += 1
            cache[x] = res
            return res
        
        pq = []
        for i in range(lo, hi+1):
            heapq.heappush(pq, (solve(i), i))
        
        for _ in range(k-1):
            heapq.heappop(pq)
        return heapq.heappop(pq)[1]