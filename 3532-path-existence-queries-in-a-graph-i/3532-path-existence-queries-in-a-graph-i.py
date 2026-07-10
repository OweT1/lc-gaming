class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component_groups = [1]*n

        for i in range(1, n):
            component_groups[i] = component_groups[i-1] + (1 if nums[i] - nums[i-1] > maxDiff else 0)

        res = []
        for u, v in queries:
            res.append(component_groups[u] == component_groups[v])
 
        return res
             
        