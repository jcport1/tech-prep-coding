# https://leetcode.com/problems/valid-sudoku/description/

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board):

        # time complexity: O(9^2)
        # space complexity: O(9^2)
        
        # create hashmaps with set value for rows/cols; key is the ith row or col
        rows = defaultdict(set)
        cols = defaultdict(set)

        # create hashmap set for 3x3 grid; where key is (r,c) index for ith grid
        grids = defaultdict(set)

        # loop through entire board
        for r in range(len(board)):
            for c in range(len(board[0])):
                # ignore empty cells
                if board[r][c] == ".":
                    continue
                # check for duplicates
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in grids[(r//3, c//3)]):
                    return False
                
                # add cell to hash sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grids[r//3, c//3].add(board[r][c])
        
        return True