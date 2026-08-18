class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (n+1)]
        for _ in range(m):
            dp.append([0] + [-1] * n)
        
        def helper(i: int, j: int):
            if dp[i][j] != -1:
                return dp[i][j]

            if text2[i-1] == text1[j-1]:
                dp[i][j] = 1 + helper(i-1, j-1)
                return dp[i][j]
            else:
                dp[i][j] = max(
                    helper(i, j-1),
                    helper(i-1, j)
                )
                return dp[i][j]
        helper(m, n)
        return dp[m][n]