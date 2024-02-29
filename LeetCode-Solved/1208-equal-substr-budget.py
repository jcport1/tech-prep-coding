# https://leetcode.com/problems/get-equal-substrings-within-budget/description/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        # approach = sliding window
        # time complexity = O(n)
        # space complexity = O(1)

        l, totalCost, maxLen = 0, 0, 0

        for r in range(len(s)):
            # find absolute diff between ith char in s and ith char in t

            # subtract abs diff from cost var
            totalCost += abs(ord(s[r]) - ord(t[r]))

            # if totalCost exceeds maxCost, budget has been depleted. move the left pointer and update totalCost until totalCost > maxCost
            while totalCost > maxCost:
                # reset totalCost (subtract cost of left pointer)
                totalCost -= abs(ord(s[l]) - ord(t[l]))
                # shift window 1 to the left
                l += 1
            maxLen = max(maxLen, r-l+1)
        
        # get length of valid substring and return result (i.e. length of window)
        return maxLen