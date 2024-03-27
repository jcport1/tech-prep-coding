# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def uniqueOccurrences(self, arr):
        
        # time complexity: O(n)
        # space complexity: O(n)

        # approach: create hash map to keep track of freqs
        my_hash = {}

        for num in arr:
            my_hash[num] = 1 + my_hash.get(num, 0)

        # then loop through values, add to set, compare. if freq exists in set return false
        res_set = set()

        for element in my_hash:
            if my_hash[element] not in res_set:
                res_set.add(my_hash[element])
            else:
                return False
        
        return True

        # important: alternatively, if I passed values of hash map into set()
        # if size of res_set == size of hash map, this implies freq counts are unique, therefore return true
