# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution:
    def evalRPN(self, tokens):

        # time complexity: O(n)
        # space complexity: O(n)

        # approach: use a stack
        # add operands to stack; if operator is encountared pop prev two operands and perform operation
        # add result to stack
    
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                b = stack.pop()
                a = stack.pop()

                stack.append(a - b)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            # add integer to stack
            else:
                stack.append(int(c))
        
        return stack[-1]
