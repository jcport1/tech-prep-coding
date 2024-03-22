# https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def searchMatrix(self, matrix, target: int):

        # approach: binary search on 2D array; flattened 2D array and use formula to find row/col for given idx
        # time complexity: O(log(m * n)); m is num of rows, n is num of columns

        # formula to find row: idx // n
        # formula to find column: idx % n

        m = len(matrix)
        n = len(matrix[0])

        # total items
        t = m * n

        l, r = 0, t-1

        while l <= r:
            mid = (l+r)//2

            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] > target:
                r = mid-1
            else:
                l = mid+1
        
        return False