class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n > 1:
            if n in visited: return False

            visited.add(n)
            t = 0
            while n:
                t += (n % 10) ** 2
                n //= 10
            n = t
        return True