'''
Filter

https://docs.python.org/3/library/functions.html#filter

filter(function, iterable)
Construct an iterator from those elements of iterable for which function is true. iterable may be either a sequence, a container which supports iteration, or an iterator. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.

Note that filter(function, iterable) is equivalent to the generator expression (item for item in iterable if function(item)) if function is not None and (item for item in iterable if item) if function is None.

See itertools.filterfalse() for the complementary function that returns elements of iterable for which function is false.
'''

def solution(x, courses):
    def shouldConsider(course):
        return len(course) != x

    return list(filter(shouldConsider, courses))


c = ["Negotiations", 
 "Chemical Engineering", 
 "LSAT", 
 "ACT", 
 "Music", 
 "Earth Sciences", 
 "Religious Studies", 
 "Engineering", 
 "Astronomy", 
 "Biomedical Engineering"]
num = 10

ans = solution(x=num,courses=c)

print(ans)

# ['Negotiations', 'Chemical Engineering', 'LSAT', 'ACT', 'Music', 'Earth Sciences', 'Religious Studies', 'Engineering', 'Astronomy', 'Biomedical Engineering']


d = 7
classes = ["Art", 
 "Finance", 
 "Business", 
 "Speech", 
 "History", 
 "Writing", 
 "Statistics"]

ans2 = solution(x=d,courses=classes)

print(ans2)
# ['Art', 'Business', 'Speech', 'Statistics']