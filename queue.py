class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def display(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def dequeue(self):
        head = self.queue[0]
        self.queue.remove(head)
        return head
