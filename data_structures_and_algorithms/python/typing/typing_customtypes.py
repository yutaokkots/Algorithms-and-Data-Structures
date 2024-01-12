"""Describes custom type creation in Python"""
from typing import List, Dict, Set

Vector = List[float]
Vectors = List[Vector]

v1:Vector = [0.5, 2.2, 5.2, -4.0]
v2:Vector = [1.5, 1.3, 4.8, -3.0]

def vector_sum(vector1:Vector, vector2:Vector) -> Vector:
    return list(map(sum, zip(vector1, vector2)))

def vector_combine(vector1:Vector, vector2:Vector) -> Vectors:
    return [vector1, vector2]

a = vector_sum(v1, v2)
print(a)

b = vector_combine(v1, v2)
print(b)