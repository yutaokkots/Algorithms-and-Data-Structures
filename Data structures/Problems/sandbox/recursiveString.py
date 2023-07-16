# Permutations - rearrangement of elements

# Given a string, print all permutations of the string
# recursion

# with string.length = n,
# how many permutations?
# n!




def string_recursion(string):
    if len(string) == 1:
        return [string]
    result = []
    for i, value in enumerate(string):
        result += [value+p for p in string_recursion(string[:1] + string[i+1:])]
    return result

str = "hello"

print(string_recursion(str))
