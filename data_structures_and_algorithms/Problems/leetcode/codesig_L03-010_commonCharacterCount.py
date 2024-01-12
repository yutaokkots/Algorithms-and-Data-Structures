'''
Common Character Count

Given two strings, s1 and s2, find the common characters between them. 


s1, s2: 
A string consisting of lowercase English letters.
constraints:
1 ≤ s1.length < 15.

Example 1:
Input:
s1: "zzzz"
s2: "zzzzzzz"
Output: 4

Example 1:
Input:
s1: "abca"
s2: "xyzbac"
Output: 3

'''

import collections
def solution(s1, s2):
    d1 = collections.Counter(s1)
    d2 = collections.Counter(s2)
    counter = 0
    for k in d1.keys():
        if k in d2:
            counter += min(d1[k], d2[k])       
    return counter  