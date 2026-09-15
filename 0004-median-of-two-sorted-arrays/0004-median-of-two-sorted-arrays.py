class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 == 0: return nums2[n2//2] if n2%2 else (nums2[n2//2-1] + nums2[n2//2])/2
        if n2 == 0: return nums1[n1//2] if n1%2 else (nums1[n1//2-1] + nums1[n1//2])/2
        total = n1 + n2
        half = (total + 1) // 2
        
        if n1 > n2: # nums1 will always be the smaller arr
            n1, n2 = n2, n1
            nums1, nums2 = nums2, nums1

        l, r = 0, n1
        while True:
            m1 = l + ((r-l) >> 1)
            m2 = half - m1 

            n1_ml = nums1[m1-1] if m1-1 >= 0 else -math.inf
            n1_mr = nums1[m1] if m1 < n1 else math.inf
            n2_ml = nums2[m2-1] if m2-1 >= 0 else -math.inf
            n2_mr = nums2[m2] if m2 < n2 else math.inf

            if n1_ml <= n2_mr and n2_ml <= n1_mr:
                if total % 2 == 1: return max(n1_ml, n2_ml)
                else: return (max(n1_ml, n2_ml) + min(n1_mr, n2_mr)) / 2
            elif n1_ml > n2_mr:
                r = m1 - 1
            else:
                l = m1 + 1

