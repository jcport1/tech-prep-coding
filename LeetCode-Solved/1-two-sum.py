# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums, target: int):

        # time complexity: O(n)

        my_hash = {}

        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in my_hash:
                return [i, my_hash[compliment]]

            my_hash[num] = i
        