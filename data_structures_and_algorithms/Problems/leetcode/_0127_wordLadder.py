'''
127. Word Ladder
Hard

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.

        #["hot","dot","dog","lot","log","cog"]]
        # "hit" -> "cog"
        # output: "hit" -> "hot" -> "dot" -> "dog" -> cog"
        # output: 5 ## did not use "lot", "log"

        #["hot","dot","dog","lot","log","cog", "hit"]]
        # beginWord = "hit"

        #["hot","dot","dog","lot","log"]
        # output -> 0
        # bfs -> 
'''

import collections
from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int: 
        if endWord not in wordList:
            return 0

        adj_lst = defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i + 1:]
                adj_lst[pattern].append(w)
        
        q_word = deque([beginWord])
        counter = 1
        visited = set([beginWord])

        while q_word:
            for _ in range(len(q_word)):
                word = q_word.popleft()
                if word == endWord:
                    return counter
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for next_word in adj_lst[pattern]:
                        if next_word not in visited:
                            q_word.append(next_word)
                            visited.add(next_word)

            counter += 1

        return 0

class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def is_adjacent(w1, w2):
            diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        if endWord not in wordList:
            return 0

        queue = collections.deque([(beginWord, 1)])

        while queue:
            current_word, level = queue.popleft()

            if current_word == endWord:
                return level

            for next_word in list(wordList):
                if is_adjacent(current_word, next_word):
                    queue.append((next_word, level + 1))
                    wordList.remove(next_word)

        return 0

