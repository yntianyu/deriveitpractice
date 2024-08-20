# Given an array of strings arr, return an array where all strings with the same anagram are grouped together. All the strings are made of lowercase characters "a" through "z".

# We recommend solving the previous problem "Validate Anagrams" first.

def groupAnagrams(arr):

    groups = {}

    for aString in arr:
        stringMap = [0]*26

        for letter in aString:
            place = ord(letter) - ord('a')
            stringMap[place] += 1
        
        tup = tuple(stringMap)
        
        if tup in groups:
            groups[tup].append(aString)
        else:
            groups[tup] = [aString]

    return groups.values()


groupAnagrams(['baa', 'aab', 'cab', 'bad', 'abd', 'dab'])
groupAnagrams(['aab', 'aba', 'abb', 'aba'])
groupAnagrams(['a'])

# Time complexity: O(n*m) where n is the number of strings in the array and m is the length of the longest string
# Space complexity: O(n*m) where n is the number of strings in the array and m is the length of the longest string