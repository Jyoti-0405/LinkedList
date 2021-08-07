class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def printlist(self):
        printval = self.head
        while(printval != None):
            print(printval.data)
            printval = printval.next
    
    def removefromindex(self, n):
        fast = slow = self.head
        for i in range(n):
            if(fast.next ==None):
                if i ==n-1:
                    self.head = self.head.next
                return self.head
            fast = fast.next
        while(fast.next != None):
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
            

list = LinkedList()
list.head = Node(12)
list.head.next = Node(13)
list.head.next.next = Node(14)
list.head.next.next.next = Node(15)
list.head.next.next.next.next = Node(16)
print("\nlist before deletion")
list.printlist()
list.removefromindex(2)
print("list after deletion")
list.printlist()




