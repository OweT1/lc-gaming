class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def find(self, s: str) -> bool:
        start = self.root
        for c in s:
            if c not in start.children: return False
            start = start.children[c]
        return start.is_end

    def insert(self, s: str):
        start = self.root
        for c in s:
            if c not in start.children:
                start.children[c] = TrieNode()
            start = start.children[c]
        start.is_end = True

    def startswith(self, s: str) -> bool:
        start = self.root
        for c in s:
            if c not in start.children: return False
            start = start.children[c]
        return True
    
    def findExact(self, s: str) -> bool:
        start = self.root
        for c in s:
            if c not in start.children or not start.children[c].is_end: return False
            start = start.children[c]
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        
        for w in words:
            trie.insert(w)
        max_len, res = 0, ""
        for w in words:
            if trie.findExact(w) and (len(w) > max_len or (len(w) == max_len and w < res)):
                res = w
                max_len = len(w)
        return res
        