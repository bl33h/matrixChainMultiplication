#Copyright (C), 2024-2025, bl33h
#FileName: dynamicP.py
#Author: Sara Echeverria, Ricardo Mendez, Andres Montoya, Francisco Castillo
#Version: I
#Creation: 26/03/2024
#Last modification: 26/03/2024
# Reference: https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/

def MatrixChainOrder(p, n):
    # initialize a 2D table to store the minimum cost of matrix multiplication
    # dp[i][j] represents the minimum number of scalar multiplications needed
    # to multiply the chain of matrices from i to j. The table is filled with 0s initially
    dp = [[0 for x in range(n)] for x in range(n)]
    
    # cost is zero when multiplying one matrix (base case)
    for i in range(1, n):
        dp[i][i] = 0
    
    # L represents the chain length being considered, the algorithm gradually increases the chain length from 2 to n
    for L in range(2, n):
        for i in range(1, n-L+1):
            # calculate the ending matrix index in the chain based on L and i
            j = i+L-1  
            # initialize the cost to infinity before finding the minimum.
            dp[i][j] = float('inf')  
            
            # chain split at every possible point (k), calculating he cost for each one, and keep track of the minimum cost found
            for k in range(i, j):
                # calculate cost of splitting at k, including the cost of multiplying the two resulting chains
                q = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                
                # update dp[i][j] if a lower cost is found
                if q < dp[i][j]:
                    dp[i][j] = q
    
    # dp[1][n-1] holds the minimum cost for the full chain of matrices
    return dp[1][n-1]

# dimensions of matrices in the chain
arr = [1, 2, 3, 4, 3]  

# number of matrices plus one
size = len(arr)  
print("Minimum number of multiplications is:", MatrixChainOrder(arr, size))