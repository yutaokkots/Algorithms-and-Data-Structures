# 424. Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string 
# and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# # example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# # example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achive this answer too.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        max_val = 0

        left = 0
        for right in range(len(s)):
            hash_map.setdefault(s[right], 0)
            hash_map[s[right]] += 1
            while (right - left + 1) - max(hash_map.values()) > 2:
                hash_map[s[left]] -= 1
                left += 1
            max_val = max(max_val, right-left+1)
        return max_val


questions = {
    "q1": ["ABAB", 2],
    "q2": ["AABABBA", 1]
}

sol = Solution()
for k, v in questions.items():
    print(f"{k}) {sol.characterReplacement(v[0], v[1])}")