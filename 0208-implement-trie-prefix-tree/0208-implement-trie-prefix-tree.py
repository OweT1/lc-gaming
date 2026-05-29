class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.node
        for c in word:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.is_end = True

    def search(self, word: str) -> bool:
        temp = self.node
        for c in word:
            if c not in temp.children:
                return False
            temp = temp.children[c]
        return temp.is_end

    def startsWith(self, prefix: str) -> bool:
        temp = self.node
        for c in prefix:
            if c not in temp.children:
                return False
            temp = temp.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)