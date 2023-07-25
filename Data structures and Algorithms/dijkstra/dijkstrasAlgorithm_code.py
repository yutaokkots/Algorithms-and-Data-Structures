# Given the following weighted graph, find the 
# smallest route:
#
#          (A)
#      6 /  ^  \ 1
# START()   |3   ()END
#      2 \  |  / 5
#          (B)

# need three hashtables
graph = {}
costs = {}
parents = {}

##### graph hash table ####
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {} 
graph["a"]["end"] = 1
graph["b"] = {} 
graph["b"]["a"] = 3 
graph["b"]["end"] = 5
graph["end"] = {}

print(graph)
# graph = {
#     'start': {
#         'a': 6, 
#         'b': 2
#         }, 
#     'a': {
#         'end': 1
#         }, 
#     'b': {
#         'a': 3, 
#         'end': 5
#         }, 
#     'end': {}
#     }

##### costs hash table ####
# represent infinity in python
infinity = float("inf")
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity

print(costs)
# costs = {
#   'a': 6, 
#   'b': 2, 
#   'end': inf
# }

##### parents hash table ####
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

print(parents)
# parents = {
#   'a': 'start', 
#   'b': 'start', 
#   'end': None
# }

##### array to keep track of all nodes ####
processed = []

##### Basic algorithm ####
# While we have nodes to process    <--------
#    |                                       |
# Grab node that is closest to start         |
#    |                                       |
# Update costs for its neighbors             |
#    |                                       |
# If any of neighbor's costs were updated,   |
# update parents too                         |
#    |                                       |
# mark this node as processed ---------------