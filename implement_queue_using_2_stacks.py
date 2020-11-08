## Implement Queue using 2 stack

class QueueStack():
    def __init__(self):
        self.item1 = []
        self.item2 = []

    def enqueue(self, item):
        self.item1.append(item)

    def dequeue(self):
        if not self.item2:
            while self.item1:
                self.item2.append(self.item1.pop())
        return self.item2.pop()


queue_stack = QueueStack()

for i in range(5):
    queue_stack.enqueue(i)

for i in range(5):
    print(queue_stack.dequeue())
