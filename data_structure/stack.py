class MinStack:
    """
    stack which supports push, pop, top, and retrieving the minimum element in constant time
    """
    __slot__ = ('stack', 'min',)

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0:
            self.min.append(len(self.stack) - 1)
        else:
            top_idx = self.min[-1]
            if self.stack[top_idx] >= val:
                self.min.append(len(self.stack) - 1)

    def pop(self) -> None:
        top_idx = len(self.stack) - 1
        self.stack.pop()
        while self.min and self.min[-1] == top_idx:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min[-1]]
