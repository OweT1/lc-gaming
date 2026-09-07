class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums)
        dp = [math.inf] * n
        dp[0] = 1
        for i in range(1, n):
            indices_dp = [dp[j] for j, num in enumerate(nums[:i]) if nums[i] > num]
            dp[i] = 1 if not indices_dp else max(indices_dp) + 1
        return max(dp)

        