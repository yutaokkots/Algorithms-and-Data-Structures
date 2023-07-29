from typing import List, Dict

# given a list, "random_nums",
# store the items in 
# an empty dictionary, array_dict, and an empty list, array_list,
# 
# and see how to retrieve them

test = [10, 5, 10, 8, 9, 0, 1, 3, 2, 3, 8, 7, 4, 5, 8, 10, 9, 8, 0, 2, 2, 7, 0, 0, 0, 2, 0, 5, 5, 3, 5, 5, 2, 5, 4, 5, 10, 4, 1, 2, 5, 0, 1, 8, 7, 8, 5, 7, 7, 9, 3, 7, 0, 4, 7, 8, 6, 6, 9, 0, 10, 2, 9, 7, 2, 6, 3, 6, 5, 5, 1, 4, 8, 4, 4, 2, 0, 3, 9, 9, 7, 9, 5, 9, 10, 9, 1, 8, 0, 6, 8, 7, 4, 10, 2, 9, 3, 8, 6, 3, 7, 8, 8, 6, 9, 9, 0, 1, 2, 4, 10, 10, 7, 8, 2, 6, 2, 4, 1, 7, 1, 9, 7, 5, 6, 4, 9, 3, 2, 10, 8, 4, 6, 9, 0, 10, 0, 5, 1, 7, 6, 4, 10, 4, 10, 5, 7, 5, 7, 8, 3, 7, 8, 3, 10, 9, 9, 2, 4, 6, 9, 1, 5, 5, 1, 5, 9, 2, 5, 0, 7, 6, 7, 2, 1, 2, 1, 6, 8, 6, 10, 9, 4, 6, 0, 3, 0, 0, 9, 6, 0, 4, 8, 8, 0, 7, 10, 1, 8, 5, 1, 8, 9, 3, 7, 8, 2, 10, 5, 9, 10, 7, 2, 0, 7, 3, 6, 7, 3, 1, 0, 9, 3, 7, 10, 2, 8, 7, 2, 7, 8, 6, 2, 6, 8, 5, 3, 8, 1, 5, 1, 7, 1, 6, 1, 10, 10, 10, 10, 0, 10, 5, 1, 9, 9, 6, 7, 7, 7, 1, 8, 10, 0, 9, 10, 2, 6, 0, 2, 9, 1, 3, 7, 1, 0, 5, 2, 5, 4, 10, 4, 4, 7, 9, 0, 2, 2, 1, 10, 2, 2, 7, 4, 5, 1, 3, 10, 7, 2, 5]
test2 = [10, 2, 5, 10, 8, 9, 0, 1, 3]

def frequency_dict(lst: List[int]) -> Dict[str, int]:
    freq_dct = {}
    for n in lst:
        if n not in freq_dct.keys():
            freq_dct[n] = 1
        else:
            freq_dct[n] += 1
    return freq_dct

def frequency_list(lst: List[int]) -> List[List[int]]:
   frequency_lst = [[10, 29], [5, 30], [8, 28], [0,27]]
   # frequency_lst = []
   for n in lst:
        # any() True if any in an iterable is true
        # checking to see if 'n' == the subarray[0], while iterating over the list
        if any(n ==  subarray[0] for subarray in frequency_lst):  ##<<<--- any() function
            print("yes")
        else:
            print("no")
       
       
   return frequency_lst

def frequency_list2(lst: List[int]) -> List[List[int]]:
    freq_dct = {}

    for n in lst:
        if n not in freq_dct.keys():
            freq_dct[n] = 1
        else:
            freq_dct[n] += 1

    ### Turn dictionary into list of list[freq., val]
    # Approach 1  ## commented out

    # freq_lst = []
    # for key, value in freq_dct.items():
    #     freq_lst.append([value, key])

    # Approach 2
    freq_lst = [[value, key] for key, value in freq_dct.items()]

    return freq_lst


#print(frequency_dict(test))
#print(frequency_list(test2))
print(frequency_list2(test))
