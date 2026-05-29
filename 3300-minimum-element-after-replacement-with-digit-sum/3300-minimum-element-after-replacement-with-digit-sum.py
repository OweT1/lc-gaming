class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_ele = math.inf
        for num in nums:
            t = 0
            while num > 0:
                t += num % 10
                num //= 10
            min_ele = min(min_ele, t)
        return min_ele
        