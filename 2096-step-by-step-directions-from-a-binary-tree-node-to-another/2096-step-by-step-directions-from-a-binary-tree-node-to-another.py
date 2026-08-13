# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNode(self, root: Optional[TreeNode], targetValue: int):
        path = None 
        temp = []

        def find(curr: Optional[TreeNode]):
            nonlocal path
            if path is not None or curr is None:
                return
            
            if curr and curr.val == targetValue:
                path = "".join(temp)
                return

            temp.append("L")
            find(curr.left)
            temp.pop()

            temp.append("R")
            find(curr.right)
            temp.pop()
        
        find(root)
        return path
        

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        startDirections = self.findNode(root, startValue)
        destDirections = self.findNode(root, destValue)

        while startDirections and destDirections:
            if startDirections[0] == destDirections[0]:
                startDirections, destDirections = startDirections[1:], destDirections[1:]
            else:
                break
        
        return "U"*len(startDirections) + destDirections