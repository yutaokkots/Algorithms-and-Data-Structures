graph = {}
graph["you"] = ["alice", "bob", "claire"]

#
#      Anuj               Thom
#         \              /
#           Bob     Claire
#          /  \    /    \
#       Peggy   You      Jonny
#          \     |
#            Alice     
#

#In order to implment the above graph in code:
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(graph)
# // graph = {
# //     'you': ['alice', 'bob', 'claire'], 
# //     'bob': ['anuj', 'peggy'], 
# //     'alice': ['peggy'], 
# //     'claire': ['thom', 'jonny'], 
# //     'anuj': [], 
# //     'peggy': [], 
# //     'thom': [], 
# //     'jonny': []}