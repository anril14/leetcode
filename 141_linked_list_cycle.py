from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_pointer = head
        slow_pointer = head
        # print(f'fast: {fast_pointer.val} slow: {slow_pointer.val}')
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            # print(f'fast: {fast_pointer.val} slow: {slow_pointer.val}')
            if fast_pointer == slow_pointer:
                return True
        return False

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

solution = Solution()
print(solution.hasCycle(node1))