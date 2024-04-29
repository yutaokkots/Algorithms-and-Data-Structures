'''
399. Evaluate Division
Medium

'''
import collections
from typing import List

####

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
adj = collections.defaultdict(list)
print(adj)

for i, eq in enumerate(equations):
    t, s = eq
    adj[t].append([s, values[i]])
    adj[s].append([t, 1/values[i]])
print(adj)
####


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_lst = collections.defaultdict(list)
        for i, vals in enumerate(equations):
            adj_lst[vals[0]].append([vals[1], values[i]])
            adj_lst[vals[1]].append([vals[0], 1/values[i]])

        def bfs(source, target):
            if source not in adj_lst or target not in adj_lst:
                return -1
            
            queue = collections.deque()
            queue.append([source, 1])
            visited = set()
            visited.add(source)

            while queue:
                n, w = queue.popleft() #n = neighbor, w = weight
                if n == target:
                    return w
                for neighbor, weight in adj_lst[n]:
                    if neighbor not in visited:
                        queue.append([neighbor, w * weight])
                        visited.add(neighbor)
            return -1
        return [bfs(q[0], q[1]) for q in queries]
