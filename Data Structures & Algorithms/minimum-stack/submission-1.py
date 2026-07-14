class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.minval = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minval is None or val < self.minval:
            self.minval = val
        self.minstack.append(self.minval)


    def pop(self) -> None:
        if not self.stack and not self.minstack:
            return 0
        self.stack.pop()
        self.minstack.pop()
        if not self.minstack:
            self.minval = None
        else:
            self.minval = self.minstack[-1]

    def top(self) -> int:
        if not self.stack:
            return 0
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minstack:
            return 0
        return self.minval
