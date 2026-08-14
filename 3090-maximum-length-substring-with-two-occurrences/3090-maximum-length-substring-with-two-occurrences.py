class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        c_counter = {}
        l, r = 0, 0
        max_len = 0
        k = 2

        while r < len(s):
            c_counter[s[r]] = c_counter.get(s[r], 0) + 1

            while c_counter[s[r]] == k+1:
                max_len = max(max_len, r-l)
                c_counter[s[l]] -= 1
                l += 1

            r += 1
        return max(max_len, r-l)

        