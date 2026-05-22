class Solution:
    def get_index(self, string: str) -> tuple[int]:
        res = [0] * 26
        for c in string:
            i = ord(c) - ord("a")
            res[i] += 1
        return tuple(res)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for s in strs:
            ind = self.get_index(s)
            if ind not in anagram_map:
                anagram_map[ind] = []
            anagram_map[ind].append(s)
        return list(anagram_map.values())

        