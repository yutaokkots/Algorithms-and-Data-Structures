from _2381_shiftingLettersII import Solution, s1, s2, shifts1, shifts2, a1, a2
import pytest


@pytest.fixture
def solution():
    return Solution()

def test_shiftingLetters(solution):
    assert solution.shiftingLetters("abc", [[0,1,0],[1,2,1],[0,2,1]]) == "ace"
    assert solution.shiftingLetters("dztz", [[0,0,0],[1,1,1]]) == "catz"
    assert solution.shiftingLetters(s1, shifts1) == a1
    assert solution.shiftingLetters(s2, shifts2) == a2