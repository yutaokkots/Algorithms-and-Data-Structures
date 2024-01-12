#Graphs and breadth-first-search
# Breadth-First-Search (BFS) can be used to find:
# 1) Is there a path from node A to node B?
# 2) What is the shortest path from node A to node B?
# Using Queues -> if a breadth first search is implemented,
#     use a queue to add and search through items that are closest. 

# Suppose the following graph. 
# You at the center. 
# Bob, Claire, Alice located in 1st degree to You
# Peggy, Anuj, Thom, and Jonny located in 2nd degree to you 

# A graph would be implemented as follows:

graph = {}
graph["you"] = ["alice", "bob", "claire"]

#
#      Anuj               Thom
#         \              /
#           Bob     Claire
#          /  \    /    \
#      Peggy    You      Jonny
#            \  |
#              Alice     
#

#In order to implment the above graph in code:
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# // print(graph)
# // graph = {
# //     'you': ['alice', 'bob', 'claire'], 
# //     'bob': ['anuj', 'peggy'], 
# //     'alice': ['peggy'], 
# //     'claire': ['thom', 'jonny'], 
# //     'anuj': [], 
# //     'peggy': [], 
# //     'thom': [], 
# //     'jonny': []
# // }

#In python, use the 'deque' class from 'collections' module
# deque -> "double ended queue"
from collections import deque

#create a new queue by instantiating a deque() class:
#search_queue = deque()

# add the neighbors relative to 'you' into the search queue
#search_queue += graph["you"]

# search condition algorithm:
def person_is_seller(name):
    return name[-1] == 'm'

# Search algorithm:
def search_algorithm():
    search_queue = deque()
    search_queue += graph["you"]
    searched = [] #keep track of which users have been searched
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
    
print(search_algorithm())

#Running Time for BFS
# If you search your entire network, that means you’ll follow each edge 
# (remember, an edge is the arrow or connection from one person to another). 

# So the running time is at least O(number of edges).

# You also keep a queue of every person to search. 
# Adding one person to the queue takes constant time: O(1). 
# Doing this for every person will take O(number of people) total. 
# 
# Breadth-first search takes O(number of people + number of edges), 
# and it’s more commonly written as O(V+E) 
# (V for number of vertices, E for number of edges).
