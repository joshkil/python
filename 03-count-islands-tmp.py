# Count the Islands in a 2D Matrix 
#
# You are given a 2D binary matrix as an input. You want to 
# return the number of islands in the binary matrix. You can 
# think of the 0's as the ocean and the 1's as land. An island 
# is surrounded by water and is formed by connecting adjacent 
# lands horizontally or vertically. You goal is to return the 
# correct number of islands.

def count_islands(matrix):
        return 0

# Clean Sample Matrix
matrix1 = [
    [1,1,0,0,0],
    [0,1,0,0,1],
    [1,0,0,1,1],
    [1,0,1,0,1]
]

print("Matrix has {} islands (expect 4)".format(count_islands(matrix1)))