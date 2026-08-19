class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedMapping = {}
        for row, col in reservedSeats:
            if col in {1, 10}:
                continue
            if row not in reservedMapping:
                reservedMapping[row] = set()
            
            # Groups
            if col in {2, 3}:
                reservedMapping[row].add(0)
            elif col in {4, 5}:
                reservedMapping[row].add(0)
                reservedMapping[row].add(1)
            elif col in {6, 7}:
                reservedMapping[row].add(1)
                reservedMapping[row].add(2)
            elif col in {8, 9}:
                reservedMapping[row].add(2)

        res = 2*n
        for _, groups in reservedMapping.items():
            res -= 2 if len(groups) == 3 else 1
        return res

        