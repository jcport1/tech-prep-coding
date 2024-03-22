# https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int):
        
        # time complexity: exponential time complexity -> O(2^n)

        # approach: global variable for stack; use backtracking/recursion

        stack = []

        result = []

        def backtrack(openedN, closedN):

            # base case
            if openedN == closedN == n:
                result.append("".join(stack))
                return
            
            if openedN < n:
                # add open parantheses to stack
                stack.append("(")
                # call backtracking method
                backtrack(openedN+1, closedN)
                stack.pop()
            
            if closedN < openedN:
                stack.append(")")
                backtrack(openedN, closedN+1)
                stack.pop()
        
        backtrack(0,0)
        return result
            

