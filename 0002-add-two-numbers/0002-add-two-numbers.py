# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        overflow = 0
        head = output = ListNode()
        while l1 is not None and l2 is not None:
            output.next = ListNode()
            output = output.next
            v = l1.val + l2.val + overflow 
            output.val = v % 10
            overflow = v // 10

            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            output.next = ListNode()
            output = output.next
            v = l1.val + overflow
            output.val = v % 10
            overflow = v // 10
            l1 = l1.next
        while l2 is not None:
            output.next = ListNode()
            output = output.next
            v = l2.val + overflow 
            output.val = v % 10
            overflow = v // 10
            l2 = l2.next
        if overflow:
            output.next = ListNode(overflow)
        return head.next
        