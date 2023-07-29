# page 68
# print all positive integer solutions to the equation, a^3 + b^3 = c^3 + d^3,
# where a, b, c, and d are all integer values from 1 through 1000

# brute force: O(N^4)
def o_n4 ():
    n = 1000
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                for d in range(1, n):
                    if a^3 + b^3 == c^3 + d^3:
                        print(f"a: {a}, b: {b}, c: {c}, d: {d}")

# reduction to O(N^3)
# d = pow(a^3 + b^3 - c^3, 1/3)
def o_n3 ():
    n = 1000
    for a in range(1,n):
        for b in range(1, n):
            for c in range(1, n):
                d = int((a^3 + b^3 - c^3)**1/3)
                if (a^3 + b^3 == c^3 + d^3) and 0 <= d and d <= n:
                    print(f"a: {a}, b: {b}, c: {c}, d: {d}")

def o_n2():
    memo = {}
    n = 1000
    for c in range(1, n):
        for d in range(1, n):
            result = c^3 + d^3
            memo[result] = f"{c, d}"
    for a in range(1, n):
        for b in range(1, n):
            result2 = a^2 + b^2
            result2_list = [res for res in memo.keys() if res == result2]
            for pair in result2_list:
                print(f"{a}, {b}, {pair}")

def o_n2_2():
    memo = {}
    n = 1000
    for c in range(1, n):
        for d in range(1, n):
            result = c^3 + d^3
            memo[result] = f"{c, d}"