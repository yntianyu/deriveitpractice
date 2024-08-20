# Given an array of integers nums, return whether there are any duplicates.

def hasDuplicate(nums):
    seenNums = set()

    for i in nums:
        if i in seenNums: 
            return True
        seenNums.add(i)
    return False


hasDuplicate([])
hasDuplicate([7])
hasDuplicate([7,7])

# Time complexity: O(n)
# Space complexity: O(n)