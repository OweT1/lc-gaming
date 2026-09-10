class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str):
        temp = self.root
        for c in word:
            if c not in temp.children: temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.is_end = True

    def find(self, word: str) -> bool:
        temp = self.root
        for c in word:
            if c not in temp.children: return False
            temp = temp.children[c]
        return temp.is_end

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.add(word)
        
        n = len(s)
        dp = [False]*n
        for i in range(n):
            if i == 0 or dp[i-1]: # check for each pos in s if it starts with any word
                curr = trie.root
                for j in range(i, n):
                    c = s[j]
                    if c not in curr.children: break

                    curr = curr.children[c]
                    if curr.is_end: dp[j] = True
        return dp[-1]