class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encoding = encoding

    def one_pass(self, n: int) -> int:
        self.encoding[0] -= n
        last_exhausted = self.encoding[1]
        if self.encoding[0] == 0:
            self.encoding = self.encoding[2:]
        return last_exhausted

    def next(self, n: int) -> int:
        if len(self.encoding) == 0:
            return -1

        # 1. n <= self.encoding[0]
        if n <= self.encoding[0]:
            return self.one_pass(n)
            
        # 2. n > self.encoding[0]
        while self.encoding and n > self.encoding[0]:
            n -= self.encoding[0]
            self.encoding = self.encoding[2:]
        
        if self.encoding:
            return self.one_pass(n)
        else:
            return -1


