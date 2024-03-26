# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        # time complexity: O(n) -> looping through array
        # space complexity: O(n) -> set and array
        # approach: two pointers


        vowels = set(['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'])
        # approach: two pointers

        print(vowels)

        l, r = 0, len(s)-1

        str_arr = list(s)

        while l <= r:
            
            # increment l until we find vowel
            while l < len(s) and str_arr[l] not in vowels:
                l += 1
            
            print(str_arr[l])

            # increment r until we find vowel
            while r >= 0 and str_arr[r] not in vowels:
                r -= 1
            
            # possible that l and r crossed but haven't reached respective ends
            # break so chars are not reversed back in original order
            if l >= r:
                break

            # swap when both vowels are found
            temp = str_arr[l]
            str_arr[l] = str_arr[r]
            str_arr[r] = temp
        
            l += 1
            r -= 1
        
        print(str_arr)
        return "".join(str_arr)