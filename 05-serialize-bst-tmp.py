# Serialize and Deserialize a Binary Search Tree
#
# Given a binary tree of integers, write code to store the tree into 
# a list of integers (i.e. serialize) and recreate the original tree 
# from a list of integers (i.e. deserialize). This means that 
# deserialize(serialize(root)) should return the exact same binary tree.

# Node Class
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def serialize(root):
    slist = list()
    return slist

def deserialize(slist):
    root = Node(None)
    return root

root = Node(None)
slist = serialize(root)
print(slist)

root2 = deserialize(slist)
print(root2)