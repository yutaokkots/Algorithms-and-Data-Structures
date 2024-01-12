'''
Reduce

https://docs.python.org/3/library/functools.html

functools.reduce(function, iterable[, initializer])
Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). The left argument, x, is the accumulated value and the right argument, y, is the update value from the iterable. If the optional initializer is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty. If initializer is not given and iterable contains only one item, the first item is returned.

https://docs.python.org/3/library/math.html

math.gcd(*integers)
Return the greatest common divisor of the specified integer arguments. If any of the arguments is nonzero, then the returned value is the largest positive integer that is a divisor of all arguments. If all arguments are zero, then the returned value is 0. gcd() without arguments returns 0.

Changed in version 3.9: Added support for an arbitrary number of arguments. Formerly, only two arguments were supported.

'''
import functools
from math import gcd


# example 1:
#For denominators = [2, 3, 4, 5, 6], the output should be solution(denominators) = 60.

def solution(denominators):
    return functools.reduce(lambda a, b: int(abs(a*b)/gcd(a,b)), denominators)

d = [2, 3, 4, 5, 6]

ans = solution(d)

print(ans)