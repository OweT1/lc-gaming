class Solution:
    def calculate(self, s: str) -> int:
        def is_op(c: str):
            return c in set(["+", "-", "*", "/"])
        
        # first pass - split numbers and ops into a stack
        stack1 = []
        curr = ""
        for c in s:
            if is_op(c):
                stack1.append(curr)
                stack1.append(c)
                curr = ""
            else:
                curr += c
        if curr: stack1.append(curr)

        # second pass - evaluate * and /
        stack2 = []
        op = None
        for e in stack1:
            if op is not None:
                n2 = e
                n1 = stack2.pop()
                if op == "*":
                    stack2.append(str(int(n1) * int(n2)))
                elif op == "/":
                    stack2.append(str(int(int(n1) / int(n2))))
                else:
                    raise ValueError(e, "is not a valid operator")
                op = None
            elif e == "*" or e == "/":
                op = e
            else:
                stack2.append(e)

        # third pass - evaluate + and -
        stack3 = []
        op = None
        for e in stack2:
            if op is not None:
                n2 = e
                n1 = stack3.pop()
                if op == "+":
                    stack3.append(str(int(n1) + int(n2)))
                elif op == "-":
                    stack3.append(str(int(n1) - int(n2)))
                else:
                    raise ValueError(e, "is not a valid operator")
                op = None
            elif e == "+" or e == "-":
                op = e
            else:
                stack3.append(e)
        return int(stack3[0])