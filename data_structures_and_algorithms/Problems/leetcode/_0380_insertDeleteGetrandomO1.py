"""380. Insert Delete GetRandom O(1)"""

from collections import defaultdict
import random

class RandomizedSet:
    """Randomized Set class - naive solution.
    
    Methods
    -------
    insert(val:int) -> bool
        O(1)
    remove(val:int) -> bool
        O(1)
    getRandom() -> int
        O(1)
    """

    def __init__(self):
        self.randomized_set = {}
        self.items = []

    def insert(self, val: int) -> bool:
        if val not in self.randomized_set:
            self.randomized_set[val] = len(self.items)
            self.items.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.randomized_set:
            last_val = self.items[-1]
            idx_to_remov = self.randomized_set[val]

            self.items[idx_to_remov] = last_val
            self.randomized_set[last_val] = idx_to_remov
            
            del self.randomized_set[val]
            self.items.pop()
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return random.choice(self.items)


class RandomizedSet2:
    """Randomized Set class.
    
    Methods
    -------
    insert(val:int) -> bool
        O(1)
    remove(val:int) -> bool
        O(1)
    getRandom() -> int
        O(N)
    """

    def __init__(self):
        self.randomized_set = {}

    def insert(self, val: int) -> bool:
        status = self.randomized_set.get(val, False)
        self.randomized_set[val] = True
        return not status

    def remove(self, val: int) -> bool:
        status = self.randomized_set.get(val, False)
        if status:
            del self.randomized_set[val]
        return status
        
    def getRandom(self) -> int:
        return random.choice(list(self.randomized_set.keys()))


rand_set = RandomizedSet()
rand_set.insert(5)
rand_set.insert(5)
rand_set.remove(5)
rand_set.remove(5)
rand_set.remove(3)
rand_set.insert(3)
rand_set.insert(2)
rand_set.insert(4)
rand_set.remove(4)
rand_set.remove(4)
rand_set.insert(5)
rand_set.insert(5)
a = rand_set.getRandom()
print(a)

# test case:

# ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
# [[],[0],[1],[0],[2],[1],[]]