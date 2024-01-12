# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        bank = []
        answer = []
        smallest_word = min(strs, key=len)
        for letter in smallest_word:
            bank.append(letter)
        #iterate over the list
        for i in range(len(strs)):
            j = 0
            k = len(bank) #flow -> k = 4
            while j < k:
                if bank[j] == strs[i][j]:
                    answer.append(bank[j])
                if bank[j] != strs[i][j]:
                    j = k
                j += 1
            bank = answer
            answer = []
        return "".join(bank)




sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))