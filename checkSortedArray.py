# Given an array of integers arr, return whether the array is sorted in ascending order.

def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i + 1]:
            return False
            
    return True


isSorted([1, 2, 3])
isSorted([1, 2, 2, 3])
isSorted([1, 3, 2])

# Time complexity: O(n)
# Space complexity: O(1)