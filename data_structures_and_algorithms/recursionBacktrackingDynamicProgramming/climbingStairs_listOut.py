'''
Climbing Stairs problem, with backtracking practice. 

'''
import time

class ClimbStairs:
    def climb_stairs_bf(self, n):
        def dynaPro(i):
            if i == 0 or i == 1:
                return 1
            one = dynaPro(i - 1)
            two = dynaPro(i - 2)
            return one + two
        return dynaPro(n)
    
    def climb_stairs_tab(self, n):
        one, two = 1, 1
        for _ in range(n - 1):
            temp = two
            two = one + two
            one = temp
        return two
    
    def climb_stairs_bt(self, n):
        ''' Backtracking solution for getting possible steps. 
        
        :type n: int
        "rtype: int
        '''
        answer = []
        permutation = []

        def dynaPro(i):
            if sum(permutation) == n:
                answer.append(permutation.copy())
                return 
            if sum(permutation) >= n:
                return 
            permutation.append(1)
            dynaPro(i + 1)
            permutation.pop()
            permutation.append(2)
            dynaPro(i + 2)
            permutation.pop()
            
        dynaPro(0)
        return answer
            

test_set = [3, 4, 5, 6, 8]
cs = ClimbStairs()

for t in test_set:
    start = time.time()
    ans = cs.climb_stairs_tab(t)
    end = time.time()
    print(f"stairs: {t}, permutations: {ans}")
    print(f"permutations: {cs.climb_stairs_bt(t)}")


'''
stairs: 3, permutations: 3
permutations: [[1, 1, 1], [1, 2], [2, 1]]

stairs: 4, permutations: 5
permutations: [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]

stairs: 5, permutations: 8
permutations: [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [1, 2, 2], [2, 1, 1, 1], [2, 1, 2], [2, 2, 1]]

stairs: 6, permutations: 13
permutations: [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2], [1, 1, 1, 2, 1], [1, 1, 2, 1, 1], [1, 1, 2, 2], [1, 2, 1, 1, 1], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 1, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1], [2, 2, 2]]

stairs: 8, permutations: 34
permutations: [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 1, 2, 1], [1, 1, 1, 1, 2, 1, 1], [1, 1, 1, 1, 2, 2], [1, 1, 1, 2, 1, 1, 1], [1, 1, 1, 2, 1, 2], [1, 1, 1, 2, 2, 1], [1, 1, 2, 1, 1, 1, 1], [1, 1, 2, 1, 1, 2], [1, 1, 2, 1, 2, 1], [1, 1, 2, 2, 1, 1], [1, 1, 2, 2, 2], [1, 2, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 2], [1, 2, 1, 1, 2, 1], [1, 2, 1, 2, 1, 1], [1, 2, 1, 2, 2], [1, 2, 2, 1, 1, 1], [1, 2, 2, 1, 2], [1, 2, 2, 2, 1], [2, 1, 1, 1, 1, 1, 1], [2, 1, 1, 1, 1, 2], [2, 1, 1, 1, 2, 1], [2, 1, 1, 2, 1, 1], [2, 1, 1, 2, 2], [2, 1, 2, 1, 1, 1], [2, 1, 2, 1, 2], [2, 1, 2, 2, 1], [2, 2, 1, 1, 1, 1], [2, 2, 1, 1, 2], [2, 2, 1, 2, 1], [2, 2, 2, 1, 1], [2, 2, 2, 2]]

'''