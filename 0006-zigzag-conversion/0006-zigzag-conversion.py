class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        items = [""] * numRows
        for i, c in enumerate(s):
            j = i % (2 * numRows - 2)
            if j < numRows:
                items[j] += c
            else:
                for k in range(len(items)):
                    if k == 2 * numRows - j - 2:
                        items[k] += c
                    else:
                        items[k] += " "
        return "".join(items).replace(" ", "")

        