# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # approach: sliding window to find max substring without repeating chars
        # time complexity: O(n) ; we loop through str once
        # space complexity: O(n) ; worse case scenario all chars are unique, so hash set would be len n

        # use a hash set to track if repeated char has been encountered
        my_set = set()

        # set left pointer (start of window)
        l = 0

        # track maxLength
        maxLength = 0

        # loop through string. R pointer will be set in for loop
        for r in range(len(s)):
            # if repeated char s[r] has been encountered, remove from hash set and update l pointer until we have no repeated chars
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            # add s[r] to hash set and update max
            my_set.add(s[r])
            # find current length: r - 1 + 1 ; array is 0-indexed so we add 1 to get length
            maxLength = max(maxLength, r - l +1) 


        # return result
        return maxLength
