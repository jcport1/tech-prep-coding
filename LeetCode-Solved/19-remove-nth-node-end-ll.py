# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=daily-question&envId=2024-03-03


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        
        # time complexity: O(n)
        # space complexity: O(1) => constant memory for dummy node

        # use two pointers: create an offset between l and r that is of size n
        # when r reaches null node, l pointer will be equal to n
        
        # create dummy node: not necessary but helps with special edge cases.
        # e.g. len of LL is 1 & remove 1st node from end
        dummy = ListNode(0, head)

        # initalize l pointer
        left = dummy

        # initialize r pointer with while loop
        right = head

        # once n == 0, we've shifted by amount we want to set r to
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # while right is not null, keep shifting both of our pointers
        while right != None:
            left = left.next
            right = right.next

        # delete nth node from end of list
        left.next = left.next.next

        # return head
        return dummy.next