a = [4, 5, 6, 7, 8]
b = [8, 9, 10, 11, 12]
def solution(a, b):
    uniqueSums = {i + j: 0 for i in a for j in b if ((i * j) % (i + j)) == 0}
    return len(uniqueSums)

ans = solution(a,b)
print(ans)

