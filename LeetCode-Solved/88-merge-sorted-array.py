# https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # len of nums1 = m + n

        # method 1: two pointers

        # time complexity = O(m+n)

        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        
        # edge case: m = 0
        while n > 0:
            nums1[m+n-1] = nums2[n-1]
            n -= 1

        # method 2: 
        # time complexity = O(n log n)

        # # loop throughs num2
        # for i, num in enumerate(nums2):
        #         # add nums2 to nums1
        #         nums1[m+i] = num

        # # sort nums 1 then return nums1
        # nums1.sort()