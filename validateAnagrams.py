# Given lowercase strings s and t, return whether the strings are anagrams of each other.

# Two strings are anagrams if the letters of one string can be rearranged into the letters of the other string.

def areAnagrams(s, t):
    smap = {}
    tmap = {}

    for letter in s:
        if letter in smap:
            smap[letter] += 1
        else: 
            smap[letter] = 1
    
    for letter in t:
        if letter in tmap:
            tmap[letter] += 1
        else:
            tmap[letter] = 1

    return smap == tmap


areAnagrams('keen', 'knee')
areAnagrams('baa', 'bba')
areAnagrams('baa', 'aba')

# Time complexity: O(n)
# Space complexity: O(n)