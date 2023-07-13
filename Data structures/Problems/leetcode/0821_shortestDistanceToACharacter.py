# Given a string, 's', and a character, 'c', that occurs in s,
# return an array of integers, 'answer', where
# answer.length == s.length and answer[i] is the distance from index, 'i'
# to the closest occurence of character c in s


class Solution:
    def shortestDistance(self, s: str, c: str ) -> list[int]:

        # example 1
        # input s = "loveleetcode"
        # input c = "e"
        # output = [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
        # analysis-[l, o, v, e, l, e, e, t, c, o, d, e]
        # answer[i] is the closest occurence from c

        # possible to use a stack to keep track of the closest from letter c
        # answer_stack = [[0, -1], [1, -1], [2, -1],     ]
        #                                           [3, 0]
        #                                  [2, -1] = answer_stack.pop()    
        #                                  [2, 1] // index of c - popped[0]
        #                           [1, -1] = answer_stack.pop()
        #                           [1, 2] index of c - popped[0]
        #                 [0, -1] = answer_stack.pop()
        #                 [0, 3] index of c - popped[0]
        # answer_stack = []
        # answer_stack = [[4, 1] ] check to see where latest c is located /// use a counter?
        #                  [4, 1] = answer_stack.pop()  vs [5, 0]
        #                   [4, 1] if current index of c - popped[0] > popped[1], then use former

        latest_c_index = None
        stack = []
        answer = []

        for i in range(len(s)):

            if s[i] == c and stack:
                latest_c_index = i
                while stack:
                    popped_letter = stack.pop()
                    if popped_letter[1] == -1 or abs(popped_letter[0] - latest_c_index) < popped_letter[1]:
                        popped_letter[1] = latest_c_index - popped_letter[0]
                    answer.append(popped_letter)
                answer.append([i, 0])
            elif s[i] == c:
                latest_c_index = i
                answer.append([i, 0])

            if s[i] != c and latest_c_index == None: ## if the current letter is not c AND the c_index has not been found
                stack.append([i, -1])
            
            if s[i] != c and latest_c_index: ## if the current letter is not c AND the c_index has been found, latest_c_
                stack.append([i, abs(latest_c_index - i)])

        answer.sort()

        return [list[1] for list in answer]
    

sol = Solution()
print(sol.shortestDistance("loveleetcode", "e"))
print(sol.shortestDistance("aaab", "b"))
