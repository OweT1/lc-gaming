class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, temp = [], []
        to_visit = Counter(nums)
        def bfs(i, to_visit: dict):
            if i == len(nums):
                res.append(temp.copy())
                return
            
            for k, v in to_visit.items():
                if v > 0:
                    temp.append(k)
                    to_visit[k] -= 1
                    bfs(i+1, to_visit)

                    temp.pop()
                    to_visit[k] += 1

        bfs(0, to_visit)
        return res
        