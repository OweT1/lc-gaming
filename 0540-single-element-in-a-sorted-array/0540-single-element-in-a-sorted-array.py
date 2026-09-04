class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        l, r = 0, len(nums)-1
        while l < r:
            m = l + ((r-l) >> 1)
            if (m % 2 == 0 and nums[m+1] == nums[m]) or (m % 2 == 1 and nums[m] == nums[m-1]):
                l = m + 1
            else:
                r = m
        return nums[l]