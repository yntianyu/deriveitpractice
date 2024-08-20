#Given an array arr, reverse the array.

#You should solve this problem in-place, without creating a new Array.

def reverseArray(arr):
    l = 0
    r = len(arr) - 1

    while r > l:
        arr[l], arr[r] = arr[r], arr[l]

        l += 1
        r -= 1
    
    return arr


reverseArray([1, 2, 3])
reverseArray([1, 2, 2, 3])
reverseArray([1, 3, 2])

# Time complexity: O(n)
# Space complexity: O(1)