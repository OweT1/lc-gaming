class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        if len(num1) > len(num2): # num1 is always the shortest str
            num1, num2 = num2, num1

        num1, num2 = num1[::-1], num2[::-1]
        for i, n1 in enumerate(num1, 0):
            for j, n2 in enumerate(num2, 0):
                digit1 = ord(n1) - ord('0')
                digit2 = ord(n2) - ord('0')

                pos = i + j
                res[pos] += digit1 * digit2
                if res[pos] >= 10:
                    res[pos+1] += res[pos] // 10
                    res[pos] = res[pos] % 10

        while res and res[-1] == 0:
            res.pop()
        
        return "".join([str(e) for e in res][::-1]) if res else "0"