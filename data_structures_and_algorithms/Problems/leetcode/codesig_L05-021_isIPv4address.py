'''
is IPv4 address

Check to see if an input string is a valid IPv4Address

Example 1:
For inputString = "172.16.254.1", the output should be
solution(inputString) = true;

Example 2:
For inputString = "172.316.254.1", the output should be
solution(inputString) = false.

316 is not in range [0, 255].

Example 3:
For inputString = ".254.255.0", the output should be
solution(inputString) = false.

Example 4:
input: "1.1.1.1a"
output: False

Example 5:
input: "64.233.161.00"
output: False

Example 6:
inputString: "01.233.161.131"
output: False
'''

def solution(inputString):
    input_lst = inputString.split(".")
    if len(input_lst) != 4:
        return False
    for n in input_lst:
        try:
            number = int(n)   
        except:
            return False
        if number in range(10) and len(n) != 1 or number not in range(256):
            return False

    return True