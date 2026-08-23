class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_scoring = {}
        for i in range(26):
            letter_scoring[chr(ord('a') + i)] = score[i]
        letter_count = Counter(letters)

        res = 0
        temp = []
        def get_score(word: str) -> int:
            return sum([letter_scoring[c] for c in word])

        def bfs(i: int, letter_count: dict[str, int]):
            if i == len(words):
                nonlocal res
                res = max(res, sum([get_score(word) for word in temp]))
                return
            
            lttr_cnt = letter_count.copy()
            to_add = True
            for c in words[i]:
                if lttr_cnt[c] == 0:
                    to_add = False
                    break
                lttr_cnt[c] -= 1
            
            if to_add:
                temp.append(words[i])
                bfs(i+1, lttr_cnt)
                temp.pop()
            
            bfs(i+1, letter_count)

        bfs(0, letter_count)
        return res