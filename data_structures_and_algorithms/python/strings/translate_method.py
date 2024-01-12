'''
string.translate()
creating a table and using the table to translate

'''
pw = "helloz"
k = "zabcdefghijklmnopqrstuvwxy"

def solution(password, key):
    table = {97+n:ord(key[n]) for n in range(26)}
    print(table)
    return password.translate(table)

ans = solution(pw, k)
print(ans)