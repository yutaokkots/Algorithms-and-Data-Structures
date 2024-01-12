'''
ticket number is lucky

Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example 1
For n = 1230, 
output = true;

Example 2
For n = 239017,
output = false.

Example 3:
For n: 134008
output = true

'''

def solution(n):
    n_str = str(n)
    mid = len(n_str)//2
    for x in n_str[:mid]:
        int(x)
    lst1 = [int(x) for x in n_str[:mid]]
    lst2 = [int(y) for y in n_str[mid:]]
    return sum(lst1) == sum(lst2)