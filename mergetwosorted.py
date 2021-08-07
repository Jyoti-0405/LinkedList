class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        

    def mergetwoSorted(self,headA, headB):
        temp = None
        if headA is None:
            return headB
        if headB is None:
            return headA
        if headA.data <= headB.data:
            temp = headA
            temp.next = mergetwoSorted(headA.next, headB)
        else:
            temp = headB
            temp.next = mergetwoSorted(headA, headB.next)
        return temp


    def printlist(self):
        printval = self.headA
        while(printval is not None):
            print(printval.data)
            printval = printval.next
if __name__ == "__main__":
    list1 = LinkedList()
    list1.headA = Node(1)
    list1.headA.next = Node(2)
    list1.headA.next.next = Node(3)
    list2 = LinkedList()
    list2.headB = Node(1)
    list2.headB.next = Node(3)
    list2.headB.next.next = Node(4)
    list3 = LinkedList()
    list3.head = mergetwoSorted(list1.head, list2.head)
    print("After Merge")
    list3.printlist()


