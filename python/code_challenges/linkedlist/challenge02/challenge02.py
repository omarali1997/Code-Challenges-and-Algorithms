# Node class
class Node:
    
    # Function to initialise the node object
    def __init__(self, value):
        self.value = value  
        self.next = None  
    
# Linked List class
class LinkedList:
    
    def __init__(self):
        self.head = None
  
    # Function to insert a new node at the beginning 
    def append(self, new_value): 
        new_node = Node(new_value) 
        new_node.next = self.head 
        self.head = new_node
  
    # Print the linked list
    def printAll(self):
        node = self.head
        l=[]
        while node:
            l.append(node.value)
            node = node.next
        return l
    
    #  Function to get the middle of the linked list
    
    def printMiddle(self):
        l2=[]
        l3=[]
        count = 0
        mid = self.head
        heads = self.head
        while(heads != None):
            l2.append(heads.value)

        # Update mid, when 'count' is odd number

            if count&1:
                mid = mid.next
            count += 1
            heads = heads.next

        # If empty list is provided
        
        for i in l2:
            if i == mid.value:
                l3.append(mid.value)
                l3.append(mid.next.value)
                mid1 = mid.next
                l3.append(mid1.next.value)

        return(l3)


  
# Code execution starts here
if __name__=='__main__':
    
    # Start with the empty list
    llist = LinkedList()
    
    for i in range(5, 0, -1):
        llist.append(i)
    # llist.append(5)
    # llist.append(4)
    # llist.append(3)
    # llist.append(2)
    # llist.append(1)
    print(llist.printAll())
    print(llist.printMiddle())

    
    llist = LinkedList()
    for i in range(6, 0, -1):
        llist.append(i)
    # llist.append(5)
    # llist.append(4)
    # llist.append(3)
    # llist.append(2)
    # llist.append(1)
    print(llist.printAll())
    print(llist.printMiddle())
    

  
