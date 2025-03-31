from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        a_head = head
        if head.next:
            a_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return a_head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
solution = Solution()

print(solution.reverseList(node1))

# cur = node1
# while cur.next is not None:
#     print(cur.val, '-> ', end='')
#     cur=cur.next
# else:
#     print(cur.val)
