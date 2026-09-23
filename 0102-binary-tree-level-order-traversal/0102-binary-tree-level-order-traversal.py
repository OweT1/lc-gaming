# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res = []
        if not root: return res
        
        curr = [root]
        while curr:
            temp, next_level = [], []
            for node in curr:
                temp.append(node.val)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            curr = next_level.copy()
            res.append(temp)
        return res

        