from _0771_jewelsAndStones import Solution
import pytest

#fixtures in pytest -> initialize test functions, to provide a fixed baseline

#pytest fixture
@pytest.fixture
def solution():
    return Solution()

def test_numJewelsInStones(solution):  
    assert solution.numJewelsInStones("aA", "aAAbbbb") == 3
    assert solution.numJewelsInStones("z", "ZZ") == 0

# # without fixture:
# def test_numJewelsInStones():  
#     solution = Solution() ##<- instantiate Solution class from imported file.
#     assert solution.numJewelsInStones("aA", "aAAbbbb") == 3
#     assert solution.numJewelsInStones("z", "ZZ") == 0