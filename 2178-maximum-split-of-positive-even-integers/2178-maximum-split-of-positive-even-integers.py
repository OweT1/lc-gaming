class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1: return []

        res = []
        cur = 2
        while finalSum > 0:
            if finalSum <= 2 * cur:
                res.append(finalSum)
                finalSum = 0
            else:
                finalSum -= cur
                res.append(cur)
                cur += 2
        return res