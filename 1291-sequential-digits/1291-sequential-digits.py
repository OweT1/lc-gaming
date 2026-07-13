class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def generateInteger(start: int, length: int):
            base = start * 10 **(length-1)
            for i in range(1, length):
                base += (start+i) * 10**(length-i-1)
            return base
        
        digit_lengths = range(len(str(low)), len(str(high))+1)
        output = []
        for length in digit_lengths:
            start_digit = 1
            while start_digit + length <= 10:
                res = generateInteger(start_digit, length)
                if res >= low and res <= high:
                    output.append(res)
                start_digit += 1
        return output

