# https://leetcode.com/problems/koko-eating-bananas/description/

class Solution:
    def minEatingSpeed(self, piles, h):
        
        # time complexity: O(log(max of p) * p)

        # approach: binary search; min val of arr is lowest possible k; max val of arr is largest possible k

        # pointers are not the positions in the array per se, but instead the spread between [1...k]
        l, r = 1, max(piles)

        res = r

        while l <= r:

            k = (l+r)//2

            # track total num of hours
            hours = 0

            for p in piles:
                # round up
                hours += math.ceil(p / k)
            
            # if total hours for cur k under h, try to find an even smaller k
            if hours <= h:
                res = min(k, res)
                r = k-1

            # else, we went over the time, so try to find greater banana eating rate (k)
            else:
                l = k + 1
        
        return res
