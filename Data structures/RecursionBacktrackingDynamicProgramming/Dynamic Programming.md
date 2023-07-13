Memoization vs Tabulation 

Memoization (Top-down approach):
Memoization involves storing the solutions to subproblems in a cache (often implemented as a dictionary or an array) and reusing those solutions when needed. It typically starts with the main problem and recursively breaks it down into smaller subproblems. Before solving a subproblem, the algorithm checks if the solution is already present in the cache. If so, it retrieves the solution from the cache instead of recomputing it. If not, it computes the solution and stores it in the cache for future use. Memoization is more naturally suited for recursive algorithms.

Tabulation (Bottom-up approach):
Tabulation involves creating a table (often implemented as a 2D array) and systematically filling it with the solutions to subproblems in a bottom-up manner. It starts with the smallest subproblems and iteratively computes and stores their solutions in the table. Then it proceeds to solve larger subproblems based on the solutions of smaller subproblems. The final solution to the main problem is obtained from the entry in the table corresponding to the main problem. Tabulation is more suited for iterative algorithms.

Dyamic programming is typically apply to optimization problems 
1) Characterize the structure of an optimal solution.
2) Recursively define the value of an optimal solution
3) Compute the value of an optimal solution
4) Construct an optimal solution from computed information (Optional)

Steps 1–3 form the basis of a dynamic-programming solution to a problem.

fibonacci 
def fib(n):
    #n = which n'th number in fibonacci sequence

fib(5)
[1, 1, 2, 3, 5, 8]
fib(0), fib(1)

