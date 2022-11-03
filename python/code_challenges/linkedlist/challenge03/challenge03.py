# Write here the code challenge solution

# create Class node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
#  create class LinkedList 
class LinkedList:
    def __init__(self):
        self.head = None
    # Function to append to linkedlist
    def append(self, value):
        New_Node = Node(value)
        New_Node.next = self.head
        self.head = New_Node
    # function to print All nodes in linkedlist
    def printAll(self):
        lis=[]
        temp = self.head
        while temp != None:
            lis.append(temp.value)
            temp = temp.next
        return lis
    # function to delete Nth Node From End
    def deleteNthNodeFromEnd(self, head, n):
        fast = head
        slow = head
    
        for i in range(n):
            if fast.next is None:
                if i==(n-1):
                    self.head = self.head.next
                return self
            fast = fast.next  
        while fast.next:
            fast = fast.next
            slow = slow.next
    
        slow.next = slow.next.next
        return head
        
        
    

# to show the results
if __name__ == '__main__':
    l = LinkedList()
    l.append(5)
    l.append(4)
    l.append(3)
    l.append(2)
    l.append(1)
    print('***** Linked List Before deletion *****')
    print(l.printAll()
 )
    l.deleteNthNodeFromEnd(l.head, 1)
 
    print('*********** Linked List after Deletion *****')
    print(l.printAll())



    l = LinkedList()
    l.append(2)
    l.append(1)
    print('***** Linked List Before deletion *****')
    print(l.printAll())
 
    l.deleteNthNodeFromEnd(l.head, 1)
 
    print('*********** Linked List after Deletion *****')
    print(l.printAll())

    l = LinkedList()
    l.append(1)
    print('***** Linked List Before deletion *****')
    print(l.printAll())
 
    l.deleteNthNodeFromEnd(l.head, 1)
 
    print('*********** Linked List after Deletion *****')
    print(l.printAll())