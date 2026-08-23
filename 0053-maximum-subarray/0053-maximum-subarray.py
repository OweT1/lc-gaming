class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        curr, res = 0, -math.inf
        while r < len(nums):
            curr += nums[r]
            res = max(res, curr)
            r += 1
            if curr < 0:
                l = r
                curr = 0
        return res
            