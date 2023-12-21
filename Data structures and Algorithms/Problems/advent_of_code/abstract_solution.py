""" Abstract class for the solution class for solving a problem."""
from abc import ABC, abstractmethod
from importer import FileReader
from typing import List

class Solution(ABC):
    """Solution class for importing a problem set and executing a solution."""
    def __init__(self, problem_path: str):
        self.problem_set: List[str] = self.load_problem_set(problem_path)
    
    @abstractmethod
    def solution(self):
        ...

    def load_problem_set(self, problem_path: str) -> List[str]:
        fr = FileReader()
        fr.load(problem_path)
        return fr.get()