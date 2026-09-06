class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        temp = []

        def backtrack(curr: int):
            if curr == target:
                nonlocal res
                res.add(tuple(sorted(temp)))
                return
            
            for cand in candidates:
                if curr + cand <= target:
                    temp.append(cand)
                    backtrack(curr+cand)
                    temp.pop()

        backtrack(0)
        return list(res)

