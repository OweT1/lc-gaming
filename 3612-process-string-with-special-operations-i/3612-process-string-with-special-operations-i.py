class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for c in s:
            if c.islower() and c.isalpha():
                result += c
            elif c == '*':
                result = result[:-1]
            elif c == '#':
                result *= 2
            elif c == '%':
                result = result[::-1]
        return result
        