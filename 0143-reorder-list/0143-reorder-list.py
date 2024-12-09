# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # we want to use a fast and slow pointer to find the middle of the list
        # we can break it into two lists 
        # then reverse the second list to make it easier to merge 
        # after reversing, we can merge the two lists back together for the reordering 
        # time complexity = O(n) and O(1) space complexity 
        
        # get the middle of the list using fast and slow pointers
        slow, fast = head, head.next 
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        # now we wanna reverse the second list 
        second = slow.next 
        prev = slow.next = None 
        while second:
            tmp = second.next # stores the second.next
            second.next = prev # then we make the pointer point to prev, null rn 
            prev = second # then we update the prev to the next node 
            second = tmp # and update the head to the next node 
            
        
        
        # then merge 
        first, second = head, prev 
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next = second 
            second.next = tmp1
            first, second = tmp1, tmp2
            
            