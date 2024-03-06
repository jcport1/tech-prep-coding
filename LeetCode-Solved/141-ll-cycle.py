# https://leetcode.com/problems/linked-list-cycle/description/?envType=daily-question&envId=2024-03-06

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:

        # time complexity: O(n) => loop through linked list
        # space complexity: O(n) => hash set
        
        # hash set to keep track of visited nodes
        node_hash = set()

        # loop through linked list
        temp = head

        while temp != None:
            if temp in node_hash:
                return True
            
            node_hash.add(temp)
            temp = temp.next
                  
        return False