# Write here the code challenge solution

# create node class
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init_(self):
        self.root = None

    # function that takes a Binary Search tree and an integer as a parameter. Return True if Binary search tree has two elements that their summation is the given integer
    def summation(self, k):
        if not self.root:
            return False
        x, y = [self.root], set()
        for i in x:
            if k - i.value in y:
                return True
            y.add(i.value)
            if i.left:
                x.append(i.left)
            if i.right:
                x.append(i.right)
        return False


# to try the function it work
if __name__ == "__main__":

    tree1 = Tree()
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

    tree1.root = node1

    # should return True
    tree1.summation(3)
    z = tree1.summation(3)
    print(z)

    # should return false
    tree1.summation(4)
    z = tree1.summation(4)
    print(z)