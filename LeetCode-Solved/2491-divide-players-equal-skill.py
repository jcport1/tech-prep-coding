# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/

from collections import deque
class Solution:
    def dividePlayers(self, skill) -> int:

        # time complexity: O(n log n) -> sorting
        # space complexity: O(n); creating a queue
        
        # sort array
        skill.sort()

        # queue to easily loop through skills; otherwise we would need to use while loop and pointers l/r to loop through
        skill = deque(skill)

        # evenly distribute skills - find total skill sum of small and largest value
        total_skill = skill[0] + skill[-1]

        # keep track of result (chemistry => product of skill a and skill b)
        chemistry = 0

        # loop through queue forming teams of 2 if the total skill of each time is equal. increment chemistry. otherwise return -1
        while len(skill) > 0:
            a = skill.popleft()
            b = skill.pop()

            # is a + b sums != then teams of equal skill cannot be formed
            if a + b != total_skill:
                return -1
            
            # calculate chemistry
            chemistry += a * b
        
        return chemistry