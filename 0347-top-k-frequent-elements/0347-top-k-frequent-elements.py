class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] for _ in range(len(nums))]

        for num, count in counter.items():
            freq[count-1].append(num)

        output = []
        print(freq)
        for i in range(len(nums), 0, -1):
            if freq[i-1] != []:
                output.extend(freq[i-1])
                if len(output) >= k:
                    break
        return output[:k]