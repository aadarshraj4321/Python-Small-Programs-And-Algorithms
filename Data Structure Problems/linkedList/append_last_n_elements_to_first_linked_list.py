

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LL:

    def appendValLL(self, head, val):
        if(val == 0):
            return None
        pos = self.lengthLL(head) - val
        curr = head
        prev = head
        for i in range(1, pos):
            curr = curr.next
        last = curr
        tmp = curr.next
        head = tmp
        while(curr.next != None):
            curr = curr.next
        curr.next = prev
        last.next = None
        return head
    
    def lengthLL(self, head):
        count = 0
        while(head != None):
            count += 1
            head = head.next
        return count
    
    def takeInput(self):
        userInput = [int(ele) for ele in input().split()]
        head = None
        tail = None
        for val in userInput:
            if(val == -1):
                break
            newNode = Node(val)
            if(head is None):
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
        return head

    def printLL(self, head):
        while(head != None):
            print(head.data, "--->", end = " ")
            head = head.next
        print("None")
        return

node = LL()
head = node.takeInput()
node.printLL(head)
head = node.appendValLL(head, 3)
node.printLL(head)
