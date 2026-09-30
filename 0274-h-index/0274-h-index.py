class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        citation_buckets = [0]*(n+1)

        for citation in citations:
            citation_buckets[min(citation, n)] += 1

        cumulative_citations = 0
        for c in range(n, -1, -1):
            cumulative_citations += citation_buckets[c]
            if cumulative_citations >= c: return c