'''
FOR/ELSE 

"for loops also have an else clause which most of us are unfamiliar with. 

The else clause executes after the loop completes normally. 
This means that the loop did not encounter a break statement. 

They are really useful once you understand where to use them. I, myself, came to know about them a lot later."
https://book.pythontips.com/en/latest/for_-_else.html
© Copyright 2017, Muhammad Yasoob Ullah Khalid Revision 9b6262ee.

'''

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break

'''
    It finds factors for numbers between 2 to 10. Now for the fun part. 
    We can add an additional else block which catches the numbers which have no factors and are therefore prime numbers:
'''
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


def solution(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found = upperBound

    return found
