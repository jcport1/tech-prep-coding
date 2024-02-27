# https://leetcode.com/problems/the-kth-factor-of-n/description/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        # time complexity: O(n)
        # space complexity: O(n)
        # create factor array
        factors = []

        # loop through range 1 - n and find factors
        # start with 1 and go up to n (this means n+1)
        for i in range(1, n+1):
            if n % i == 0:
                factors.append(i)


        # return kth factor of n

        # if array has less than k factors, return -1
        # if max len == k, this is ok, because we still need to subtract 1 from k to get kth factor
        if len(factors) < k:
            return -1

        # array is 0 indexed, so to get the kth factor subtract 1 from k
        return factors[k-1]