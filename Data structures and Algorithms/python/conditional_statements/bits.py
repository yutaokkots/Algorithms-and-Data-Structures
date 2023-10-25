'''
implement a function that, 
given an integer n,
returns the number of bits in its binary representation. 

example 1: 
n: 50
output = 6

example 2: 
n: 1
output = 1

example 3:
n: 1000000000
output = 30

example 4:
n: 237487384
output = 30

***********
answer: use 

.bit_length()
***********
'''

def solution(n):
    return n.bit_length()

print(solution(50))
print(solution(1))
print(solution(1000000000))
print(solution(237487384))

# 6
# 1
# 30
# 28