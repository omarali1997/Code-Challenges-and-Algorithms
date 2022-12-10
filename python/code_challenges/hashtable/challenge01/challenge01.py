# Write here the code challenge solution

# create node class
class TreeNode():
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    # create function that sorted Array To BST
    def sortedArrayToBST(self,num):
        num.sort()
        def BST_Tree(nums):
            if not nums:
                return None                                          
            m = len(nums)//2
            return (TreeNode(nums[m],BST_Tree(nums[:m]),BST_Tree(nums[m+1:])) )
        root=BST_Tree(num)
        return root


# pre order function
def pre_order(root , x):
    if root is not None:
        x.append(root.value)
    if root.left is not None:
        pre_order(root.left , x)
    if root.right is not None:
        pre_order(root.right , x)
    return x





# function that takes a Binary Search tree and an integer as a parameter. Return True if Binary search tree has two elements that their summation is the given integer
def summation(root,k):
    x = pre_order(root,[])
    for i in range(len(x)):
        if (x[i] - k ) not in x:
            continue
        else:
            return True
    else:
        return False

# to try the function it work 

if __name__ == "__main__":

    tree = TreeNode()
    T=tree.sortedArrayToBST([7,2,9,1,5,14])
    print(summation(T,4))
    

