'''
understanding the difference between 

mid = (left + right) // 2

vs

mid = left + ((right - left) // 2)

'''


lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

left, right = 0, len(lst1) - 1

mid1 = (left + right) // 2
## (left + right) // 2

mid2 = left + ((right - left) // 2)
## (right - left) // 2

target = 16

while left < right:
    mid1 = (left + right) // 2

    print(f"({left} + {right}) // 2 = {mid1}")
    if target == lst1[mid1]:
        print(f"~~~{target}~~~")
        break
    elif target > lst1[mid1]:
        left = mid1 + 1
    else:
        right = mid1 - 1


left, right = 0, len(lst1) - 1

while left < right:
    mid2 = left + ((right - left) // 2)

    print(f"{left} + (({right} - {left}) // 2) = {mid2}")
    if target == lst1[mid2]:
        print(f"~~~{target}~~~")
        break
    elif target > lst1[mid2]:
        left = mid2 + 1
    else:
        right = mid2 - 1