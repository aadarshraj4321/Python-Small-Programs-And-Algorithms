
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LL:
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
    
    def isPalindrome(self, head):
        length = 0
        curr = head
        while(curr != None):
            length += 1
            curr = curr.next
        left = head
        for i in range(length // 2):
            right = head
            for j in range(length - i - 1):
                right = right.next
            if(left.data != right.data):
                return False
            left = left.next
        return True

    def printLL(self, head):
        while(head != None):
            print(head.data, "--->", end = " ")
            head = head.next
        print("None")
        return



node = LL()
head = node.takeInput()
node.printLL(head)
print(node.isPalindrome(head))
