class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        startSet = set()
        for w in startWords:
            bm = 0
            for ch in w: bm = bm ^ (1 << (ord(ch) - ord('a')))
            startSet.add(bm)
        
        res = 0
        for w in targetWords:
            bm = 0
            for ch in w: bm = bm ^ (1 << (ord(ch) - ord('a')))
            for ch in w:
                new_bm = bm ^ (1 << (ord(ch) - ord('a')))
                if new_bm in startSet:
                    res += 1
                    break
        
        return res


                