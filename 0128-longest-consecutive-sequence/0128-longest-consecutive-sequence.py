class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        visited = set()
        res = 0

        for num in nums_set:
            l, r = num - 1, num + 1
            while l in nums_set and l not in visited:
                visited.add(l)
                l -= 1
            visited.add(l)

            while r in nums_set and r not in visited:
                visited.add(r)
                r += 1
            visited.add(r)

            res = max(res, r-l-1)
        return res



        