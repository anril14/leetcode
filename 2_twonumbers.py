from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print(l1.reverse())

solution = Solution()
print(solution.addTwoNumbers([1, 2, 3], [1, 2, 3, 4]))
#unfinished