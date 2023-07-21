# Selection Sort:
# 1. loop through the array, and for each index, run another function to find the index of the smallest number 
# 2. use that index to pop the array from the origin array, and append to a new array. 

# Time complexity:
# O(n^2)
class SelectionSort:
    def findSmallest(self, arr):
        smallest = arr[0]           #stores the smallest value
        smallest_index = 0          #stores the index of the smallest value
        for i in range(1, len(arr)):
            if arr[i] < smallest:   # if the current element is smaller than the 'smallest', then
                smallest = arr[i]   # make 'smallest' equal to this element
                smallest_index = i  # make 'smallest_index' equal to this element's index
        return smallest_index
    # 'findSmallest(arr)' -> takes array,  

    def selectionSort(self, arr):
        newArr = []
        for i in range(len(arr)):
            smallest = self.findSmallest(arr)
            newArr.append(arr.pop(smallest))    ## KEY -> pops out (removes) the smallest item from the original array and appends to 'newArr'
        return newArr


selection_sort = SelectionSort()
example_1 = [5, 3, 6, 2, 10]

print(selection_sort.selectionSort(example_1))

