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
        
        #[index, distance from c]
        for i in range(len(s)):
            if s[i] == c:
                latest_c_index = i
                stack.append([i, 0])
            else:
                if latest_c_index == None:
                    stack.append([i, None])
                else:
                    stack.append([i, abs(latest_c_index - i)])  
            if s[i] == c or i == len(s) - 1:
                if stack:
                    while stack:
                        popped_element = stack.pop()
                        if popped_element[1] == 0:
                            pass
                        elif popped_element[1] == None:
                            diff = abs(latest_c_index - popped_element[0])
                            popped_element[1] = diff
                        else:
                            popped_element[1] = min(abs(latest_c_index - popped_element[0]), popped_element[1])
                        answer.append(popped_element)
        answer.sort()

        return [list[1] for list in answer]
    

sol = Solution()
print(sol.shortestDistance("loveleetcode", "e"))
print(sol.shortestDistance("aaab", "b"))
