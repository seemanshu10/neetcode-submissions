class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, i: int) -> int:
        curr = self.head
        index = 0

        while curr:
            if index == i:
                return curr.val
            curr = curr.next
            index += 1

        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if self.tail is None:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def remove(self, i: int) -> bool:
        if self.head is None:
            return False

        # Remove head
        if i == 0:
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return True

        prev = self.head
        curr = self.head.next
        index = 1

        while curr:
            if index == i:
                prev.next = curr.next

                if curr == self.tail:
                    self.tail = prev

                return True

            prev = curr
            curr = curr.next
            index += 1

        return False

    def getValues(self):
        values = []
        curr = self.head

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values