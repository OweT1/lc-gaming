class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        for i, num in enumerate(nums):
            if num <= 0: nums[i] = n+1
        
        for num in nums:
            if abs(num) <= n: nums[abs(num)-1] = -abs(nums[abs(num)-1])

        for i, num in enumerate(nums, start=1):
            if num > 0: return i
        return n+1