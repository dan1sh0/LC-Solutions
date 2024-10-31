# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        # initialize a new node to None 
        node = None 
        
        # we go through the linked list and define a temp 
        # temp stores the head.next 
        # and we make the head.next point to node, the begining it is null 
        # then we move the node, head, and temp up and continue 
        # time complexity = O(n)
        while head:
            temp = head.next 
            head.next = node 
            node = head 
            head = temp
        return node 
    
    
    
    #        n h t
   # 1 2 3 4 5 