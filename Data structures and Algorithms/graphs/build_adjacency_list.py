'''
Potential way to build an adjacency list

'''
prerequisites = [[3,2],[2,1],[2,0]]

def adj_lst(prerequisites):
        adj_lst = {}
        for a, b in prerequisites:
            adj_lst[a] = adj_lst.setdefault(a, set())
            adj_lst[a].add(b)
            if b not in adj_lst:
                adj_lst[b] = set()