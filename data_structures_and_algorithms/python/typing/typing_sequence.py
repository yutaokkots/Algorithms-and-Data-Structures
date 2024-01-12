"""Sequence typing in Python."""
from typing import Sequence

def seq_reader(seq:Sequence[int]) -> None:
    print(seq)

seq1 = (1, 2, 3, 4)
seq2 = [1, 2, 3, 4]

seq_reader(seq1)
seq_reader(seq2)