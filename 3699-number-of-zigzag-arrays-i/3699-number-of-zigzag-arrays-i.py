class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        """
        Explanation:
        We initialise the dp with 1 for each position, where each position is the number of arrays where the last element is that position.
        For m = 3, we have [[1], [2], [3]] as our starter.
        Thereafter, we will iterate through n-1 times, where each time we will do a prefix sum for each position.
        Reason being that for each position, the number of possible arrays that can end with the position number is the number of arrays that were lower than the position number.

        Using the same example and assuming increasing direction at the start,
        For turn 1, there are 0 arrays that can end with 1, 1 array that can end with 2 (which is [[1]]), 2 arrays that can end with 3 (which is [[1], [2]], since 3 > 2 > 1)
        For turn 2, there are 3 arrays that can end with 1 (which is [[1, 2], [1, 3], [2, 3]]), 2 arrays that can end with 2 (which is [[1, 3], [2, 3]]) and 0 arrays that can end with 3.

        Code wise, to facilitate the alternating direction, we can just reverse the dp at each turn, and always assume increasing direction.

        The calculation:
        Turn 0: [1, 1, 1]
        Turn 1: [0, 1, 2]
        Turn 2: [0, 2, 3]

        where each term in each turn is calculated by reversing the previous dp, and calculating the prefix cumulative sum.
        """
    
        mod = 10**9 + 7
        m = r - l + 1

        dp = [1] * m

        for _ in range(n-1):
            dp.reverse()

            pref = 0

            for i in range(m):
                old = dp[i]
                dp[i] = pref
                pref = (pref + old) % mod

        return (sum(dp) % mod * 2) % mod




