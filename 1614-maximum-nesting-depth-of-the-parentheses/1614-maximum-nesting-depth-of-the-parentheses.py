class Solution:
    def maxDepth(self, s: str) -> int:
        depth, res = 0, 0
        for c in s:
            match c:
                case '(': depth += 1
                case ')':
                    res = max(res, depth)
                    depth -= 1
        return res