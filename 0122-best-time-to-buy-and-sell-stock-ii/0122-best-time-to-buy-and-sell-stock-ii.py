class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = i = 0

        buy: int = -1
        while i < len(prices)-1:
            c, n = prices[i], prices[i+1]
            if buy != -1:
                if c > n:
                    profit += c - buy
                    buy = -1
            else:
                if c < n:
                    buy = c
            i += 1
        
        if buy != -1:
            profit += max(prices[-1] - buy, 0)
        return profit


        