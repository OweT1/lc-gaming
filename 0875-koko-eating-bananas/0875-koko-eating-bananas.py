class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k: int) -> bool:
            return sum([int(pile / k) + (1 if pile % k else 0) for pile in piles]) <= h
        
        l, r = 1, max(piles)
        while l < r:
            m = l + ((r - l) >> 1)
            if canFinish(m):
                r = m
            else:
                l = m + 1
        return l
        