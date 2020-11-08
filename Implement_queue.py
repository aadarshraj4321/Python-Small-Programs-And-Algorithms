## Implement Queue

class Queue():
    def __init__(self):
        self.item = []

    # Check queue is empty or not
    def isEmpty(self):
        return self.item == []

    # Enqueue data in queue
    def Enqueue(self, item):
        self.item.insert(0, item)

    # Dequeue(remove) the data from queue
    def Dequeue(self):
        return self.item.pop()

    # Check size of queue
    def size(self):
        return len(self.item)



queue = Queue()

#Check queue is empty or not
print(queue.isEmpty())

# Enqueue some data in queue
queue.Enqueue("Hello")
queue.Enqueue("World")

# Check size of queue
print(queue.size())

# Dequeue(remove) data from queue
print(queue.Dequeue() + " " + queue.Dequeue())
