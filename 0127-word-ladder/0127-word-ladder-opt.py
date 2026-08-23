class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet: return 0

        beginSet = {beginWord}
        endSet = {endWord}
        visited = set()
        turns = 1 # we want number of words

        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            
            nextSet = set()
            for word in beginSet:
                for i in range(len(word)):
                    for j in range(26):
                        c = chr(ord('a')+j)
                        if c == word[i]: continue

                        new_word = word[:i] + c + word[i+1:]
                        if new_word in endSet:
                            return turns + 1
                        
                        if new_word in wordSet and new_word not in visited:
                            nextSet.add(new_word)
                            visited.add(new_word)
            beginSet = nextSet
            turns += 1
        return 0