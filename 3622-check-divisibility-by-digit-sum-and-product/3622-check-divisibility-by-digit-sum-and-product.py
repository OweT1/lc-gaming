class Solution:
    def checkDivisibility(self, n: int) -> bool:
        o = n
        n_sum = n_product = n % 10
        n //= 10
        while n > 0:
            d = n % 10
            n_sum += d
            n_product *= d
            n //= 10
        return (o % (n_sum + n_product)) == 0
        