class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.node = Node()

    def insert(self, word: str):
        temp = self.node

        for c in word:
            if c not in temp.children:
                temp.children[c] = Node()
            temp = temp.children[c]
        
        temp.is_end = True

    def get_max_length(self, word: str) -> int:
        temp = self.node
        m = 0

        for c in word:
            if c not in temp.children:
                break

            temp = temp.children[c]
            m += 1
        return m
            


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()

        for x in arr1:
            trie.insert(str(x))

        m = 0
        for x in arr2:
            m = max(m, trie.get_max_length(str(x)))

        return m


        