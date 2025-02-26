from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next

node1 = ListNode(val = 1)
node2 = ListNode(val = 2)
node3 = ListNode(val = 3)

node1.next = node2
node2.next = node3

node4 = ListNode(val = 4)
node5 = ListNode(val = 5)
node6 = ListNode(val = 6)

node4.next = node5
node5.next = node6

solution = Solution()
merged = solution.mergeTwoLists(list1 = node1,list2 = node2)

def print_linked_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

print_linked_list(merged)