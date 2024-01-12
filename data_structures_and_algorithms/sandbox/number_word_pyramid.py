"""
The following code was written as a quick exercise. 

A Python function that can read an encoded message from a .txt file, to return a decoded message as a string. 

Overall, the provided function reads the contents of the "file" line-by-line, appends the order (as an integer) and the word (as a string) into a list called "nums_lst", and sorts the "nums_lst". 
The sorted "nums_lst" is then iterated over, where two counters, called "level" and "counter", are either incremented or decremented, such that at each increasing level, the counter also increases by 1. As a result, each level contains 1 additional word compared to the previous level. 
The last word at each level is then appended to the "message" list, and finally, a string containing the words in the "message" is returned by the function by converting the "message" list into a string. 
"""

def decode(file: str) -> str:
    word_lst = []
    with open(file, "r") as fp:
        contents = fp.readlines()
        for c in contents:
            num, word = c.rstrip("\n").split(" ")
            word_lst.append([int(num), word])

    word_lst.sort()
    level = counter = 1
    message = []
    for i in range(len(word_lst)):
        if counter == 1:
            message.append(word_lst[i][1])
            level += 1
            counter = level
        else:
            counter -= 1
    return " ".join(message)

answ = decode("number_word_pyramid.txt")
print(answ)
