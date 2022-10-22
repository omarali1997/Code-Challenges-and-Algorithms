# Write here the code challenge solution


class Node:
    def __init__(self, value) :
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self) :
        self.head= None
    
    def append(self, node):
        if self.head is None:
            self.head=node
        else:
            current = self.head
            while current.next is not None :
                current = current.next
            current.next = node

    def printAll(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            current = self.head
            l=[]
            while current is not None :
                l.append(current.value)
                current = current.next
            return l


# class Delete:

    def delete_a_node(self,delno):

        current=self.head
        
        if current is not None:
            if(current.value == delno):
                self.head=current.next
                current=None
                return 

        while current is not None :
            if current.value == delno:
                break
            
            s = current
            current = current.next

        s.next = current.next
        current = None

        

        # if(current == None):
        #     return None

        if self.head is None:
            print("The linked list is empty")
        else:
            j=[]
            current = self.head
            while current is not None :
                j.append(current.value)
                current = current.next
            return j



if __name__=="__main__":
    linkedlist=LinkedList()
    node1=Node(4)
    node2=Node(5)
    node3=Node(1)
    node4=Node(9)

    linkedlist.append(node1)
    linkedlist.append(node2)
    linkedlist.append(node3)
    linkedlist.append(node4)
    print(linkedlist.printAll())
    n=int(input("input anything ==>  "))
    linkedlist.delete_a_node(n)
    print(linkedlist.printAll())


