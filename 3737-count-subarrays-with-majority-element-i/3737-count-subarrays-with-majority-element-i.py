class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        pre = [0] * (2*n + 1)
        pre[n] = 1

        pre_sum = 0
        curr = n
        res = 0

        for num in nums:
            if num == target:
                pre_sum += pre[curr]
                curr += 1
                pre[curr] += 1
            else:
                curr -= 1
                pre_sum -= pre[curr]
                pre[curr] += 1
            res += pre_sum
        return res