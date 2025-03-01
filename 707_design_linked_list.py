class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self,):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i=0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.head.next
        self.head.next = new_head
        if self.tail == self.head:
            self.tail = self.head.next

    def addAtTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        curr = self.head
        i = -1
        while curr:
            if i == index-1:
                if not curr.next:
                    self.addAtTail(val)
                    return
                else:
                    new_node.next = curr.next
                    curr.next = new_node
                    return
            curr = curr.next
            i+=1
        return

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        i = -1
        while curr:
            if i == index-1:
                if curr.next:
                    if not curr.next.next:
                        curr.next = None
                        return
                    else:
                        curr.next = curr.next.next
                        curr.next.next = None
                        return
                else:
                    return
            curr = curr.next
            i += 1
        return

obj = MyLinkedList()
obj.deleteAtIndex(0)

# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(0,2)
#
# print(obj.get(0))
# print(obj.get(1))
# print(obj.get(2))

# obj.deleteAtIndex(0)
# print(obj.get(0))

# obj.addAtTail(1)
# obj.addAtTail(2)
# obj.addAtTail(3)
#
# obj.addAtIndex(3,4)
#
# print(obj.get(0))
# print(obj.get(1))
# print(obj.get(2))
# print(obj.get(3))
#
# obj.deleteAtIndex(0)
# obj.deleteAtIndex(0)
#
# print(obj.get(0))