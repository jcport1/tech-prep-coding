# https://leetcode.com/problems/number-of-divisible-triplet-sums/submissions/1186963380/

from collections import defaultdict

class Solution:
    def divisibleTripletCount(self, nums, d: int) -> int:

        # time complexity: O(n^2) -> the nested loop goes through all pairs of indices
        # space complexity: O(n) -> the hash map stores pairs and the space grows linearly with the input size

        # strategy: work with remainder, i.e., % (modulo operator)

        # step 1: for each (i, j) associate it with the remainder (A[i] + A[j]) % d

        # create hash map for pairs and reminders. buckets based on the reminder

        """
        nums = [3,3,4,7,8], d = 5

        aux = {
            1: [(0,1), (0,4), (1,4), (2,3)],
            2: [(0,2), (1, 2), (2,4)],
            0: [(0,3), (1,3). (3,4)]
        }
        """

        # step 1: find each (i,j) pair and it's reminder (set as key)

        # variance of a two-sum problem
        n = len(nums)
        hash_map = defaultdict(list)
        for i in range(n-1):
            for j in range(i+1, n):
                key = (nums[i] + nums[j]) % d
                hash_map[key].append((i,j))

        # step 2: linear scan/ dict-and-check / two-sum with filtering

        valid_triplets_sum = 0

        # k is at least 2, since following condition must be true
        # for valid triplet:  i < j < k
        for k in range(2, n):
            cur_remainder = nums[k] % d
            # if cur is zero, we want to do an additional mod operation
            # e.g. nums[k] = 5 & d = 5, 5 % 5 = 0 -> (5 - 5) % 5 = 5 = d

            # calculate the remainder needed to reach the next multiple of d
            # if nums[k] = 4, d = 5, then cur_num = 1
            # (d - cur_num) % d = (5 - 1) % 5 = 1
            required_remainder = (d - cur_remainder) % d

            # filter for i < j < k, j by design is greater than i since array is sorted
            valid_triplets_sum += sum(1 for (i, j) in hash_map.get(required_remainder, []) if j < k)

        return valid_triplets_sum

