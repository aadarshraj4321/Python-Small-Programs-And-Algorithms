

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LL:
    def mergeLL(self, head1, head2):
        fh = Node(3)
        ft = fh
        while(head1 is not None and head2 is not None):
            if(head1.data < head2.data):
                ft.next = head1
                ft = ft.next
                head1 = head1.next
            else:
                ft.next = head2
                ft = ft.next
                head2 = head2.next
        while(head1 is not None):
            ft.next = head1
            ft = ft.next
            head1 = head1.next
        while(head2 is not None):
            ft.next = head2
            ft = ft.next
            head2 = head2.next
        return fh.next
            
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
            print(head.data, "-->", end = " ")
            head = head.next
        print("None")
        return


node = LL()
head1 = node.takeInput()
head2 = node.takeInput()
node.printLL(head1)
node.printLL(head2)
newHead = node.mergeLL(head1, head2)
node.printLL(newHead)
