'''
Map

https://docs.python.org/3/library/functions.html#map
map(function, iterable, *iterables)
Return an iterator that applies function to every item of iterable, yielding the results. If additional iterables arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted. For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().

'''
def solution(result):
    def fix(x):
        return x // 10

    return list(map(fix, result))

result = [31, 41, 59, 26, 53, 58, 97, 93]

ans = solution(result)
print(ans)