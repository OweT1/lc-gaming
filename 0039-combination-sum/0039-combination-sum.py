class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []

        def backtrack(i: int, curr: int):
            if i >= len(candidates) or curr > target: return
            if curr == target:
                nonlocal res
                res.append(temp.copy())
                return
            
            temp.append(candidates[i])
            backtrack(i, curr + candidates[i])
            temp.pop()
            backtrack(i+1, curr)
        
        backtrack(0, 0)
        return res

