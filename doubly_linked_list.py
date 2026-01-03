from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node: ListNode):
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node

    def prepend(self, node: ListNode):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def find(self, value):
        current = self.head
        while current.next is not None:
            if current.next.val == value:
                return current.next
            current = current.next
        return None

    def remove(self, value):
        node = self.find(value)
        if node is None:
            return None

        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = None
        node.prev = None

        return node.val


linked_list = DoublyLinkedList()
linked_list.append(ListNode(4))

print(linked_list.tail.prev.val)
print(linked_list.head.next.val)

linked_list.prepend(ListNode(3))

print(linked_list.head.next.val)

print(linked_list.remove(3))
print(linked_list.head.next.val)
