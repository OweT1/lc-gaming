class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = m = 0
        contain_set = set()
        while r < len(s):
            if s[r] in contain_set:
                m = max(m, r-l)
                while s[r] in contain_set:
                    contain_set.remove(s[l])
                    l += 1
            contain_set.add(s[r])
            r += 1

        return max(m, r-l)