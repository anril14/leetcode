from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

print(Solution.mergeTwoLists([node1, node2, node3], [node4, node5, node6]))
#unfinished