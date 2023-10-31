'''
New Style Formatting

Implement a function that will turn the old-style string formating s into a new one so that the following two strings have the same meaning:

s % (*args)
s.format(*args)

Example

For s = "We expect the %f%% growth this week"

solution(s) = "We expect the {}% growth this week".
'''

def solution(s):
    dict = {
        "%d":"{}",
        "%i":"{}",
        "%o":"{}",
        "%u":"{}",
        "%x":"{}",
        "%X":"{}",
        "%e":"{}",
        "%E":"{}",
        "%f":"{}",
        "%F":"{}",
        "%g":"{}",
        "%G":"{}",
        "%c":"{}",
        "%r":"{}",
        "%s":"{}",
        "%%":"%"
    }
    left, right = 0, 1
    new_sentence = []
    while right < len(s) + 1:
        if s[left:right+1] in dict:
            val = dict[s[left:right+1]]
            new_sentence.append(val)
            left +=2
            right +=2
            continue
        new_sentence.append(s[left])
        
        left += 1
        right += 1

    return "".join(new_sentence)