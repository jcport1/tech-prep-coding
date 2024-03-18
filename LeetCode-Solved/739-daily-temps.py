# https://leetcode.com/problems/daily-temperatures/description/

class Solution:
    def dailyTemperatures(self, temperatures):
        
        # approach: monotonic decreasing stack
        # time complexity: O(n)
        # space complexity: O(n)
        # alternative: brute force by checking each element using nested for loop -> O(n^2)

        res = [0] * len(temperatures)

        stack = [] # [temp, idx]

        # enumerate allows us to extract idx
        for i, t in enumerate(temperatures):
            # while t is greater than curr element(s), we've found warmer temperature, so update results arr
            # essentially maintaining monotonic decreasing stack order
            # we update once a value greater than top of stack is discovered
            while stack and t > stack[-1][0]:
                stack_t, stack_idx = stack.pop()
                # update res
                res[stack_idx] = i - stack_idx # num of days for warmer days == idx differences
            
            stack.append([t, i])
        
        return res
            