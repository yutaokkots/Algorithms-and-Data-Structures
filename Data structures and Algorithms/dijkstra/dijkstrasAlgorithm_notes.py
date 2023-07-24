# Dijkstra's Algorithm

# suppose: an algorithm to get from point A to point B
# first graph
#
#              ()------()
#             /      / |  \
# (Twin Peaks)     ()  |   (Golden Gate Bridge)
#             \   /    |
#              ()------()  
#
# second graph with times
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