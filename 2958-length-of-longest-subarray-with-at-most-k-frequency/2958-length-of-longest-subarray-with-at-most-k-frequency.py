class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        res = 0
        nums_counter = {}

        while r < len(nums):
            nums_counter[nums[r]] = nums_counter.get(nums[r], 0) + 1
            while nums_counter[nums[r]] == k+1:
                res = max(res, r-l)
                nums_counter[nums[l]] -= 1
                l += 1
            r += 1
        
        return max(res, r-l)




        