# Reverse a string
str_1 = "Hello"
str_2 = ""
str_3 = "k"
str_4 = "hi there"

# O(log N)

def reverse_string(s: str) -> str:
    left = 0
    right = len(s) - 1
    str_list = list(s)
    while right > left:

        interm = str_list[right]
        str_list[right] = str_list[left]
        str_list[left] = interm
        left += 1
        right -= 1

    return "".join(str_list)

print(reverse_string(str_1))
print(reverse_string(str_2))
print(reverse_string(str_3))
print(reverse_string(str_4))
