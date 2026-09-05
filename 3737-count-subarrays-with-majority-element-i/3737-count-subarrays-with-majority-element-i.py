class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        if not nums: return 0

        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + (1 if nums[i-1] == target else -1)
    
        res = 0
        for i in range(n):
            for j in range(i, n):
                if prefix[j+1] - prefix[i] > 0:
                    res += 1
        return res