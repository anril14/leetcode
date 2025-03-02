import collections

class MyStack:

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[len(self.queue)-1]

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False

obj = MyStack()
obj.push(1)
obj.push(2)

param_2 = obj.pop()
print(param_2)
param_3 = obj.top()
print(param_3)
param_4 = obj.pop()
print(param_4)

# param_3 = obj.top()
# print(param_3)

param_5 = obj.empty()
print(param_5)