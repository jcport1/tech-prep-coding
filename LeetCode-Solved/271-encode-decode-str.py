# https://leetcode.com/problems/encode-and-decode-strings/description/

class Codec:

    # time complexity: O(n)
    # space complexity: O(n) -> encoding str, decoding arr
    """ approach: use following encoding scheme -> int for len of str + "#"
        example: "4#word"
        why? strs[i] can contain any possible alphanumeric chars so important to divide
        str len integers from str num chars (# services as as a delimiter)
    """

    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""

        for string in strs:
            num = len(string)
            res += str(num) + "#" + string
        
        return res
        

    def decode(self, s: str):
        """Decodes a single string to a list of strings.
        """

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            # get len val of str by extracing num and converting to int
            length = int(s[i:j])

            # extract str based on len
            add_str = s[j + 1: j + 1 + length]

            res.append(add_str)
            
            i = j + 1 +  length
        
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))