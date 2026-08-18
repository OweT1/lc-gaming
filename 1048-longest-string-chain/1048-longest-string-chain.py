class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        res = 0
        for w in sorted(words, key=lambda x: len(x)):
            temp = 0
            if len(w) == 1:
                temp = 1
            else:
                for i in range(len(w)):
                    new_w = w[:i] + w[i+1:]
                    temp = max(temp, dp.get(new_w, 0) + 1)

            dp[w] = temp
            res = max(res, temp)
        return res
                