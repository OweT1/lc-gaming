class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        if nums1 == nums2: return 0

        diffs = [abs(n1-n2) for n1, n2 in zip(nums1, nums2) if n1 != n2]
        prefix = [0]*max(diffs)

        for diff in diffs:
            prefix[diff-1] += 1

        k = k1 + k2
        i = len(prefix)-1

        while i >= 0 and k > 0:
            to_minus = min(prefix[i], k)
            prefix[i] -= to_minus
            if i > 0: prefix[i-1] += to_minus
            k -= to_minus
            i -= 1

        return sum([i**2 * num for i, num in enumerate(prefix, start=1)])