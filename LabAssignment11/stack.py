class Stack:
    """
    Simple stack (LIFO) implementation.

    Methods
    -------
    push(item): Add item to top
    pop(): Remove and return top item
    peek(): Return top item without removing
    is_empty(): Check if stack is empty
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0
s = Stack()
s.push(10)
s.push(20)
print(s.peek())    # 20
print(s.pop())     # 20
print(s.pop())     # 10
print(s.is_empty())  # True
