class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        cand1, cand2 = None, None
        cnt1, cnt2 = 0, 0

        for num in nums:
            if cand1 == num:
                cnt1 += 1
            elif cand2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                cand1 = num
                cnt1 += 1
            elif cnt2 == 0:
                cand2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        n = len(nums)
        threshold = n // 3
        return ([cand1] if nums.count(cand1) > threshold else []) + ([cand2] if nums.count(cand2) > threshold else [])