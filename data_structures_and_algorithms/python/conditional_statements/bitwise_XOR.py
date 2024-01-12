'''
In python, XOR is a bitwise operator
known as => Exclusive OR

it is a logical operator that 
- outputs 1 when either of the operands is 1 (1 | 0)
- both are not 1
- both are not 0
'''

num1 = 1
num2 = 0
xor_num = num1 ^ num2

print(xor_num)
# 1

num1 = 1
num2 = 1
xor_num = num1 ^ num2
print(xor_num)
# 0

num1 = 0
num2 = 0
xor_num = num1 ^ num2
print(xor_num)
# 0

a = 2
b = 7
c = 2
print(a ^ b ^ c)
# 7

d = 2
e = 7
f = 7
print(d ^ e ^ f)
# 2

def solution(a, b, c):
    print(f"{a=}")
    print(f"{b=}")
    print(f"{c=}")
    print(f"{a^b=}")
    print(f"{b^c=}")
    print(f"{a^c=}")
    return a ^ b ^ c

print(solution(2,7,2))
# a=2
# b=7
# c=2
# a^b=5  -> difference between 2, 7 => 5
# b^c=5
# a^c=0
# return 7

print(solution(3,2,2))
# a=3
# b=2
# c=2
# a^b=1
# b^c=0
# a^c=1
#return 3

def solution(a, b, c, d):
    print(f"{a=}")
    print(f"{b=}")
    print(f"{c=}")
    print(f"{d=}")
    print(f"{a^b=}")
    print(f"{b^c=}")
    print(f"{a^c=}")
    print(f"{b^d=}")
    return a ^ b ^ c ^ d

print(solution(3,2,2,11))
# a=3
# b=2
# c=2
# d=11
# a^b=1
# b^c=0
# a^c=1
# b^d=9
# 8

print(solution(3,2,2,2))
# a=3
# b=2
# c=2
# d=2
# a^b=1
# b^c=0
# a^c=1
# b^d=0
# 1

def solution(a, b, c, d, e):
    return a ^ b ^ c ^ d ^ e

print(solution(8,2,2,2,2))

print(5^2)