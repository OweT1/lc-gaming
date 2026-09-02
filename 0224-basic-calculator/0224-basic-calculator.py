class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        temp = []
        curr_num = ""
        for c in "(" + s + ")":
            if c == ' ': continue
            elif c == ')':
                if curr_num:
                    stack.append(curr_num)
                    curr_num = ""

                while stack:
                    ele = stack.pop()
                    if ele == '(': break
                    temp.append(ele)

                while temp and len(temp) >= 3:
                    e1 = temp.pop()
                    if e1 == "-":
                        e1 += temp.pop()
                        if e1[:2] == '--': e1 = e1[2:]
                    op = temp.pop()
                    e2 = temp.pop()

                    if op == "+":
                        temp.append(str(int(e1) + int(e2)))
                    elif op == "-":
                        temp.append(str(int(e1) - int(e2)))
                    else:
                        raise ValueError("Unknown op {}", op)
                
                stack.append("".join(temp[::-1]))
                temp = []

            elif c in set(['-', '+', '(']):
                if curr_num:
                    stack.append(curr_num)
                    curr_num = ""
                stack.append(c)
            else: # c is a number
                curr_num += c
        return int(stack.pop())
            