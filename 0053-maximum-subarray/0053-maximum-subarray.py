class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -math.inf
        curr = 0
        for num in nums:
            curr += num
            res = max(res, curr)
            if curr < 0:
                curr = 0
        return res