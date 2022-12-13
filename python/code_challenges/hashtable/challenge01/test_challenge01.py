# Write your test here
from challenge01 import Tree, Node
import pytest 

#build the tree
tree = Tree()
node1 = Node(7)
node2 = Node(2)
node3 = Node(9)
node4 = Node(1)
node5 = Node(5)
node6 = Node(14)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
tree.root = node1

# test k=3
def test1():
    z = tree.summation(3)
    assert z == True

# test k=4
def test2():
    z = tree.summation(4)
    assert z == False

# test k=5
def test3():
    z = tree.summation(5)
    assert z == False