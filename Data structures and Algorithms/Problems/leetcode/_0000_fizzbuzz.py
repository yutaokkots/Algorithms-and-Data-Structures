'''
with input n:
print fizz if the number is divisible by 3
print buzz if the number is divisible by 5
print fizzbuzz if the number is divisible by both 3 and 5
else print the number itself if it is neither
'''

from time_measure import timer

num = 24

@timer
def fizzbuzz_naive(n):
    answer = []
    for i in range(1, n+1):
        if i % 5 == 0 and i % 3 == 0:
            answer.append("fizzbuzz")
        elif i % 5 == 0:
            answer.append("buzz")
        elif i % 3 == 0:
            answer.append("fizz")
        else:
            answer.append(i)
    return answer
    
@timer
def fizzbuzz(n):
    answer = []
    for i in range(1, n+1):
        output = ""
        if i % 3 == 0:
            output += "fizz"
        if i % 5 == 0:
            output += "buzz"
        if output == "":
            output += f"{i}"
        answer.append(output)
    return answer


ans1 = fizzbuzz_naive(num)
print(ans1)
ans2 = fizzbuzz(num)
print(ans2)