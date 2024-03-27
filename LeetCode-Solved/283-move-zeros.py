# https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # time complexity: O(n)

        # approach: two pointers
        # move non-zeros to left of arr, zeros to right of arr

        # initialize left pointer
        l = 0

        # use right pointer to scan through array searching for non-zeros
        for r, num in enumerate(nums):
            # if r finds non-zero num swap with l pointer & increment l
            if num != 0:
                # swap
                temp = nums[l]
                nums[l] = num
                nums[r] = temp
                l += 1