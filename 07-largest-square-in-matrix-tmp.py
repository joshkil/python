# Find the largest square in a 2D Matrix 
#
# You are given a 2D binary matrix as an input. The 1's in the matrix
# mark squares inside the matrix. A single 1 is a square of dimension
# 1X1 (one-by-one). Find the largest square and return it's N where NXN
# is the size of the largest square. 
#
# Examples: 
# Input: 
#    [0,0,0,0,0,0]
#    [0,1,1,0,0,0]
#    [0,1,1,1,0,0]
#    [0,1,1,1,0,0]
#    [0,1,1,1,0,0]
#
# Output: 3 (largest square has top-left corner in third row, second column)

def max_square(matrix):
        return 0

# Clean Sample Matrix
matrix1 = [
    [0,0,0,0,0,0],
    [0,1,1,0,0,0],
    [0,1,1,1,0,0],
    [0,1,1,1,0,0],
    [0,1,1,1,0,0]
]

print("Largest island is {N} by {N} (expect 3 by 3)".format(N = max_square(matrix1)))