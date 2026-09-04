class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        res = -math.inf
        curr = 1
        for num in nums:
            curr *= num
            res = max(res, curr)
            if curr == 0:
                curr = 1
        
        curr = 1
        for num in nums[::-1]:
            curr *= num
            res = max(res, curr)
            if curr == 0:
                curr = 1

        return res

