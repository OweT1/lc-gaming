class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, temp = [], []
        to_visit = set(nums)
        def bfs(i, to_visit):
            if i == len(nums):
                res.append(temp.copy())
                return
            
            for n in nums:
                if n in to_visit:
                    temp.append(n)
                    to_visit.remove(n)
                    bfs(i+1, to_visit)

                    temp.pop()
                    to_visit.add(n)

        bfs(0, to_visit)
        return res
