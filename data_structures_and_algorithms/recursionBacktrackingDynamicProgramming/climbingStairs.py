'''
Fibonacci problem 

Solving Climbing Stairs with the 
    - brute force (bf) method 
    - memoization (memo) method
    - tabulation (tab) method
'''

import time

def climb_stairs_bf(n):
    ''' Solves the climbing stairs problem with brute-force.

    :type n: int
    :rtype: int
    '''
    def dp(i):
        if i == 0 or i == 1:
            return 1
        left = dp(i - 1)
        right = dp(i - 2)
        return left + right
    return dp(n)

def climb_stairs_memo(n):
    ''' Solves the climbing stairs problem using memoization.

    :type n: int
    :rtype: int
    '''
    memo = {}
    def dp(i):
        if i == 0 or i == 1:
            return 1
        if i in memo:
            return memo[i]
        left = dp(i - 1)
        right = dp(i - 2)
        memo[i] = left + right
        return left + right
    return dp(n)

def climb_stairs_tab(n):
    ''' Solves the climbing stairs problem using tabulation.

    :type n: int
    :rtype: int
    '''
    one, two = 1, 1
    for _ in range(n - 1):
        temp = two
        two = one + two
        one = temp

    return two

test_set = [3, 4, 5, 6, 8, 10, 15, 20, 30]
test_set2 = [3, 4, 5, 6, 8, 10, 15, 20, 30, 60, 120]

# Brute Force
for t in test_set:
    start = time.time()
    ans = climb_stairs_bf(t)
    end = time.time()
    print(f"stairs: {t}, permutations: {ans}, {end - start} sec")

# Memoization
for t in test_set2:
    start = time.time()
    ans = climb_stairs_memo(t)
    end = time.time()
    print(f"stairs: {t}, permutations: {ans}, {end - start} sec")

# Tabulation
for t in test_set2:
    start = time.time()
    ans = climb_stairs_tab(t)
    end = time.time()
    print(f"stairs: {t}, permutations: {ans}, {end - start} sec")

'''
Time Complexities

Brute Force: O(2^N)
stairs: 3,  permutations: 3,                2.86 e-06 sec
stairs: 4,  permutations: 5,                3.81 e-06 sec
stairs: 5,  permutations: 8,                3.09 e-06 sec
stairs: 6,  permutations: 13,               1.90 e-06 sec
stairs: 8,  permutations: 34,               5.72 e-06 sec
stairs: 10, permutations: 89,               1.50 e-05 sec
stairs: 15, permutations: 987,              0.00016 sec
stairs: 20, permutations: 10946,            0.0017 sec
stairs: 30, permutations: 1346269,          0.199 sec
stairs: 37, permutations: 39088169,         5.656 sec
stairs: 39, permutations: 102334155,        14.32 sec

Memoization: O(N)
stairs: 3,  permutations: 3,                6.914 e-06 sec
stairs: 4,  permutations: 5,                1.120 e-05 sec
stairs: 5,  permutations: 8,                2.145 e-06 sec
stairs: 6,  permutations: 13,               2.145 e-06 sec
stairs: 8,  permutations: 34,               3.099 e-06 sec
stairs: 10, permutations: 89,               3.099 e-06 sec
stairs: 15, permutations: 987,              9.298 e-06 sec
stairs: 20, permutations: 10946,            6.198 e-06 sec
stairs: 30, permutations: 1346269,          1.192 e-05 sec
stairs: 37, permutations: 39088169,         1.192 e-05 sec
stairs: 60, permutations: 2504730781961,    2.002 e-05 sec
stairs: 120,permutations: 8670007398507948658051921, 5.483 e-05 sec

Tabulation: O(N)
stairs: 3,  permutations: 3,                1.192 e-05 sec
stairs: 4,  permutations: 5,                9.536 e-07 sec
stairs: 5,  permutations: 8,                1.192 e-06 sec
stairs: 6,  permutations: 13,               9.536 e-07 sec
stairs: 8,  permutations: 34,               1.192 e-06 sec
stairs: 10, permutations: 89,               9.536 e-07 sec
stairs: 15, permutations: 987,              9.536 e-07 sec
stairs: 20, permutations: 10946,            2.145 e-06 sec
stairs: 30, permutations: 1346269,          9.536 e-07 sec
stairs: 60, permutations: 2504730781961,    3.099 e-06 sec
stairs: 120,permutations: 8670007398507948658051921, 5.960 e-06 sec
'''