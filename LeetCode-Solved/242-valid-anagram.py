# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # time complexity = O(n)
        # space complexity = O(n)

        # first check if strings are equal, if so proceed. Otherwise return false
        if len(s) != len(t):
            return False

        # create hashmap: with key set to letter and value set to frequency
        # intuition: anagrams have same string length, same letters with same frequency

        s_hashmap = {}
        t_hashmap = {}

        # loop through s
        for char in s:
            # add key/update frequency
            # get method on hashmap returns default value if key not found
            s_hashmap[char] = 1 + s_hashmap.get(char, 0)


        # loop through t
        # add key/update frequency
        for char in t:
            t_hashmap[char] = 1 + t_hashmap.get(char, 0)

        # return if hashmaps are equal 
        # alternatively loop through each key in hashmap s and see if key exists in hashmap t and values are same
        return s_hashmap == t_hashmap
        