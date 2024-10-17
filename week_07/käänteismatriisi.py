from sympy import Matrix

# Define the given inverse matrix A_inv
A_inv = Matrix([[0, 1, 1], [5, -3, -1], [-3, 2, 1]])

# Calculate the original matrix A by finding the inverse of A_inv
A = A_inv.inv()

print(A)