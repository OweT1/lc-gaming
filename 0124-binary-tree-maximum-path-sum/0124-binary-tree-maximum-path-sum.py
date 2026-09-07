# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -math.inf
        def dfs(node: Optional[TreeNode]):
            if node is None: return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            nonlocal res
            res = max(res, left + right + node.val)
            return node.val + max(left, right)
        
        dfs(root)
        return res

            