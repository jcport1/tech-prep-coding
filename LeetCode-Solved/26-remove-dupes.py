# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums):
        
        # time complexity: O(n)

        # approach: two pointers

        # left pointer keeps track of where to insert unique value
        # right pointer scans the array

        # initialize to 1, because element at index 0 will always take first pos in modified arr

        # example: [0,0,0,1]
        l = 1
        
        for r in range(1, len(nums)):
            # if unique element found, update arr in place
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        
        # left pointer will also tell us the len (because we increment every time we see unique val)
        return l