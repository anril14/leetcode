class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self,):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        head_node = ListNode(val)
        head_node.next = self.left.next
        head_node.prev = self.left
        self.left.next.prev = head_node
        self.left.next = head_node

    def addAtTail(self, val: int) -> None:
        head_node = ListNode(val)
        head_node.next = self.right
        head_node.prev = self.right.prev
        self.right.prev.next = head_node
        self.right.prev = head_node
        pass

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next

        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and index == 0:
            new_node = ListNode(val)
            new_node.next = curr
            new_node.prev = curr.prev
            curr.prev.next = new_node
            curr.prev = new_node
        return None

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next

        while curr.next and index > 0:
            curr = curr.next
            index -= 1

        if curr and (curr != self.right and curr != self.left) and index == 0:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr.next = None
            curr.prev = None
        return None

obj = MyLinkedList()

# obj.addAtHead(3)
# obj.addAtHead(2)
# obj.addAtHead(1)
#
# obj.addAtIndex(3,4)

obj.deleteAtIndex(0)
#
# print(obj.get(0))
# print(obj.get(1))
# print(obj.get(2))
# print(obj.get(3))

# obj.addAtTail(3)

# print(obj.get(0))
# print(obj.get(1))
# print(obj.get(2))

# obj.addAtTail(1)
# obj.addAtTail(2)
# obj.addAtTail(3)

# print(obj.get(0))
# print(obj.get(1))
# print(obj.get(2))
# print(obj.get(3))

# obj.deleteAtIndex(0)
# obj.deleteAtIndex(0)

# print(obj.get(0))