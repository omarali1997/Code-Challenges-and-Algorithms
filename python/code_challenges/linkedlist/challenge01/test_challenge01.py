# Write your test here

from challenge01 import Node,LinkedList



def test1():
    linkedlist=LinkedList()
    node1=Node(4)
    node2=Node(5)
    node3=Node(1)
    node4=Node(9)

    linkedlist.append(node1)
    linkedlist.append(node2)
    linkedlist.append(node3)
    linkedlist.append(node4)
    actual = linkedlist.delete_a_node(5)
    expected = [4,1,9]
    assert actual == expected

def test2():
    linkedlist=LinkedList()
    node1=Node(4)
    node2=Node(5)
    node3=Node(1)
    node4=Node(9)

    linkedlist.append(node1)
    linkedlist.append(node2)
    linkedlist.append(node3)
    linkedlist.append(node4)
    actual = linkedlist.delete_a_node(1)
    expected = [4,5,9]
    assert actual == expected
    

def test4():
    linkedlist=LinkedList()
    node1=Node(4)
    node2=Node(5)
    node3=Node(1)
    node4=Node(9)
    linkedlist.append(node1)
    linkedlist.append(node2)
    linkedlist.append(node3)
    linkedlist.append(node4)
    actual = linkedlist.delete_a_node(9)
    expected = [4,5,1]
    assert actual == expected