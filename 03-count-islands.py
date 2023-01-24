def print_matrix(matrix):
    if matrix == None: 
        return
    for i in range(len(matrix)):
        print("  ", end="")
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="")
        print("")

def count_islands(matrix):
    # check input
    if matrix == None \
        or (not isinstance(matrix,list)) \
        or (not all(isinstance(ele, list) for ele in matrix)):
        return 0

    # create new matrix to keep track of visits
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    num_islands = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1 and not visited[i][j]:
                dfs(i, j, matrix, visited)
                num_islands += 1
                
    return num_islands

def dfs(i, j, matrix, visited):
    if i in range(len(matrix)) and j in range(len(matrix[i])) \
        and matrix[i][j] == 1 \
        and visited[i][j] == False:

        visited[i][j] = True
        dfs(i-1, j,   matrix, visited) # visit north
        dfs(i+1, j,   matrix, visited) # visit south
        dfs(i,   j+1, matrix, visited) # visit east
        dfs(i,   j-1, matrix, visited) # visit west
    

# Clean Sample Matrix
matrix1 = [
    [1,1,0,0,0],
    [0,1,0,0,1],
    [1,0,0,1,1],
    [1,0,1,0,1]
]

print_matrix(matrix1)
print("Matrix has: {} islands (expect 4)".format(count_islands(matrix1)))

# PR Example Matrix
matrix2 = [
    [1,1,0,0,0],
    [0,1,0,0,1],
    [1,0,0,1,1],
    [0,0,0,0,0],
    [1,0,1,0,1]
]

print_matrix(matrix2)
print("Matrix has: {} islands (expect 6)".format(count_islands(matrix2)))

# Empty Column
matrix3 = [
    [],
    [],
    [],
    [],
    []
]

print_matrix(matrix3)
print("Matrix has: {} islands (expect 0)".format(count_islands(matrix3)))

# single column
matrix4 = [
    [1],
    [1],
    [0],
    [1],
    [1]
]

print_matrix(matrix4)
print("Matrix has: {} islands (expect 2)".format(count_islands(matrix4)))

# Single Row
matrix5 = [
    [1, 0, 1, 1, 0, 1]
]

print_matrix(matrix5)
print("Matrix has: {} islands (expect 3)".format(count_islands(matrix5)))

# Null matrix
matrix6 = None

print_matrix(matrix6)
print("Matrix has: {} islands (expect 0)".format(count_islands(matrix6)))

# Malformed Matrix
matrix7 = [
    [1,1,0,0,0],
    [0,1],
    [1,0,0,1,1],
    [0,0,1],
    [1,0,1,0,1]
]

print_matrix(matrix7)
print("Matrix has: {} islands (expect 6)".format(count_islands(matrix7)))