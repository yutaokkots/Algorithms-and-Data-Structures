import collections
from datetime import datetime as dt

nums = [1, 2, 1, 2, 3, 2, 3, 5, 2, 12, 1, 1, 13, 12, 23, 98, 3, 3, 3, 4, 5, 23, 1,1,1,2,2,3,4,5,3,3,2,5,5,5,1,5,12, 98, 2, 1, 1, 13, 12, 23, 97, 3, 3, 3, 4, 5, 23, 1,1,1,2,2,3,33,23,56,-1]

#####################
## measuring execution time for creating a collections.Counter()
## -> creates a dictionary of frequencies

### START TIME ###
start = dt.now()

count_nums = collections.Counter(nums)

###  END TIME ###
end = dt.now()

### execution time
et = end - start
print(f"The operation (collections.count) took: \n{et * 10**3} ms")

#####################
## measuring execution time for creating a hashmap of frequencies, O(N) time
## 

### START TIME ###
start = dt.now()

nums_dict = {}
for num in nums:
    if num not in nums_dict.keys():
        nums_dict[num] = 1
    else:
        nums_dict[num] += 1

###  END TIME ###
end = dt.now()

### execution time
et = end - start
print(f"The operation (creating a count dict) took: \n{et * 10**3} ms")

# The operation (collections.count) took: 
# 0:00:00.030000 ms
# The operation (creating a count dict) took: 
# 0:00:00.017000 ms
