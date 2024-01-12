"""Generics typing in Python."""

"""
Documentation about generics. 
https://docs.python.org/3/library/typing.html#generics

"""

from typing import List, TypeVar
from random import randint
T = TypeVar('T')

def get_item(lst: List[T], idx:int) -> T:
    """Get and return the item in the list, 'lst' at index. 
    
    We do not know what type of data structure is inside the lst. 
    """
    print(lst[idx])
    return lst[idx]

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

Node(randint(0,20))
lst_numbers = [0,1,2]
lst_strings = ['position0', 'position1', 'position2']
lst_nodes = [Node(randint(0,20)), Node(randint(0,20)), Node(randint(0,20))]

get_item(lst_numbers, 1)
get_item(lst_strings, 1)
get_item(lst_nodes, 1)