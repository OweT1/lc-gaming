class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_len, max_str = 0, ""
        
        for i in range(len(s)):
            centre1, centre2 = s[i], s[i:i+2]
            diff = 1
            while i-diff >= 0 and i+diff < len(s):
                if s[i-diff] == s[i+diff]:
                    centre1 = s[i-diff] + centre1 + s[i+diff]
                    diff += 1
                    continue
                break
            if len(centre1) > max_len:
                max_str = centre1

            if len(centre2) == 2 and centre2[0] == centre2[1]:
                diff = 1
                while i-diff >= 0 and i+diff+1 < len(s):
                    if s[i-diff] == s[i+diff+1]:
                        centre2 = s[i-diff] + centre2 + s[i+diff+1]
                        diff += 1
                        continue
                    break
                
                if len(centre2) > len(max_str):
                    max_str = centre2
            max_len = len(max_str)
        return max_str
        
