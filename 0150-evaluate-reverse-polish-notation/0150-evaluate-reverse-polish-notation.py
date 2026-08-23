class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        
        for token in tokens:
            if token in ops:
                e2, e1 = stack.pop(), stack.pop()
                res = None
                match token:
                    case '+': res = e1 + e2
                    case '-': res = e1 - e2
                    case '*': res = e1 * e2
                    case '/': res = int(e1 / e2)
                stack.append(res) 
            else:
                stack.append(int(token))
        return stack.pop()
        