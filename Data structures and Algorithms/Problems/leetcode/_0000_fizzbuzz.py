'''
with input n:
print fizz if the number is divisible by 3
print buzz if the number is divisible by 5
print fizzbuzz if the number is divisible by both 3 and 5
else print the number itself if it is neither


'''

num = 24

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
    print(answer)
    

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
    print(answer)


fizzbuzz_naive(num)
fizzbuzz(num)