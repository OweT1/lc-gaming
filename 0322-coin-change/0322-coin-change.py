class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def solve(curr: int):
            if curr < 0: return -1
            if curr == 0: return 0
            if curr in cache: return cache[curr]

            res = math.inf
            for coin in coins:
                temp = solve(curr-coin)
                if temp != -1:
                    res = min(res, temp+1)
            
            cache[curr] = res if res != math.inf else -1
            return cache[curr]

        return solve(amount)

       




        