class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def pop(self):
        head = self.stack[-1]
        self.stack.remove(head)
        return head
