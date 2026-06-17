class Solution:
    def mergeArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        dq1, dq2 = deque(arr1), deque(arr2)
        while dq1 and dq2:
            if dq1[0] < dq2[0]:
                res.append(dq1.popleft())
            else:
                res.append(dq2.popleft())
        
        while dq1:
            res.append(dq1.popleft())
        while dq2:
            res.append(dq2.popleft())
        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        arrs = [[n] for n in nums]
        while len(arrs) > 1:
            # print(arrs)
            arrs = [self.mergeArray(arrs[i], [] if i == len(arrs) - 1 else arrs[i+1]) for i in range(0, len(arrs), 2)]
            # print(arrs)
        return arrs[0]

        