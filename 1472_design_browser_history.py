class ListNode:
    def __init__(self, url):
        self.url = str(url)
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.left = ListNode(homepage)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.current = self.left

    def visit(self, url: str) -> None:
        new_site = ListNode(url)
        new_site.next = self.right
        self.current.next = new_site
        self.right.prev = new_site
        new_site.prev = self.current
        self.current = new_site

    def back(self, steps: int) -> str:
        while self.current != self.left and steps != 0:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps: int) -> str:
        while self.current != self.right.prev and steps != 0:
            self.current = self.current.next
            steps -= 1
        return self.current.url

obj = BrowserHistory('leetcode.com')

obj.visit('vk.com')
obj.visit('aboba.com')
obj.visit('youtube.com')
obj.visit('gmail.com')

# param_2 = obj.back(2)
# print(param_2)
# param_2 = obj.back(3)
# print(param_2)

print('\n\n')
param_2 = obj.back(2)
print(param_2)
param_3 = obj.forward(1)
print(param_3)

# param_3 = obj.forward(steps)