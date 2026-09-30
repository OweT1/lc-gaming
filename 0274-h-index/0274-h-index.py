class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        index_counter = Counter(citations)
        for i in range(1001):
            if n < i: return i-1
            n -= index_counter.get(i, 0)