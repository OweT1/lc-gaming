# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = -math.inf
        ancestors = []

        def dfs(node: Optional[TreeNode]):
            if node is None: return

            nonlocal res
            for anc in ancestors:
                res = max(res, abs(node.val - anc.val))
            
            ancestors.append(node)
            dfs(node.left)
            dfs(node.right)
            ancestors.pop()

        dfs(root)
        return res
        