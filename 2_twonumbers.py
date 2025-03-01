from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        curr = l3
        over10 = 0
        while l1 or l2 or over10:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            curr.next = ListNode((val1 + val2 + over10) %10)
            if val1 + val2 + over10 > 9:
                over10 = 1
            else:
                over10 = 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            print(curr.next.val)
            curr = curr.next
        return l3.next

node3 = ListNode(9)
node2 = ListNode(6, node3)
node1 = ListNode(4, node2)

node6 = ListNode(4)
node5 = ListNode(6, node6)
node4 = ListNode(3, node5)

solution = Solution()
print(solution.addTwoNumbers(node1, node4))