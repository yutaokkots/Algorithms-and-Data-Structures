'''
Company name

Given the names of the companies, return the list of characters that are popular but not mainstream sorted by their ASCII codes.

example 1:
companies = ["coolcompany", "nicecompany", "legendarycompany"],
the output should be
solution(companies) = ['e', 'l'].

Here's how the answer can be obtained:

these letters appear in all three company names and are thus mainstream: 'a', 'c', 'm', 'n', 'o', 'p', 'y';
these letters appear only in one of the company names and are thus not popular: 'd', 'g', 'i', 'r';
the remaining letters are popular and not mainstream: 'e', 'l'.

& -> is a bitwise operator

'''
comp = ["coolcompany", "nicecompany", "legendarycompany"]

def solution(companies):
    cmp1 = set(companies[0])
    cmp2 = set(companies[1])
    cmp3 = set(companies[2])
    print(cmp1)
    # companies[0] =        'coolcompany'
    # set(companies[0] =    {'a', 'n', 'o', 'l', 'c',      'p', 'm', 'y'}
    print(cmp2)
    # companies[1] =        'nicecompany'
    # set(companies[1] =    {'n', 'a', 'o', 'c', 'i', 'e', 'p', 'm', 'y'}
    print(f"{(cmp1 & cmp2)=}")
    # (cmp1 & cmp2) =       {'n', 'a', 'o', 'c', 'p', 'm', 'y'}
    print(f"{(cmp2 & cmp3)=}")
    print(f"{(cmp1 & cmp3)=}")

    res = ((cmp1 & cmp2) | (cmp2 & cmp3) | (cmp1 & cmp3)) - (cmp1 & cmp2 & cmp3)
    return list(sorted(list(res)))

ans = solution(comp)

print(ans)

words = ['abcdef', 'efghijk', 'bagel']
w1 = set(words[0])
w2 = set(words[1])
w3 = set(words[2])

print(w1 & w2)          # {'e', 'f'}
print(w2 & w3)          # {'e', 'g'}
print(w1 & w3)          # {'a', 'b', 'e'}

print(w1 & w2 & w3)     # {'e'} 


