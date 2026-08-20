class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        wordDictionary = defaultdict(list)
        for word in words:
           wordDictionary[word[0]].append(word)
        
        res = 0
        for c in s:
            if c in wordDictionary:
                wordList = wordDictionary.pop(c)
                for w in wordList:
                    if len(w) == 1:
                        res += 1
                        continue
                    
                    wordDictionary[w[1]].append(w[1:])
        return res