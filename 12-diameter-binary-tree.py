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
        max_diameter = 0
        def visit(root) -> int:
            if not root: 
                return 0
            nonlocal max_diameter
            # get maxDept L and R
            max_depth_l = visit(root.left)
            max_depth_r = visit(root.right)
            # aggregate to find max_diameter at this node
            # update nonlocal max_diameter
            max_diameter = max(max_diameter, max_depth_l+max_depth_r)
            # return max depth of this node from perspective of parent
            return max(max_depth_l, max_depth_r) + 1
        visit(root)
        return max_diameter
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s =  Solution()
print(s.diameterOfBinaryTree(root))