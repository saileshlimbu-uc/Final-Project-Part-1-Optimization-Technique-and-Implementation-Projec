import numpy as np
import time

# Function for cache-optimized matrix multiplication
def cache_optimized_matrix_multiplication(A, B):
    n = A.shape[0]
    C = np.zeros((n, n))  # Initialize result matrix with zeros
    
    # Cache-optimized matrix multiplication
    block_size = 64  # Define block size to fit cache lines
    
    # Process the matrix in blocks to optimize cache usage
    for ii in range(0, n, block_size):
        for jj in range(0, n, block_size):
            for kk in range(0, n, block_size):
                for i in range(ii, min(ii + block_size, n)):
                    for j in range(jj, min(jj + block_size, n)):
                        for k in range(kk, min(kk + block_size, n)):
                            C[i, j] += A[i, k] * B[k, j]
                            
    return C

# Time the cache-optimized matrix multiplication
start_time = time.time()
C_optimized = cache_optimized_matrix_multiplication(A, B)
end_time = time.time()

print(f"Cache-Optimized Matrix Multiplication took {end_time - start_time:.2f} seconds.")
