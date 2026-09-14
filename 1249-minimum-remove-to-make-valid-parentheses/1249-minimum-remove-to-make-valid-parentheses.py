class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        open_p = []
        for i, c in enumerate(s):
            if c == '(':
                open_p.append(i)
            elif c == ')':
                if open_p:
                    open_p.pop()
                else:
                    stack.append("")
                    continue
            stack.append(c)
        for i in open_p:
            stack[i] = ""
        return "".join(stack)