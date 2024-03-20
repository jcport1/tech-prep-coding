# https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height):
        
        # approach: use two pointers for linear time complexity
        # start with max width (possible best solution) and
        # increment if r > l -> we have found the best possible solution for that l, so no need to look at every permutation
        # decrement if r < l > -> we have found the best possible solution for that r, so no need to look at every permutation 

        # alternative approach would be to use brute force (look at every possible area)
        # time complexity of O(n^2)
        
        # initialize pointers
        l, r = 0, len(height)-1

        res = 0

        while l < r:
            # get area, width * height; width -> r index - l index
            area = (r - l) * min(height[l], height[r])

            # find max area
            res = max(res, area)

            # update pointers
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res