'''
886. Possible Bipartition
Medium

We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group has [1,4], and the second group has [2,3].

Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.

Example 3:
Input: n=10, dislikes = [[1,2],[3,4],[5,6],[6,7],[8,9],[7,8]]
Output: true

'''
import collections

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        default_dict = collections.defaultdict(list)

        for person_A, person_B in dislikes:
            default_dict[person_A].append(person_B)
            default_dict[person_B].append(person_A)

        group = {i: None for i in range(1, n + 1)}

        def dfs(node, g):
            if not group[node]:
                group[node] = g
            else:
                return group[node] == g

            for people in default_dict[node]:
                if not dfs(people, 2 if g == 1 else 1):
                    return False
            return True

        for n in range(1, n + 1):
            if not group[n] and not dfs(n, 1):
                return False

        return True