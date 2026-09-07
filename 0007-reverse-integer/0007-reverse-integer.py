class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = -x if is_negative else x
        res = 0

        while x:
            res += x % 10
            res *= 10
            x //= 10
        
        res //= 10
        res = -res if is_negative else res
        return 0 if res < -2**31 or res >= 2**31 else res 
        