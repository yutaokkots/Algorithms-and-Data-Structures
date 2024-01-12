# Given a smaller string s and a bigger string b, design an algorithm to find all permutations
# of the shorter string with the longer one. 
# print the location of each permutation. 

# example
# substr = "abbc"
# str = "cbabadcbbabbcbabaabccbabc"
# output: 0, 6, 9

substr = "abbc"
str = "cbabadcbbabbcbabaabccbabc"

class Solution():
    def find_substring_slidingwindow(self, str, substr):
        substr_lst = list(substr) 
        left = 0
        answer = []
        # generally, time complexity of O(M+N)
        while left < len(str) - 3:
            window = list(str[left:left+4])
            window.sort()       # O(NlogN)
            if substr_lst == window:
                answer.append(left)
            left += 1
        print(answer)

sol = Solution()
sol.find_substring_slidingwindow(str, substr)

