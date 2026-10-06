class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        stack = []
        for c in s:
            if c == '(': stack.append(c)
            else: # c is ')'
                if stack and stack[-1] == '(': stack.pop()
                else: res += 1
        return res + len(stack)