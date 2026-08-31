class MinStack:

    def __init__(self):
        self.curr_stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.curr_stack.append(value)
        self.min_stack.append(value) if not self.min_stack else self.min_stack.append(min(self.min_stack[-1], value))

    def pop(self) -> None:
        self.curr_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.curr_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()