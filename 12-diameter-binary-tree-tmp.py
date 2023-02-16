# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any 
# two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of 
# edges between them.
# 
# Example: 
#               1
#            /     \
#           2       3
#         /   \   
#        4     5
# 
# Answer: 3 (the path from 4 -> 2 -> 1 -> 3)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        return 0
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s =  Solution()
print(s.diameterOfBinaryTree(root))