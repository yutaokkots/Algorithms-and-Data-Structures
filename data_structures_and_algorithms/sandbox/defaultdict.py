import collections

'''
The Python defaultdict type behaves almost exactly like a regular Python dictionary, 
but if you try to access or modify a missing key, then defaultdict will automatically create 
the key and generate a default value for it. 
This makes defaultdict a valuable option for handling missing keys in dictionaries.
'''

def_dict_lst = collections.defaultdict(list)
print(def_dict_lst)
# defaultdict(<class 'list'>, {})

def_dict_lst["a"]       # because key, "a" is not contained in def_dict_lst, k:v pair of "a":[] is generated
print(def_dict_lst)
# defaultdict(<class 'list'>, {'a': []})


def_dict_int = collections.defaultdict(int)
def_dict_int["a"] 
## defaultdict(<class 'int'>, {'a': 0})

def_dict_str = collections.defaultdict(str)
def_dict_str["a"] 
print(def_dict_str)
## defaultdict(<class 'str'>, {'a': ''})

def_dict_dict = collections.defaultdict(dict)
def_dict_dict["a"] 
print(def_dict_dict)
## defaultdict(<class 'dict'>, {'a': {}})

def_dict_q = collections.defaultdict(collections.deque)
def_dict_q["a"] 
print(def_dict_q)
## defaultdict(<class 'collections.deque'>, {'a': deque([])})

