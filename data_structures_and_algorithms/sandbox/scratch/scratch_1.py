"""Testing an algorithm for efficiency"""
import time
from scratch_1_cases import case_1, case_2, case_3, case_4

class Solution:
    def solutionJ(self, a):
        tree = []
        for i in reversed(range(len(a))):
            if (a[i] == -1):
                a.pop(i)
                tree.append(i)
        a.sort()
        tree.sort()
        for i in range(len(tree)):
            a.insert(tree[i], -1)
        return a
    
    def solutionY(self, a):
        heights = []
        for i in range(len(a)):
            if a[i] != -1:
                heights.append(a[i])
                a[i] = 0

        heights.sort(reverse=True)
        for j in range(len(a)):
            if a[j] == 0:
                a[j] = heights.pop()
        return a
    
    def solutionZ(self, a):
        non_negatives = [x for x in a if x != -1]
        non_negatives.sort(reverse=True)

        for i in range(len(a)):
            if a[i] == 0:
                a[i] = non_negatives.pop()
        return a


def timemeasure(func, **kwargs):
    start = time.time()
    func(case_1)
    func(case_2)
    func(case_3)
    func(case_4)
    end = time.time()
    lapse = end - start
    return lapse

sol = Solution()        
t1 = timemeasure(sol.solutionJ, case_1=case_1, case_2=case_2, case_3=case_3, case_4=case_4)
t2 = timemeasure(sol.solutionY, case_1=case_1, case_2=case_2, case_3=case_3, case_4=case_4)
t3 = timemeasure(sol.solutionZ, case_1=case_1, case_2=case_2, case_3=case_3, case_4=case_4)

print(t1)
print(t2)
print(t3)
