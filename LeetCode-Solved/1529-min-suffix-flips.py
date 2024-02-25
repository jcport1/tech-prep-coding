# https://leetcode.com/problems/minimum-suffix-flips/description/

class Solution:
    def minFlips(self, target: str) -> int:
        
        # key: min flips is equal to flips that occurs between t[i] and its predecesor

        # time complexity = O(n)
        # space complexity = O(1)

        flip_counts = 0
        # set prev to zero since we always start with zero in str s
        prev = "0"

        # loop through c and count number of flips
        # if flip occurs, set prev equal to c; this essentially signifies that all bits in range s[idx of c] - s[-1] 
        # have been flipped
        for c in target:
            # if c and s[idex of c] are different (remeber prev == s[index of c]) then count a flip
            # and set prev == c, which are new bits for s[idex of c] - s[-1]
            if c != prev:
                flip_counts += 1
                prev = c
        
        return flip_counts