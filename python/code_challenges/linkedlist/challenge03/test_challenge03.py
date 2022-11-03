# Write your test here
from challenge03 import LinkedList, Node
#  test 1
def test1():
    l = LinkedList()
    l.append(1)
    l.deleteNthNodeFromEnd(l.head, 1)
    actual = l.printAll()
    expected = []
    assert actual == expected

#  test 2
def test2():
    l = LinkedList()
    l.append(2)
    l.append(1)
    l.deleteNthNodeFromEnd(l.head, 1)
    actual = l.printAll()
    expected = [1]
    assert actual == expected


#  test 3
def test3():
    l = LinkedList()
    l.append(5)
    l.append(4)
    l.append(3)
    l.append(2)
    l.append(1)
    l.deleteNthNodeFromEnd(l.head, 1)
    actual = l.printAll()
    expected = [1,2,3,4]
    assert actual == expected

