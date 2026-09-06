# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = l + ((r-l) >> 1)
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return r
        