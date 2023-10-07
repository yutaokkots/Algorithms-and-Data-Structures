'''
.split(separator=" ", maxsplit=-1)

string.split() (without the optional separator) splits the string into alphanum elements regarless of spacing

'''
################
# .split()
#########


s = "  hello  world,  you    are awesome   !"

s_lst_1 = s.split()
print(s_lst_1)
# ['hello', 'world,', 'you', 'are', 'awesome', '!']

s_lst_2 = s.split(" ")
print(s_lst_2)
# ['', '', 'hello', '', 'world,', '', 'you', '', '', '', 'are', 'awesome', '', '', '!']

s_lst_3 = s.split(",")
print(s_lst_3)
# ['  hello  world', '  you    are awesome   !']

t = "  hello 54  world,  you    are awesom55e0 476  !"

s_lst_1 = t.split()
print(s_lst_1)
#['hello', '54', 'world,', 'you', 'are', 'awesom55e0', '476', '!']

s_lst_2 = t.split(" ")
print(s_lst_2)
#['', '', 'hello', '54', '', 'world,', '', 'you', '', '', '', 'are', 'awesom55e0', '476', '', '!']

s_lst_3 = t.split(",")
print(s_lst_3)
#['  hello 54  world', '  you    are awesom55e0 476  !']
