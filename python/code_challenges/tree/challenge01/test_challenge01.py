# Write your test here

from challenge01 import buildTree,pre_order,TreeNode


def test1():
    tree=TreeNode()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    tree.root = buildTree( preorder, inorder)
    assert pre_order([],tree.root)==[3,9,20,15,7]



def test2():
    tree=TreeNode()
    preorder = [-1]
    inorder = [-1]
    tree.root = buildTree( preorder, inorder)
    assert pre_order([],tree.root)== [-1]