'''
Truthiness
What is the value of res after the following code?

d = [()]
res = [False] * 2
if d:
    res[0] = True
if d[0]:
    res[0] = True

-> In Python, an empty list or tuple is considered falsy, while a non-empty list is considered truthy, regardless of the contents of the elements in the list.
'''

d = [()]
res = [False] * 2
if d:
    res[0] = True
if d[0]:
    res[1] = True
print(res)                  ## [True, False]    
print(d, bool(d))           ## [()] True        In Python, a non-empty list is considered "truthy," regardless of its contents. 
print(d[0], bool(d[0]))     ## () False         In Python, an empty tuple is considered "falsy," meaning it evaluates to False in a boolean context. This is because it contains no elements, and empty containers are typically treated as falsy.






'''
Given two boolean variables, a and b,
which one of the following is different than the other?

a == (not b)
a == not b  
not a == b  
not (a == b)

'''
a = True
b = True

choice_a = a == (not b)
#choice_b = a == not b  <- INVALID SYNTAX
choice_c = not a == b  
choice_d = not (a == b)

print(choice_a)
#print(choice_b)
print(choice_c)
print(choice_d)