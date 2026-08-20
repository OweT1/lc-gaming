class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [list(range(n+1))]
        for i in range(1,m+1):
            dp.append([i] + [-1]*n)

        def dfs(i: int, j: int):
            if dp[i][j] != -1: return dp[i][j]
            if word1[j-1] == word2[i-1]:
                dp[i][j] = dfs(i-1, j-1)
                return dp[i][j]
            else:
                dp[i][j] = 1 + min(
                    dfs(i-1, j-1),
                    dfs(i-1, j),
                    dfs(i, j-1)
                )
                return dp[i][j]

        dfs(m, n)
        return dp[-1][-1]
        