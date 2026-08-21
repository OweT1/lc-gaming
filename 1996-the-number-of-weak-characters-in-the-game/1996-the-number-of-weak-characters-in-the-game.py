class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        stack = []
        res = 0
        for a, d in sorted(properties, key=lambda x: (x[0], -x[1])):
            while stack and stack[-1] < d:
                res += 1
                stack.pop()
            stack.append(d)
        return res
