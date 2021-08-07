class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.headA= None
        self.headB= None
    
    def intersection(self):
        pA = self.headA
        pB = self.headB
        while pA != pB:
            pA = self.headB if pA is None else pA.next
            pB = self.headA if pB is None else pB.next
            break

        return pA.data
            

list = LinkedList()
list.headA = Node(4)
list.headA.next = Node(1)
list.headA.next.next = Node(8)
list.headA.next.next.next = Node(4)
list.headA.next.next.next.next = Node(5)
list1 = LinkedList()
list1.headB = Node(5)
list1.headB.next = Node(6)
list1.headB.next.next = Node(9)
list1.headB.next.next.next = Node(8)
list1.headB.next.next.next.next = Node(4)
list1.headB.next.next.next.next.next = Node(5)
print(list.intersection())








