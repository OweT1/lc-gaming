class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1

        n = len(nums)
        dp = [1]*n
        counts = [1]*n
        for i in range(1, n):
            indexes = [j for j, num in enumerate(nums[:i]) if num < nums[i]]
            if indexes:
                max_ind = max([dp[ind] for ind in indexes])
                dp[i] = max_ind + 1
                counts[i] = sum([counts[ind] for ind in indexes if dp[ind] == max_ind])
        max_length = max(dp)
        max_indices = [i for i, length in enumerate(dp) if length == max_length]
        return sum([counts[ind] for ind in max_indices])