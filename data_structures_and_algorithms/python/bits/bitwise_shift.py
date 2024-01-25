"""operation >> and <<"""
"""
x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). 
This is the same as multiplying x by 2**y.

x >> y
Returns x with the bits shifted to the right by y places. 
This is the same as //'ing x by 2**y.
"""

print(f"1 << 1: {1 << 1}, is equal to 2**1")     # 1 << 1:   2, is equal to 2**1
print(f"1 << 2: {1 << 2}, is equal to 2**2")     # 1 << 2:   4, is equal to 2**2
print(f"1 << 3: {1 << 3}, is equal to 2**3")     # 1 << 3:   8, is equal to 2**3
print("""
    1 -> 00000001
    1 << 3 (the bits moved to the left by 3 places)
    3 -> 00001000
    00001000 => 8

    This is the same as:
    x * (2**y)
    1 * (2**3) => 8
""")
print(f"1 << 4: {1 << 4}, is equal to 2**4")     # 1 << 4:  16, is equal to 2**4
print(f"1 << 5: {1 << 5}, is equal to 2**5")     # 1 << 5:  32, is equal to 2**5
print(f"1 << 6: {1 << 6}, is equal to 2**6")     # 1 << 6:  64, is equal to 2**6
print(f"1 << 7: {1 << 7}, is equal to 2**7")     # 1 << 7: 128, is equal to 2**7
print(f"1 << 8: {1 << 8}, is equal to 2**8")     # 1 << 8: 256, is equal to 2**8
print("""
    1 -> 000000001
    1 << 8 (the bits moved to the left by 8 places)
    3 -> 100000000
    100000000 => 256
""")
print(f"2 << 0: {2 << 0}, is equal to ")
print(f"2 << 1: {2 << 1}, is equal to ")
print(f"2 << 2: {2 << 2}, is equal to ")
print(f"2 << 3: {2 << 3}, is equal to ")
print(f"2 << 4: {2 << 4}, is equal to ")
print(f"2 << 5: {2 << 5}, is equal to ")
print(f"2 << 0: {2 << 0}, is equal to ")

print(f"3 << 1: {3 << 1}, is equal to ")
print(f"3 << 2: {3 << 2}, is equal to ")
print(f"3 << 3: {3 << 3}, is equal to ")
print("""
    3 -> 00000011
    1 << 3 (the bits moved to the left by 3 places)
    3 -> 00011000
    00011000 => 24

    This is the same as:
    x * (2**y)
    3 * (2**3) => 24
""")
print(int("00011000", 2))
print(f"3 << 4: {3 << 4}, is equal to ")
print(f"3 << 5: {3 << 5}, is equal to ")

print(f"1 >> 1: {1 >> 1}")
print(f"2 >> 1: {2 >> 1}")
print(f"3 >> 1: {3 >> 1}")
print(f"4 >> 1: {4 >> 1}")
print("""
    4 -> 00000100
    4 >> 1 (the bits moved to the right by 1 place)
      -> 00000010
    00000010 => 2

    This is the same as:
    x // (2**y)
    4 // (2**1) => 2
""")
print(f"5 >> 1: {5 >> 1}")
print(f"6 >> 1: {6 >> 1}")
print(f"7 >> 1: {7 >> 1}")
print(f"8 >> 2: {8 >> 2}")

print("""
    8 -> 00001000
    8 >> 2 (the bits moved to the right by 2 places)
      -> 00000010
    00000010 => 2

    This is the same as:
    x // (2**y)
    8 // (2**2) => 2
""")