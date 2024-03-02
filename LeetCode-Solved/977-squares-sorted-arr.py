# https://leetcode.com/problems/squares-of-a-sorted-array/description/?envType=daily-question&envId=2024-03-02

class Solution:
    def sortedSquares(self, nums):
        
        # approach: use two pointers to populate arr from smallest to largest in non-decreasing order (ascending)

        """The largest squared number could originate from either end of the original array 
        due to the presence of negative numbers, whose squares can be large
        Thus, we just need to make a comparsion between 
        these two ends to add the correct squared number into the result array """

        # time complexity: O(n)
        # space complexity: O(n)

        # create result array
        n = len(nums)
        res_arr = [0] * n

        # create l, r pointers
        start, end = 0, n-1

        # loop through arr with two pointers 
        while start <= end:
            # if squared neg int at start is >= positive int at end
            # append squared neg int to end of res_arr
            if abs(nums[start]) >= abs(nums[end]):
                res_arr.append(nums[start] ** 2)
                # increment start pointer
                start += 1
            else:
                res_arr.append(nums[end] ** 2)
                # decrement end pointer
                end -= 1
        
        return res_arr[::-1] # [::-1] is commonly used to reverse the order of an list in python: O(n)