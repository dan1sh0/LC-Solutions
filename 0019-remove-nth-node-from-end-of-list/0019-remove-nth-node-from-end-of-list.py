# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # convert to array 
        array = []
        current = head 
        while current:
            array.append(current)
            current = current.next 
        

        # remove the number using array notations 
        index = len(array) - n 
        del array[index]

        # convert the array back to a linkedList 
        if not array:
            return None

        head = ListNode(array[0].val)
        current = head

        for i in range(1, len(array)):
            current.next = ListNode(array[i].val)
            current = current.next

        return head
