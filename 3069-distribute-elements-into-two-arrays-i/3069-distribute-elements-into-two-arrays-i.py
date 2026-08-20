class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return nums
        arr1, arr2 = [nums[0]], [nums[1]]
        for e in nums[2:]:
            arr1.append(e) if arr1[-1] > arr2[-1] else arr2.append(e)
        return arr1 + arr2
        