# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        
        # approach: sliding window. Shrink subarray if result is > target sum
        # time complexity: O(n)
        # space complexity: O(1) ; no extra memory as computation happens in place

        # set l pointer
        l = 0

        # track minSum. Since we're trying to find min, set to infinity or len(nums) + 1
        minLen = float("inf")

        # track currSum
        curSum = 0

        # loop through array; set r pointer
        for r in range(len(nums)):
            # curSum += arr[r]
            curSum += nums[r]
            
            # while condition holds that curSum >= target
            # figure out if cur minLen is less than minLen
            # this condition could be true for multiple subarrays, so we check until curSum is less than target
            # once curSum is less than target, we increment r
            while curSum >= target:
                minLen = min(minLen, r-l+1)
                # update curSum
                curSum -= nums[l]
                # move l pointer
                l += 1

        # return minLen
        return 0 if minLen == float("inf") else minLen