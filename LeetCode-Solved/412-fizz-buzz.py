# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int):
        
        # time complexity = O(n)
        # space complexity = O(n)

        result = []

        for i in range(n):
            num = i+1

            if num % 3 == 0 and num % 5 == 0:
                result.append("FizzBuzz")
            elif num % 3 == 0:
                result.append("Fizz")
            elif num % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(num))
        
        
        return result