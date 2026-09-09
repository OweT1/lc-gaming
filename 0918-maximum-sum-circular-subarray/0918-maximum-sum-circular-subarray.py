class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max, res_max = 0, -math.inf
        curr_min, res_min = 0, math.inf
        total_sum = 0

        for num in nums:
            curr_max = max(num, curr_max + num)
            res_max = max(res_max, curr_max)

            curr_min = min(num, curr_min + num)
            res_min = min(res_min, curr_min)

            total_sum += num

        res_circular = total_sum - res_min
        return res_max if res_circular == 0 else max(res_max, res_circular)