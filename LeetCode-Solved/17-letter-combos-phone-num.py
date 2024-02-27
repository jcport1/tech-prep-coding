# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letterCombinations(self, digits: str):

        # strategy: build string recursively using backtracking function
        # base case: created string == len(digits)

        # time complexity: O(4^n), example = "999" = 4 x 4 x 4

        # create hash map
        digits_hash = {"2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "pqrs",
                        "8": "tuv",
                        "9": "wxyz"
                        }

        # results array
        res = []

        # back tracking
        def backtracking(i, curStr):
            # base case
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            # recursive call
            for char in digits_hash[digits[i]]:
                # update recursive call: increment i and append char to curStr
                backtracking(i+1, curStr+char)
        
        # if digits is empty, return []
        # without this if statement, empty digit string will return [""]
        if digits:
            backtracking(0, "")
        
        # return result
        return res