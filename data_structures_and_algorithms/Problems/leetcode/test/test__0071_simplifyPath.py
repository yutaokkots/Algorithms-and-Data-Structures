'''Test for LC0071 - Simplify Path'''

from unittest import TestCase
from leetcode._0071_simplifyPath import Solution

TEST_CASES = [
    {
        "input": "/home/",
        "output": "/home"
    },
    {
        "input": "/../",
        "output": "/"
    },
    {
        "input": "/home//foo/",
        "output": "/home/foo"
    },
    {
        "input": "home///path/",
        "output": "/home/path"
    },
    {
        "input": "_home///_path/",
        "output": "/_home/_path"
    },
    {
        "input": "//",
        "output": "/"
    },
    {
        "input": "/",
        "output": "/"
    },
    {
        "input": "/a/./b/../../c/",
        "output": "/c"
    },
    {
        "input": "/a/../../b/../c//.//",
        "output": "/c"
    }
]

class TesttLC0071(TestCase):
    ''' Test Case for LC0071, Simplify Path. 

    Given a string path, which is an absolute path (starting with a slash '/') to a file or directory 
    in a Unix-style file system, convert it to the simplified canonical path.

    In a Unix-style file system, a period '.' refers to the current directory, 
    a double period '..' refers to the directory up a level, and 
    any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. 
    For this problem, any other format of periods such as '...' are treated as file/directory names.

    The canonical path should have the following format:

        The path starts with a single slash '/'.
        Any two directories are separated by a single slash '/'.
        The path does not end with a trailing '/'.
        The path only contains the directories on the path from the root directory 
            to the target file or directory (i.e., no period '.' or double period '..')

    Return the simplified canonical path.
    '''
    def setUp(self) -> None:
        self.test_cases = TEST_CASES
        self.sol = Solution()
        return super().setUp()
    
    def tests(self)-> None:
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Test {i + 1}"):
                self.assertEqual(self.sol.simplifyPath(case["input"]), case["output"])