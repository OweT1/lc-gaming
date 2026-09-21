class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                ele = stack.pop()
                res[ele] = i-ele
            stack.append(i)
        return res
