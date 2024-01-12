'''
Palindrome Rearranging

Given a string, return True if the string can be rearranged to form a palindrome, otherwise return False. 
'''

import collections
def solution(inputString):
    ct_input = collections.Counter(inputString)
    odd_counter = 0
    
    for k, v in ct_input.items():
        if v % 2 == 1:
            odd_counter += 1
    
    if (odd_counter > 1 or 
            odd_counter == 1 and 
            len(inputString) % 2 == 0):
        return False
        
    return True