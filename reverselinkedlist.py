class Node:
    def __init__(self, data= None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode

    def reverselinkedlist(self):
        prev = None
        curr = self.head
        while(curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def printlist(self):
        printval = self.head
        while(printval is not None):
            print(printval.data)
            printval = printval.next
            break

list1 = LinkedList()
list1.push(23)
list1.push(6)
list1.push(15)
print("\nlist before reversing:")
list1.printlist()
list1.reverselinkedlist()
print("list after reversing:")
list1.printlist()