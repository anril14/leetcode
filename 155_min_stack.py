class MinStack():

    def __init__(self):
        self.stack = list()
        self.min = list()

    def push(self, val: int) -> None:
        if not self.stack:
            self.min.append(val)
        else:
            if val <= self.getMin():
                self.min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[len(self.stack) - 1] == self.min[len(self.min)-1]:
            self.min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min[len(self.min)-1]


# Your MinStack object will be instantiated and called as such:

obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.getMin())
