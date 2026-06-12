class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        items = [[] for _ in range(numRows)]
        for i, c in enumerate(s):
            j = i % (2 * numRows - 2)
            if j < numRows:
                items[j].append(c)
            else:
                for k in range(len(items)):
                    if k == 2 * numRows - j - 2:
                        items[k].append(c)
                    else:
                        items[k].append(" ")
        return "".join(["".join(i) for i in items]).replace(" ", "")

        