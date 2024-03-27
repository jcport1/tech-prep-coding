class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # time complexity: O(m + n)
        # space complexity: O(n) -> result string, two arrays

        # approach: use two pointers

        res = []

        j = 0
        n = len(word2)

        # loop through 1st str & 2nd str, alternate adding char to result str

        for char in word1:
            res += char
            # add char from word2
            if j < n:
                res += word2[j]
                j += 1

        # check if there is any chars left in either 2nd str and then add to result
        while j < n:
            res += word2[j]
            j += 1
        
        return "".join(res)