'''Test for LC0433 - Minimum Genetic Mutation.'''

from unittest import TestCase
from leetcode._0433_minimumGeneticMutation import Solution

TEST_CASES = [
    {
        "startGene": "AACCGGTT",
        "endGene": "AACCGGTA",
        "bank": ["AACCGGTA"],
        "output": 1
    },
    {
        "startGene": "AACCGGTT",
        "endGene": "AAACGGTA",
        "bank": ["AACCGGTA","AACCGCTA","AAACGGTA"],
        "output": 2
    },
    {
        "startGene": "AACCGGTT",
        "endGene": "ATACGGTA",
        "bank": ["AACCGGTA","AACCGCTA","AAACGGTA"],
        "output": -1
    },
    {
        "startGene": "TTCTTAGA",
        "endGene": "ATGTACTA",
        "bank": ["TTCTAAGA", "TTGTAAGA", "ATGTAAGA", "ATGTAATA", "ATGTACTA"],
        "output": 5
    },
    {
        "startGene": "TTCTTAGA",
        "endGene": "ATGTACTA",
        "bank": ["TTCTAAGA", "TTGTAAGA", "ATGTAATA", "ATGTACTA"],
        "output": -1
    },
]

class TestLC0433(TestCase):
    ''' Test for LC0433 - Minimum Genetic Mutation

    A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

    Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene 
    where one mutation is defined as one single character changed in the gene string.

    For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
    There is also a gene bank bank that records all the valid gene mutations. 
    A gene must be in bank to make it a valid gene string.

    Given the two gene strings startGene and endGene and the gene bank bank, 
    return the minimum number of mutations needed to mutate from startGene to endGene. 
    If there is no such a mutation, return -1.     
    '''
    def setUp(self) -> None:
        self.test_cases = TEST_CASES
        self.sol = Solution()
        return super().setUp()

    def test(self) -> None:
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Test {i+1}"):
                self.assertEqual(
                    self.sol.minMutation(
                        startGene=case["startGene"], 
                        endGene=case["endGene"], 
                        bank=case["bank"]
                    ),
                    case["output"]
                )
            