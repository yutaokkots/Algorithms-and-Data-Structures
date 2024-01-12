# Dijkstra's Algorithm

# suppose: an algorithm to get from point A to point B
# first graph:
# (unweighted graph)
#              ()------()
#             /      / |  \
# (Twin Peaks)     ()  |   (Golden Gate Bridge)
#             \   /    |
#              ()------()  
#
# second graph with the time it takes to travel:
#(weighted graph)
#                 21min
#              ()------()
#         4min/     5/ |  \4min
# (Twin Peaks)     ()  |   (Golden Gate Bridge)
#             \  5/  12|
#              ()------()  
#                 8min
#
# BFS (first graph) will allow finding the shortest path
# Dijkstra's algorithm (second graph) will allow finding the fastest path

# To calculate the shortest path in an unweighted graph, use breadth-first search. 
# To calculate the shortest path in a weighted graph, use Dijkstra’s algorithm

# Dijkstra's algorithm 
# 1. Find the “cheapest” node;  
#    the node you can get to in the least amount of time.
# 2. Check whether there’s a cheaper path to the neighbors of this node.
#    Update the costs of the neighbors of this node. 
# 3. Repeat until you’ve done this for every node in the graph.
# 4. Calculate the final path.


# given the following directional graph, how to acquire the piano
# in the cheapest way by trading through the items?
#             LP   $15   guitar
#              ()------>()
#          $5 /    \ /^$30 \$20
#(start)book()      X       () piano (finish)
#           $0\    / \$20 /$10
#      poster ()------->() drumset 
#                 $35
#
# use the four steps, and record in a table. initial setup:
#
#  PARENT  NODE    COST
#  Book    LP      5
#  Book    poster  0
#   -      guitar  inf <- set as infinite, because nodes haven't been reached yet
#   -      drums   inf <- set as infinite
#   -      piano   inf <- set as infinite
#
# 1. Find the “cheapest” node;  
#    the node you can get to in the least amount of time.
# The poster is the cheapest trade. 

# 2. figure out how long it takes to get to its neighbors (the cost) 
# Check whether there’s a cheaper path to the neighbors of this node:
#
#  PARENT  NODE    COST
#  Book    LP      5
#  Book    poster  0
#  *poster guitar  del(inf) -> 30
#  *poster drums   del(inf) -> 35
#   -      piano   inf
#
# Step 1 again: The LP is the next cheapest node
# Step 2 again: Update the values of all of its neighbors

#  PARENT  NODE    COST
#  Book    LP      5
#  Book    poster  0
#  *LP     guitar  del(30) -> 20
#  *LP     drums   del(35) -> 25 
#   -      piano   inf
#
# the guitar is the next cheapest item,
# so update its neighbors:

#  PARENT  NODE    COST
#  Book    LP      5
#  Book    poster  0
#  *LP     guitar  20
#  *LP     drums   25 
#  guitar  piano   40
#
# trading the drums for the piano is even cheaper:
#  PARENT  NODE    COST
#  Book    LP      5
#  Book    poster  0
#  *LP     guitar  20
#  *LP     drums   25 
#  drums   piano   35

# how to figure out the path? Look at the PARENT column
# piano -> drums -> LP -> Book

