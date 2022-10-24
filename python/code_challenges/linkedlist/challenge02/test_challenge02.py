# Write your test here
from challenge02 import LinkedList

def test1():
    llist = LinkedList()

    for i in range(5, 0, -1):
        llist.append(i)

    print(llist.printAll())
    x=llist.printMiddle()
    actual = x
    expected = [3, 4, 5]
    assert actual == expected


def test2():
    llist = LinkedList()

    for i in range(6, 0, -1):
        llist.append(i)

    print(llist.printAll())
    x=llist.printMiddle()
    actual = x
    expected = [4, 5, 6]
    assert actual == expected