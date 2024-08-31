#Given a string s, return whether the string is a palindrome.

#A "palindrome" is a string that's the same forwards and backwards.

def isValid(s):
    l = 0
    r = len(s) - 1

    while l <= r:
        if s[l] != s[r]:
            return False
        
        l += 1
        r -= 1
        
    return True


isValid('racecar')
isValid('a')
isValid('ab')

# Time complexity: O(n)
# Space complexity: O(1)