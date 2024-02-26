# https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # time complexity = O(n)

        # two pointers: l, r
        l, r = 0, len(s)-1

        # find mid
        # len(s) == 5, mid = 2, 5 // 2 = integer division (floor) = 2
        mid = len(s) // 2

        # while l < mid and r > mid, swap chars to modify in place
        while l <= mid and r >= mid:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
        