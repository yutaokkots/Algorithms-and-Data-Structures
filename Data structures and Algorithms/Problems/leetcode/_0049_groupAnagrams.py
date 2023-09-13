'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        result = [] 
        # loop through input string
        for word in strs:
        #   sorted_string = sort the string so it is alphabetical
            sorted_string = list(word)
            sorted_string.sort()
            sorted_word = "".join(sorted_string)
            if sorted_word not in memo.keys():
                memo[sorted_word] = []
            memo[sorted_word].append(word)

        # for key, value in memo.items():
        #     result.append(value)
        #   add sorted_string to the memo as a key
        #.  append string as a value of the sorted_string key
        # loop through the memo, and convert back to a list
        return memo.values()
    
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        answer = []
        for str in strs:
            str_lst = list(str)
            str_lst.sort()
            str_new = "".join(str_lst)
            if str_new not in memo:
                memo[str_new] = []
            memo[str_new].append(str)

        for val in memo.values():
            answer.append(val)
        return answer