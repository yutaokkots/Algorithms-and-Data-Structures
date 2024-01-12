"""Callable typing in Python."""
from typing import Callable, Dict

"""
Dict[str, str]
     │    └── value
     └── key

func : Callable[[str, str], str]
       │
       └── Callable takes 2 str parameters, and returns str

"""

Person = Dict[str, str]

def hyphenate(substr1:str, substr2:str) -> str:
    return f"{substr1}-{substr2}"

def mix(substr1:str, substr2:str) -> str:
    return f"{substr2}{substr1.lower()}"

def join_families(modifier_funct:Callable[[str, str], str], person1:Person, person2:Person) -> str:
    joined = modifier_funct(person1["last_name"], person2["last_name"] )
    print(f"Mr. and Mrs. {joined}")
    return f"Mr. and Mrs. {joined}"

p1 = {
    "first_name": "Juan",
    "last_name": "Doe"
}

p2 = {
    "first_name": "Tara",
    "last_name": "Yamada"
}

join_families(hyphenate, p1, p2)
join_families(mix, p1, p2)
    # Mr. and Mrs. Doe-Yamada
    # Mr. and Mrs. Yamadadoe