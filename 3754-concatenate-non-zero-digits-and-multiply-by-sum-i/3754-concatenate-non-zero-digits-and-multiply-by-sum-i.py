class Solution:
    def sumAndMultiply(self, n: int) -> int:
        res, s, i = 0, 0, 0
        while n:
            cur = n % 10
            if cur > 0:
                res += cur * (10**i)
                s += cur
                i += 1
            n //= 10
        return res * s
