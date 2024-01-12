Memoization vs Tabulation 

Memoization (Top-down approach):
Memoization involves storing the solutions to subproblems in a cache (often implemented as a dictionary or an array) and reusing those solutions when needed. It typically starts with the main problem and recursively breaks it down into smaller subproblems. Before solving a subproblem, the algorithm checks if the solution is already present in the cache. If so, it retrieves the solution from the cache instead of recomputing it. If not, it computes the solution and stores it in the cache for future use. Memoization is more naturally suited for recursive algorithms.

Tabulation (Bottom-up approach):
Tabulation involves creating a table (often implemented as a 2D array) and systematically filling it with the solutions to subproblems in a bottom-up manner. It starts with the smallest subproblems and iteratively computes and stores their solutions in the table. Then it proceeds to solve larger subproblems based on the solutions of smaller subproblems. The final solution to the main problem is obtained from the entry in the table corresponding to the main problem. Tabulation is more suited for iterative algorithms.

Dyamic programming is typically applied to optimization problems 
1) Characterize the structure of an optimal solution.
2) Recursively define the value of an optimal solution
3) Compute the value of an optimal solution
4) Construct an optimal solution from computed information (Optional)

Steps 1–3 form the basis of a dynamic-programming solution to a problem.

Dynamic programming is an optimization over plain recursion.
A recursive solution that has repeated calls for same inputs, can be optmized using Dynamic Programming.
Optimization can be done by storing the solution. 

A) Identify and solve subproblem
B) Use subproblems together to solve larger problem

5 steps:
1) Visualize the example
2) Find an appropriate sub-problem
3) Find relationships among sub-problems
4) Generalize the relationships
5) Implement by solving sub-problems in order

Another 5 step version:
1. Coming up with a recursive solution to the problem
2. Take a look at the parameters you are passing to the recursive function
3. Check which parameters can change between calls; those are likely the coordinates in your dp array/matrix
4. Understand how the recursive call generates its answers from the sub recursive calls, and try to put that into an equation
5. Lastly, find the exit case of the recursive function that is the base case you need to build up from in DP.

Longest Increasing Subsequence:
ex. [3,1,8,2,5] -> 3 (1 -> 2 -> 5)


Memoization
Memoization refers to the technique of caching and reusing previously computed results. 

Tabulation
Tabulation is similar in the sense that it builds up a cache, but the approach is different. A tabulation algorithm focuses on filling the entries of the cache, until the target value has been reached.


fibonacci 
def fib(n):
    #n = which n'th number in fibonacci sequence

fib(5)
[1, 1, 2, 3, 5, 8]
fib(0), fib(1)

https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns
https://leetcode.com/discuss/study-guide/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions
https://www.youtube.com/watch?v=oBt53YbR9Kk