# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findDifference(self, nums1, nums2):
        
        # approach: use hash sets
        # time complexity: O(m + n)
        # space complexity: O(m + n)

        # create two sets
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        # create answer arr
        res = [[],[]]

        # loop through set 1
        for num in nums1_set:
            # if num not in set2; add to num1 subarr ans
            if num not in nums2_set:
                res[0].append(num)
        
        # loop through set 2
        for num in nums2_set:
            # if num not in set2; add to num1 subarr ans
            if num not in nums1_set:
                res[1].append(num)
        
        #return answer arr
        return res


        # other possible solution: use set operations
        # subarr1 = list(nums1_set - nums2_set)
        # subbar2 = list(nums2_set - nums1_set)
        # return [subarr1, subarr2]