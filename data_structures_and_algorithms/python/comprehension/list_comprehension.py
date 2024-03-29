'''
List Comprehension

'''
# construct a multiplication table. Given an integer n, return the multiplication table of size n × n.
def solution(n):
    return [[i * j for i in range(1, n+1)] for j in range(1, n+1)]

a_4 = solution(4)
a_5 = solution(5)
a_9 = solution(9)

print(a_4)
print(a_5)
print(a_9)


#       [[1, 2, 3, 4], 
#        [2, 4, 6, 8], 
#        [3, 6, 9, 12], 
#        [4, 8, 12, 16]]

#       [[1, 2, 3, 4, 5], 
#        [2, 4, 6, 8, 10], 
#        [3, 6, 9, 12, 15], 
#        [4, 8, 12, 16, 20], 
#        [5, 10, 15, 20, 25]]

#       [[1, 2, 3, 4, 5, 6, 7, 8, 9], 
#        [2, 4, 6, 8, 10, 12, 14, 16, 18], 
#        [3, 6, 9, 12, 15, 18, 21, 24, 27], 
#        [4, 8, 12, 16, 20, 24, 28, 32, 36], 
#        [5, 10, 15, 20, 25, 30, 35, 40, 45], 
#        [6, 12, 18, 24, 30, 36, 42, 48, 54], 
#        [7, 14, 21, 28, 35, 42, 49, 56, 63], 
#        [8, 16, 24, 32, 40, 48, 56, 64, 72], 
#        [9, 18, 27, 36, 45, 54, 63, 72, 81]]