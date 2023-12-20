import re

str_lst = ["/",".","4","8","&"]
pattern = r'[^a-zA-Z0-9.]'
for l in str_lst:
    print(bool(re.match(pattern, l)))
