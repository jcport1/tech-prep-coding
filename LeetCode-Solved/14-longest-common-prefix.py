# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs) -> str:

        # keep track of longest prefix
        res = []
        
        # we only need to check str a against str b and str c, because by transitive property
        # if b = a, and c = a, then b = c

        # loop through one of the strings (arbitarily)
        for i in range(len(strs[0])):
        # then loop through arr strs and check to see if letters are same for each str, otherwise return
            for str in strs:
                # make sure that curr str index is within bounds, otherwise return
                if i == len(str) or str[i] != strs[0][i]:
                    return "".join(res)
            # if all letters the same increment result str
            res.append(strs[0][i])

        # return result string
        my_string = "".join(res)
        return my_string