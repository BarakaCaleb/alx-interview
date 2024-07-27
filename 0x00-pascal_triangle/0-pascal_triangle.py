

"""A script that prints the pascal triangle of a given number"""

def pascal_triangle(n):
    """
    Returns list of integers representing the pascal triangle
    """
    if n <= 0:
        return []

    # Start with the first row
    triangle = [[1]]
    

    for i in range(1, n):
        row = [1]  # Every row starts with 1
        for j in range(1, i):
            # Sum the two numbers above this position
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)
    
    return triangle



