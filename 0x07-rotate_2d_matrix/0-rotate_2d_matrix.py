#!/usr/bin/python3

# Rotating a 2D matrix 90 degrees clockwise
# The first step is to transpose the matrix
# The second step is to reverse the rows of the transposed matrix
# Transpose: matrix[i][j] = matrix[j][i] invlove swapping of rows and columns
# Reverse: matrix[i][j] = matrix[i][n-1-j] involves swapping of elements in the same row

def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise in place."""
    # Step 1: Transpose the matrix(SWAP ROWS AND COLUMNS)
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each Row to get the Rotated matrix in clockwise direction
    for i in  range(n):
        matrix[i].reverse
