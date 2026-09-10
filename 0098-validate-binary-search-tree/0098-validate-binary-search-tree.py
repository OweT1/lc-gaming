# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        order = []
        def dfs(root: Optional[TreeNode]):
            if root is None: return
            if root and not root.left and not root.right: return root.val # leaf node

            nonlocal order
            if root.left: order.append(dfs(root.left))
            order.append(root.val)
            if root.right: order.append(dfs(root.right))
        dfs(root)

        if not order: return True
        prev = order[0]
        for num in order[1:]:
            if num is None: continue
            if prev >= num: return False
            prev = num
        return True
        
