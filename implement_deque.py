## Implement Deque

class Deque():
    def __init__(self):
        self.item = []

    # Check deque is empty or not
    def isEmpty(self):
        return self.item == []

    # push data from front
    def FrontPush(self, item):
        self.item.append(item)

    # push data from rear
    def RearPush(self, item):
        self.item.insert(0, item)

    # pop(remove) the data from front deque
    def FrontPop(self):
        return self.item.pop()

    # pop(remove) the data from rear deque
    def RearPop(self):
        return self.item.pop(0)

    # Check size of deque
    def size(self):
        return len(self.item)


deque = Deque()

# Check deque is empty or not
print(deque.isEmpty())

# push the data from FrontPush
deque.FrontPush(20)

# push the data from RearPush
deque.RearPush(21)

# Check size of deque
print(deque.size())

# pop data from RearPop and FrontPop
print(deque.RearPop(), deque.FrontPop())

# Now check deque is empty or not
print(deque.isEmpty())


