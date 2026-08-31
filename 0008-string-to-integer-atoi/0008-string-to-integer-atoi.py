class Solution:
    def getInt(self, c: str) -> int:
        return ord(c) - ord('0')

    def myAtoi(self, s: str) -> int:
        if len(s) == 0 or len(s.strip()) == 0: return 0
        
        clean_s = s.strip()
    
        is_negative = True if clean_s[0] == "-" else False
        if clean_s[0] in ("-", "+"):
            clean_s = clean_s[1:]
        res = ""
        for c in clean_s:
            if not c.isnumeric():
                break
            
            elif c == "0" and len(res) == 0:
                continue
            else:
                res += c
        
        if res == "":
            return 0
        
        converted_res = 0
        for i, c in enumerate(res, start=1):
            converted_res += self.getInt(c)
            converted_res *= 10 if i < len(res) else 1

        if is_negative:
            return max(-converted_res, -2**31)
        else:
            return min(converted_res, 2**31-1)

        