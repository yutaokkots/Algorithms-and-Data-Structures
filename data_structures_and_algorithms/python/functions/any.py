"""Review on any() function"""

"""
any(iterable)

Return True if any element of the iterable is true. If the iterable is empty, return False.

Equivalent to:

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
"""

token = "abcDefghijk"

if any(char.isnumeric() for char in token):
    print("Number found!")
else:
    print("No numbers found.")

if any(char.isupper() for char in token):
    print("Capital letter found!")
else:
    print("No capital letters found.")

# No numbers found.
# Capital letter found!
