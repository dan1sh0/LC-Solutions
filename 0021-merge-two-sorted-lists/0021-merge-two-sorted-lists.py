# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        # create a dummy node that we can append either list1 or list2 depending on the case 
        dummy = ListNode()
        # tail and dummy next are pointing to the same thing 
        # when modifying the tail pointer, it modifies the dummy next and so forth but dummy is
        # still pointing to the begining of the list 
        # time complexity = O(m+n)
        tail = dummy 
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next 
            else:
                tail.next = list2
                list2 = list2.next 
            tail = tail.next 
        
        # now we have to make sure, that if there is still nodes remaining in either, just append to the end 
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return dummy.next 