class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        last_digit, seen = None, False

        while r < len(nums):
            nums[l] = nums[r]
            if last_digit is None or nums[r] != last_digit:
                last_digit = nums[r]
                seen = False
                l += 1
                r += 1
            else:
                if seen:
                    r += 1
                else:
                    l += 1
                    r += 1
                    seen = True
        return l