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
    vstack = list()

    vstack.append(root)

    while len(vstack) > 0:
        cur = vstack.pop(0)
        if cur == None:
            slist.append(None)
        else:
            slist.append(cur.value)
            vstack.append(cur.left)
            vstack.append(cur.right)

    return slist

def deserialize(slist):
    vstack = list()
    root_val = slist.pop(0)
    root = Node(root_val)
    vstack.append(root)

    while len(vstack) > 0:
        cur = vstack.pop(0)
        cur_left_val = slist.pop(0)
        cur_right_val = slist.pop(0)

        if(cur_left_val != None):
            cur.left = Node(cur_left_val)
            vstack.append(cur.left)

        if(cur_right_val != None):
            cur.right = Node(cur_right_val)
            vstack.append(cur.right)

    return root


# You need some way to compare if the two trees are the same
def compare_trees(root1, root2):
    if root1 == None and root2 == None:
        return True
    elif root1 == None or root2 == None: 
        return False
    elif root1.value != root2.value: 
        return False
    
    return compare_trees(root1.left, root2.left) \
            and compare_trees(root1.right, root2.right)  


# The next functions are not strictly necessary to solve the problem
# but they are needed to verify that the tree has been reconstructed
# correctly. 
def find_depth_r(root, depth):
    if root == None:
        return depth
    left_max_depth = find_depth_r(root.left, depth+1)
    right_max_depth = find_depth_r(root.right, depth+1)

    if left_max_depth > right_max_depth:
        return left_max_depth
    else:
        return right_max_depth

def find_depth(root):
    return find_depth_r(root, 0)


def fill_sub_tree(root, level, index, width, matrix):
    if root == None:
        return
    matrix[level][index] = root.value
    fill_sub_tree(root.left, level+1, index - (width//2), width//2, matrix)
    fill_sub_tree(root.right, level+1, index + (width//2), width//2, matrix)


def print_tree (root):
    depth = find_depth(root)
    m_width = 2*(2**(depth-1)) - 1
    matrix = [[" " for _ in range(m_width)] for _ in range(depth)]

    t_width = 2**(depth-1)

    fill_sub_tree(root, 0, m_width//2, t_width, matrix)

    for i in range(depth):
        for j in range (m_width):
            print(matrix[i][j], end="")
        print()
    return

# Build the Tree
#                 6
#              /     \
#             /       \
#           3          8 
#         /   \      /   \
#        1     4    7     9 
#          \    \
#            2    5
#
root = Node(6)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(7)
root.right.right = Node(9)
root.left.left.left = None
root.left.left.right = Node(2)
root.left.right.left = None
root.left.right.right = Node(5) 
root.right.left.left = None
root.right.left.right = None

slist = serialize(root)
print(slist)
print_tree(root)

root2 = deserialize(slist)
print_tree(root2)

print("Compare Trees: {}".format(compare_trees(root, root2)))
print("-----------")


# Build the Tree
#                 3
#              /     \
#             /       \
#           2          4 
#         /              \
#        1                5
#                          \
#                           6
#                            \
#                             7 
#                
#                  
#
root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = None
root.right.left = None
root.right.right = Node(5)
root.right.right.right = Node(6)
root.right.right.right.right = Node(7)

print_tree(root)
slist = serialize(root)
print(slist)

root2 = deserialize(slist)
print_tree(root2)

print("Compare Trees: {}".format(compare_trees(root, root2)))
print("-----------")

# Build the Tree
#                 3
#                    \
#                     \
#                      4 
#                        \
#                         5
#                          \
#                           6
#                            \
#                             7 
#                              \
#                               8
#                                \
#                                 9
#                
root = Node(3)
root.right = Node(4)
root.right.right = Node(5)
root.right.right.right = Node(6)
root.right.right.right.right = Node(7)
root.right.right.right.right.right = Node(8)
root.right.right.right.right.right.right = Node(9)

print_tree(root)
slist = serialize(root)
print(slist)

root2 = deserialize(slist)
print_tree(root2)

print("Compare Trees: {}".format(compare_trees(root, root2)))
print("-----------")
