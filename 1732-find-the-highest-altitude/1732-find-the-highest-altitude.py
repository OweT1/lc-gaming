class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        c, m = 0, 0
        for g in gain:
            c = c + g
            m = max(m, c)
        return m
        