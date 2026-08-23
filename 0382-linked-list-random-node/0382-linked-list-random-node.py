# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.node_mapping = {}
        i = 0
        while head:
            self.node_mapping[i] = head
            i += 1
            head = head.next
        self.length = i

    def getRandom(self) -> int:
        rand = random.randint(0, self.length-1)
        return self.node_mapping[rand].val

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()