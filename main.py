arr = [10,8,3,2,1]

def selection_sort(arr):

    # Iterate through array several times, [finding the minimum] and placing it in the "beginning",
    # which will be the right-most position of the [sorted sub-array with the previous minimum elements]
    for i in range(len(arr)):

        # Start with the first index in the current loop as the min_index.
        min_index = i

        # Iterate through the rest of the array
        for j in range(i+1,len(arr)):
            #If it finds a lesser value, set the MIN_INDEX to the current INDEX (J)
            if arr[j] < arr[min_index]:
                min_index = j
        # Once it's done, it has the INDEX of the new min value.
        # Use the Index to place the item in the end of the sorted sub-array
        # by swapping the first item in the current outer loop with the item with the min_value.
        arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(arr)
print(arr)



