'''
string.translate()
creating a table and using the table to translate

'''

def solution(password, key):
    table = {97+n:ord(key[n]) for n in range(26)}
    return password.translate(table)
