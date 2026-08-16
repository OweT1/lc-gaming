class Solution:
    def minimumPushes(self, word: str) -> int:
        word_count = sorted(Counter(word).items(), key=lambda x:x[1])
        
        res = 0
        for i in range(1, 5):
            counts = word_count[(i-1)*8:i*8]
            res += sum([c[1] * i for c in counts])
        return res

        