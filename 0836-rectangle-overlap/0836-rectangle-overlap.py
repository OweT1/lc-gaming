class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        return (x4 - x1) > 0 and (y4 - y1) > 0 and (x2 - x3) > 0 and (y2 - y3) > 0