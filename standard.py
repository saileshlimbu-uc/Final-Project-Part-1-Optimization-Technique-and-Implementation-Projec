import numpy as np
import time

# Function for standard matrix multiplication
def standard_matrix_multiplication(A, B):
    n = A.shape[0]
    C = np.zeros((n, n))  # Initialize result matrix with zeros
    
    # Standard matrix multiplication
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]
                
    return C

# Initialize matrices
n = 1000  # Size of the matrix
A = np.random.rand(n, n)
B = np.random.rand(n, n)

# Time the standard matrix multiplication
start_time = time.time()
C_standard = standard_matrix_multiplication(A, B)
end_time = time.time()

print(f"Standard Matrix Multiplication took {end_time - start_time:.2f} seconds.")
