# Function to transpose an nxm matrix using nested loops
def transpose_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])  # Assuming all rows have the same length
    
    # Create a new matrix to store the transposed values
    transposed = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            # Swap rows and columns
            transposed[j][i] = matrix[i][j]
    
    return transposed

# Testing the Function
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = transpose_matrix(matrix)

for row in result:
    print(row)
