class Solution:
    def is_linked(self, s1: str, s2: str) -> bool:
        is_off = False
        for c1, c2 in zip(s1, s2):
            if c1 != c2 and is_off:
                return False
            elif c1 != c2:
                is_off = True
        return True
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        neighbours = {}
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                word_i, word_j = wordList[i], wordList[j]
                if self.is_linked(word_i, word_j):
                    if word_i not in neighbours:
                        neighbours[word_i] = []
                    if word_j not in neighbours:
                        neighbours[word_j] = []
                    neighbours[word_i].append(word_j)
                    neighbours[word_j].append(word_i)

        nearest = [endWord]
        visited = set(nearest)
        # 1 is because we want number of words, which is number of transformations + 1
        turn = 1
        candidates = set([word for word in wordList if self.is_linked(beginWord, word)])
        while nearest:
            print(nearest)
            
            temp = []
            for node in nearest:
                if node == beginWord:
                    return turn
                elif node in candidates:
                    return turn + 1
                visited.add(node)
                if node not in neighbours: continue

                for n in neighbours[node]:
                    # if n == beginWord:
                    #     return turn
                    # if n in candidates:
                    #     return turn + 1
                    
                    if n not in visited:
                        temp.append(n)
                        visited.add(n)

            nearest = temp.copy()
            turn += 1
        return 0