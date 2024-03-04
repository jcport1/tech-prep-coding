# https://leetcode.com/problems/bag-of-tokens/description/?envType=daily-question&envId=2024-03-04

class Solution:
    def bagOfTokensScore(self, tokens, power: int) -> int:
        
        # approach: sorting & two pointers
        # goal: is to maximize number of points

        # time complexity: O(n log n) => array sorting
        # space complexity: O(1)

        # greedy algorithm: we want to always grab the smallest value for points (face down)
        # and if we have points but cannot buy tokens (we trade points for power for largest value)
        # if we cannot buy tokens or trade in points for Power, we're done

        # sort array of tokens
        tokens.sort()

        # keep track of maxPoints and curPoints
        maxPoints, currPoints = 0, 0

        # initialize pointers
        l, r = 0, len(tokens)-1

        # loop through tokens using greedy algorithm
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                currPoints += 1
                maxPoints = max(maxPoints, currPoints)
                l += 1
            elif power < tokens[l] and currPoints >= 1:
                power += tokens[r]
                currPoints -= 1
                r -= 1
            # we either cannot buy tokens or trade in points for power, so we're done
            else:
                return maxPoints
        
        return maxPoints
