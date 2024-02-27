# https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:

        # time complexity: O(n)
        
        # symbol list with special cases
        # why array instead of hash map? Order matters. We will start building roman numeral string from largest to smallest
        symbol_list = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
                        ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        
        # result string
        res = ""

        for symbol, value in reversed(symbol_list):
            # use integer division. If num is not divisible by value, then result will round to 0 which is false (i.e. num / value will be decimal)
            if num // value:
                # how many times is num divisible by value?
                count = num // value
                # create string
                res += symbol * count
                # update num: get next place in number by moding num by val and extracing remainder
                num = num % value
        
        # return result string
        return res