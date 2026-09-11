class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target: return 0
        l, r = 0, len(nums)-1

        while l < r:
            m = l + ((r-l) >> 1)
            if nums[m] == target: return m
            if (nums[m] > nums[r] and (target >= nums[m] or target <= nums[r])) or \
                (nums[m] < nums[r] and nums[m] <= target <= nums[r]):
                l = m + 1
            else:
                r = m
        return l if nums[l] == target else -1