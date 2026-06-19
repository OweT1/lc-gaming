class Solution:
    def mergeArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        p1, p2 = 0, 0
        n1, n2 = len(arr1), len(arr2)
        while p1 < n1 and p2 < n2:
            if arr1[p1] < arr2[p2]:
                res.append(arr1[p1])
                p1 += 1
            else:
                res.append(arr2[p2])
                p2 += 1
        
        while p1 < n1:
            res.append(arr1[p1])
            p1 += 1
        while p2 < n2:
            res.append(arr2[p2])
            p2 += 1
        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        arrs = [[n] for n in nums]
        while len(arrs) > 1:
            arrs = [self.mergeArray(arrs[i], [] if i == len(arrs) - 1 else arrs[i+1]) for i in range(0, len(arrs), 2)]
        return arrs[0]

        