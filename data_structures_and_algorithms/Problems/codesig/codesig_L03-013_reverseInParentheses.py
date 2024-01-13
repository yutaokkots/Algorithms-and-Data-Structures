'''
Reverse in Parentheses

For inputString = "(bar)", the output should be
solution(inputString) = "rab";

For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";

For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";

For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

foo (bar (baz) ) blim
->              foo ((zab) rab) blim
foo (bar zab) blim
->              foo ((baz) rab) blim
foo baz rab blim


'''

def solution(inputString):
    str_lst = list(inputString)
    stack = []
    for i in range(len(inputString)):
        if inputString[i] == "(":
            stack.append(i)
            continue
        if inputString[i] == ")":
            opening_index = stack.pop()
            sublst = str_lst[opening_index: i+ 1]
            sublst.reverse()
            str_lst[opening_index: i + 1] = sublst
    answer = []
    for n in str_lst:
        if n != '(' and n != ')':
            answer.append(n)
    return "".join(answer)