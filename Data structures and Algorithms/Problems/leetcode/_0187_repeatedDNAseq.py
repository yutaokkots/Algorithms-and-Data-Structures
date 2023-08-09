# 187. Repeated DNA Sequences

# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

#Example 1:
# Input: s "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

#Example 2:
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]

#Example 3:
# Input: s = "AAAAAGGGTTACTGACTGACTGACTGACTGACTGACAAAAAGGGTT"
# Output: ["ACTGACTGAC", "AAAAAGGGTT"]

from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        record = {}
        left = 0
        right = 9
        result = set()

        while right < len(s):
            substring = s[left:right+1]
            record[substring] = 1 + record.get(substring, 0)
            if record[substring] > 1:
                result.add(substring)
            right += 1
            left += 1

        return list(result)
    
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        record, result = set(), set()

        for i in range(len(s) - 9):
            substring = s[i: i+10]
            if substring in record:
                result.add(substring)
            else:
                record.add(substring)
        return list(result)