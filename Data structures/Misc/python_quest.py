def even_numbers():
    num = 0
    while True:
        yield num
        num += 2


evens = even_numbers()

for _ in range(10):
    print(next(evens))

# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18

def fibonacci():
    num_1 = 0
    num_2 = 1
    while True:
        yield num_1
        #[num_1, num_2] = [num_2, num_1 + num_2]
        num_1, num_2 = num_2, num_1 + num_2
        

fib = fibonacci()

for _ in range(20):
    print(next(fib))