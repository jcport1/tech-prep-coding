# https://leetcode.com/problems/maximum-odd-binary-number/description/?envType=daily-question&envId=2024-03-01

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        # time complexity: O(n) => for loop to count 1s / operation to construct result string
        # space complexity: O(n) => size of result string

        # approach: in order for binary string to be odd, 1 must be in last position => s[-1] == "1"
        # extract 1s from str; get len of string; add 1 to end, then build string from left to right
        # if num of 1s == 1, then place at end and return str

        # len of s => num of total bits
        n = len(s)

        # num of "1s"
        count = 0

        for bit in s:
            if bit == "1":
                count += 1
        
        # create string: 
        # 1.) place 1s at beginning => (count - 1) because there needs to be a 1 @ end to make binary num odd
        # 2.) add zeros: num of zeros => num of zeros = total num bits - total 1s
        # 3.) add 1 at end of string

        res_string = '1' * (count - 1) + '0' * (n - count) + '1'

        # return result
        return res_string