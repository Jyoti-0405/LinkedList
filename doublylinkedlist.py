class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def addathead(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        NewNode.prev = None
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
        
    def addattail(self, newdata):
        NewNode = Node(newdata)
        last = self.head
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        while last.next is not None:
            last = last.next
        last.next = NewNode
        NewNode.prev = last
    def addatindex(self, prev_node, newdata):
        if prev_node is None:
            print("Node not available")
        NewNode = Node(newdata)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode
    def get(self):
        printval = self.head
        while(printval is not None):
            print(printval.data)
            printval = printval.next
    def deleetatindex(self, node_D):
        if node_D is None:
            print("Cannot be deleted")
        if self.head == node_D:
            self.head = node_D
        while node_D is not None:
            node_D.prev.next = node_D.next
            node_D.next.prev = node_D.prev
            return 
        
        
list1 = LinkedList()
print("Doubly Linked List:")
list1.addathead(12)
list1.addattail(13)
list1.addatindex(list1.head.next, 14)
list1.deleetatindex(list1.head.next)
list1.get()

