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
# Output: 3 (largest square has top-left corner in third (3rd) row, second (2nd) column)

# An optimized dynamic programming approach to find the max square in a matrix
# for an NXN matrix, complexity is O(N^2)
def max_square(matrix):
    # declare variable to hold maximum square discovered
    max_size = 0

    # declare record-keeping matrix
    numrows = len(matrix)
    numcols = len(matrix[0])
    r = [[0]*numcols for i in range(numrows)]

    # step 1: initialize existing 1's
    for i in range (numrows):
        for j in range (numcols): 
            r[i][j] = matrix[i][j]

    # NOTE: We could have accomplished defining and initializing
    # the matrix 'r' with one line of Python list comprejension (below). I 
    # avoided this to make the code more clear for those less familiar with 
    # list comprehension. 
    #
    #    r = [[matrix[i][j] for j in range(numcols)] for i in range(numrows)]
    #

    for i in range (numrows):
        for j in range (numcols): 
            print(r[i][j], end=" ")
        print()
    print()

    # step 2: iterate over the matrix left to right, top to bottom
    #
    # As a visual, consider this 3X3 matrix, and imagine we are
    # processing the element marked 'o' at (2, 2). We need to evaluate
    # the values of indicies marked with 'x' to know the value of 'o'.
    # I call these, left, above, and diag (diagonal)
    # 
    #      0  1  2  
    #   0  _  _  _
    #   1  _  x  x
    #   2  _  x  o
    #
    for i in range (numrows):
        for j in range (numcols): 
            if r[i][j] == 1:
                # find values of 3 corners around this cell
                left  = 0 if (j-1 < 0) else r[i][j-1] 
                above = 0 if (i-1 < 0) else r[i-1][j]
                diag  = 0 if (i-1 < 0 or j-1 < 0) else r[i-1][j-1]
                r[i][j] = min(left, above, diag) + 1
                max_size = max(max_size, r[i][j])
    
    for i in range (numrows):
        for j in range (numcols): 
            print(r[i][j], end=" ")
        print()

    return max_size

def scan_border(matrix, i, j, dim):  # i: 2, j: 1, d 2
    i_bound = i+dim+1  # 5
    j_bound = j+dim+1  # 4
    if i_bound > len(matrix) or j_bound > len(matrix[0]):
         return False
    
    # scan rows at column j
    for r in range(i, i_bound, 1):
        if matrix[r][j] != 1:
            return False
    
    # scan columns at row i
    for c in range(j, j_bound, 1):
        if matrix[i][c] != 1:
            return False
    return True

# a recursive function to determine max size of square of 1's at a given
# (i,j) coordinate. Imagine the square's upper-left corner is at i,j 
# and we search to see if we can extend the square from there. 
def find_max_at_index(matrix, i, j):  
    if i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == 0:
        return 0
    else:
        left = find_max_at_index(matrix, i, j+1)
        below = find_max_at_index(matrix, i+1, j)
        diag = find_max_at_index(matrix, i+1, j+1)
        return min(left, below, diag) + 1

# A brute-force programming approach to find the max square in a matrix
# For NXN matrix, complexity is O(N^4)
def max_square_brute(matrix):
    # declare variable to hold maximum square discovered
    max_size = 0
    numrows = len(matrix)
    numcols = len(matrix[0])
    
    # As a visual, consider this 3X3 matrix, and imagine we are
    # processing the element marked 'o' at (0, 0). Think of 'o'
    # as the top left corner of a potential matrix. We will iteratively
    # test for a square of size 2, 3, .. etc up to size of matrix. 
    # For array of 2, we need to scan the cells marked x. For array of
    # 3, we need to scan cells marked y. 
    # 
    # Assume we are iterating over the matrix with i as row and j as col. 
    #
    # To scan size 2 from i:0 and j:0, we need to check the column 
    #    i from i to (i+2) where j is j+2 AND
    #    j from j to (j+2) where i is i+2
    # If i+2 or j+2 > len(matrix), stop. 
    # 
    #      0  1  2  
    #   0  o  x  y
    #   1  x  x  y
    #   2  y  y  y

    for i in range (numrows):                           
        for j in range (numcols): 
            largest_dim = min(numrows, numcols)
            for dim in range(largest_dim): 
                if scan_border(matrix, i, j, dim) == False:
                    break
                else:
                    max_size = max(max_size, dim+1)

    return max_size

# Clean Sample Matrix
matrix1 = [
    [0,0,0,0,0,0],
    [0,1,1,0,0,0],
    [0,1,1,1,0,0],
    [0,1,1,1,0,0],
    [0,1,1,1,0,0]
]

print("Largest island is {N} by {N} (expect 3 by 3)".format(N = max_square(matrix1)))

print("Largest island is {N} by {N} (expect 3 by 3)".format(N = max_square_brute(matrix1)))

matrix2 = [
    [1,1,1,1,0,0],
    [1,1,1,1,1,0],
    [1,1,1,1,1,0],
    [1,1,1,1,1,0],
    [0,1,1,1,1,0]
]
print(find_max_at_index(matrix2, 1, 1))



