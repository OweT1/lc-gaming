# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
    
        temp = head
        curr = temp.val
        while temp.next:
            if curr == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
                curr = temp.val
        return head
