class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l, r = 0, 0
        curr = 0
        res, length = None, math.inf
        while r < len(s):
            if s[r] == "1":
                if curr < k:
                    curr += 1
                    if curr == k and (r-l < length or (r-l == length and s[l:r+1] < s[res[0]:res[1]])):
                        res = (l, r+1)
                        length = r-l
                else: # curr == k
                    if r-l < length:
                        res = (l, r+1)
                        length = r-l
                    l += 1
                    while s[l] == "0" and l < len(s):
                        l += 1
                    if r-l < length or (r-l == length and s[l:r+1] < s[res[0]:res[1]]):
                        res = (l, r+1)
                        length = r-l
            else:
                if curr == 0:
                    l += 1
            r += 1

        return s[res[0]:res[1]] if res is not None else ""
