#Copyright (C), 2024-2025, bl33h
#FileName: divideAndConquer.py
#Author: Sara Echeverria, Ricardo Mendez, Andres Montoya, Francisco Castillo
#Version: I
#Creation: 26/03/2024
#Last modification: 26/03/2024
# Reference: https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/

import sys

def MatrixChainOrderRecursive(p, i, j, dp):
    # base case: when the chain consists of a single matrix, no multiplication is needed
    if i == j:
        return 0
    
    # if the solution for this subproblem has already been calculated, return it
    if dp[i][j] != sys.maxsize:
        return dp[i][j]
    
    # recursively find the minimum multiplication cost by dividing the problem into smaller subproblems and trying all possible places to split the chain
    for k in range(i, j):
        count = (MatrixChainOrderRecursive(p, i, k, dp) +
                 MatrixChainOrderRecursive(p, k+1, j, dp) +
                 p[i-1] * p[k] * p[j])
        
        # update dp[i][j] with the minimum cost found so far
        if count < dp[i][j]:
            dp[i][j] = count
    
    # return the minimum cost for multiplying matrices from i to j
    return dp[i][j]

def MatrixChainOrderDnC(p, n):
    # initialize the DP table with sys.maxsize indicating that the minimum cost has not been calculated yet [memoization]
    dp = [[sys.maxsize for i in range(n)] for j in range(n)]
    
    # start the recursive process from the first matrix to the last
    return MatrixChainOrderRecursive(p, 1, n-1, dp)

# dimensions of matrices in the chain
arr = [1, 2, 3, 4, 3]  

# number of matrices plus one
size = len(arr) 
print("Minimum number of multiplications is:", MatrixChainOrderDnC(arr, size))