# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:


        # time complexity: O(n)
        # space complexity: O(1) -> roman_hash not depended on size s

        result = 0

        roman_hash = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}

        # "IX" = 9
        # subtract element if next element is larger
        # add element if next element is smaller

        # iterate through the string of roman numeral
        for i in range(len(s)):
            # first check if i + 1 is in bounds 
            if i+1 < len(s) and roman_hash[s[i+1]] > roman_hash[s[i]]:
                result -= roman_hash[s[i]]
            else:
                result += roman_hash[s[i]]

        return result
        