# Write your test here
import pytest 

from challenge01 import TreeNode ,summation
# test k=3
def test1():
    k=3
    tree1 = TreeNode()
    T=tree1.sortedArrayToBST([7,2,9,1,5,14])
    assert summation(T,k) == True

# test k=4
def test2():
    k=4
    tree1 = TreeNode()
    T=tree1.sortedArrayToBST([7,2,9,1,5,14])
    assert summation(T,k) == True

# test k=22
def test3():
    k=22
    tree1 = TreeNode()
    T=tree1.sortedArrayToBST([7,2,9,1,5,14])
    assert summation(T,k) == False