"""Test Case for LC394 - Decode Strings."""
from unittest import TestCase
from leetcode._0394_decodeStrings import Solution

TEST_CASES = [
    {
        "s" : "3[a]2[bc]",
        "answer": "aaabcbc"
    },
    {
        "s" : "3[a2[c]]",
        "answer": "accaccacc"
    },
    {
        "s" : "2[abc]3[cd]ef",
        "answer": "abcabccdcdcdef"
    },
    {
        "s" : "2[abc]ef3[c2[k]d]",
        "answer": "abcabcefckkdckkdckkd"
    }
]

class TestLC394(TestCase):
    def setUp(self):
        self.test_cases = TEST_CASES
        self.sol = Solution()
    
    def test_cases(self):
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Test {i + 1}"):
                self.assertEqual(self.sol.decodeString(case["s"]), case["answer"])