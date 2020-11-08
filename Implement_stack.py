## Implement Stack From Scratch


class Stack():
    def __init__(self):
        self.item = []

    # Check Stack Is Empty Or Not
    def isEmpty(self):
        return self.item == []

    # Push Data 
    def push(self, item):
        self.item.append(item)

    # Pop Data
    def pop(self):
        return self.item.pop()

    def peek(self):
        # return self.item[-1]
        return self.item[len(self.item)-1]

    # Check size of stack
    def size(self):
        return len(self.item)


stack = Stack()

# Check stack is empty or not
print(stack.isEmpty())

# push some int and string in stack
stack.push("Hello Data!")
stack.push(4)

# check now stack is empty or not
print(stack.isEmpty())

# check size of stack
print(stack.size())

print("------")
print(stack.peek())
print("------")

# pop(remove) data from stack
stack.pop()
stack.pop()

# now again check stack is empty or not and size of stack
print(stack.isEmpty())
print(stack.size())
