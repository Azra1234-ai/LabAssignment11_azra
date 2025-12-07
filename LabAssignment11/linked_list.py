class Node:
    """A node of the singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    """
    Singly Linked List implementation.

    Methods
    -------
    insert_at_beginning(value): Insert node at the start
    insert_at_end(value): Insert node at the end
    display(): Return list of values
    """

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values
ll = SinglyLinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_beginning(5)
print(ll.display())
