class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        for i in range(1, len(nums)+1):
            if i == len(nums) or nums[i] != nums[i-1] + 1:
                break

        seq_prefix_sum = sum(nums[:i])
        nums_set = set(nums)
        while seq_prefix_sum in nums_set:
            seq_prefix_sum += 1
        return seq_prefix_sum