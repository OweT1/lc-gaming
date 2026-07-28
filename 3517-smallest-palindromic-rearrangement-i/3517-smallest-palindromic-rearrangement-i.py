class Solution:
    def smallestPalindrome(self, s: str) -> str:
        first_half = "".join(sorted(s[:len(s)//2]))
        return first_half + (s[len(s)//2] if len(s) % 2 == 1 else "") + first_half[::-1]
        